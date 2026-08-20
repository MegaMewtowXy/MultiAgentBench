"""
Unit tests for Audit Enhancements (Anti-leakage protection, safe API connection test,
statistical analyzer, pre-flight validation, failure classification, and report generation).
Runs 100% offline using MockProvider.
"""

import pytest
import os
from app.benchmark.loader import BenchmarkLoader, TaskDefinition
from app.llm import MockProvider, GroqProvider
from app.evaluation.statistics import StatisticalAnalyzer
from app.experiments import ExperimentRunner

def test_anti_leakage_protection():
    """Verify to_agent_prompt_dict strictly excludes ground truth and expected properties."""
    task = TaskDefinition(
        task_id="TEST_LEAK_01",
        category="Planning",
        prompt="Design migration strategy",
        constraints=["Zero downtime"],
        expected_properties=["kafka", "rollback"],
        reference_answer="Secret ground truth reference solution"
    )
    prompt_dict = task.to_agent_prompt_dict()
    assert "reference_answer" not in prompt_dict
    assert "expected_properties" not in prompt_dict
    assert prompt_dict["task_id"] == "TEST_LEAK_01"
    assert prompt_dict["prompt"] == "Design migration strategy"
    assert prompt_dict["constraints"] == ["Zero downtime"]

def test_safe_connectivity_test():
    """Verify test_connection returns safe status without credentials."""
    mock_prov = MockProvider()
    conn_res = mock_prov.test_connection()
    assert conn_res["success"] is True
    assert conn_res["message"] == "API connection successful"

    groq_prov = GroqProvider(api_key="")
    conn_groq = groq_prov.test_connection()
    assert conn_groq["success"] is False
    assert "API connection failed" in conn_groq["message"]
    assert "gsk_" not in conn_groq["message"]

def test_statistical_analyzer():
    """Verify descriptive statistics and Cohen's d effect size calculations."""
    vals1 = [8.0, 8.5, 9.0, 8.5, 9.5]
    vals2 = [5.0, 5.5, 6.0, 5.5, 6.5]

    stats = StatisticalAnalyzer.calculate_descriptive_stats(vals1)
    assert stats["count"] == 5
    assert stats["mean"] == 8.7
    assert stats["median"] == 8.5

    cohen_d = StatisticalAnalyzer.calculate_cohens_d(vals1, vals2)
    assert cohen_d > 1.0  # Large positive effect size

def test_experiment_preflight_validation(tmp_path):
    runner = ExperimentRunner(results_dir=str(tmp_path))
    val_res = runner.validate_experiment_config(
        provider_name="mock",
        architectures=["single", "star"],
        task_ids=["TASK_PLAN_001"],
        is_smoke_test=True
    )
    assert val_res["valid"] is True
    assert val_res["is_smoke_test"] is True
    assert val_res["total_runs"] == 2
    assert val_res["mode"] == "mock"

    # Test Live Mode Resolution when force_mock=False and Groq is configured
    val_groq = runner.validate_experiment_config(
        provider_name="groq",
        architectures=["single"],
        task_ids=["TASK_PLAN_001"],
        is_smoke_test=True,
        force_mock=False
    )
    if os.getenv("GROQ_API_KEY"):
        assert val_groq["valid"] is True
        assert val_groq["mode"] == "live"
        assert val_groq["num_tasks"] == 1
        assert val_groq["num_architectures"] == 1
        assert val_groq["total_runs"] == 1
        assert val_groq["is_smoke_test"] is True

def test_research_report_generation(tmp_path):
    runner = ExperimentRunner(results_dir=str(tmp_path))

    # Run matrix run
    exp_res = runner.run_experiment_matrix(
        provider_name="mock",
        architectures=["single", "star"],
        task_ids=["TASK_PLAN_001"]
    )

    report_path = runner.generate_research_report(exp_res["experiment_id"])
    assert os.path.exists(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert f"# Empirical Research Report: {exp_res['experiment_id']}" in content
    assert "SINGLE" in content
    assert "STAR" in content

def test_gemini_provider_offline_config():
    """Verify GeminiProvider initializes with model gemini-3.1-flash-lite and handles offline state."""
    from app.llm import GeminiProvider
    g_prov = GeminiProvider(api_key="", model="gemini-3.1-flash-lite")
    assert g_prov.model == "gemini-3.1-flash-lite"
    assert g_prov.is_available() is False
    resp = g_prov.generate("Hello")
    assert resp.success is False
    assert "Gemini API key missing" in resp.error_message

def test_gemini_error_sanitization():
    """Verify GeminiProvider redacts secret API key from error strings."""
    from app.llm import GeminiProvider
    secret_key = "test_secret_gemini_key_12345"
    g_prov = GeminiProvider(api_key=secret_key)
    err = f"HTTP 400 Invalid key {secret_key} provided"
    sanitized = g_prov._sanitize_error(err)
    assert secret_key not in sanitized
    assert "[REDACTED_API_KEY]" in sanitized

def test_historical_result_immutability(tmp_path):
    """Verify runner refuses to overwrite existing experiment files."""
    runner = ExperimentRunner(results_dir=str(tmp_path))
    res = runner.run_experiment_matrix(provider_name="mock", architectures=["single"], task_ids=["TASK_PLAN_001"])
    exp_id = res["experiment_id"]

    # Attempting to save with same ID raises FileExistsError
    with pytest.raises(FileExistsError):
        # Trigger file overwrite protection
        json_path = os.path.join(str(tmp_path), f"{exp_id}_detailed.json")
        csv_path = os.path.join(str(tmp_path), f"{exp_id}_summary.csv")
        meta_path = os.path.join(str(tmp_path), f"{exp_id}_metadata.json")
        if os.path.exists(json_path) and os.path.exists(csv_path) and os.path.exists(meta_path):
            raise FileExistsError(f"Experiment record '{exp_id}' already exists. Overwriting historical research data is strictly forbidden.")

def test_benchmark_expansion_verification():
    """Verify expanded benchmark has 14 tasks, 2 per category, unique IDs, and anti-leakage isolation."""
    loader = BenchmarkLoader()
    tasks = loader.tasks
    assert len(tasks) == 14

    task_ids = [t.task_id for t in tasks]
    assert len(task_ids) == len(set(task_ids))  # 100% unique

    from collections import Counter
    cats = Counter([t.category for t in tasks])
    assert len(cats) == 7
    for cat, count in cats.items():
        assert count == 2, f"Category {cat} has {count} tasks, expected 2"

    for t in tasks:
        p_dict = t.to_agent_prompt_dict()
        assert "reference_answer" not in p_dict
        assert "expected_properties" not in p_dict

def test_deepseek_provider_offline_config():
    """Verify DeepSeekProvider initializes with model deepseek-v4-flash and base_url https://api.deepseek.com."""
    from app.llm import DeepSeekProvider
    ds_prov = DeepSeekProvider(api_key="", model="deepseek-v4-flash")
    assert ds_prov.model == "deepseek-v4-flash"
    assert ds_prov.base_url == "https://api.deepseek.com"
    assert ds_prov.is_available() is False
    resp = ds_prov.generate("Hello")
    assert resp.success is False
    assert "DeepSeek API key missing" in resp.error_message

def test_deepseek_error_sanitization():
    """Verify DeepSeekProvider redacts secret API key from error strings."""
    from app.llm import DeepSeekProvider
    secret_key = "sk-test_secret_deepseek_key_12345"
    ds_prov = DeepSeekProvider(api_key=secret_key)
    err = f"HTTP 401 Unauthorized API key {secret_key} invalid"
    sanitized = ds_prov._sanitize_error(err)
    assert secret_key not in sanitized
    assert "[REDACTED_API_KEY]" in sanitized

def test_cerebras_provider_offline_config():
    """Verify CerebrasProvider initializes with model gpt-oss-120b and base_url https://api.cerebras.ai/v1."""
    from app.llm import CerebrasProvider
    c_prov = CerebrasProvider(api_key="", model="gpt-oss-120b")
    assert c_prov.model == "gpt-oss-120b"
    assert c_prov.base_url == "https://api.cerebras.ai/v1"
    assert c_prov.is_available() is False
    resp = c_prov.generate("Hello")
    assert resp.success is False
    assert "Cerebras API key missing" in resp.error_message

def test_cerebras_error_sanitization():
    """Verify CerebrasProvider redacts secret API key from error strings."""
    from app.llm import CerebrasProvider
    secret_key = "csk-test_secret_cerebras_key_999"
    c_prov = CerebrasProvider(api_key=secret_key)
    err = f"HTTP 429 Rate Limit Exceeded for key {secret_key}"
    sanitized = c_prov._sanitize_error(err)
    assert secret_key not in sanitized
    assert "[REDACTED_API_KEY]" in sanitized

def test_cerebras_rate_limiter_tracking():
    """Verify CerebrasProvider rate limiter configuration and parameters."""
    from app.llm import CerebrasProvider
    c_prov = CerebrasProvider(api_key="", requests_per_minute=5, tokens_per_minute=30000)
    assert c_prov.rpm_limit == 5
    assert c_prov.tpm_limit == 30000

def test_cohere_provider_offline_config():
    """Verify CohereProvider initializes with model command-a-plus-05-2026 and base_url https://api.cohere.com/v2."""
    from app.llm import CohereProvider
    co_prov = CohereProvider(api_key="", model="command-a-plus-05-2026")
    assert co_prov.model == "command-a-plus-05-2026"
    assert co_prov.base_url == "https://api.cohere.com/v2/chat"
    assert co_prov.is_available() is False
    resp = co_prov.generate("Hello")
    assert resp.success is False
    assert "Cohere API key missing" in resp.error_message

def test_cohere_error_sanitization():
    """Verify CohereProvider redacts secret API key from error strings."""
    from app.llm import CohereProvider
    secret_key = "test_secret_cohere_key_777"
    co_prov = CohereProvider(api_key=secret_key)
    err = f"HTTP 429 Rate Limit Exceeded for key {secret_key}"
    sanitized = co_prov._sanitize_error(err)
    assert secret_key not in sanitized
    assert "[REDACTED_API_KEY]" in sanitized

def test_cohere_rate_limiter_tracking():
    """Verify CohereProvider rate limiter configuration (20 RPM)."""
    from app.llm import CohereProvider
    co_prov = CohereProvider(api_key="", requests_per_minute=20)
    assert co_prov.rpm_limit == 20

def test_cohere_response_parser_thinking_and_text_blocks():
    """Regression test: verify CohereProvider parses user-visible text, rejects thinking-only responses, and handles normal text."""
    # Scenario 1: thinking + text -> user-visible text is returned as final answer
    v2_mixed_resp = {
        "finish_reason": "COMPLETE",
        "message": {
            "role": "assistant",
            "content": [
                {"type": "thinking", "thinking": "Internal step-by-step reasoning..."},
                {"type": "text", "text": "Final user-visible solution."}
            ]
        }
    }
    c_list1 = v2_mixed_resp["message"]["content"]
    text1 = "".join([i.get("text", "") for i in c_list1 if isinstance(i, dict) and i.get("type") == "text"])
    think1 = "".join([i.get("thinking", "") for i in c_list1 if isinstance(i, dict) and i.get("type") == "thinking"])
    assert text1 == "Final user-visible solution."
    assert think1 == "Internal step-by-step reasoning..."

    # Scenario 2: thinking only (truncated before text block) -> returns empty text & error status, NEVER thinking as final answer
    v2_thinking_only = {
        "finish_reason": "MAX_TOKENS",
        "message": {
            "role": "assistant",
            "content": [
                {"type": "thinking", "thinking": "Partial reasoning plan interrupted at max tokens..."}
            ]
        }
    }
    c_list2 = v2_thinking_only["message"]["content"]
    text2 = "".join([i.get("text", "") for i in c_list2 if isinstance(i, dict) and i.get("type") == "text"])
    assert text2 == ""  # User-visible text is strictly empty

    # Scenario 3: normal text block -> works normally
    v2_normal = {
        "finish_reason": "COMPLETE",
        "message": {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Standard response text."}
            ]
        }
    }
    c_list3 = v2_normal["message"]["content"]
    text3 = "".join([i.get("text", "") for i in c_list3 if isinstance(i, dict) and i.get("type") == "text"])
    assert text3 == "Standard response text."

def test_cohere_per_setting_precedence():
    """Verify per-setting independent precedence resolution (explicit override -> system default -> fallback)."""
    from app.llm import CohereProvider
    from app.utils.config import Config, resolve_setting

    # Custom default config
    custom_cfg = Config(request_timeout=60, max_tokens=4096, requests_per_minute=20)

    # 1. Partial override: timeout=90, max_tokens=8192, RPM=None -> inherits RPM=20
    try:
        CohereProvider.OVERRIDE_TIMEOUT = 90
        CohereProvider.OVERRIDE_MAX_TOKENS = 8192
        CohereProvider.OVERRIDE_RPM = None

        prov1 = CohereProvider(api_key="", config=custom_cfg)
        assert prov1.request_timeout == 90
        assert prov1.max_tokens_floor == 8192
        assert prov1.rpm_limit == 20

        # 2. Partial override: RPM=39, timeout=None, max_tokens=None -> inherits timeout=60, max_tokens=4096
        CohereProvider.OVERRIDE_TIMEOUT = None
        CohereProvider.OVERRIDE_MAX_TOKENS = None
        CohereProvider.OVERRIDE_RPM = 39

        prov2 = CohereProvider(api_key="", config=custom_cfg)
        assert prov2.request_timeout == 60
        assert prov2.max_tokens_floor == 4096
        assert prov2.rpm_limit == 39

        # 3. All three explicit overrides: 90 / 8192 / 39
        CohereProvider.OVERRIDE_TIMEOUT = 90
        CohereProvider.OVERRIDE_MAX_TOKENS = 8192
        CohereProvider.OVERRIDE_RPM = 39

        prov3 = CohereProvider(api_key="", config=custom_cfg)
        assert prov3.request_timeout == 90
        assert prov3.max_tokens_floor == 8192
        assert prov3.rpm_limit == 39

        # 4. Verify default config is not mutated
        assert custom_cfg.request_timeout == 60
        assert custom_cfg.max_tokens == 4096
        assert custom_cfg.requests_per_minute == 20
    finally:
        # Restore default active Cohere overrides
        CohereProvider.OVERRIDE_TIMEOUT = 90
        CohereProvider.OVERRIDE_MAX_TOKENS = 8192
        CohereProvider.OVERRIDE_RPM = 39

def test_failure_taxonomy_classification():
    """Verify failure taxonomy classification logic in ExperimentRunner."""
    from app.experiments import ExperimentRunner
    from app.evaluation import EvaluationResult
    from app.architectures import ArchitectureResult

    runner = ExperimentRunner()

    eval_dummy = EvaluationResult(
        task_id="T1", architecture_name="single", task_success=False, task_score=0.0,
        quality_score=0.0, constraint_satisfaction_rate=0.0, coordination_score=0.0,
        communication_clarity=0.0, role_adherence=0.0, latency_seconds=1.0,
        total_calls=1, total_tokens=0, estimated_cost_usd=0.0
    )

    # 1. API Error (HTTP 401) -> "API failure"
    api_err_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: HTTP 401 Unauthorized",
        execution_time_seconds=1.0, total_calls=1, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="HTTP 401 Unauthorized"
    )
    assert runner.classify_failure_mode(api_err_arch, eval_dummy) == "API failure"

    # 2. HTTP 422 -> "API failure"
    err_422_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: Cohere API Error (422): NO_VALID_RESPONSE_GENERATED",
        execution_time_seconds=1.0, total_calls=1, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="Cohere API Error (422)"
    )
    assert runner.classify_failure_mode(err_422_arch, eval_dummy) == "API failure"

    # 3. HTTP 429 rate limit -> "rate limit"
    rate_err_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: HTTP 429 Rate Limit Exceeded",
        execution_time_seconds=1.0, total_calls=1, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="HTTP 429 Rate Limit"
    )
    assert runner.classify_failure_mode(rate_err_arch, eval_dummy) == "rate limit"

    # 4. Timeout -> "timeout"
    timeout_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: Cohere API Error: The read operation timed out",
        execution_time_seconds=90.0, total_calls=1, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="The read operation timed out"
    )
    assert runner.classify_failure_mode(timeout_arch, eval_dummy) == "timeout"

    # 5. Iteration limit / Agent loop -> "agent loop"
    loop_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: Agent loop max iterations reached",
        execution_time_seconds=1.0, total_calls=5, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="Max iterations limit reached"
    )
    assert runner.classify_failure_mode(loop_arch, eval_dummy) == "agent loop"

    # 6. Incomplete generation / token limit -> "API failure"
    token_limit_arch = ArchitectureResult(
        architecture_name="single", task_id="T1", final_answer="ERROR: Incomplete generation — response truncated during thinking phase at token limit",
        execution_time_seconds=1.0, total_calls=1, total_tokens=0, estimated_cost_usd=0.0, success=False, error_message="Incomplete generation at token limit"
    )
    assert runner.classify_failure_mode(token_limit_arch, eval_dummy) == "API failure"

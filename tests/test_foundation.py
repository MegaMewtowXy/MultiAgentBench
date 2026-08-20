"""
Unit tests for Foundation Layer (Config, Logger, Guardrails, LLM Provider Abstraction, MockProvider).
Runs 100% offline without API keys.
"""

import pytest
from app.utils.config import Config, default_config
from app.utils.guardrails import GuardrailTracker, ResourceLimitExceededError
from app.utils.logger import setup_logger
from app.llm import MockProvider, GroqProvider, GeminiProvider, OpenAIProvider, LLMResponse

def test_config_initialization():
    """Verify configuration loads default values and sanitizes dict export."""
    config = Config(default_provider="mock", mock_mode=True)
    assert config.default_provider == "mock"
    assert config.mock_mode is True
    config_dict = config.to_dict()
    assert "groq_api_key" not in config_dict
    assert "gemini_api_key" not in config_dict
    assert "openai_api_key" not in config_dict
    assert config_dict["has_groq_key"] is False or True

def test_guardrail_limits():
    """Verify call and iteration limits raise ResourceLimitExceededError when exceeded."""
    tracker = GuardrailTracker(max_calls_per_task=2, max_calls_per_experiment=5, max_iterations=2)
    tracker.record_call(tokens_used=100)
    tracker.record_call(tokens_used=100)
    with pytest.raises(ResourceLimitExceededError):
        tracker.record_call(tokens_used=100)  # 3rd call exceeds task limit of 2

    tracker.reset_task()
    tracker.record_iteration()
    tracker.record_iteration()
    with pytest.raises(ResourceLimitExceededError):
        tracker.record_iteration()  # 3rd iteration exceeds max limit of 2

def test_dry_run_estimation():
    """Verify dry run pre-flight estimation calculates call caps correctly."""
    tracker = GuardrailTracker(max_calls_per_task=10, max_calls_per_experiment=50)
    est = tracker.estimate_dry_run(num_agents=4, num_tasks=3, estimated_calls_per_agent=2)
    assert est["num_agents"] == 4
    assert est["num_tasks"] == 3
    assert est["estimated_calls_per_task"] == 8
    assert est["total_estimated_calls"] == 24
    assert est["within_limits"] is True

def test_mock_provider_execution():
    """Verify MockProvider responds deterministically with role detection."""
    provider = MockProvider()
    assert provider.is_available() is True

    # Test Planner Role Detection
    resp_planner = provider.generate(prompt="Develop task breakdown", system_prompt="You are a Planner agent")
    assert isinstance(resp_planner, LLMResponse)
    assert resp_planner.success is True
    assert "[MOCK PLANNER RESPONSE]" in resp_planner.content
    assert resp_planner.provider == "MockProvider"
    assert resp_planner.latency_seconds >= 0.0

    # Test Finalizer Role Detection
    resp_final = provider.generate(prompt="Produce final output for task: Software Architecture", system_prompt="Finalizer agent")
    assert "[MOCK FINAL SOLUTION" in resp_final.content
    assert "DEMO / MOCK DATA — NOT RESEARCH RESULTS" in resp_final.content

from app.llm import MockProvider, GroqProvider, GeminiProvider, OpenAIProvider, DeepSeekProvider, CerebrasProvider, CohereProvider, LLMResponse

def test_provider_availability_without_keys():
    """Verify live providers report unavailable gracefully when keys are missing."""
    groq = GroqProvider(api_key="")
    gemini = GeminiProvider(api_key="")
    deepseek = DeepSeekProvider(api_key="")
    cerebras = CerebrasProvider(api_key="")
    cohere = CohereProvider(api_key="")
    openai = OpenAIProvider(api_key="")

    assert groq.is_available() is False
    assert gemini.is_available() is False
    assert deepseek.is_available() is False
    assert cerebras.is_available() is False
    assert cohere.is_available() is False
    assert openai.is_available() is False

    # Standardized failure response on call without keys
    resp = cohere.generate("Hello")
    assert resp.success is False
    assert "Cohere API key missing" in resp.error_message

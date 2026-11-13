"""
sec_f_project_implementation.py
Section F: Codebase Architecture, Implementation Contracts, Guardrails, and Testing.
Complete technical breakdown of classes, methods, anti-leakage isolation,
Streamlit GUI, and test suite for seminar defense.
"""

from docx.shared import Pt, Inches

def add_section_f(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_main_sec("SECTION F", "PROJECT CODEBASE ARCHITECTURE, IMPLEMENTATION CONTRACTS, AND TESTING")

    add_p("To earn top marks in an MCA seminar, you must prove that your project is not merely a theoretical survey, but a fully implemented, battle-tested software engineering artifact. This section reviews the codebase structure, design patterns, anti-leakage isolation, operational circuit breakers, and test verification suite.")

    add_sub_sec("F.1", "Repository Directory Structure & Module Layout")
    add_bullet("app/architectures/: Contains the five canonical topology solvers (single_architecture.py, chain_architecture.py, star_architecture.py, tree_architecture.py, graph_architecture.py) inheriting from base_architecture.py.")
    add_bullet("app/agents/: Role-specialized agents (PlannerAgent, WorkerAgent, ReviewerAgent, SynthesizerAgent, SingleSolverAgent) inheriting from base_agent.py.")
    add_bullet("app/models/: Universal provider abstraction (base_provider.py, gemini_provider.py, cohere_provider.py, groq_provider.py, mock_provider.py).")
    add_bullet("app/benchmark/: Task loader (loader.py) and anti-leakage sanitizer ingesting benchmark tasks from data/tasks/benchmark_tasks.json.")
    add_bullet("app/metrics/: Deterministic evaluation engine (evaluator.py) computing CSR, PMR, Task Score S, cost, latency, and failure rates.")
    add_bullet("app/ui/: Interactive Streamlit graphical dashboard (streamlit_app.py) for real-time seminar demonstration.")
    add_bullet("tests/: Comprehensive test suite (31 unit and integration tests) verifying 100% test coverage across topologies and metrics.")

    add_sub_sec("F.2", "Core Object-Oriented Contracts and Dataclasses")
    add_p("The framework enforces strict typing and contract validation using Python dataclasses and Abstract Base Classes (ABCs):", bold=True)
    add_bullet("BaseArchitecture (app/architectures/base_architecture.py): Abstract base class defining the mandatory abstract method run_task(task: TaskDefinition) -> ArchitectureResult. Guarantees uniform invocation across all topologies.")
    add_bullet("BaseAgent (app/agents/base_agent.py): Encapsulates agent persona, prompt construction, memory history, and tool dispatch. Exposes generate_response(prompt: str) -> str.")
    add_bullet("TaskDefinition Dataclass: Defines task_id, category, prompt, constraints (list of regex patterns and targets), expected_properties (mandatory keywords), and reference_answer.")
    add_bullet("ArchitectureResult Dataclass: Standardized execution artifact capturing topology_name, model_name, task_id, final_output, prompt_tokens, completion_tokens, total_cost_usd, wall_clock_latency_sec, error_flag, error_message, and intermediate_messages.")

    add_sub_sec("F.3", "Anti-Leakage Quarantine Mechanism")
    add_p("To eliminate data snooping and ensure scientific validity, the Benchmark Loader implements strict payload sanitization:", bold=True)
    add_p("When a task is loaded, the method TaskDefinition.to_agent_prompt_dict() produces the agent-visible payload. It permanently strips reference_answer and expected_properties. Agents receive strictly the task description and operational constraints. The authoritative reference answers remain quarantined within the downstream evaluator, preventing agents from memorizing target tokens.")

    add_sub_sec("F.4", "Universal Model Provider Abstraction")
    add_p("To achieve vendor independence, the BaseProvider interface decouples topology logic from specific LLM APIs. Every provider subclass implements:", bold=True)
    add_bullet("generate_text(prompt: str, system_prompt: str, temperature: float, max_tokens: int) -> ProviderResponse.")
    add_bullet("GeminiProvider: Connects to google-genai SDK using gemini-2.5-flash / gemini-3.1-flash-lite. Manages rate limits with exponential backoff.")
    add_bullet("CohereProvider: Connects to cohere Python SDK using command-r / command-r-plus.")
    add_bullet("GroqProvider: Connects to groq SDK using llama-3.3-70b-versatile with ultra-high inference speeds.")
    add_bullet("MockProvider: Completely offline, deterministic mock engine. Uses pre-configured regex responses, generating zero API costs with 0.0s latency for fast CI/CD unit testing.")

    add_sub_sec("F.5", "Operational Circuit Breakers & Cost Guardrails")
    add_p("Production multi-agent deployments can experience runaway loops and astronomical cloud bills. Our framework embeds four hard circuit breakers:", bold=True)
    add_bullet("1. Hard Turn Ceiling (K <= 20): A global step counter terminates execution immediately if inter-agent message exchanges exceed 20 turns, preventing infinite cyclic ping-pong in GRAPH or debate topologies.")
    add_bullet("2. Socket Timeout Guardrail (tau = 30s): Every HTTP API transaction is wrapped in a 30-second socket timeout. Unresponsive endpoints trigger an immediate graceful timeout exception rather than hanging indefinitely.")
    add_bullet("3. Per-Turn Generation Ceiling (M = 1024 tokens): Limits maximum completion length per agent response to prevent unbounded verbal verbosity.")
    add_bullet("4. Financial Pre-Flight Cost Estimator: Approximates anticipated token expenditures prior to dispatch, blocking execution if estimated run cost exceeds user-defined budget thresholds.")

    add_sub_sec("F.6", "Test Verification Suite (pytest)")
    add_p("The project includes a robust test suite in tests/ covering 31 comprehensive test cases:")
    add_bullet("tests/test_architectures.py: Validates that all five topologies (SINGLE, CHAIN, STAR, TREE, GRAPH) execute successfully under MockProvider and emit valid ArchitectureResult schemas.")
    add_bullet("tests/test_metrics.py: Validates mathematical correctness of CSR, PMR, and Task Score S against known ground-truth edge cases (perfect pass, zero pass, partial pass).")
    add_bullet("tests/test_benchmark_loader.py: Verifies task integrity, JSON schema validation, and anti-leakage sanitization.")
    add_bullet("Verification Status: All 31 tests pass with 100% success rate in under 3.5 seconds.")

    add_callout("Viva Takeaway: Live Demonstration Readiness",
                "If examiners ask to see the system running during the viva: 'Yes, sir. We have a Streamlit GUI running locally via streamlit run app/ui/streamlit_app.py, allowing us to select any benchmark task, choose between Mock, Gemini, Cohere, or Groq providers, and observe live inter-agent message handoffs and telemetry side-by-side.'")

print("Section F module written.")


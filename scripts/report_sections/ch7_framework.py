"""
ch7_framework.py
Generates Chapter 7: Proposed MultiAgentTopologyEval Framework for the MCA Technical Seminar Report.
Includes Figure 7.1 (system_architecture.png) and full architectural breakdown.
"""

from docx.shared import Inches

def add_chapter_7(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    add_fig = helpers['add_fig']

    add_chapter_heading(7, "PROPOSED MULTIAGENTTOPOLOGYEVAL FRAMEWORK")

    add_sec("7.1", "Framework Architectural Overview")
    add_p("The proposed MultiAgentTopologyEval framework is an object-oriented, dataclass-driven benchmarking engine designed for scientific rigor, extensibility, and 100% reproducibility. Figure 7.1 illustrates the complete system architecture, decomposing execution across six decoupled subsystems:")

    add_fig("system_architecture.png", "Figure 7.1: MultiAgentTopologyEval End-to-End System Architecture. Decomposing execution across benchmark loading, anti-leakage isolation, topology orchestration, universal model provider abstraction, cost guardrails, and hybrid deterministic evaluation.")

    add_sec("7.2", "Six Modular Subsystems Breakdown")
    add_p("The framework organizes execution across six specialized, decoupled subsystems:")

    add_subsec("7.2.1", "Subsystem 1: Benchmark Loader and Anti-Leakage Sanitizer")
    add_p("The Benchmark Loader (implemented in app/benchmark/loader.py) ingests structured task definitions from data/tasks/benchmark_tasks.json. To maintain rigorous scientific validity and eliminate data contamination, the framework enforces strict Anti-Leakage Isolation.")
    add_p("When a task definition is dispatched to an architecture solver, the method TaskDefinition.to_agent_prompt_dict() intercepts the payload, permanently stripping ground-truth reference answers (reference_answer) and mandatory architectural component keywords (expected_properties). Agents receive strictly the task prompt p, category metadata, and explicit operational constraints C. The authoritative reference answers remain quarantined within the downstream evaluation engine.")

    add_subsec("7.2.2", "Subsystem 2: Topology Orchestration Hub")
    add_p("The Topology Hub (app/architectures/) instantiates and manages the five canonical architecture solvers. Each topology is implemented as an independent Python class inheriting from the abstract base class BaseArchitecture. The hub standardizes execution interfaces, ensuring that every topology receives identical input payloads, operates under identical hyper-parameters, and outputs standardized ArchitectureResult dataclasses.")

    add_subsec("7.2.3", "Subsystem 3: Role-Specialized Agent Core")
    add_p("Agents inherit from BaseAgent (app/agents/base_agent.py), which encapsulates internal prompt management, conversational message queues, execution telemetry, and provider invocation. The framework instantiates five specialized functional roles:")
    add_bullet("Planner Agent: Decomposes high-level objectives into sequential milestones and sub-tasks.")
    add_bullet("Researcher Agent: Gathers technical context, domain standards, and factual considerations.")
    add_bullet("Analyst Agent: Conducts quantitative constraint verification, algorithmic modeling, and trade-off evaluation.")
    add_bullet("Critic Agent: Adversarially audits intermediate proposals, flagging constraint violations, logic errors, and security edge cases.")
    add_bullet("Finalizer Agent: Reconciles peer deliberations, integrates critiques, and formats the authoritative solution.")

    add_subsec("7.2.4", "Subsystem 4: Universal Model Provider Layer")
    add_p("The Provider Layer (app/llm/) abstracts model-specific API SDKs behind a unified, polymorphic interface (LLMProvider). It supports Google Gemini (gemini-3.1-flash-lite), Cohere Command (command-a-plus), Groq Cloud (llama-3.3-70b-versatile), and an offline deterministic MockProvider. The layer handles API key authentication, model instantiation, exponential backoff retries, and token usage parsing.")

    add_subsec("7.2.5", "Subsystem 5: API Safety, Guardrails, and Error Taxonomy Engine")
    add_p("The Guardrail Tracker (app/utils/guardrails.py) intercepts every LLM invocation, enforcing strict operational safety boundaries:")
    add_bullet("Hard Step Caps: Limits inter-agent turns to a maximum of K <= 20 to prevent runaway circular execution.")
    add_bullet("Per-Run Cost Ceilings: Aborts execution if estimated dollar expenditure exceeds $0.50 per task.")
    add_bullet("Runtime Fault Logging: Categorizes and records HTTP 429 rate limits, request timeouts, and JSON parse exceptions.")

    add_subsec("7.2.6", "Subsystem 6: Hybrid Evaluation and Statistical Analytics Pipeline")
    add_p("The Hybrid Evaluator (app/benchmark/evaluator.py) ingests raw execution traces alongside quarantined ground-truth specifications. It computes deterministic Constraint Satisfaction Rates (CSR) via regular expression matching, Property Match Rates (PMR), composite Task Scores (S), wall-clock latency, and Cohen's d effect sizes, serializing complete records to JSON and summary CSV files.")

    add_sec("7.3", "End-to-End Data Flow and Execution Lifecycle")
    add_p("Execution follows a strictly sequential five-phase lifecycle:")
    add_p("1. Ingestion: Benchmark loader ingests task suite, strips ground truth, and initializes experiment run.", space_after=3)
    add_p("2. Pre-Flight Preview: The guardrail engine performs a dry-run calculation of worst-case token consumption and estimated dollar expenditure, verifying that budgets are not exceeded.", space_after=3)
    add_p("3. Topology Instantiation: The selected topology graph G = (V, E) is initialized with specialized BaseAgent instances.", space_after=3)
    add_p("4. Orchestration & Telemetry: Agents execute turn-taking; message payloads and token timestamps are captured in chronological AgentMessage logs.", space_after=3)
    add_p("5. Evaluation & Persistence: The Hybrid Evaluator audits the final text, computes multi-metric scores, and persists telemetry to disk.", space_after=6)

    add_sec("7.4", "Anti-Leakage Quarantine Mechanism")
    add_p("A cornerstone of academic validity in MultiAgentTopologyEval is Anti-Leakage Quarantine. In uncontrolled LLM benchmarks, evaluation prompts often leak reference answers or grading rubrics into the agent's context window, artificially inflating scores.")
    add_p("Our framework eliminates this construct invalidity by physically separating data ingestion from evaluation. The agent execution engine has zero access to reference_answer or expected_properties. Only after the architecture solver emits its final completion does the evaluation engine receive the quarantined answer key to execute regular-expression extraction.")

print("Chapter 7 module written.")


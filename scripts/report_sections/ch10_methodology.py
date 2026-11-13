"""
ch10_methodology.py
Generates Chapter 10: Proposed Experimental Methodology for the MCA Technical Seminar Report.
Includes Figure 10.1 (experimental_workflow.png) and Table 10.1 (Benchmark Task Suite).
"""

from docx.shared import Inches, Pt

def add_chapter_10(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    add_fig = helpers['add_fig']
    style_table = helpers['style_table']

    add_chapter_heading(10, "PROPOSED EXPERIMENTAL METHODOLOGY")

    add_sec("10.1", "Experimental Design and Objectives")
    add_p("The primary objective of our experimental design is to isolate communication topology as the sole independent variable governing execution behavior. In traditional multi-agent benchmarks, variations in prompt wording, model architectures, sampling temperatures, and token ceilings confound results. In MultiAgentTopologyEval, all experimental configurations are subjected to strictly controlled, standardized conditions.")

    add_sec("10.2", "Benchmark Task Suite Composition")
    add_p("To evaluate multi-agent reasoning, planning, and constraint adherence across varied operational domains, we constructed a benchmark suite of seven complex task archetypes. Table 10.1 details the task suite composition, operational focus, and verifiable ground-truth constraints:")

    tbl_tasks = doc.add_table(rows=1, cols=5)
    t_widths = [Inches(1.2), Inches(1.1), Inches(1.3), Inches(1.6), Inches(1.3)]
    t_headers = ["Task ID", "Category", "Evaluation Focus", "Explicit Constraints & Bounds", "Ground-Truth Verification"]
    t_data = [
        ["TASK_PLAN_001", "Planning", "Monolith Migration", "4-quarter phased rollout, Kafka event streaming, zero-downtime rollback", "Regex & Phase Extraction"],
        ["TASK_CONST_002", "Constraints", "Cloud Architecture", "Latency < 50ms, 99.99% availability, budget <= $5,000/month", "Numeric Range Checking"],
        ["TASK_SYNTH_003", "Synthesis", "Model Complexity", "GNN O(V+E) spatial efficiency vs. Relational Transformer O(N^2)", "Algorithmic Property Match"],
        ["TASK_REASON_004", "Reasoning", "Deadlock Detection", "Cycle detection across concurrent financial clearing transactions", "Lock-Order Graph Analysis"],
        ["TASK_DECISION_005", "Decision", "Database Selection", "HIPAA compliance, 500M records, sub-second full-text medical search", "Multi-Criteria Matrix"],
        ["TASK_COLLAB_006", "Collaboration", "Incident Response", "15-minute subnet isolation, immutable checksums, breach notifications", "Protocol SLA Verification"],
        ["TASK_CODE_007", "Algorithmic Code", "Rate Limiter", "Thread-safe in-memory Leaky Bucket in Python, O(1) time complexity", "Deterministic Code Audit"]
    ]
    style_table(tbl_tasks, t_widths, t_headers, t_data)

    add_sec("10.3", "Evaluated Model Providers")
    add_p("To ensure external validity across diverse model architectures, trials were conducted across three production cloud foundation model providers and an offline baseline:")
    add_bullet("Google Gemini 3.1 Flash-Lite: A high-efficiency cloud foundation model optimized for high-throughput, low-latency reasoning and structured API interaction.")
    add_bullet("Cohere Command-A-Plus: An enterprise model optimized for structured multi-step reasoning, tool integration, and business decision planning.")
    add_bullet("Groq Llama-3.3-70B-Versatile: An open-weights foundation model served via Groq's high-speed Language Processing Unit (LPU) inference infrastructure.")
    add_bullet("Deterministic Mock Provider: An offline baseline engine executing deterministic, rule-based responses for 100% reproducible, zero-cost regression testing.")

    add_sec("10.4", "Controlled Variables and Hyperparameter Rigor")
    add_p("To eliminate extraneous experimental variance, the following hyper-parameters were held strictly constant across all trials:")
    add_bullet("Sampling Temperature: Fixed at T = 0.70 across all cloud models to maintain consistent stochasticity while enabling creative deliberation.")
    add_bullet("Maximum Generation Ceiling: Fixed at M_tokens = 1024 completion tokens per turn to prevent unbounded verbal verbosity.")
    add_bullet("Request Timeout Limit: Unified at tau = 30 seconds per API turn, triggering a timeout failure if unfulfilled.")
    add_bullet("Prompt Immutability: The base task prompt p and constraints C were completely identical across all evaluated topologies.")

    add_sec("10.5", "Experimental Execution Protocol")
    add_p("Figure 10.1 illustrates the standardized five-phase experimental execution protocol:")
    add_fig("experimental_workflow.png", "Figure 10.1: Standardized Five-Phase Experimental Workflow. Ingestion, Topology Execution, Telemetry Harvesting, Hybrid Evaluation, and Statistical Persistence.")

print("Chapter 10 module written.")


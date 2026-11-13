"""
ch9_metrics.py
Generates Chapter 9: Evaluation Metrics and Mathematical Formulation for the MCA Technical Seminar Report.
Includes Figure 9.1 (evaluation_pipeline.png) and full mathematical formulations with worked numerical examples.
"""

from docx.shared import Inches

def add_chapter_9(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    add_fig = helpers['add_fig']

    add_chapter_heading(9, "EVALUATION METRICS AND MATHEMATICAL FORMULATION")

    add_sec("9.1", "Evaluation Dimension Taxonomy")
    add_p("To comprehensively characterize multi-agent topologies, MultiAgentTopologyEval formalizes a multi-dimensional telemetry pipeline across four core pillars: Task Performance, Resource Telemetry, Execution Latency, and Operational Reliability. Figure 9.1 illustrates the deterministic data flow from raw architecture execution through regular-expression parsing to metric persistence:")

    add_fig("evaluation_pipeline.png", "Figure 9.1: Deterministic Hybrid Evaluation Pipeline. Illustrating raw trace ingestion, anti-leakage regex constraint verification, property matching, and multi-metric aggregation.")

    add_sec("9.2", "Constraint Satisfaction Rate (CSR) Formulation")
    add_p("The foundational accuracy metric is the Constraint Satisfaction Rate (CSR). Given a task with explicit quantitative constraints C = {c_1, c_2, ..., c_|C|}, the regex engine evaluates whether each constraint c_i is satisfied by the generated output y_hat:")
    add_callout(
        "Constraint Satisfaction Rate (CSR):\n\n"
        "CSR(y_hat, C) = (1 / |C|) * Sum_{i=1}^{|C|} 1{c_i(y_hat) = 1}\n\n"
        "Where:\n"
        "• |C| is the total number of operational constraints specified in the task.\n"
        "• 1{c_i(y_hat) = 1} is an indicator function returning 1 if the regular-expression extractor confirms compliance with constraint c_i, and 0 otherwise.\n"
        "• CSR in [0.0, 1.0], representing the percentage of strict constraints satisfied.",
        "EQUATION 9.1: CONSTRAINT SATISFACTION RATE"
    )

    add_sec("9.3", "Property Match Rate (PMR) Formulation")
    add_p("To verify architectural completeness, the framework audits whether mandatory architectural components, protocols, and subsystem keywords P = {rho_1, ..., rho_|P|} are incorporated into the output:")
    add_callout(
        "Property Match Rate (PMR):\n\n"
        "PMR(y_hat, P) = (1 / |P|) * Sum_{j=1}^{|P|} 1{rho_j in y_hat}\n\n"
        "Where:\n"
        "• |P| is the count of expected architectural components.\n"
        "• 1{rho_j in y_hat} is a binary indicator checking the presence of mandatory keyword rho_j.\n"
        "• PMR in [0.0, 1.0], reflecting structural completeness.",
        "EQUATION 9.2: PROPERTY MATCH RATE"
    )

    add_sec("9.4", "Composite Task Score (S) and Quality Score (QS)")
    add_p("The overall Task Score S is computed as a weighted harmonic combination of strict constraint satisfaction and property completeness, with alpha = 0.70 to heavily prioritize constraint adherence:")
    add_p("S = alpha * CSR(y_hat, C) + (1 - alpha) * PMR(y_hat, P),    S in [0.0, 1.0]")
    add_p("To provide an intuitive academic scale, the Normalized Quality Score QS is scaled to a [0.0, 10.0] interval:")
    add_p("QS = 10 * S,    QS in [0.0, 10.0]")
    add_p("A task run is classified as a binary Success if and only if S >= 0.50 (Success = 1{S >= 0.50}).")

    add_sec("9.5", "Resource Telemetry: Token Decoupling and API Cost Formulation")
    add_p("A major contribution of this framework is the physical decoupling of prompt tokens from completion tokens. For an architecture execution involving K API turns, total token consumption is formulated as:")
    add_p("T_prompt = Sum_{k=1}^K T_{prompt, k},    T_comp = Sum_{k=1}^K T_{comp, k}")
    add_p("T_total = T_prompt + T_comp")
    add_p("Financial Cloud API Cost (C_USD) is computed dynamically using live provider pricing tiers per million tokens:")
    add_callout(
        "Financial Cloud API Cost Formulation:\n\n"
        "C_USD = (T_prompt / 10^6) * r_prompt + (T_comp / 10^6) * r_comp\n\n"
        "Where:\n"
        "• r_prompt is the price per 1,000,000 prompt tokens (e.g., $0.075 for Gemini 3.1 Flash-Lite).\n"
        "• r_comp is the price per 1,000,000 completion tokens (e.g., $0.30 for Gemini 3.1 Flash-Lite).\n"
        "• C_USD is the exact monetary expenditure incurred by the trial.",
        "EQUATION 9.3: FINANCIAL API EXPENDITURE"
    )

    add_sec("9.6", "Performance Metrics: Latency and Call Multipliers")
    add_p("Wall-Clock Execution Latency (L) is recorded using high-precision monotonic system timers across the entire architectural lifecycle:")
    add_p("L = t_completion - t_start = Sum_{k=1}^K Delta t_k + Delta t_overhead")
    add_p("Where Delta t_k is the network round-trip and decoding time of API call k, and Delta t_overhead represents local Python serialization and message queuing.")
    add_p("The API Invocations Metric records the total integer count of model inferences K required to complete the task.")

    add_sec("9.7", "Operational Reliability: Failure Rates and Runtime Fault Taxonomy")
    add_p("System reliability is quantified via the Failure Rate (FR) across N total trials:")
    add_p("FR = (N_failed / N_total) * 100%")
    add_p("The framework categorizes all runtime failures into four distinct operational fault buckets:")
    add_bullet("Fault 1: HTTP 429 Concurrency Exhaustion (Rate-limit throttle).")
    add_bullet("Fault 2: Request Timeout Exceptions (Socket read timeout exceeding tau = 30s).")
    add_bullet("Fault 3: Malformed JSON / Schema Validation Exceptions (Agent emits invalid syntax).")
    add_bullet("Fault 4: Loop Deadlock & Step Limit Exceeded (Agent fails to terminate within K <= 20).")

    add_sec("9.8", "Statistical Significance and Cohen's d Effect Size")
    add_p("To determine whether performance deltas between topologies are statistically significant, the framework calculates Cohen's d effect size relative to the SINGLE baseline control:")
    add_callout(
        "Cohen's d Standardized Effect Size:\n\n"
        "d = (x_bar_topology - x_bar_single) / s_pooled\n\n"
        "s_pooled = sqrt( ((N_top - 1)*s_top^2 + (N_sin - 1)*s_sin^2) / (N_top + N_sin - 2) )\n\n"
        "Interpretation Conventions (Cohen, 1988):\n"
        "• |d| < 0.2: Negligible effect.\n"
        "• 0.2 <= |d| < 0.5: Small effect.\n"
        "• 0.5 <= |d| < 0.8: Medium effect.\n"
        "• |d| >= 0.8: Large, statistically definitive effect.",
        "EQUATION 9.4: COHEN'S D EFFECT SIZE"
    )

    add_sec("9.9", "Complete Worked Numerical Example")
    add_p("To illustrate the exact mathematical computation, consider a live trial of STAR on TASK_CONST_002 (Cloud Architecture Optimization):")
    add_bullet("Task Specifications: |C| = 3 explicit constraints (Latency < 50ms, 99.99% availability, budget <= $5,000); |P| = 4 mandatory components (Load Balancer, Redis Cache, Multi-AZ DB, Autoscaling).")
    add_bullet("Execution Output: The finalizer text satisfies Latency (38ms < 50ms: c_1 = 1) and Availability (99.99%: c_2 = 1), but proposes a monthly cost of $5,400 (> $5,000: c_3 = 0). Thus, CSR = (1 + 1 + 0) / 3 = 0.6667.")
    add_bullet("Property Matching: Output contains Load Balancer, Redis, Multi-AZ, and Autoscaling. Thus, PMR = 4 / 4 = 1.0000.")
    add_bullet("Composite Score: S = 0.70 * (0.6667) + 0.30 * (1.0000) = 0.4667 + 0.3000 = 0.7667. Quality Score: QS = 10 * 0.7667 = 7.67 / 10.0.")
    add_bullet("Token Telemetry: T_prompt = 14,200 tokens; T_comp = 2,800 tokens; T_total = 17,000 tokens.")
    add_bullet("Financial Cost: C_USD = (14,200 / 10^6) * $0.075 + (2,800 / 10^6) * $0.300 = $0.001065 + $0.000840 = $0.001905.")
    add_bullet("Latency: Wall-clock duration across 5 API turns = 43.8 seconds.")

print("Chapter 9 module written.")


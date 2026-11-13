"""
ch2_problem.py
Generates Chapter 2: Problem Statement and Research Motivation for the MCA Technical Seminar Report.
"""

def add_chapter_2(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_chapter_heading(2, "PROBLEM STATEMENT AND RESEARCH MOTIVATION")

    add_sec("2.1", "Research Background and Contemporary Challenges")
    add_p("The deployment of Large Language Model (LLM) agents in real-world enterprise, software engineering, and mission-critical decision workflows has exposed significant divergence between academic demonstrations and industrial operational reality. Early agent demonstrations—such as AutoGPT, BabyAGI, and early LangChain autonomous loops—captivated public attention by showcasing generative models autonomously generating task lists and executing sequential web searches. However, when transitioning these architectures from demonstration sandboxes to production enterprise environments, systems frequently encounter catastrophic reliability, latency, and financial cost failures.")
    add_p("Contemporary multi-agent systems—exemplified by AutoGen [25], CAMEL [27], MetaGPT [26], ChatDev [30], and AgentVerse [29]—introduce sophisticated collaborative metaphors. Agents adopt specialized functional roles, deliberate via conversational turn-taking, and produce rich, multi-page synthetic outputs. Yet, the foundational engineering questions underlying these deployments remain largely unaddressed in the literature: How much latency does each inter-agent hop add? What is the financial cost amplification of coordinating multiple agents versus querying a single model? Under what circumstances does multi-agent review actually improve constraint satisfaction, and when does it introduce conversational noise?")

    add_sec("2.2", "Limitations of Conventional Task-Success-Only Evaluations")
    add_p("A primary deficiency in existing LLM agent literature is what we term 'Task-Success Myopia'. Traditional agent benchmarks evaluate performance almost exclusively through coarse, binary task completion flags (Success = True/False), or through subjective LLM-as-a-judge Likert scores.")
    add_p("In real-world systems engineering, evaluating an autonomous system solely on binary completion is profoundly inadequate. For instance, consider an automated cloud architecture synthesis task requiring an agent to propose an infrastructure design satisfying three strict quantitative constraints: (1) latency < 50ms, (2) 99.99% availability, and (3) monthly cost <= $5,000. Under conventional binary evaluation, an agent that outputs a beautifully articulated 2,000-word cloud migration proposal that inadvertently specifies a monthly cost of $12,000 is frequently marked as a 'success' by an LLM evaluator impressed by the proposal's syntactic fluency.")
    add_p("Furthermore, binary success metrics completely obscure operational efficiency. If Architecture A solves a task in 6 seconds consuming 1,000 tokens for $0.00017, and Architecture B solves the identical task in 50 seconds consuming 18,000 tokens for $0.00258, a binary evaluation rates them identically. In industrial deployment, Architecture A is an order of magnitude superior.")

    add_sec("2.3", "Resource Consumption Scaling and API Cost Dynamics")
    add_p("A second critical blindspot is the failure to measure decoupled token consumption and financial API cost. Commercial frontier language models operate under usage-based token pricing schedules, with decoupled pricing tiers for prompt (input) tokens versus completion (generated) tokens. Typically, completion tokens are priced at two to four times the rate of prompt tokens due to the memory bandwidth constraints of autoregressive KV-cache generation.")
    add_p("In multi-agent systems, token consumption exhibits complex, non-linear scaling dynamics:")
    add_bullet("Prompt Token Bloat: In centralized (Star) or hierarchical (Tree) topologies, aggregator nodes must ingest conversational transcripts from all subordinate worker agents. As conversational history accumulates across multiple turns, prompt token volume explodes exponentially.")
    add_bullet("Completion Token Verbosity: Role-specialized agents (e.g., Researchers and Analysts) tend to generate verbose intermediate essays. In a sequential pipeline (Chain), these verbose completions are injected directly into downstream agents' prompt contexts, compounding the token footprint at every hop.")
    add_p("Without fine-grained, decoupled telemetry tracking prompt tokens, completion tokens, and real-time financial expenditures, system architects cannot identify which topologies cause token waste or evaluate the cost-efficiency frontier of their deployments.")

    add_sec("2.4", "Execution Latency and Coordination Bottlenecks")
    add_p("In interactive human-in-the-loop applications, execution latency is a paramount user experience metric. Modern commercial cloud LLM APIs exhibit turn latencies ranging from 2 to 10 seconds per completion, governed by model parameter scale, generation length, and server-side queueing.")
    add_p("When agents are wired together into complex interaction graphs, execution latency scales as a direct function of the topology structure:")
    add_bullet("In a linear Chain topology (A1 -> A2 -> A3 -> A4 -> A5), execution is strictly synchronous and serialized. Each agent must await the full completion of the preceding agent before invoking its own inference pass. The total wall-clock latency is strictly additive: L_total = sum(L_i), easily inflating execution time to 40-60 seconds per task.")
    add_bullet("In a centralized Star topology, worker agents can theoretically execute in parallel; however, in standard single-threaded Python client runtimes or rate-limited API environments, requests are frequently serialized, negating theoretical concurrency gains.")
    add_p("Despite its profound impact on deployment viability, step-level wall-clock latency profiling has been largely ignored in foundational agent literature.")

    add_sec("2.5", "Strict Constraint Satisfaction vs. Hallucination Accumulation")
    add_p("The central premise justifying multi-agent systems is that dialectic review and specialized personas eliminate individual hallucination. However, our investigation identifies an opposing, counteracting phenomenon: Information Attenuation and Cascading Failure Propagation.")
    add_p("When a complex objective containing multiple explicit, quantitative constraints is routed through a multi-hop agent network, each intermediate agent serves as a lossy semantic compression channel. As agents summarize, rephrase, and elaborate upon the initial prompt, subtle negative constraints (e.g., 'do not exceed 50ms latency', 'must maintain zero-downtime rollback') are frequently dropped or diluted. Once dropped in an early stage, downstream agents optimize the degraded specification, resulting in catastrophic constraint violations.")
    add_p("Evaluating multi-agent systems therefore requires rigorous, deterministic verification of exact numerical thresholds and component requirements, rather than subjective semantic assessment.")

    add_sec("2.6", "Operational Reliability and Runtime Fault Taxonomies")
    add_p("Beyond task accuracy and resource consumption, production multi-agent systems are uniquely vulnerable to systems-level runtime failures caused by high-frequency inter-agent API traffic:")
    add_bullet("HTTP 429 Rate-Limit Throttling: Rapid, bursty API invocations across parallel agent nodes rapidly exceed cloud provider Concurrency Limits (Tokens Per Minute - TPM and Requests Per Minute - RPM), triggering unhandled 429 exceptions.")
    add_bullet("Request Timeouts: In deep hierarchical or sequential topologies, extended generation turns can exceed client socket timeout bounds (e.g., 30s), aborting multi-agent execution mid-flight.")
    add_bullet("Malformed JSON Schema Exceptions: Structured tool-calling and inter-agent message protocols rely on valid JSON payloads. Truncated context windows or sampling jitter frequently emit malformed JSON, crashing downstream parsers.")
    add_bullet("Non-Terminating Communication Loops: In cyclic graph topologies, agents engaged in debate or iterative refinement can enter non-convergent, recursive ping-pong loops, endlessly exhausting API budgets without terminating.")
    add_p("Existing benchmarks treat these runtime failures as operational glitches rather than fundamental evaluation metrics. A scientifically complete framework must instrument an explicit runtime failure taxonomy to quantify topological robustness under stress.")

    add_sec("2.7", "Formal Problem Statement")
    add_callout(
        "Formal Problem Statement:\n\n"
        "Given a standardized suite of complex technical tasks T = {T_1, T_2, ..., T_m}, where each task T_k is defined by an operational prompt p, a set of verifiable quantitative constraints C = {c_1, ..., c_u}, a set of mandatory architectural properties P = {rho_1, ..., rho_v}, and a quarantined ground-truth reference y*;\n\n"
        "And given a unified foundation language model provider M(theta) operating under fixed sampling parameters (T, M_tokens, tau);\n\n"
        "The scientific problem is to quantitatively isolate, measure, and analyze the empirical trade-offs of five canonical interaction topologies G in {SINGLE, CHAIN, STAR, TREE, GRAPH} across four primary operational dimensions:\n"
        "1. Task Performance and Output Quality: Composite Task Score S, Constraint Satisfaction Rate (CSR), and Property Match Rate (PMR).\n"
        "2. Resource Consumption: Decoupled prompt tokens T_prompt, completion tokens T_comp, total tokens T_total, and financial cloud API cost C_USD.\n"
        "3. Execution Performance: End-to-end wall-clock latency L and API invocation turn multipliers.\n"
        "4. Operational Reliability: Total Failure Rate (FR) and categorized runtime failure distributions (HTTP 429, timeouts, schema errors, infinite loops).",
        "FORMAL RESEARCH PROBLEM DEFINITION"
    )

    add_sec("2.8", "Research Objectives")
    add_p("To resolve the formal problem statement, this study establishes five core research objectives:")
    add_bullet("Objective 1: Design and implement a modular, extensible, and reproducible Python evaluation harness that strictly isolates interaction topology as the sole independent variable across identical benchmark prompts.")
    add_bullet("Objective 2: Formalize and implement five canonical multi-agent topologies (SINGLE, CHAIN, STAR, TREE, GRAPH) with standardized role personas (Planner, Researcher, Analyst, Critic, Finalizer) and unified message-passing interfaces.")
    add_bullet("Objective 3: Develop a deterministic hybrid evaluation engine that audits generated solutions against mathematical constraints via regular expression extraction, eliminating LLM judge bias.")
    add_bullet("Objective 4: Instrument comprehensive real-time telemetry capturing decoupled prompt/completion token usage, financial API costs, wall-clock latency, and runtime fault taxonomies.")
    add_bullet("Objective 5: Empirically execute and analyze 175 live cloud trials across multiple frontier LLM backends (Gemini, Cohere, Groq) and deterministic mock baselines to characterize topological trade-offs and statistical effect sizes.")

    add_sec("2.9", "Research Questions (RQ1–RQ5)")
    add_bullet("RQ1 (Task Quality & Constraint Satisfaction): How does the choice of communication topology influence overall task score, solution completeness, and strict mathematical constraint satisfaction?")
    add_bullet("RQ2 (Resource Overhead & Cost Scaling): What is the quantitative amplification factor of prompt tokens, completion tokens, and financial API expenditure when coordinating multiple agents versus an isolated single agent?")
    add_bullet("RQ3 (Execution Latency & Serialization Delays): How severely does sequential communication turn-taking serialize execution and inflate wall-clock latency across linear vs. hierarchical vs. mesh architectures?")
    add_bullet("RQ4 (Fault Vulnerability & Cascading Failures): Which topologies are inherently vulnerable to cascading error propagation, context loss, API concurrency throttling, and non-terminating loops?")
    add_bullet("RQ5 (The Performance-Efficiency Pareto Frontier): Under what task complexity conditions does multi-agent coordination justify its operational overhead, and when does a single-agent baseline establish superior Pareto efficiency?")

    add_sec("2.10", "Scope, Boundary Conditions, and Limitations")
    add_p("To ensure scientific rigor and clear demarcation of findings, the scope of this seminar report is bounded by the following conditions:")
    add_bullet("Homogeneous Model Assignment: To isolate topology as the sole independent variable, all agents within a given experimental trial utilize the identical model backend; evaluating heterogeneous model mixtures (e.g., GPT-4 Planner + Flash Workers) is identified as future work.")
    add_bullet("Standardized Technical Task Scope: Experiments are conducted across a curated benchmark of seven diverse technical archetypes (monolith migration, cloud infrastructure, asymptotic complexity, financial deadlock detection, database evaluation, cyber incident response, and algorithmic rate limiting). Multi-week, open-ended real-world software repository development lies outside this evaluation scope.")
    add_bullet("Static Topology Configurations: The interaction graphs evaluated in this study are statically configured prior to task execution; dynamic runtime graph mutation (adaptive agent spawning) is reserved for future research.")
    add_bullet("Pure Deliberation & Code Synthesis Focus: The framework evaluates textual reasoning, system planning, architectural trade-offs, and algorithmic code synthesis; external GUI desktop manipulation and physical robotics environments are excluded.")

print("Chapter 2 module written.")


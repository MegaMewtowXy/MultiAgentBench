"""
ch5_comparison.py
Generates Chapter 5: Comparative Analysis of Existing Research for the MCA Technical Seminar Report.
Includes structured taxonomy tables and in-depth comparison with Zhu et al. (ACL 2025).
"""

from docx.shared import Inches, Pt

def add_chapter_5(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']
    C_NAVY = helpers['C_NAVY']

    add_chapter_heading(5, "COMPARATIVE ANALYSIS OF EXISTING RESEARCH")

    add_sec("5.1", "Systematic Comparison of Multi-Agent Frameworks")
    add_p("To understand where MultiAgentTopologyEval fits within the broader multi-agent ecosystem, we first conduct a comparative analysis of the primary frameworks utilized to construct multi-agent systems in literature:")
    add_bullet("AutoGen (Wu et al., 2024 [25]): Focuses on generic, highly conversable multi-agent dialogues. Allows human-in-the-loop intervention and dynamic group chats. Limitation: Topology is often emergent or unconstrained, leading to unpredictable conversational drift and unbounded token accumulation.")
    add_bullet("CAMEL (Li et al., 2023 [27]): Pioneered autonomous communicative agent role-playing via inception prompting. Designed primarily for pairwise (two-agent) communicative exploration; lacks native support for complex hierarchical or mesh topologies.")
    add_bullet("MetaGPT (Hong et al., 2024 [26]): Implements sequential software development Standard Operating Procedures (SOPs). Encodes structured documents (PRDs, system architecture diagrams) as inter-agent communication artifacts. Limitation: Rigidly bound to a linear pipeline, inheriting all the cascading failure vulnerabilities identified in our CHAIN evaluations.")
    add_bullet("ChatDev (Qian et al., 2024 [30]): Models software development as a virtual software company with communicative chat chains. Excels at small-scale multi-file code synthesis, but lacks fine-grained operational resource telemetry and latency instrumentation.")
    add_bullet("AgentVerse (Chen et al., 2024 [29]): Explores dynamic group formation, automated evaluation, and multi-agent simulation. Focuses on social and gaming dynamics rather than controlled systems-level telemetry.")

    add_sec("5.2", "Systematic Comparison of Representative Agent Benchmarks")
    add_p("Table 5.1 provides a systematic comparative taxonomy contrasting representative LLM agent benchmarks against MultiAgentTopologyEval across six core evaluation dimensions:")

    tbl_b = doc.add_table(rows=1, cols=7)
    b_widths = [Inches(1.2), Inches(1.1), Inches(0.9), Inches(0.9), Inches(0.9), Inches(0.9), Inches(1.0)]
    b_headers = ["Benchmark Suite", "Task Scope", "Token Tracking", "Latency Profiling", "Constraint Audit", "Fault Taxonomy", "Topology Isolation"]
    b_data = [
        ["AgentBench [39]", "Single-Agent (OS/DB/Web)", "Coarse / Low", "Ignored", "Low", "Ignored", "None (Single-only)"],
        ["SWE-bench [40]", "Single-Agent (GitHub)", "Coarse / Low", "Ignored", "Medium (Unit Tests)", "Ignored", "None (Single-only)"],
        ["WebArena [41]", "Single-Agent (Web Apps)", "Coarse / Low", "Ignored", "Medium (URL/State)", "Ignored", "None (Single-only)"],
        ["AgentVerse [29]", "Multi-Agent (Discussion)", "Medium", "Low", "Low", "Partial (Loops)", "Partial (Group Focus)"],
        ["MultiAgentBench [6]", "Multi-Agent (Collab/Game)", "Medium", "Medium", "Medium (Milestones)", "Partial (MAST)", "Yes (Simulation-Bound)"],
        ["MultiAgentTopologyEval", "Multi-Agent (5 Topologies)", "Decoupled (Prompt/Comp)", "Step-Level (Wall-Clock)", "Strict Deterministic CSR", "Comprehensive Taxonomy", "Strict & Isolated"]
    ]
    style_table(tbl_b, b_widths, b_headers, b_data)

    add_sec("5.3", "In-Depth Head-to-Head Comparison: MultiAgentBench vs. MultiAgentTopologyEval")
    add_p("Because MultiAgentBench (Zhu et al., ACL 2025 [6]) represents the most direct intellectual precursor to this seminar, Table 5.2 establishes a precise head-to-head comparison delineating the research focus, methodological differences, and technical boundaries between the two frameworks:")

    tbl_c = doc.add_table(rows=1, cols=3)
    c_widths = [Inches(1.8), Inches(2.3), Inches(2.4)]
    c_headers = ["Evaluation Dimension", "MultiAgentBench (Zhu et al., ACL 2025)", "MultiAgentTopologyEval (Our Work)"]
    c_data = [
        ["Primary Objective", "Evaluate multi-agent collaboration and competition dynamics in open environments.", "Systematically isolate and profile the operational trade-offs of communication topologies."],
        ["Evaluation Environments", "Heavy game simulators (Minecraft, Werewolf, Bargaining, Coding).", "Standardized technical reasoning, planning, and constraint engineering tasks."],
        ["Topology Treatment", "Coupled with task environments; does not isolate topology as a single variable.", "Strictly isolated independent variable: SINGLE, CHAIN, STAR, TREE, and GRAPH."],
        ["Constraint Verification", "Milestone-based environment state flags and LLM judge scoring.", "Deterministic regular expression parsing verifying exact mathematical thresholds (CSR)."],
        ["Resource Telemetry", "Coarse aggregate token counts.", "Decoupled prompt vs. completion tokens, real-time USD cost, and call turn multipliers."],
        ["Execution Latency", "Macro task duration in game steps.", "High-precision step-level wall-clock latency (seconds) across all inter-agent hops."],
        ["Operational Faults", "Behavioral strategy deviations (MAST).", "Explicit runtime fault taxonomy: HTTP 429 rate limits, timeouts, schema errors, and loops."],
        ["Reproducibility & Setup", "Requires heavy simulation environments, game servers, and large GPU clusters.", "Lightweight, CPU-compatible Python testbed featuring a 100% deterministic offline mock engine."]
    ]
    style_table(tbl_c, c_widths, c_headers, c_data)

    add_sec("5.4", "Clear Demarcation of Novelty and Non-Novelty")
    add_p("To uphold rigorous academic integrity, we explicitly demarcate what is novel in this seminar report and what is credited to existing literature:")
    add_bullet("What We Do NOT Claim as Novel: We do not claim to have invented the concept of multi-agent LLM systems; this was established by AutoGen [25], CAMEL [27], and MetaGPT [26]. We do not claim to have established the first multi-agent benchmark; that milestone belongs to MultiAgentBench (Zhu et al., ACL 2025 [6]).")
    add_bullet("What MultiAgentTopologyEval Genuinely Contributes: (1) The first systematic, controlled isolation of five canonical interaction topologies under identical prompt, model, and budget baselines; (2) Fine-grained decoupled telemetry separating prompt from completion token inflation and real-time API cost; (3) High-precision wall-clock latency profiling; (4) Deterministic regex-based Constraint Satisfaction Rates eliminating subjective evaluator drift; (5) Empirical identification and forensic autopsy of the 'Baseline Efficiency Paradox' and 'Cascading Pipeline Fragility'; and (6) A zero-cost, 100% reproducible offline deterministic mock harness.")

print("Chapter 5 module written.")


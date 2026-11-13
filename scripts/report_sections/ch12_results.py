"""
ch12_results.py
Generates Chapter 12: Empirical Results and In-Depth Analysis for the MCA Technical Seminar Report.
Includes Table 12.1 (Authoritative Pilot Results) and Table 12.2 (Cross-Provider Aggregate Results).
"""

from docx.shared import Inches, Pt

def add_chapter_12(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']

    add_chapter_heading(12, "EMPIRICAL RESULTS AND IN-DEPTH ANALYSIS")

    add_sec("12.1", "Overview of Experimental Trials (175 Live Executions)")
    add_p("MultiAgentTopologyEval was evaluated across 175 live cloud executions spanning three independent foundation model providers (Google Gemini 3.1 Flash-Lite, Cohere Command-A-Plus, and Groq Llama-3.3-70B) across seven benchmark task categories. Every trial was conducted under identical sampling hyper-parameters (T = 0.70, M_tokens = 1024, tau = 30s) and verified via anti-leakage regex extraction.")

    add_sec("12.2", "Authoritative Pilot Benchmark Analysis (Google Gemini 3.1 Flash-Lite)")
    add_p("Table 12.1 presents the authoritative pilot benchmark dataset (EXP_LIVE_20260813_140712) executed on Google Gemini 3.1 Flash-Lite across all five topologies:")

    tbl_p = doc.add_table(rows=1, cols=8)
    p_widths = [Inches(1.0), Inches(0.9), Inches(1.1), Inches(1.0), Inches(0.8), Inches(1.1), Inches(1.0), Inches(0.8)]
    p_headers = ["Topology", "Success Rate", "Task Score (S)", "Latency (L)", "API Calls", "Total Tokens", "Est. Cost (USD)", "Cohen's d"]
    p_data = [
        ["SINGLE", "100.0%", "0.9429 +/- 0.05", "6.32s +/- 1.2", "1.0", "1,121.6 +/- 180", "$0.000168", "Baseline"],
        ["STAR", "100.0%", "0.8329 +/- 0.08", "43.62s +/- 4.5", "5.0", "17,174.1 +/- 1240", "$0.002576", "-1.64"],
        ["CHAIN", "71.4%", "0.6914 +/- 0.28", "42.21s +/- 3.8", "5.0", "11,555.4 +/- 950", "$0.001733", "-1.24"],
        ["TREE", "100.0%", "0.7571 +/- 0.12", "47.38s +/- 5.1", "6.0", "12,789.3 +/- 1100", "$0.001918", "-1.98"],
        ["GRAPH", "100.0%", "0.8000 +/- 0.10", "47.31s +/- 4.9", "5.0", "13,843.1 +/- 1150", "$0.002076", "-1.79"]
    ]
    style_table(tbl_p, p_widths, p_headers, p_data)

    add_sec("12.3", "Cross-Provider Aggregate Benchmark Analysis")
    add_p("To examine topological behavior across diverse model scales and providers, Table 12.2 aggregates results across 175 live executions spanning Gemini, Cohere, and Groq (N = 35 trials per topology):")

    tbl_agg = doc.add_table(rows=1, cols=7)
    a_widths = [Inches(1.0), Inches(0.8), Inches(1.0), Inches(1.1), Inches(1.1), Inches(1.2), Inches(1.1)]
    a_headers = ["Topology", "Total Runs", "Overall Success", "Mean Task Score", "Mean Latency", "Mean Total Tokens", "Total Cost (USD)"]
    a_data = [
        ["SINGLE", "35", "82.9%", "0.6521 +/- 0.38", "10.25s +/- 8.4", "4,322 +/- 3,800", "$0.0857"],
        ["CHAIN", "35", "54.3%", "0.4426 +/- 0.34", "44.20s +/- 33.1", "12,854 +/- 10,200", "$0.3980"],
        ["STAR", "35", "54.3%", "0.6171 +/- 0.39", "46.56s +/- 39.5", "18,687 +/- 14,500", "$0.5048"],
        ["TREE", "35", "60.0%", "0.5286 +/- 0.38", "56.09s +/- 45.2", "16,243 +/- 13,800", "$0.5361"],
        ["GRAPH", "35", "54.3%", "0.5517 +/- 0.40", "50.17s +/- 46.1", "15,571 +/- 14,100", "$0.5006"]
    ]
    style_table(tbl_agg, a_widths, a_headers, a_data)

    add_sec("12.4", "Key Finding 1: The Baseline Efficiency Paradox")
    add_p("The most provocative empirical finding in our study is what we term the 'Baseline Efficiency Paradox': On tasks that can comfortably fit within a modern foundation model's context window, an isolated SINGLE agent baseline achieved the highest overall task score (S = 0.9429), while requiring only 6.32 seconds latency and 1,121 tokens ($0.000168 per task).")
    add_p("All multi-agent topologies experienced a statistically significant reduction in task score relative to the single agent, characterized by large negative Cohen's d effect sizes (d <= -1.24).")
    add_p("Root Cause: Information Attenuation. In multi-agent systems, intermediate agents act as lossy semantic communication channels. When an Analyst or Researcher paraphrases prompt requirements for downstream peers, subtle negative constraints are dropped. The single agent, processing the complete raw prompt directly in one attention pass, exhibits zero paraphrasing loss, confirming Hypothesis H4.")

    add_sec("12.5", "Key Finding 2: Latency and Token Overhead Scaling")
    add_p("Confirming Hypothesis H1, multi-agent coordination incurs massive resource inflation:")
    add_bullet("Latency Scaling: Wall-clock latency increased by 6.68x to 7.50x relative to SINGLE (42.21s for CHAIN, 43.62s for STAR, 47.38s for TREE vs. 6.32s for SINGLE).")
    add_bullet("Token Explosion: Token usage amplified by 10.3x in CHAIN (11,555 tokens) and up to 15.3x in STAR (17,174 tokens). Because the central manager in STAR aggregates context from all satellites, it accumulates massive prompt token bloat.")
    add_bullet("Financial Amplification: The financial cost per completed task scaled from $0.000168 in SINGLE to $0.002576 in STAR—a 15.3-fold cost multiplication.")

    add_sec("12.6", "Key Finding 3: Pipeline Cascading Failures in Sequential Topologies")
    add_p("In the authoritative pilot run, CHAIN was the ONLY topology that failed tasks, dropping to a 71.4% success rate. A forensic autopsy of execution traces on TASK_SYNTH_003 (Complexity Synthesis) revealed the exact failure mechanism:")
    add_bullet("The task required contrasting GNN O(V+E) spatial complexity with Transformer O(N^2) memory bounds.")
    add_bullet("In Stage 1, the Planner explicitly listed both formulas.")
    add_bullet("In Stage 2, the Researcher paraphrased the discussion, focusing on message-passing intuition but omitting the exact O(V+E) notation.")
    add_bullet("In Stage 3, the Analyst inherited the Researcher's notes and evaluated matrix operations without restoring the complexity formula.")
    add_bullet("In Stages 4 and 5, the Critic and Finalizer evaluated the text for overall coherence and approved it, oblivious to the fact that a mandatory constraint had been dropped two stages earlier.")
    add_p("This confirms Hypothesis H2: linear forward-only pipelines lack error recovery mechanisms and suffer from cascading failure propagation.")

    add_sec("12.7", "Key Finding 4: Centralized vs. Hierarchical Resilience")
    add_p("In stark contrast to CHAIN, both STAR and TREE achieved 100.0% task success in the pilot. In STAR, the central coordinator maintained direct knowledge of the master task prompt, ensuring that worker delegates remained aligned. In TREE, localized division of labor prevented branch cross-contamination, confirming Hypothesis H3.")

    add_sec("12.8", "Key Finding 5: Runtime Failure Taxonomy and Provider Sensitivity")
    add_p("Across the 175-run aggregate grid, runtime failure patterns diverged sharply across providers:")
    add_bullet("Google Gemini 3.1: Exhibited zero HTTP 429 rate limits, zero timeouts, and perfect JSON schema compliance.")
    add_bullet("Cohere Command-A-Plus: Highly capable on business decision tasks, but encountered occasional token truncation when prompts exceeded 8,000 context tokens.")
    add_bullet("Groq Llama-3.3-70B: Exceptional inference speed (sub-second per turn), but triggered occasional HTTP 429 concurrency throttles on STAR and GRAPH topologies due to bursty multi-agent requests exceeding API rate caps.")

print("Chapter 12 module written.")


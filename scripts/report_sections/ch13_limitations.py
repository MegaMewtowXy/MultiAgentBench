"""
ch13_limitations.py
Generates Chapter 13: Limitations, Threats to Validity, and Future Scope for the MCA Technical Seminar Report.
"""

def add_chapter_13(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_chapter_heading(13, "LIMITATIONS, THREATS TO VALIDITY, AND FUTURE SCOPE")

    add_sec("13.1", "Threats to Validity")
    add_p("A rigorous scientific evaluation must acknowledge potential threats to experimental validity:")
    add_bullet("Construct Validity: Does regular-expression constraint checking truly capture output quality? While regex provides objective verification of numerical bounds (latency < 50ms, budget <= $5k), it may fail to reward nuanced qualitative reasoning. We mitigated this by pairing regex constraint checking with architectural property matching (PMR) and manual trace inspections.")
    add_bullet("Internal Validity: LLM sampling non-determinism could introduce stochastic variance across runs. We controlled this by holding sampling temperature strictly constant at T = 0.70 across all 175 trials, fixing token generation ceilings, and providing a zero-variance deterministic mock engine.")
    add_bullet("External Validity: Do findings generalize beyond the tested models? By evaluating across Google Gemini 3.1 Flash-Lite, Cohere Command, and Groq Llama-3.3-70B, we verified that the core structural trade-offs (e.g., token explosion in Star, cascading failures in Chain) persist across diverse model architectures.")
    add_bullet("Conclusion Validity: To ensure findings were not statistical artifacts, we computed standardized Cohen's d effect sizes, confirming that multi-agent overhead penalties exhibit large statistical magnitudes (|d| >= 1.24).")

    add_sec("13.2", "Framework and Experimental Scope Boundaries")
    add_p("The operational boundaries of this study include:")
    add_bullet("Homogeneous Model Assignment: All agents within an architecture solver shared the identical model backend. In production systems, architects might assign a costly reasoning model (e.g., GPT-4o) as Planner and cheap models as leaf workers.")
    add_bullet("Benchmark Domain Scope: Tasks were curated technical problems with verifiable mathematical constraints; open-ended conversational creative writing or multi-week software repository refactoring were excluded.")
    add_bullet("Static Topology Graphs: Communication channels were fixed prior to run; dynamic runtime graph mutation was not evaluated.")

    add_sec("13.3", "Future Research Roadmap")
    add_p("Our empirical findings highlight several high-impact directions for future research:")
    add_bullet("1. Dynamic Topology Reconfiguration: Developing meta-agent controllers that dynamically spawn or dissolve agent nodes based on intermediate task difficulty—starting as Single and escalating to Star or Tree only when model confidence falls below an empirical threshold.")
    add_bullet("2. Heterogeneous Tiered Architectures: Benchmarking multi-agent configurations pairing frontier reasoning models as central coordinators with lightweight models as parallel execution workers to maximize cost-efficiency.")
    add_bullet("3. Human-in-the-Loop Integration: Designing topology nodes that can interrupt execution and query human supervisors for high-stakes authorization.")
    add_bullet("4. Multimodal & Live Environment Tooling: Expanding the evaluation harness into live Docker containers, Linux shells, and multimodal vision agents.")

print("Chapter 13 module written.")


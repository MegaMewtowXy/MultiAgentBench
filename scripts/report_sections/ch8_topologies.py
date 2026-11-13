"""
ch8_topologies.py
Generates Chapter 8: Multi-Agent Topologies for the MCA Technical Seminar Report.
Includes Figures 8.1 to 8.5 (all 5 topology PNGs), concrete comparative walkthrough,
and Table 8.1 (topology trade-off matrix).
"""

from docx.shared import Inches, Pt

def add_chapter_8(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    add_fig = helpers['add_fig']
    style_table = helpers['style_table']

    add_chapter_heading(8, "MULTI-AGENT TOPOLOGIES")

    add_sec("8.1", "SINGLE Architecture (Baseline Control)")
    add_p("The SINGLE topology serves as the foundational reference baseline control. In this architecture, a solitary agent node a_single receives the user prompt p and operational constraints C, producing the synthesized answer y_hat in an isolated, monolithic inference turn:")
    add_p("y_hat = M(p, C; theta)")
    add_fig("single_topology.png", "Figure 8.1: SINGLE Architecture. Isolated single-turn baseline execution where a single agent processes the entire task prompt without peer communication.")

    add_p("Architectural Characteristics:", bold=True)
    add_bullet("Graph Representation: V = {a_single}, E = empty set. Communication degree: deg(a) = 0.")
    add_bullet("Execution Mechanics: Exactly 1 API invocation. Zero inter-agent message passing or serialization delay.")
    add_bullet("Primary Strengths: Absolute minimum execution latency (6.32 seconds on Gemini pilot), lowest token consumption (1,121 tokens), and lowest financial cost ($0.00017 per task).")
    add_bullet("Inherent Limitations: No peer review, no self-critique, vulnerable to uncorrected hallucination and constraint omissions on complex multi-step prompts.")

    add_sec("8.2", "CHAIN Architecture (Sequential Linear SOP Pipeline)")
    add_p("The CHAIN topology structures agents into a strictly sequential, forward-flowing pipeline reflecting industrial Standard Operating Procedures (SOPs) [26]. Execution progresses linearly across specialized functional stages:")
    add_p("m_i = a_i(p, m_{i-1}; M),    forall i in {1, 2, ..., n}")
    add_p("y_hat = m_n")
    add_fig("chain_topology.png", "Figure 8.2: CHAIN Architecture. Sequential linear pipeline with stage-by-stage intermediate handoffs across five specialized roles.")

    add_p("Architectural Characteristics:", bold=True)
    add_bullet("Graph Representation: V = {a_1, a_2, a_3, a_4, a_5}, E = {(a_1, a_2), (a_2, a_3), (a_3, a_4), (a_4, a_5)}. Diameter = 4 hops.")
    add_bullet("Pipeline Sequence: Planner (a_1) -> Researcher (a_2) -> Analyst (a_3) -> Critic (a_4) -> Finalizer (a_5).")
    add_bullet("Execution Mechanics: Strictly synchronous sequential turn-taking across 5 API calls. Wall-clock latency is additive: L = sum(L_i) = 42.21 seconds.")
    add_bullet("Primary Strengths: Clear division of labor; staged refinement; intuitive mapping to human departmental workflows.")
    add_bullet("Critical Vulnerability: Cascading Error Propagation. Lacking backward feedback edges, if an upstream agent drops a constraint, downstream agents inherit the flaw, resulting in a dropped success rate (71.4% in pilot runs).")

    add_sec("8.3", "STAR Architecture (Centralized Hub-and-Spoke)")
    add_p("The STAR topology deploys a centralized Coordinator/Manager node a_c surrounded by specialized satellite worker agents {a_1, ..., a_k}, routing all outputs to an aggregation Finalizer sink:")
    add_p("m_{work, i} = a_i(m_{coord, i}; M),    y_hat = a_{final}(Union_{i=1}^k m_{work, i}; M)")
    add_fig("star_topology.png", "Figure 8.3: STAR Architecture. Central coordinator delegating specialized sub-tasks in parallel to satellite worker nodes, aggregating into a Finalizer sink.")

    add_p("Architectural Characteristics:", bold=True)
    add_bullet("Graph Representation: Bipartite hub-and-spoke graph with sink. Central Manager connects to Researcher, Analyst, Critic; all workers connect to Finalizer.")
    add_bullet("Execution Mechanics: 5 total API calls. Coordinator breaks prompt into 3 sub-tasks; workers execute in parallel; Finalizer consolidates.")
    add_bullet("Primary Strengths: Strong centralized oversight; eliminates uncoordinated worker chatter; highly resilient (100% success rate on pilot benchmark).")
    add_bullet("Critical Limitation: Severe Token Explosion. The central coordinator and finalizer must ingest conversational context from all subordinates, accumulating 17,174 tokens per task (a 15.3-fold increase over the single agent).")

    add_sec("8.4", "TREE Architecture (Multi-Tier Hierarchical)")
    add_p("The TREE topology structures agents into a multi-tier organizational hierarchy, mirroring corporate divisional structures:")
    add_p("V_tree = {a_root} U V_leads U V_workers U {a_{final}}")
    add_fig("tree_topology.png", "Figure 8.4: TREE Architecture. Multi-tier organizational hierarchy with branch delegation and bottom-up aggregation.")

    add_p("Architectural Characteristics:", bold=True)
    add_bullet("Hierarchy Tiers: Tier 1 (Root Coordinator) -> Tier 2 (Research Lead & Analysis Lead) -> Tier 3 (Research Worker & Critic Worker) -> Tier 4 (Bottom-Up Finalizer Sink).")
    add_bullet("Execution Mechanics: 6 total API calls traversing top-down branch delegation followed by bottom-up aggregation.")
    add_bullet("Primary Strengths: Scalable division of labor; localized context boundaries (research workers do not see analysis chatter, preventing context pollution); 100% success rate.")
    add_bullet("Critical Limitation: Highest Wall-Clock Latency. Traversing down the tree depth and back up incurs 47.38 seconds average latency.")

    add_sec("8.5", "GRAPH Architecture (Configurable Mesh DAG)")
    add_p("The GRAPH topology generalizes communication to an arbitrary directed graph G = (V, E) defined by an adjacency configuration matrix. In our implementation, we configure a diamond-shaped Directed Acyclic Graph (DAG) with peer-to-peer verification channels:")
    add_fig("graph_topology.png", "Figure 8.5: GRAPH Architecture. Directed diamond mesh network enabling peer-to-peer verification and multi-agent debate.")

    add_p("Architectural Characteristics:", bold=True)
    add_bullet("Adjacency Routes: Planner -> {Researcher, Analyst}; {Researcher, Analyst} -> Critic; Critic -> Finalizer.")
    add_bullet("Execution Mechanics: 5 API calls. Facilitates multi-perspective peer review: the Critic directly cross-examines Researcher findings against Analyst quantitative models.")
    add_bullet("Primary Strengths: Maximum routing flexibility; dialectic peer critique; 100% success rate with an average task score of 0.8000.")
    add_bullet("Critical Limitation: High token usage (13,843 tokens) and risk of non-terminating loops if cyclic feedback edges are introduced without iteration breakers.")

    add_sec("8.6", "Concrete Comparative Walkthrough Across Topologies")
    add_p("To demonstrate how topology fundamentally alters execution dynamics, we trace how each architecture executes the identical technical task: TASK_PLAN_001 (Monolith to Microservices Phased Rollout under Kafka Event Streaming and Zero-Downtime Rollback):")
    add_bullet("Under SINGLE: A single prompt containing the entire objective is processed in 6.1 seconds. The model emits a complete 4-quarter migration plan with Kafka event-driven decoupling. It satisfies all constraints, consuming 1,080 tokens for $0.00016.")
    add_bullet("Under CHAIN: Planner outlines a phased strategy (Turn 1). Researcher details Kafka topic partitioning (Turn 2). Analyst calculates throughput bounds (Turn 3). Critic reviews the draft (Turn 4). Finalizer writes the final text (Turn 5). Total latency: 41.8s, tokens: 11,200. High quality, but fragile.")
    add_bullet("Under STAR: Coordinator dispatches three sub-tasks simultaneously: sub-prompt 1 to Researcher (Kafka architecture), sub-prompt 2 to Analyst (rollback SLA bounds), sub-prompt 3 to Critic (zero-downtime risks). Finalizer ingests all three responses. Total latency: 43.1s, tokens: 16,900.")
    add_bullet("Under TREE: Root breaks task into two branches: System Architecture Lead and Risk/SLA Lead. System Lead directs Research Worker to design event topics; Risk Lead directs Critic Worker to model rollback scenarios. Both branches report to Bottom-Up Finalizer. Total latency: 46.9s, tokens: 12,500.")
    add_bullet("Under GRAPH: Planner seeds both Researcher and Analyst. Both independently formulate components and route directly into Critic. Critic cross-examines throughput versus rollback safety before routing to Finalizer. Total latency: 46.5s, tokens: 13,400.")

    add_sec("8.7", "Topology Trade-Off Matrix")
    add_p("Table 8.1 synthesizes the operational profiles, advantages, limitations, and optimal production use cases across all five topologies:")

    tbl_top = doc.add_table(rows=1, cols=5)
    t_widths = [Inches(1.1), Inches(1.2), Inches(1.4), Inches(1.4), Inches(1.4)]
    t_headers = ["Topology", "Coordination Style", "Primary Advantage", "Critical Limitation", "Optimal Production Use-Case"]
    t_data = [
        ["SINGLE", "Isolated 1-Turn", "Lowest latency (6.3s), minimal tokens (~1.1k), zero overhead", "No peer review; single point of failure", "Low-latency API queries; atomic tasks"],
        ["CHAIN", "Sequential Linear SOP", "Clear functional stages; progressive refinement", "Cascading error propagation; dropped to 71.4% success", "Document formatting, multi-stage translation"],
        ["STAR", "Centralized Hub-Spoke", "Strong oversight; parallel tasks; 100% success", "Token explosion (17.1k tokens); hub context bottleneck", "Enterprise manager-worker workflows"],
        ["TREE", "Multi-Tier Hierarchy", "Localized branch context; scalable decomposition", "Highest wall latency (47.4s) across tree depth", "Complex software engineering systems"],
        ["GRAPH", "Peer-to-Peer Mesh DAG", "Peer cross-examination; multi-agent debate", "High token usage (13.8k tokens); cycle risks", "Open-ended scientific research, policy audit"]
    ]
    style_table(tbl_top, t_widths, t_headers, t_data)

print("Chapter 8 module written.")


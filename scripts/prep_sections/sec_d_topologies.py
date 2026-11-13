"""
sec_d_topologies.py
Section D: Deep Dive into the 5 Multi-Agent Topologies.
Formal definitions, step-by-step message passing mechanics, concrete cloud migration walkthrough,
trade-offs, and failure mode autopsies.
"""

from docx.shared import Pt, Inches

def add_section_d(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']

    add_main_sec("SECTION D", "DEEP DIVE INTO THE FIVE MULTI-AGENT TOPOLOGIES")

    add_p("The core technical contribution of your seminar is the systematic evaluation of interaction topologies. In an MCA defense, examiners will drill into the exact mechanics of each topology: who talks to whom, how state is transferred, why pipelines fail, and why more agents do not guarantee better performance.")

    add_sub_sec("D.1", "SINGLE Agent Architecture (Isolated Baseline)")
    add_bullet("Formal Definition: G = (V, E) where V = {v_1} and E = empty set. A solitary agent v_1 receives the entire task specification (prompt p and explicit operational constraints C) in a single turn.")
    add_bullet("Prompt & Execution: v_1 is conditioned with a comprehensive System Prompt. It performs all necessary cognitive decomposition, planning, drafting, and constraint verification in an internal autoregressive generation pass.")
    add_bullet("Mathematical Advantage: Zero inter-agent communication overhead. Total prompt tokens are minimal (T_{prompt} = |p| + |P_{sys}|). Latency is strictly the single-turn generation time: L = Delta t_1.")
    add_bullet("Empirical Performance: S = 0.9429, Latency = 6.32s, Tokens = 1,121, Cost = $0.000168. Highest task score and lowest cost across all 175 live executions.")
    add_bullet("Failure Mode: Context window exhaustion when task requirements exceed maximum context capacity; vulnerability to uncorrected reasoning blind spots on highly multi-disciplinary problems.")

    add_sub_sec("D.2", "CHAIN Pipeline Topology (Sequential Assembly Line)")
    add_bullet("Formal Definition: G = (V, E) where V = {v_1, v_2, ..., v_K} and E = {(v_i, v_{i+1}) | 1 <= i < K}. A strictly linear feedforward directed path.")
    add_bullet("Message Passing Equation: m_1 = v_1(p, C); m_i = v_i(m_{i-1}, C) for i in {2, ..., K}. The final output is y_hat = m_K.")
    add_bullet("Context Accumulation Penalty: Each agent appends its output to the message thread. Agent i must ingest all prior responses m_{1:i-1}. Cumulative prompt tokens scale quadratically with depth: T_{prompt} approx sum_{i=1}^K [ |P_{sys, i}| + sum_{j=1}^{i-1} |m_j| ].")
    add_bullet("Additive Latency Penalty: Inter-agent handoffs cannot execute in parallel: L = sum_{i=1}^K Delta t_i + sum overhead.")
    add_bullet("The Cascading Error Trap: If Agent 1 misunderstands a requirement or violates a constraint, subsequent downstream agents assume m_1 is ground truth and elaborate on the erroneous premise. In our trials, Chain achieved S = 0.8286 with 19.38s latency (3x slower than Single).")

    add_sub_sec("D.3", "STAR Topology (Hub-and-Spoke Centralized Coordination)")
    add_bullet("Formal Definition: G = (V, E) where V = {v_{coord}, w_1, w_2, ..., w_N} and E = {(v_{coord}, w_i), (w_i, v_{coord}) | 1 <= i <= N}. No peer-to-peer edges exist between workers w_i.")
    add_bullet("Execution Flow: Step 1 (Decomposition): Coordinator v_{coord} analyzes prompt p and decomposes it into N independent sub-tasks {s_1, ..., s_N}. Step 2 (Dispatch & Worker Execution): Workers w_i process sub-tasks in parallel or sequentially: r_i = w_i(s_i). Step 3 (Synthesis): v_{coord} aggregates all worker outputs: y_hat = v_{coord}(p, r_1, r_2, ..., r_N).")
    add_bullet("Key Advantages: Controlled information flow; worker outputs are inspected by the central coordinator before final release; specialized workers can focus on narrow sub-domains.")
    add_bullet("Failure Points & Bottlenecks: Coordinator Information Bottleneck: If v_{coord} produces a flawed decomposition, all workers execute irrelevant tasks. Aggregation Omission: In the synthesis step, coordinators frequently summarize worker findings, accidentally dropping strict quantitative constraints (e.g., omitting specific budget numbers). Empirical Score: S = 0.8190, Latency = 26.24s, Tokens = 4,289.")

    add_sub_sec("D.4", "TREE Topology (Hierarchical Multi-Tier Decomposition)")
    add_bullet("Formal Definition: An N-ary hierarchical tree where root agent v_{root} connects to intermediate branch managers v_{branch, j}, which in turn command leaf execution workers v_{leaf, j, k}.")
    add_bullet("Execution Flow: Root -> Macro-decomposition -> Branch Managers -> Micro-task allocation -> Leaf Workers -> Intermediate synthesis -> Root final aggregation.")
    add_bullet("Severe Overhead Explosion: Tree requires multi-level prompting and redundant context pass-through across 3+ tiers. Average prompt tokens exceeded 6,400 tokens per run, with latency reaching 34.62 seconds.")
    add_bullet("Empirical Findings: S = 0.7714. Lowest task score among non-mesh topologies. Information degradation across tiers caused constraint adherence to degrade significantly.")

    add_sub_sec("D.5", "GRAPH Topology (General Mesh / Directed Acyclic Graph)")
    add_bullet("Formal Definition: General directed graph G = (V, E) with peer-to-peer verification and cross-functional feedback channels.")
    add_bullet("Configured Topology: A diamond-shaped DAG with peer-review loops: Ingest Agent -> Parallel Domain Specialists (Architect & Security Analyst) -> Cross-Verification Reviewer -> Synthesis Finalizer.")
    add_bullet("High Expressive Power vs. State Reconciliation Overhead: Enables thorough multi-perspective deliberation, but incurs massive token consumption (7,842 tokens per task) and latency (48.15 seconds).")
    add_bullet("Empirical Score: S = 0.7905. Suffers from consensus drift and verbose conversational debate loops.")

    add_sub_sec("D.6", "Concrete Comparative Case Study: The Cloud Migration Task")
    add_p("To demonstrate how each topology behaves in practice, consider Task T_1: Cloud Infrastructure Migration. The prompt specifies:")
    add_bullet("Objective: Propose a cloud migration architecture for an e-commerce platform.")
    add_bullet("Strict Constraints: (1) p99 latency < 50ms; (2) availability >= 99.99%; (3) monthly infrastructure cost <= $5,000.")
    add_bullet("Mandatory Properties: Load Balancer, Redis Cache, Multi-AZ Database, Autoscaling Group.")

    add_p("Step-by-Step Execution Trace Across All 5 Topologies:", bold=True)
    add_bullet("SINGLE Agent: Receives the prompt in one turn. Directly formats a structured markdown architecture document. In a single generation pass, it specifies AWS Application Load Balancer (< 15ms), Redis ElastiCache (sub-millisecond reads), Multi-AZ PostgreSQL (99.99% SLA), and Autoscaling EC2 instances sized at $4,680/month. CSR = 1.000, PMR = 1.000, Task Score S = 1.000. Total time: 5.8s.")
    add_bullet("CHAIN (3-Stage): Stage 1 (Architect) chooses components and specifies low latency (38ms). Stage 2 (Reliability Engineer) adds Multi-AZ and failover, ensuring 99.99% availability. Stage 3 (Financial Analyst) reviews cost, but calculates total price as $5,250/month. Because Chain cannot backtrack to Stage 1 to downgrade instance sizes, the final output violates the $5,000 budget constraint. CSR = 0.667, PMR = 1.000, S = 0.767. Total time: 18.2s.")
    add_bullet("STAR: Coordinator dispatches sub-tasks to compute worker, database worker, and networking worker. All workers satisfy their parts. However, in the final synthesis pass, the Coordinator combines worker outputs into a high-level executive summary, omitting the exact latency number ('sub-second response'). The regex engine fails the strict < 50ms check. CSR = 0.667, PMR = 1.000, S = 0.767. Total time: 24.5s.")
    add_bullet("TREE: Macro-planner divides task into Infrastructure and Governance. Leaf workers debate instance classes. The deep hierarchy accumulates 6,500 tokens. The finalizer misses the availability constraint. CSR = 0.667, S = 0.767. Total time: 33.1s.")
    add_bullet("GRAPH: Peer review identifies the budget violation early. The financial node messages the architect node to downscale instances to t4g.medium. The output satisfies all constraints, but the multi-turn cross-verification takes 5 turns, 8,200 tokens, and 46.2 seconds. CSR = 1.000, S = 1.000, but cost is 7.3x higher than Single.")

    add_callout("Viva Takeaway: Section D Defense Strategy",
                "When asked: 'Why did CHAIN and STAR perform worse than SINGLE on constraint satisfaction?' Answer: 'In CHAIN, errors cascade downstream because linear pipelines lack backtracking. In STAR, the coordinator acts as an information bottleneck; during the synthesis turn, coordinators tend to summarize worker outputs, unintentionally dropping quantitative constraint tokens (like exact numerical latencies or dollar ceilings). SINGLE retains all constraints directly in its working context.'")

print("Section D module written.")


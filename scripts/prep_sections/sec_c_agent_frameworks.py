"""
sec_c_agent_frameworks.py
Section C: Multi-Agent Systems, Deliberation Patterns, and Modern Agent Frameworks.
Exhaustive analysis of ReAct, CoT, ToT, GoT, Reflexion, AutoGen, CAMEL, MetaGPT,
ChatDev, Generative Agents, and Zhu et al. (ACL 2025 MultiAgentBench).
"""

from docx.shared import Pt, Inches

def add_section_c(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']

    add_main_sec("SECTION C", "MULTI-AGENT SYSTEMS, REASONING PATTERNS, AND AGENT FRAMEWORKS")

    add_p("To command authority in your seminar defense, you must articulate how an LLM transforms into an autonomous agent, how individual agents deliberate, and how popular multi-agent orchestration frameworks operate under the hood. You must also defend why existing frameworks do not solve the topology evaluation problem.")

    add_sub_sec("C.1", "The Anatomy of an Autonomous LLM Agent")
    add_p("An autonomous agent is an encapsulated computational entity that uses an LLM as its central decision-making core. It is defined by four interacting subsystems:")
    add_bullet("1. Cognitive Reasoning Core: A foundation model prompted with a System Persona P_sys defining its role, behavioral constraints, available tools, and structured response schema (e.g., JSON or XML).")
    add_bullet("2. Planning & Decomposition: Breaks down complex high-level goals into ordered sequences of sub-tasks, choosing whether to execute sequentially, explore multiple paths, or backtrack upon failure.")
    add_bullet("3. Working & Long-Term Memory: Short-term memory maintains conversation history within the context window. Long-term memory retrieves relevant past experiences or external knowledge using vector databases and dense embedding similarity.")
    add_bullet("4. Action & Tool Execution: Dispatches external function calls (e.g., SQL queries, Python code execution, REST API invocations) and ingests the raw execution environment output back into the context window as new perceptual observations.")

    add_sub_sec("C.2", "Autonomous Deliberation and Cognitive Reasoning Patterns")
    add_bullet("Chain-of-Thought (CoT; Wei et al., NeurIPS 2022 [11]): Prompts the model to generate intermediate natural language reasoning steps ('Let's think step by step') before emitting the final answer. Allocates more inference FLOPs and KV-cache tokens to computation, preventing the model from jumping to premature, incorrect conclusions.")
    add_bullet("ReAct: Synergizing Reasoning and Acting (Yao et al., ICLR 2023 [10]): Establishes the foundational agent loop: Thought -> Action -> Observation. The agent first reasons about the current state, selects an action from a tool catalog, observes the environment output, and repeats until the goal is solved.")
    add_bullet("Tree-of-Thoughts (ToT; Yao et al., NeurIPS 2024 [12]): Generalizes CoT from linear sequences to a tree search space. At each step, the model generates multiple candidate thoughts, evaluates their promise using an LLM heuristic evaluator, and executes search algorithms (Breadth-First Search or Depth-First Search) with lookahead and backtracking.")
    add_bullet("Graph-of-Thoughts (GoT; Besta et al., AAAI 2024 [13]): Extends ToT to arbitrary directed graphs. Enables combining thoughts from independent branches, synthesizing multiple intermediate ideas, and creating feedback loops where later thoughts refine earlier reasoning.")
    add_bullet("Reflexion (Shinn et al., NeurIPS 2024 [14]): Introduces episodic reinforcement via verbal self-reflection. When an agent fails a task, an evaluator generates verbal feedback describing why the attempt failed. This reflection is prepended to the agent's memory buffer, allowing it to rapidly adapt on the next attempt without gradient updates.")
    add_bullet("Self-Refine (Madaan et al., NeurIPS 2024 [15]): A cyclic iterative improvement loop: Generate -> Feedback -> Refine. The model inspects its own generated draft, identifies constraint violations or stylistic errors, and rewrites the draft to satisfy all criteria.")

    add_sub_sec("C.3", "Survey of Pioneering Multi-Agent Frameworks")
    add_bullet("AutoGen (Wu et al., 2023 [17]): Developed by Microsoft Research. Centers around the concept of 'Conversable Agents'. Multi-agent interaction is implemented as multi-party chat exchanges where agents take turns posting messages to a shared conversation thread until a human or termination condition intervenes.")
    add_bullet("CAMEL: Communicative Agents for 'Mind' Exploration (Li et al., NeurIPS 2023 [18]): Pioneered 'Inception Prompting' to enable autonomous role-playing cooperation between two agents (e.g., a Python Programmer and a Stock Trader) with zero human intervention.")
    add_bullet("MetaGPT: Meta-Programming for Multi-Agent Collaborative Framework (Hong et al., ACL 2024 [19]): Introduces Standard Operating Procedures (SOPs) inspired by real-world software companies. Agents are assigned roles (Product Manager, Architect, Project Manager, Engineer, QA) and communicate via structured documents (PRDs, architecture designs, API specifications) rather than unstructured chat.")
    add_bullet("ChatDev (Qian et al., ACL 2024 [22]): A virtual software company simulator that organizes agents across sequential phases: Designing -> Coding -> Testing -> Documenting. Within each phase, pairs of agents conduct peer-review discussions before handing off deliverables downstream.")
    add_bullet("AgentVerse (Chen et al., ACL 2024 [20]): A modular framework supporting dynamic group formation, role assignment, and multi-stage evaluation across cooperative, competitive, and collaborative multi-agent environments.")
    add_bullet("Generative Agents (Park et al., UIST 2023 [23]): Simulated 25 autonomous agents living in an interactive sandbox town (Smallville), featuring architecture modules for Observation, Memory Stream, Reflection, and Daily Planning.")

    add_sub_sec("C.4", "Comprehensive Audit of Zhu et al. (ACL 2025 MultiAgentBench)")
    add_p("A critical component of your defense is explicitly distinguishing your project from Zhu et al. (ACL 2025):", bold=True)
    add_p("What Zhu et al. (ACL 2025) Actually Did:", bold=True)
    add_bullet("Title: 'MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents'.")
    add_bullet("Published: Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), pages 11847–11874.")
    add_bullet("Focus: Social, behavioral, and game-theoretic dynamics between agents.")
    add_bullet("Evaluated Scenarios: Complex multi-agent games including Minecraft, Werewolf (social deduction), Prisoner's Dilemma, and auction bidding.")
    add_bullet("Evaluated Dimensions: Social cooperation, betrayal, strategic deception, communication efficiency, and competitiveness.")

    add_p("What MultiAgentTopologyEval Does and Why it is Methodologically Different:", bold=True)
    add_bullet("Focus: Software engineering and systems-level structural evaluation of communication topologies (SINGLE, CHAIN, STAR, TREE, GRAPH).")
    add_bullet("Evaluation Conditions: Controlled, deterministic conditions holding all variables constant (identical task prompts, identical models, identical sampling temperature T=0.70, identical token generation ceilings).")
    add_bullet("Telemetry Metrics: Quantitative metrics including strict regex Constraint Satisfaction Rate (CSR), Property Match Rate (PMR), token usage decoupled into prompt vs completion tokens, financial API cost in USD, wall-clock latency, and operational circuit-breaker failure rates.")
    add_bullet("Empirical Contribution: First systematic discovery and quantification of the 'Baseline Efficiency Paradox' across live cloud LLM APIs.")

    add_callout("Viva Takeaway: Distinguishing from Zhu et al.",
                "If asked: 'Isn't MultiAgentBench already published at ACL 2025?' Answer: 'Yes, Zhu et al. published MultiAgentBench at ACL 2025 to study behavioral game theory and social deception in games like Werewolf and Minecraft. In contrast, our project—MultiAgentTopologyEval—is a systems engineering benchmark evaluating communication topologies (SINGLE, CHAIN, STAR, TREE, GRAPH) under controlled constraints, token economics, latency, and operational failure modes.'")

print("Section C module written.")


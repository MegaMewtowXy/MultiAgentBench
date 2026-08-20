# Technical Seminar PowerPoint Presentation Content

**Project Title:** Evaluating Multi-Agent Coordination Strategies for LLM-Based Task Solving  
**Research Foundation:** MultiAgentBench: Evaluating Collaboration and Competition of LLM Agents (ACL 2025)  
**Authoritative Pilot Dataset:** `EXP_LIVE_20260813_140712` (Gemini `gemini-3.1-flash-lite`, 35 runs)  
**Output PPTX File:** [`Technical_Seminar_MultiAgentBench.pptx`](Technical_Seminar_MultiAgentBench.pptx)

---

## Slide 1: Title Slide
- **Title:** EVALUATING MULTI-AGENT COORDINATION STRATEGIES FOR LLM-BASED TASK SOLVING
- **Subtitle:** Technical Seminar Presentation
- **Presenter:** Kshitij Patil (MCA Candidate)
- **Department:** Department of Computer Applications
- **Institution:** Veermata Jijabai Technological Institute (VJTI), Mumbai
- **Academic Year:** 2025–2026
- **Faculty Guide / Coordinator:** MCA Department Seminar Faculty

---

## Slide 2: Introduction: Evolution of LLM Execution
- **From Single Prompt to Agentic Systems:**
  - Single-turn LLMs are constrained by single context windows and stateless execution.
  - LLM Agents introduce autonomous reasoning loops, tool usage, and environment interaction.
  - Multi-Agent Systems decompose complex tasks across specialized agent roles.
  - Collective Intelligence: Multiple agents collaborate, critique, and synthesize solutions.
- **The Core Coordination Question:**
  - Adding more agents increases communication links and token usage.
  - Hierarchical vs Sequential vs Mesh topologies exhibit different bottleneck profiles.
  - Goal: Scientifically quantify how coordination architecture impacts task score, latency, and cost.

---

## Slide 3: Motivation: The Multi-Agent Trade-Off
- **Specialization & Roles:** Decomposing complex tasks into distinct roles (Planner, Analyst, Critic, Finalizer) improves thoroughness.
- **Verification Loops:** Multi-agent review catches errors that single-pass LLM calls miss.
- **Overhead & Token Explosion:** Every message passing step consumes API tokens and adds network latency.
- **Central Research Question:** *"Does adding more agents actually improve task solving, or does it primarily add latency and cost?"*

---

## Slide 4: Problem Statement
- **Research Problem Definition:**
  - Different multi-agent systems employ diverse communication topologies (Single, Star, Chain, Tree, Graph).
  - While additional agents provide specialization and peer review, they also introduce communication overhead, compounding network latency, and increased API costs.
  - Currently, there is a lack of rigorous, controlled benchmarks evaluating how coordination topology directly impacts task success, solution quality, latency, and token efficiency.

---

## Slide 5: Research Paper Foundation: MultiAgentBench (ACL 2025)
- **Authoritative Paper Details:**
  - Title: *MultiAgentBench: Evaluating Collaboration & Competition of LLM Agents*
  - Publication: Proceedings of the Association for Computational Linguistics (ACL 2025)
  - Authors: Kunlun Zhu, Hongyi Du, Zhaochen Hong et al.
  - Official Code Repository: `ulab-uiuc/MARBLE`
- **Scope & Adaptation Boundaries:**
  - Our Work: Student-Scale Adapted Research Implementation.
  - Reproduction Boundary: We adapt core task categories and agent roles.
  - Experimental Extension: We systematically isolate and compare 5 distinct coordination topologies.
  - Strict Distinction: Our project is an adapted experimental study inspired by MultiAgentBench.

---

## Slide 6: Original MARBLE Research Framework
- **Conceptual Architecture from ACL 2025 Paper:**
  - Coordination Engine: Manages multi-agent turn-taking and message routing.
  - Agent Graph ($G = (V, E)$): Models agents as nodes and communication channels as edges.
  - Cognitive Module: Handles LLM prompting, role-specific reasoning, and tool invocations.
  - Memory System: Stores shared environment state, execution history, and inter-agent messages.
  - *Explicit Designation:* Labeled as "Original Research Framework" to distinguish from our implementation.

---

## Slide 7: Research Gap & Proposed Extension
- **Original Paper Limitation:** MultiAgentBench focused primarily on game-like environments and macro task benchmarks without systematically isolating topology structure.
- **Identified Research Gap:** Lack of controlled, head-to-head empirical evaluations comparing Single Agent vs Star vs Chain vs Tree vs Graph topologies under identical benchmark tasks.
- **Our Proposed Extension:** Implement a modular multi-topology experimental runner with strict cost guardrails, anti-leakage evaluation, and statistical effect size analysis.

---

## Slide 8: Research Questions (RQ1 – RQ5)
- **RQ1 (Coordination Benefit):** Does multi-agent coordination improve task performance over a single LLM agent?
- **RQ2 (Topology Specificity):** Which coordination topology performs best for different task categories?
- **RQ3 (Efficiency Trade-off):** Does multi-agent collaboration improve quality at the cost of higher latency and API cost?
- **RQ4 (Task Dependence):** Does optimal coordination architecture depend on task characteristics and complexity?
- **RQ5 (Pareto Efficiency):** What is the performance-efficiency Pareto trade-off across topologies?

---

## Slide 9: Research Hypotheses (H1 – H5)
- **H1 (Quality Hypothesis):** Multi-agent topologies will achieve higher quality scores on complex tasks than a single agent.
- **H2 (Hierarchical Superiority):** Hierarchical structures (Tree/Star) will outperform linear pipelines (Chain) on complex planning.
- **H3 (Overhead Scaling):** Latency and token consumption will scale non-linearly with agent communication links.
- **H4 (Task Shift):** Optimal topology choice will shift depending on task difficulty and constraint count.
- **H5 (Efficiency Baseline):** Single Agent will remain the most token-efficient approach for straightforward tasks.

---

## Slide 10: Proposed Research Approach & Workflow
1. **Problem Formulation:** Identify research gap in topology trade-offs.
2. **Student-Scale Benchmark:** Standardize 7 task categories with anti-leakage isolation.
3. **Multi-Topology Solvers:** Implement Single, Star, Chain, Tree, and Graph execution solvers.
4. **Provider Abstraction:** Support Google Gemini, Groq Cloud, and Mock Provider deterministically.
5. **Controlled Execution:** Run matrix experiments keeping model, prompts, and settings constant.
6. **Evaluation & Statistics:** Measure task score, latency, tokens, cost, and Cohen's d effect size.

---

## Slide 11: System Architecture & Layered Implementation
- **Layer 1 — Presentation:** Streamlit Dashboard (🔬 Research Suite & 🎓 Demonstration Suite)
- **Layer 2 — Experiment Control:** `ExperimentRunner` (Pre-flight Preview, Matrix Execution, Immutability)
- **Layer 3 — Coordination Topologies:** `BaseArchitecture` (Single, Star, Chain, Tree, Graph Solvers)
- **Layer 4 — Agent Roles:** Role Definitions (Planner, Researcher, Analyst, Critic, Finalizer)
- **Layer 5 — Provider Abstraction:** `LLMProvider` (Google Gemini, Groq, OpenAI, `MockProvider`)
- **Layer 6 — Evaluation & Storage:** `HybridEvaluator` + `StatisticalAnalyzer` + CSV/JSON Results Storage

---

## Slide 12: Specialized Agent Roles & Responsibilities
- **Planner:** Decomposes complex task prompt into structured sub-tasks and strategy plan.
- **Researcher:** Gathers information, domain context, and technical considerations.
- **Analyst:** Evaluates trade-offs, synthesizes findings, and structures draft solution.
- **Critic:** Audits draft for constraint violations, logical flaws, and edge cases.
- **Finalizer:** Consolidates all inputs into final, authoritative task response.

---

## Slide 13: Five Evaluated Coordination Topologies
1. **Single (1 Agent):** Direct LLM call baseline.
2. **Star (1 Leader + N Workers):** Central coordinator delegates & merges worker outputs.
3. **Chain (Pipeline $N \rightarrow N+1$):** Sequential stage-by-stage handoff across roles.
4. **Tree (Hierarchical):** Branch delegation & bottom-up aggregation.
5. **Graph (Dynamic Mesh $G=(V,E)$):** Configurable inter-agent communication network.

---

## Slide 14: Student-Scale Benchmark Suite
- **1. Planning (`TASK_PLAN_001`):** Design cloud migration strategy.
- **2. Constraint Satisfaction (`TASK_CONST_002`):** Allocate resources under strict constraints.
- **3. Information Synthesis (`TASK_SYNTH_003`):** Summarize multi-source technical reports.
- **4. Multi-step Reasoning (`TASK_REASON_004`):** Algorithmic problem solving.
- **5. Decision Making (`TASK_DECISION_005`):** Evaluate architecture trade-offs.
- **6. Collaborative Problem Solving (`TASK_COLLAB_006`):** Joint problem solving across roles.
- **7. Coding (`TASK_CODE_007`):** Python algorithm & refactoring task.

---

## Slide 15: Evaluation Metrics Engine
- **Performance Metrics:** Task Success (True/False), Task Score (0.0–1.0), Constraint Satisfaction Rate (0–100%).
- **Quality Metrics:** Quality Score (0.0–10.0), Coordination Score (0.0–10.0), Evaluator: Objective Regex + LLM Judge.
- **Efficiency Metrics:** Latency (seconds), Total API Calls, Total Tokens (Input + Output), Estimated Cost (USD).
- **Reliability & Taxonomy:** Failure Rate (%), MAST Taxonomy: API Failure, Timeout, Rate Limit, Constraint Violation, Agent Loop.

---

## Slide 16: Controlled Experimental Methodology
- **Controlled Independent Variable:** Coordination Topology (Single, Star, Chain, Tree, Graph).
- **Strictly Controlled Factors:** Provider (`gemini`), Model (`gemini-3.1-flash-lite`), Task Prompts, Temperature (0.7), Max Tokens (1024).
- **Measured Dependent Variables:** Task Score, Quality Score, Latency, Total Calls, Tokens, Estimated Cost, Failure Mode.
- **Repetition & Isolation:** Each matrix run evaluates every architecture against all 7 benchmark categories under identical execution parameters.

---

## Slide 17: Evaluation Pipeline & Benchmark Anti-Leakage
- **Pipeline:** Task Definition -> Architecture Solver -> Final Answer -> Hybrid Evaluator -> Results CSV/JSON.
- **Strict Anti-Leakage Guardrails:**
  - `TaskDefinition.to_agent_prompt_dict()`: Strips reference answers & ground-truth keyword sets.
  - Agent Input Isolation: Agents receive ONLY `task_id`, `category`, `prompt`, and `constraints`.
  - Evaluator Isolation: Ground-truth reference solutions are visible strictly to the evaluator engine.

---

## Slide 18: Technology Stack & Tools
- **Core Language & OS:** Python 3.13.9 | Windows OS | Object-Oriented Dataclasses
- **LLM API Providers:** Google Generative AI SDK (`google-generativeai`) | Groq Cloud SDK | OpenAI SDK Abstraction
- **User Interface:** Streamlit 1.42.0 (Dual Suite: Research Suite & Demonstration Suite)
- **Analytics & Testing:** Pandas | NumPy | Pytest (100% Offline Suite) | Graphviz / Mermaid

---

## Slide 19: Streamlit Implementation & GUI Overview
- **🔬 Research Suite Features:** Executive Dashboard, Experiment Runner (Pre-flight preview, matrix footprint estimation), Comparative Analytics, Task & Failure Analysis, Report Generator.
- **🎓 Demonstration Suite Features:** Seminar Live Demo, Topology Visualizer, Safe API Connectivity Test.

---

## Slide 20: PILOT EXPERIMENT — PRELIMINARY RESULTS
> ⚠️ **PRELIMINARY RESULTS — NOT FINAL RESEARCH RESULTS** (Authorized Pilot Dataset: `EXP_LIVE_20260813_140712`)

| Architecture | Success Rate | Avg Task Score | Avg Quality | Avg Latency (s) | Avg Calls | Avg Tokens | Avg Cost ($) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Single** | 100.0% | 0.9429 | 9.429 | 6.32s | 1.0 | 1,121.6 | $0.000168 |
| **Star** | 100.0% | 0.8329 | 8.329 | 43.62s | 5.0 | 17,174.1 | $0.002576 |
| **Chain** | 71.4% | 0.6914 | 6.914 | 42.21s | 5.0 | 11,555.4 | $0.001733 |
| **Tree** | 100.0% | 0.7571 | 7.571 | 47.38s | 6.0 | 12,789.3 | $0.001918 |
| **Graph** | 100.0% | 0.8000 | 8.000 | 47.31s | 5.0 | 13,843.1 | $0.002076 |

---

## Slide 21: Pilot Observations & Empirical Insights
- **Baseline Efficiency:** Single Agent achieved highest average task score (0.9429) at lowest latency (6.32s) and tokens (1,121.6).
- **Overhead Scaling:** Multi-agent topologies incurred 6.7x to 7.5x higher latency (42.2s–47.4s) and 10.3x to 15.3x higher token usage.
- **Topology Robustness:** Star, Tree, and Graph achieved 100% success rate on the pilot suite.
- **Preliminary Indication:** Multi-agent coordination introduces overhead that must be justified by task complexity.
- **Methodological Note:** These pilot observations provide initial patterns requiring validation in the final controlled experiment.

---

## Slide 22: Pilot Failure Analysis (EXP_LIVE_20260813_140712)
- **Chain Topology on `TASK_SYNTH_003` (Information Synthesis):** Classified as `constraint violation` (Task Score: 0.16, Quality: 1.6). *Reason:* Sequential compression omitted required source metadata constraints.
- **Chain Topology on `TASK_DECISION_005` (Decision Making):** Classified as `reasoning failure` (Task Score: 0.46, Quality: 4.6). *Reason:* Downstream agent misapplied trade-off criteria from preceding stage.
- **Architectural Vulnerability:** Linear pipeline (Chain) topologies exhibit single-point vulnerability where errors propagate down the chain.
- **Star, Tree, Graph Integrity:** Zero failures recorded for Star, Tree, and Graph topologies in this pilot run.

---

## Slide 23: Final Controlled Experiment Plan
1. **Pilot Validation Completed:** Verified live API execution pipeline, data persistence, and evaluation engine.
2. **Final Controlled Experiment:** Expand trial count per cell ($N \ge 5$ repetitions per task-topology pair) for statistical power.
3. **Multi-Provider Comparison:** Execute controlled comparative runs across Google Gemini and Groq Cloud.
4. **Controlled Execution Protocol:** Enforce identical generation parameters, staggered call delays, and cost limits.
5. **Final Data Derivatives:** Populate definitive findings and thesis conclusions following controlled execution.

---

## Slide 24: Statistical Analysis Methodology
- **Statistical Testing Framework:**
  - Descriptive Stats: Mean, Median, Std Dev, 95% Confidence Intervals.
  - Paired Methodology: Because architectures evaluate identical tasks, Paired Wilcoxon Signed-Rank Tests are required.
  - Effect Size: Cohen's d vs Single Agent Baseline.
  - Sample Size Requirement: Minimum $N \ge 5$ repetitions per cell for parametric tests.
- **Final Statistical Placeholders:**
  - `FINAL STATISTICAL ANALYSIS: [TO BE POPULATED AFTER FINAL CONTROLLED EXPERIMENT]`
  - `FINAL HYPOTHESIS TESTING RESULTS: [TO BE POPULATED AFTER FINAL CONTROLLED EXPERIMENT]`
  - `FINAL PARETO FRONTIER: [TO BE POPULATED AFTER FINAL CONTROLLED EXPERIMENT]`

---

## Slide 25: Limitations & Future Scope
- **Project Limitations:**
  - API Rate & Quota Limits: Free-tier daily token limits constrain matrix trial count.
  - LLM Nondeterminism: Output variability requires multiple runs for tight confidence bounds.
  - Student-Scale Benchmark: Focused on 7 representative categories rather than exhaustive industrial tasks.
- **Future Scope:**
  - Dynamic Adaptive Routing: Dynamically adjust topology based on real-time task difficulty.
  - Local Model Execution: Integrate local LLMs (Ollama / vLLM) for zero-cost execution.
  - Heterogeneous Agent Swarms: Mix different model sizes (e.g. 70B coordinator + 8B workers).

---

## Slide 26: Current Status & References
- **Current Project Status:**
  - ✓ Research framework & 5 topology solvers implemented.
  - ✓ Benchmark suite & anti-leakage evaluator operational.
  - ✓ Streamlit dual-suite GUI fully functional.
  - ✓ Authoritative live pilot experiment completed (`EXP_LIVE_20260813_140712`).
  - ⏳ Final controlled experiment & thesis synthesis pending.
- **Key Academic References:**
  1. Zhu et al. "MultiAgentBench: Evaluating Collaboration and Competition of LLM Agents." *ACL 2025*.
  2. Wu et al. "AutoGen: Enabling Next-Gen LLM Applications." *arXiv 2023*.
  3. Qian et al. "Communicative Agents for Software Development (ChatDev)." *ACL 2024*.
  4. Hong et al. "MetaGPT: Meta Programming for A Multi-Agent Framework." *ICLR 2024*.

# Experiment Protocol & Reproducibility Guide

## 1. Executive Summary
This document establishes the standardized experimental protocol for evaluating multi-agent coordination topologies based on **MultiAgentBench** (Zhu et al., ACL 2025). Every run executed by this platform strictly adheres to the protocol detailed below to guarantee academic transparency, fairness, and 100% reproducibility.

---

## 2. Research Questions & Operational Hypotheses

| RQ | Research Question | Primary Hypothesis |
| :- | :--- | :--- |
| **RQ1** | Does multi-agent coordination improve task performance over a single agent? | Multi-agent coordination topologies achieve higher constraint satisfaction and quality on complex tasks through role division. |
| **RQ2** | Which topology performs best for different task categories? | Mesh/Graph topology excels in synthesis tasks, while Chain topology excels in sequential reasoning. |
| **RQ3** | Does increased collaboration improve quality at the cost of higher latency and API cost? | Inter-agent interaction yields diminishing marginal quality returns while exponentially increasing token consumption and latency. |
| **RQ4** | Does optimal coordination architecture depend on task characteristics? | Hierarchical Tree topologies outperform Star and Chain topologies on high-constraint, highly decomposable problems. |
| **RQ5** | What is the performance-efficiency trade-off across topologies? | Star topology provides the optimal Pareto trade-off between quality score and API cost efficiency for medium-complexity tasks. |

---

## 3. Experimental Controls & Variables

### A. Independent Variables
1. **Coordination Topology:** `Single-Agent (Baseline)`, `Star`, `Chain`, `Tree`, `Graph`.
2. **Task Category:** `Planning`, `Constraint Satisfaction`, `Information Synthesis`, `Multi-step Reasoning`, `Decision-making`, `Collaborative Problem Solving`, `Coding`.
3. **LLM Provider / Model:** `MockProvider (mock-llm-v1)`, `Groq (llama-3.3-70b-versatile)`, `Gemini (gemini-1.5-flash)`, `OpenAI (gpt-4o-mini)`.

### B. Controlled Variables (Fair Comparison Guarantee)
- **Model Temperature:** Fixed at $T = 0.7$ across all comparative topology runs.
- **Max Output Tokens:** Fixed at 1,024 tokens per agent turn.
- **System Role Prompts:** Identical system prompts per role (`Planner`, `Researcher`, `Analyst`, `Critic`, `Finalizer`) regardless of topology.
- **Task Order & Data:** Identical task prompts and constraints evaluated across all topologies in sequence.

### C. Dependent Variables (Measured Outputs)
- **Task Success Rate (0.0 - 1.0):** Binary metric derived from constraint satisfaction rate $\ge 0.5$.
- **Task Score (0.0 - 1.0):** Weighted combination of constraint satisfaction (60%) and property keyword matching (40%).
- **Quality Score (0.0 - 10.0):** Scaled task accomplishment and solution thoroughness.
- **Coordination Score (0.0 - 10.0):** Evaluates interaction quality, role adherence, and message clarity.
- **Execution Latency (seconds):** Wall-clock time recorded from task dispatch to final response generation.
- **Total LLM API Calls:** Integer count of LLM inference requests executed per task.
- **Total Token Consumption:** Input tokens + output tokens measured per execution trace.
- **Estimated API Cost ($ USD):** Standardized pricing calculation based on provider token rates.

---

## 4. Benchmark Dataset Composition
The benchmark consists of 7 structured technical tasks defined in `data/tasks/benchmark_tasks.json`:
- `TASK_PLAN_001`: Legacy E-Commerce Monolith Migration (Planning)
- `TASK_CONST_002`: Real-time Multiplayer Gaming Backend Layout (Constraint Satisfaction)
- `TASK_SYNTH_003`: GNN vs. Transformer Knowledge Graph Completion (Information Synthesis)
- `TASK_REASON_004`: Distributed Financial Clearing Deadlock Root Cause Analysis (Multi-step Reasoning)
- `TASK_DECISION_005`: Global HIPAA Health Record Database Selection (Decision-making)
- `TASK_COLLAB_006`: Ransomware Attack Disaster Recovery Protocol (Collaborative Problem Solving)
- `TASK_CODE_007`: Thread-safe Leaky Bucket Rate Limiter (Coding/Problem-solving)

---

## 5. Execution & Reproducibility Procedure

### Step 1: Pre-flight Verification & Environment Setup
```bash
python -m pip install -r requirements.txt
python -m pytest tests/
```

### Step 2: Reproducible Matrix Run (Command Line)
To execute a reproducible matrix run across all 5 topologies and 7 benchmark tasks:
```bash
python scripts/run_experiments.py --provider mock --archs single star chain tree graph
```

### Step 3: Interactive Dashboard & Live Visualizer
Launch the Streamlit research dashboard to inspect comparative graphs, metrics, and logs:
```bash
streamlit run main.py
```

### Step 4: Result Inspection & Data Storage
- Detailed JSON traces: `data/results/EXP_<TIMESTAMP>_detailed.json`
- Summary CSV tables: `data/results/EXP_<TIMESTAMP>_summary.csv`

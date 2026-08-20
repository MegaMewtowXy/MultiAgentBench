# Benchmark Design Document

## 1. Overview & Research Objective
The benchmark dataset (`data/tasks/benchmark_tasks.json`) provides a standardized evaluation suite for measuring LLM multi-agent coordination performance. The benchmark is specifically structured to test tasks requiring task decomposition, role specialization, quantitative constraint handling, information synthesis, and multi-agent verification.

---

## 2. Benchmark Task Suite Composition

| Task ID | Category | Difficulty | Evaluation Type | Why Multi-Agent Collaboration is Required | Anti-Leakage Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TASK_PLAN_001** | Planning | High | Constraint Validation | Requires decomposing legacy monolith migration into 4-quarter phases with Kafka event streaming and zero-downtime rollback scripts. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_CONST_002** | Constraint Satisfaction | Medium | Constraint Validation | Requires balancing sub-50ms latency, 99.99% availability, and $5,000 monthly budget constraints across regional EKS clusters. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_SYNTH_003** | Information Synthesis | High | Hybrid (Rules + Judge) | Synthesizes complex architectural trade-offs between O(V+E) GNN spatial efficiency vs. O(N^2) Relational Transformers. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_REASON_004** | Multi-step Reasoning | High | Hybrid (Rules + Judge) | Traces distributed database deadlock lock order mismatches across concurrent financial clearing transactions. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_DECISION_005** | Decision-making | Medium | Constraint Validation | Selects HIPAA-compliant multi-region database stack with sub-second full-text medical search over 500M records. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_COLLAB_006** | Collaborative Problem Solving | High | Hybrid (Rules + Judge) | Coordinates 15-minute subnet isolation, immutable checksum validation, and regulatory breach notification following ransomware attack. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |
| **TASK_CODE_007** | Coding / Problem Solving | Medium | Deterministic | Formulates thread-safe in-memory Leaky Bucket rate limiter in Python with O(1) time complexity per rate check. | Sanitized inputs passed to agents; ground truth strictly isolated for evaluator. |

---

## 3. Anti-Leakage Protection Protocol
- **Strict Isolation:** When tasks are executed by agents (`TaskDefinition.to_agent_prompt_dict()`), only the task `prompt`, `category`, and operational `constraints` are provided.
- **Evaluator Access Only:** Ground-truth `reference_answer` strings and `expected_properties` keyword sets are strictly withheld from agents and made available exclusively to `HybridEvaluator`.

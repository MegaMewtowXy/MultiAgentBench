# Benchmark Expansion Specification — Second Pilot Task Set

## 1. Overview
The benchmark suite has been expanded from 7 tasks to **14 benchmark tasks**, adding exactly ONE counterpart task for each of the 7 task categories. The purpose of this expansion is to establish a balanced 14-task testbed ($14 \times 5 = 70$ total runs) for the second pilot research stage.

---

## 2. Benchmark Task Matrix & Counterpart Difficulty Mapping

| Task ID | Category | Existing Counterpart | Difficulty | Why Comparable | Evaluation Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TASK_PLAN_008** | Planning | `TASK_PLAN_001` (Cloud Migration) | Medium-High | Both evaluate multi-stage system transitions (Monolith vs KMS Zero-Trust) with zero downtime & rollback constraints. | `constraint_validation` |
| **TASK_CONST_009** | Constraint Sat. | `TASK_CONST_002` (Gaming Infra) | Medium-High | Both mandate quantitative budget caps ($8k vs $5k), SLA targets (99.999%), latency bounds, and compliance constraints. | `constraint_validation` |
| **TASK_SYNTH_010** | Information Synthesis | `TASK_SYNTH_003` (GNN vs Transformer) | Medium | Both compare complex AI/data structures (HNSW Vectors vs Graphs) across scaling complexity, memory, and precision. | `hybrid` |
| **TASK_REASON_011** | Multi-step Reasoning | `TASK_REASON_004` (Deadlock Analysis) | High | Both require root-cause diagnosis of concurrency failures (GC Memory Leak vs DB Lock Deadlock) and non-blocking mitigation. | `hybrid` |
| **TASK_DECISION_012**| Decision-making | `TASK_DECISION_005` (Healthcare DB) | Medium-High | Both require architecture selection under competing latency, reliability, and ordering constraints (MQTT/Kafka vs Postgres/ES). | `constraint_validation` |
| **TASK_COLLAB_006** | Collaborative Problem Solving | `TASK_COLLAB_006` (Ransomware Recovery) | High | Both require multi-role incident response (Zero-Day Vulnerability vs Ransomware), subnet isolation, hotfixes, and compliance disclosure. | `hybrid` |
| **TASK_CODE_014** | Coding/problem-solving | `TASK_CODE_007` (Leaky Bucket Limiter) | Medium | Both require thread-safe $O(1)$ concurrent data structures in Python (LRU Cache vs Leaky Bucket Limiter) with locking and eviction. | `deterministic` |

---

## 3. Benchmark Category Balance Verification

- **Planning:** 2 tasks (`TASK_PLAN_001`, `TASK_PLAN_008`)
- **Constraint Satisfaction:** 2 tasks (`TASK_CONST_002`, `TASK_CONST_009`)
- **Information Synthesis:** 2 tasks (`TASK_SYNTH_003`, `TASK_SYNTH_010`)
- **Multi-step Reasoning:** 2 tasks (`TASK_REASON_004`, `TASK_REASON_011`)
- **Decision-making:** 2 tasks (`TASK_DECISION_005`, `TASK_DECISION_012`)
- **Collaborative Problem Solving:** 2 tasks (`TASK_COLLAB_006`, `TASK_COLLAB_013`)
- **Coding/problem-solving:** 2 tasks (`TASK_CODE_007`, `TASK_CODE_014`)

**Total Tasks:** **14 tasks** ($14 \times 5 = 70$ matrix runs)

---

## 4. Benchmark Neutrality & Anti-Leakage Isolation
- **Architecture Neutrality:** Prompts contain zero references to agent topology names (`Single`, `Star`, `Chain`, `Tree`, `Graph`) or prompts favoring specific architectures.
- **Anti-Leakage Isolation:** Ground-truth `reference_answer` strings and `expected_properties` keyword lists are strictly isolated from agent prompts via `TaskDefinition.to_agent_prompt_dict()`. Agents receive ONLY `task_id`, `category`, `prompt`, and `constraints`.

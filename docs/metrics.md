# Evaluation Metrics Specification

This document provides exact mathematical definitions, ranges, and types for all evaluation metrics tracked by the MultiAgentBench implementation.

---

## 1. Metrics Registry

| Metric Name | Definition | Type | Range | Higher Better? | Calculation Method |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Task Score** | Overall milestone accomplishment rate combining constraint verification and expected property matching. | Objective | `0.0 - 1.0` | Yes | `(ConstraintSatisfactionRate * 0.6) + (PropertyMatchRate * 0.4)` |
| **Constraint Satisfaction Rate** | Fraction of explicitly defined task constraints satisfied in final solution text. | Objective | `0.0 - 1.0` | Yes | `Satisfied Constraints Count / Total Defined Constraints Count` |
| **Task Success** | Binary indicator confirming whether task completion met minimum quality threshold. | Objective | `True / False` | Yes | `TaskScore >= 0.5 AND ExecutionSuccess == True` |
| **Quality Score** | Scaled solution completeness and technical rigor score. | Objective / Judge | `0.0 - 10.0` | Yes | `TaskScore * 10.0` (Objective) or Structured LLM Judge rating |
| **Coordination Score (CS)** | Evaluates inter-agent message relevance, role adherence, and delegation structure. | Subjective (Judge) | `0.0 - 10.0` | Yes | Evaluated via structured LLM Judge or fixed topology heuristic (Star=7.5, Single=5.0) |
| **Communication Clarity** | Assesses clarity, conciseness, and structural readability of agent outputs. | Subjective (Judge) | `0.0 - 10.0` | Yes | Structured rating from evaluator LLM |
| **Role Adherence** | Measures compliance of agent node outputs with assigned role persona. | Subjective (Judge) | `0.0 - 10.0` | Yes | Structured rating from evaluator LLM |
| **Execution Latency** | Wall-clock execution time in seconds from initial prompt dispatch to final output. | Efficiency | `> 0.0 sec` | No | `TimeEnd - TimeStart` |
| **Total LLM Calls** | Total number of API inference calls made across all agents in topology. | Efficiency | `>= 1` | No | Sum of `total_calls` across all agent states |
| **Total Token Usage** | Combined sum of prompt input tokens and generated completion output tokens. | Efficiency | `>= 0` | No | `InputTokens + OutputTokens` |
| **Estimated API Cost** | Calculated API expenditure in USD based on provider model token pricing. | Efficiency | `>= $0.0` | No | Provider token pricing calculation |
| **Cohen's d Effect Size** | Standardized difference between topology score distribution vs. Single Agent baseline. | Statistical | `Real Number` | N/A | `(Mean_Arch - Mean_Single) / StandardDev_Pooled` |

---

## 2. LLM-as-Judge Protocol & Safety
When LLM-based evaluation is enabled (`use_llm_judge=True`), judges follow a structured prompt evaluating:
1. `Solution Quality` (0–10)
2. `Coordination Score` (0–10)
3. `Communication Clarity` (0–10)
4. `Role Adherence` (0–10)

> [!IMPORTANT]
> LLM-as-Judge scores are explicitly labeled as subjective qualitative metrics and are **never presented as objective ground truth**. Primary success tracking relies strictly on deterministic constraint verification.

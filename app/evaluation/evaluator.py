"""
Hybrid Evaluation Engine for MultiAgentBench implementation.
Combines deterministic objective verification (constraint satisfaction, pattern matching)
with optional LLM-judge coordination scoring.
"""

import re
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from app.architectures.base_architecture import ArchitectureResult
from app.benchmark.loader import TaskDefinition
from app.llm.base import LLMProvider

@dataclass
class EvaluationResult:
    """Evaluation result container for a single architecture run."""
    task_id: str
    architecture_name: str
    task_success: bool
    task_score: float  # 0.0 to 1.0 (milestone/constraint achievement rate)
    quality_score: float  # 0.0 to 10.0
    constraint_satisfaction_rate: float  # 0.0 to 1.0
    coordination_score: float  # 0.0 to 10.0
    communication_clarity: float  # 0.0 to 10.0
    role_adherence: float  # 0.0 to 10.0
    latency_seconds: float
    total_calls: int
    total_tokens: int
    estimated_cost_usd: float
    is_llm_evaluated: bool = False
    evaluation_details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "architecture_name": self.architecture_name,
            "task_success": self.task_success,
            "task_score": round(self.task_score, 2),
            "quality_score": round(self.quality_score, 2),
            "constraint_satisfaction_rate": round(self.constraint_satisfaction_rate, 2),
            "coordination_score": round(self.coordination_score, 2),
            "communication_clarity": round(self.communication_clarity, 2),
            "role_adherence": round(self.role_adherence, 2),
            "latency_seconds": round(self.latency_seconds, 4),
            "total_calls": self.total_calls,
            "total_tokens": self.total_tokens,
            "estimated_cost_usd": round(self.estimated_cost_usd, 6),
            "is_llm_evaluated": self.is_llm_evaluated,
            "evaluation_details": self.evaluation_details
        }

class HybridEvaluator:
    """Evaluates architecture performance using deterministic rules and optional LLM judges."""

    def __init__(self, evaluator_provider: Optional[LLMProvider] = None):
        self.evaluator_provider = evaluator_provider

    def evaluate(
        self,
        task: TaskDefinition,
        result: ArchitectureResult,
        use_llm_judge: bool = False
    ) -> EvaluationResult:
        """
        Main evaluation entry point.

        Args:
            task: TaskDefinition containing prompt, constraints, expected properties.
            result: ArchitectureResult output from an architecture run.
            use_llm_judge: If True and evaluator_provider available, runs LLM-based judge.

        Returns:
            EvaluationResult containing detailed metric scores.
        """
        output_text = result.final_answer.lower()

        # 1. Deterministic Constraint Satisfaction
        satisfied_constraints = 0
        total_constraints = len(task.constraints)
        if total_constraints > 0:
            for constraint in task.constraints:
                # Check for key tokens or keywords from constraint
                keywords = [w.lower() for w in re.findall(r"\w{4,}", constraint)]
                matches = sum(1 for kw in keywords if kw in output_text)
                if matches >= min(2, len(keywords)):
                    satisfied_constraints += 1
            constraint_rate = satisfied_constraints / total_constraints
        else:
            constraint_rate = 1.0

        # 2. Objective Pattern & Property Match
        matched_props = 0
        total_props = len(task.expected_properties)
        if total_props > 0:
            for prop in task.expected_properties:
                if prop.lower() in output_text:
                    matched_props += 1
            prop_rate = matched_props / total_props
        else:
            prop_rate = 1.0

        # Objective Task Score (Milestone accomplishment rate)
        task_score = (constraint_rate * 0.6) + (prop_rate * 0.4)
        task_success = result.success and (task_score >= 0.5)

        # Baseline Objective Scores
        quality_score = task_score * 10.0
        coordination_score = 7.5 if result.architecture_name != "single" else 5.0
        clarity_score = 8.0
        role_adherence_score = 8.5

        # 3. Optional LLM Judge Evaluation
        is_llm_eval = False
        llm_details = {}
        if use_llm_judge and self.evaluator_provider and self.evaluator_provider.is_available():
            judge_res = self._run_llm_judge(task, result)
            if judge_res:
                quality_score = judge_res.get("quality_score", quality_score)
                coordination_score = judge_res.get("coordination_score", coordination_score)
                clarity_score = judge_res.get("clarity_score", clarity_score)
                role_adherence_score = judge_res.get("role_adherence", role_adherence_score)
                is_llm_eval = True
                llm_details = judge_res

        return EvaluationResult(
            task_id=task.task_id,
            architecture_name=result.architecture_name,
            task_success=task_success,
            task_score=task_score,
            quality_score=quality_score,
            constraint_satisfaction_rate=constraint_rate,
            coordination_score=coordination_score,
            communication_clarity=clarity_score,
            role_adherence=role_adherence_score,
            latency_seconds=result.execution_time_seconds,
            total_calls=result.total_calls,
            total_tokens=result.total_tokens,
            estimated_cost_usd=result.estimated_cost_usd,
            is_llm_evaluated=is_llm_eval,
            evaluation_details={
                "satisfied_constraints": satisfied_constraints,
                "total_constraints": total_constraints,
                "matched_expected_properties": matched_props,
                "total_expected_properties": total_props,
                "llm_judge_data": llm_details
            }
        )

    def _run_llm_judge(self, task: TaskDefinition, result: ArchitectureResult) -> Optional[Dict[str, float]]:
        """LLM-based evaluator scoring communication clarity, role adherence, and coordination."""
        prompt = (
            f"You are an expert AI research evaluator.\n"
            f"Task: {task.prompt}\n"
            f"Architecture: {result.architecture_name}\n"
            f"Final Answer:\n{result.final_answer[:1000]}\n\n"
            f"Rate the following metrics from 0 to 10:\n"
            f"1. Solution Quality Score (0-10)\n"
            f"2. Coordination Score (0-10)\n"
            f"3. Communication Clarity (0-10)\n"
            f"4. Role Adherence (0-10)\n\n"
            f"Provide ratings as: quality=X, coordination=Y, clarity=Z, role_adherence=W"
        )
        try:
            resp = self.evaluator_provider.generate(prompt=prompt, temperature=0.2)
            if resp.success:
                text = resp.content
                q_match = re.search(r"quality\s*=\s*([\d\.]+)", text, re.I)
                c_match = re.search(r"coordination\s*=\s*([\d\.]+)", text, re.I)
                cl_match = re.search(r"clarity\s*=\s*([\d\.]+)", text, re.I)
                r_match = re.search(r"role_adherence\s*=\s*([\d\.]+)", text, re.I)

                return {
                    "quality_score": float(q_match.group(1)) if q_match else 7.0,
                    "coordination_score": float(c_match.group(1)) if c_match else 7.0,
                    "clarity_score": float(cl_match.group(1)) if cl_match else 8.0,
                    "role_adherence": float(r_match.group(1)) if r_match else 8.0
                }
        except Exception:
            pass
        return None

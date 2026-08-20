"""
Single-Agent Baseline Architecture.
One LLM agent receives the complete task specification and produces the final answer in isolation.
Serves as the control condition (baseline) for all multi-agent performance comparisons.
"""

import time
from typing import Dict, Any, Optional
from .base_architecture import BaseArchitecture, ArchitectureResult
from app.agents.finalizer import FinalizerAgent
from app.agents.base_agent import AgentMessage
from app.llm.base import LLMProvider
from app.utils.guardrails import GuardrailTracker

class SingleAgentArchitecture(BaseArchitecture):
    """Control condition topology utilizing a single autonomous agent."""

    def __init__(self, provider: LLMProvider, guardrails: Optional[GuardrailTracker] = None):
        super().__init__(architecture_name="single", provider=provider, guardrails=guardrails)
        self.agent = FinalizerAgent(agent_id="single_agent_1", provider=provider)

    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        task_id = task.get("task_id", "unknown_task")
        prompt = task.get("prompt", "")
        constraints = task.get("constraints", [])

        if constraints:
            prompt += f"\n\nConstraints to satisfy:\n" + "\n".join([f"- {c}" for c in constraints])

        self.guardrails.reset_task()
        self.messages_log.clear()
        self.communication_edges.clear()

        start_time = time.time()
        try:
            self.guardrails.record_call()
            msg: AgentMessage = self.agent.execute(prompt=prompt)
            self.record_message(msg, receiver_role="user")

            elapsed = time.time() - start_time
            agent_dict = {self.agent.agent_id: self.agent.state.to_dict()}

            return ArchitectureResult(
                architecture_name="single",
                task_id=task_id,
                final_answer=self.agent.state.output,
                execution_time_seconds=elapsed,
                total_calls=self.agent.state.total_calls,
                total_tokens=self.agent.state.token_usage["total_tokens"],
                estimated_cost_usd=self.agent.state.estimated_cost_usd,
                messages=[m.to_dict() for m in self.messages_log],
                agent_states=agent_dict,
                communication_edges=[("user", "finalizer")],
                success=self.agent.state.status == "completed"
            )
        except Exception as e:
            elapsed = time.time() - start_time
            return ArchitectureResult(
                architecture_name="single",
                task_id=task_id,
                final_answer=f"ERROR: {str(e)}",
                execution_time_seconds=elapsed,
                total_calls=1,
                total_tokens=0,
                estimated_cost_usd=0.0,
                success=False,
                error_message=str(e)
            )

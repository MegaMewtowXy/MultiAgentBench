"""
Chain Architecture Implementation (Sequential Pipeline Topology).
Executes a linear, stage-by-stage pipeline where each agent receives the refined context from the preceding agent.
Pipeline: TASK -> PLANNER -> RESEARCHER -> ANALYST -> CRITIC -> FINALIZER.
"""

import time
from typing import Dict, Any, Optional
from .base_architecture import BaseArchitecture, ArchitectureResult
from app.agents import PlannerAgent, ResearcherAgent, AnalystAgent, CriticAgent, FinalizerAgent
from app.llm.base import LLMProvider
from app.utils.guardrails import GuardrailTracker

class ChainArchitecture(BaseArchitecture):
    """Sequential pipeline topology executing linear agent hand-offs."""

    def __init__(self, provider: LLMProvider, guardrails: Optional[GuardrailTracker] = None):
        super().__init__(architecture_name="chain", provider=provider, guardrails=guardrails)
        self.planner = PlannerAgent(agent_id="chain_planner", provider=provider)
        self.researcher = ResearcherAgent(agent_id="chain_researcher", provider=provider)
        self.analyst = AnalystAgent(agent_id="chain_analyst", provider=provider)
        self.critic = CriticAgent(agent_id="chain_critic", provider=provider)
        self.finalizer = FinalizerAgent(agent_id="chain_finalizer", provider=provider)

    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        task_id = task.get("task_id", "unknown_task")
        prompt = task.get("prompt", "")
        constraints = task.get("constraints", [])

        self.guardrails.reset_task()
        self.messages_log.clear()
        self.communication_edges.clear()

        start_time = time.time()
        try:
            # Stage 1: Planner
            self.guardrails.record_call()
            msg_plan = self.planner.execute(prompt=prompt)
            self.record_message(msg_plan, receiver_role="researcher")

            # Stage 2: Researcher
            self.guardrails.record_call()
            self.researcher.receive_message(msg_plan)
            msg_res = self.researcher.execute(prompt=f"Original Task: {prompt}\nDeconstructed Plan:\n{msg_plan.content}")
            self.record_message(msg_res, receiver_role="analyst")

            # Stage 3: Analyst
            self.guardrails.record_call()
            self.analyst.receive_message(msg_res)
            msg_analyst = self.analyst.execute(prompt=f"Research Input:\n{msg_res.content}\nConstraints to verify: {constraints}")
            self.record_message(msg_analyst, receiver_role="critic")

            # Stage 4: Critic
            self.guardrails.record_call()
            self.critic.receive_message(msg_analyst)
            msg_critic = self.critic.execute(prompt=f"Quantitative Analysis:\n{msg_analyst.content}\nEvaluate for potential flaws.")
            self.record_message(msg_critic, receiver_role="finalizer")

            # Stage 5: Finalizer
            self.guardrails.record_call()
            self.finalizer.receive_message(msg_critic)
            msg_final = self.finalizer.execute(prompt=f"Refined Critique:\n{msg_critic.content}\nProduce definitive final answer.")
            self.record_message(msg_final, receiver_role="user")

            elapsed = time.time() - start_time

            agents = [self.planner, self.researcher, self.analyst, self.critic, self.finalizer]
            total_calls = sum(a.state.total_calls for a in agents)
            total_tokens = sum(a.state.token_usage["total_tokens"] for a in agents)
            total_cost = sum(a.state.estimated_cost_usd for a in agents)
            agent_states = {a.agent_id: a.state.to_dict() for a in agents}

            edges = [
                ("planner", "researcher"),
                ("researcher", "analyst"),
                ("analyst", "critic"),
                ("critic", "finalizer")
            ]

            return ArchitectureResult(
                architecture_name="chain",
                task_id=task_id,
                final_answer=msg_final.content,
                execution_time_seconds=elapsed,
                total_calls=total_calls,
                total_tokens=total_tokens,
                estimated_cost_usd=total_cost,
                messages=[m.to_dict() for m in self.messages_log],
                agent_states=agent_states,
                communication_edges=edges,
                success=all(a.state.status == "completed" for a in agents)
            )
        except Exception as e:
            elapsed = time.time() - start_time
            return ArchitectureResult(
                architecture_name="chain",
                task_id=task_id,
                final_answer=f"ERROR: {str(e)}",
                execution_time_seconds=elapsed,
                total_calls=5,
                total_tokens=0,
                estimated_cost_usd=0.0,
                success=False,
                error_message=str(e)
            )

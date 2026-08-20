"""
Star Architecture Implementation (Centralized Coordination Topology).
A central Planner node delegates tasks to specialized workers (Researcher, Analyst, Critic) in parallel or fan-out fashion,
and aggregates all worker responses into a Finalizer node.
"""

import time
from typing import Dict, Any, Optional
from .base_architecture import BaseArchitecture, ArchitectureResult
from app.agents import PlannerAgent, ResearcherAgent, AnalystAgent, CriticAgent, FinalizerAgent
from app.llm.base import LLMProvider
from app.utils.guardrails import GuardrailTracker

class StarArchitecture(BaseArchitecture):
    """Centralized star topology with fan-out delegation and central aggregation."""

    def __init__(self, provider: LLMProvider, guardrails: Optional[GuardrailTracker] = None):
        super().__init__(architecture_name="star", provider=provider, guardrails=guardrails)
        self.planner = PlannerAgent(agent_id="planner_center", provider=provider)
        self.researcher = ResearcherAgent(agent_id="researcher_worker", provider=provider)
        self.analyst = AnalystAgent(agent_id="analyst_worker", provider=provider)
        self.critic = CriticAgent(agent_id="critic_worker", provider=provider)
        self.finalizer = FinalizerAgent(agent_id="finalizer_sink", provider=provider)

    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        task_id = task.get("task_id", "unknown_task")
        prompt = task.get("prompt", "")
        constraints = task.get("constraints", [])

        self.guardrails.reset_task()
        self.messages_log.clear()
        self.communication_edges.clear()

        start_time = time.time()
        try:
            # Step 1: Central Planner formulates delegation strategy
            self.guardrails.record_call()
            plan_msg = self.planner.execute(prompt=prompt)
            self.record_message(plan_msg, receiver_role="workers")

            # Step 2: Parallel Delegation to Worker Agents
            # Delegate to Researcher
            self.guardrails.record_call()
            self.researcher.receive_message(plan_msg)
            res_msg = self.researcher.execute(prompt=f"Task: {prompt}\nPlan: {plan_msg.content}")
            self.record_message(res_msg, receiver_role="planner")

            # Delegate to Analyst
            self.guardrails.record_call()
            self.analyst.receive_message(plan_msg)
            analyst_msg = self.analyst.execute(prompt=f"Task: {prompt}\nPlan: {plan_msg.content}\nConstraints: {constraints}")
            self.record_message(analyst_msg, receiver_role="planner")

            # Delegate to Critic
            self.guardrails.record_call()
            self.critic.receive_message(plan_msg)
            critic_msg = self.critic.execute(prompt=f"Task: {prompt}\nResearch: {res_msg.content}\nAnalysis: {analyst_msg.content}")
            self.record_message(critic_msg, receiver_role="planner")

            # Step 3: Central Aggregation & Final Output Generation
            self.guardrails.record_call()
            self.finalizer.receive_message(plan_msg)
            self.finalizer.receive_message(res_msg)
            self.finalizer.receive_message(analyst_msg)
            self.finalizer.receive_message(critic_msg)

            aggregation_prompt = (
                f"Synthesize the final answer for task: {prompt}\n\n"
                f"1. Central Plan:\n{plan_msg.content}\n\n"
                f"2. Research Findings:\n{res_msg.content}\n\n"
                f"3. Quantitative Analysis:\n{analyst_msg.content}\n\n"
                f"4. Critical Review:\n{critic_msg.content}"
            )
            final_msg = self.finalizer.execute(prompt=aggregation_prompt)
            self.record_message(final_msg, receiver_role="user")

            elapsed = time.time() - start_time

            agents = [self.planner, self.researcher, self.analyst, self.critic, self.finalizer]
            total_calls = sum(a.state.total_calls for a in agents)
            total_tokens = sum(a.state.token_usage["total_tokens"] for a in agents)
            total_cost = sum(a.state.estimated_cost_usd for a in agents)
            agent_states = {a.agent_id: a.state.to_dict() for a in agents}

            # Explicit communication graph edges
            edges = [
                ("planner", "researcher"),
                ("planner", "analyst"),
                ("planner", "critic"),
                ("researcher", "finalizer"),
                ("analyst", "finalizer"),
                ("critic", "finalizer")
            ]

            return ArchitectureResult(
                architecture_name="star",
                task_id=task_id,
                final_answer=final_msg.content,
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
                architecture_name="star",
                task_id=task_id,
                final_answer=f"ERROR: {str(e)}",
                execution_time_seconds=elapsed,
                total_calls=5,
                total_tokens=0,
                estimated_cost_usd=0.0,
                success=False,
                error_message=str(e)
            )

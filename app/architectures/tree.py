"""
Tree Architecture Implementation (Hierarchical Topology).
Delegates sub-tasks through a multi-tier hierarchy: Root Coordinator -> Specialized Sub-Leads -> Sub-Task Agents -> Bottom-Up Aggregation.
"""

import time
from typing import Dict, Any, Optional
from .base_architecture import BaseArchitecture, ArchitectureResult
from app.agents import PlannerAgent, ResearcherAgent, AnalystAgent, CriticAgent, FinalizerAgent
from app.llm.base import LLMProvider
from app.utils.guardrails import GuardrailTracker

class TreeArchitecture(BaseArchitecture):
    """Hierarchical tree topology with sub-lead delegation and bottom-up aggregation."""

    def __init__(self, provider: LLMProvider, guardrails: Optional[GuardrailTracker] = None):
        super().__init__(architecture_name="tree", provider=provider, guardrails=guardrails)
        self.root_planner = PlannerAgent(agent_id="root_coordinator", provider=provider)

        # Branch 1: Research Lead & Sub-agents
        self.research_lead = ResearcherAgent(agent_id="research_lead", provider=provider)
        self.research_worker_a = ResearcherAgent(agent_id="research_worker_a", provider=provider)

        # Branch 2: Analysis Lead & Sub-agents
        self.analysis_lead = AnalystAgent(agent_id="analysis_lead", provider=provider)
        self.critic_worker_b = CriticAgent(agent_id="critic_worker_b", provider=provider)

        # Aggregation Sink
        self.finalizer = FinalizerAgent(agent_id="tree_finalizer", provider=provider)

    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        task_id = task.get("task_id", "unknown_task")
        prompt = task.get("prompt", "")
        constraints = task.get("constraints", [])

        self.guardrails.reset_task()
        self.messages_log.clear()
        self.communication_edges.clear()

        start_time = time.time()
        try:
            # Tier 1: Root Coordinator breaks task into two branches
            self.guardrails.record_call()
            msg_root = self.root_planner.execute(prompt=f"Hierarchical decomposition for task: {prompt}")
            self.record_message(msg_root, receiver_role="leads")

            # Tier 2 Branch 1: Research Lead -> Research Worker A
            self.guardrails.record_call()
            self.research_lead.receive_message(msg_root)
            msg_r_lead = self.research_lead.execute(prompt="Synthesize core domain requirements.")
            self.record_message(msg_r_lead, receiver_role="research_worker_a")

            self.guardrails.record_call()
            self.research_worker_a.receive_message(msg_r_lead)
            msg_r_worker = self.research_worker_a.execute(prompt="Detailed factual breakdown of sub-components.")
            self.record_message(msg_r_worker, receiver_role="research_lead")

            # Tier 2 Branch 2: Analysis Lead -> Critic Worker B
            self.guardrails.record_call()
            self.analysis_lead.receive_message(msg_root)
            msg_a_lead = self.analysis_lead.execute(prompt=f"Analyze quantitative rules and constraints: {constraints}")
            self.record_message(msg_a_lead, receiver_role="critic_worker_b")

            self.guardrails.record_call()
            self.critic_worker_b.receive_message(msg_a_lead)
            msg_c_worker = self.critic_worker_b.execute(prompt="Verify constraints and identify branch edge cases.")
            self.record_message(msg_c_worker, receiver_role="analysis_lead")

            # Tier 3: Bottom-up Aggregation to Finalizer
            self.guardrails.record_call()
            self.finalizer.receive_message(msg_r_worker)
            self.finalizer.receive_message(msg_c_worker)

            aggregation_prompt = (
                f"Combine branch outputs into final solution for task: {prompt}\n\n"
                f"Branch 1 (Research Hierarchy Result):\n{msg_r_worker.content}\n\n"
                f"Branch 2 (Analysis Hierarchy Result):\n{msg_c_worker.content}"
            )
            msg_final = self.finalizer.execute(prompt=aggregation_prompt)
            self.record_message(msg_final, receiver_role="user")

            elapsed = time.time() - start_time

            agents = [
                self.root_planner, self.research_lead, self.research_worker_a,
                self.analysis_lead, self.critic_worker_b, self.finalizer
            ]
            total_calls = sum(a.state.total_calls for a in agents)
            total_tokens = sum(a.state.token_usage["total_tokens"] for a in agents)
            total_cost = sum(a.state.estimated_cost_usd for a in agents)
            agent_states = {a.agent_id: a.state.to_dict() for a in agents}

            edges = [
                ("planner", "researcher"),
                ("planner", "analyst"),
                ("researcher", "researcher"),
                ("analyst", "critic"),
                ("researcher", "finalizer"),
                ("critic", "finalizer")
            ]

            return ArchitectureResult(
                architecture_name="tree",
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
                architecture_name="tree",
                task_id=task_id,
                final_answer=f"ERROR: {str(e)}",
                execution_time_seconds=elapsed,
                total_calls=6,
                total_tokens=0,
                estimated_cost_usd=0.0,
                success=False,
                error_message=str(e)
            )

"""
Graph Architecture Implementation (Configurable Mesh Topology).
Represents inter-agent communication pathways dynamically via an adjacency configuration graph G = (A, E).
Nodes are agent instances, and directed edges define valid communication channels between peer agents.
"""

import time
from typing import Dict, Any, List, Tuple, Optional
from .base_architecture import BaseArchitecture, ArchitectureResult
from app.agents import PlannerAgent, ResearcherAgent, AnalystAgent, CriticAgent, FinalizerAgent, BaseAgent
from app.llm.base import LLMProvider
from app.utils.guardrails import GuardrailTracker

DEFAULT_GRAPH_CONFIG = {
    "planner": ["researcher", "analyst"],
    "researcher": ["critic"],
    "analyst": ["critic"],
    "critic": ["finalizer"]
}

class GraphArchitecture(BaseArchitecture):
    """Configurable graph topology allowing dynamic network message routing."""

    def __init__(
        self,
        provider: LLMProvider,
        graph_config: Optional[Dict[str, List[str]]] = None,
        guardrails: Optional[GuardrailTracker] = None
    ):
        super().__init__(architecture_name="graph", provider=provider, guardrails=guardrails)
        self.graph_config = graph_config or DEFAULT_GRAPH_CONFIG

        # Map role identifiers to agent node instances
        self.agents_map: Dict[str, BaseAgent] = {
            "planner": PlannerAgent(agent_id="graph_planner", provider=provider),
            "researcher": ResearcherAgent(agent_id="graph_researcher", provider=provider),
            "analyst": AnalystAgent(agent_id="graph_analyst", provider=provider),
            "critic": CriticAgent(agent_id="graph_critic", provider=provider),
            "finalizer": FinalizerAgent(agent_id="graph_finalizer", provider=provider)
        }

    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        task_id = task.get("task_id", "unknown_task")
        prompt = task.get("prompt", "")
        constraints = task.get("constraints", [])

        self.guardrails.reset_task()
        self.messages_log.clear()
        self.communication_edges.clear()

        # Build list of directed communication edges from configuration
        edges: List[Tuple[str, str]] = []
        for sender_role, receivers in self.graph_config.items():
            for recv_role in receivers:
                edges.append((sender_role, recv_role))

        start_time = time.time()
        try:
            # 1. Execute Entry Point (Planner Node)
            planner = self.agents_map["planner"]
            self.guardrails.record_call()
            msg_planner = planner.execute(prompt=prompt)
            self.record_message(msg_planner, receiver_role="adj_nodes")

            # 2. Dynamic Message Routing based on Graph Adjacency
            node_outputs: Dict[str, str] = {"planner": msg_planner.content}

            # Level 1 Neighbors (Researcher, Analyst)
            for neighbor_role in self.graph_config.get("planner", []):
                if neighbor_role in self.agents_map:
                    agent_node = self.agents_map[neighbor_role]
                    self.guardrails.record_call()
                    agent_node.receive_message(msg_planner)
                    sub_prompt = f"Task: {prompt}\nUpstream Plan ({planner.role}):\n{msg_planner.content}"
                    if neighbor_role == "analyst" and constraints:
                        sub_prompt += f"\nConstraints: {constraints}"
                    msg_out = agent_node.execute(prompt=sub_prompt)
                    node_outputs[neighbor_role] = msg_out.content
                    self.record_message(msg_out, receiver_role="downstream")

            # Level 2 Node (Critic - receiving inputs from Researcher & Analyst)
            critic_inputs = []
            if "critic" in self.agents_map:
                critic_node = self.agents_map["critic"]
                for upstream in ["researcher", "analyst"]:
                    if upstream in node_outputs:
                        critic_inputs.append(f"[{upstream.upper()}]: {node_outputs[upstream]}")

                if critic_inputs:
                    self.guardrails.record_call()
                    critic_prompt = f"Task: {prompt}\nUpstream Node Inputs:\n" + "\n\n".join(critic_inputs)
                    msg_critic = critic_node.execute(prompt=critic_prompt)
                    node_outputs["critic"] = msg_critic.content
                    self.record_message(msg_critic, receiver_role="finalizer")

            # Level 3 Sink Node (Finalizer)
            finalizer = self.agents_map["finalizer"]
            final_inputs = [f"[{role.upper()}]: {content}" for role, content in node_outputs.items()]
            self.guardrails.record_call()
            aggregation_prompt = f"Synthesize graph network contributions for task: {prompt}\n\n" + "\n\n".join(final_inputs)
            msg_final = finalizer.execute(prompt=aggregation_prompt)
            self.record_message(msg_final, receiver_role="user")

            elapsed = time.time() - start_time

            agents = list(self.agents_map.values())
            total_calls = sum(a.state.total_calls for a in agents)
            total_tokens = sum(a.state.token_usage["total_tokens"] for a in agents)
            total_cost = sum(a.state.estimated_cost_usd for a in agents)
            agent_states = {a.agent_id: a.state.to_dict() for a in agents}

            return ArchitectureResult(
                architecture_name="graph",
                task_id=task_id,
                final_answer=msg_final.content,
                execution_time_seconds=elapsed,
                total_calls=total_calls,
                total_tokens=total_tokens,
                estimated_cost_usd=total_cost,
                messages=[m.to_dict() for m in self.messages_log],
                agent_states=agent_states,
                communication_edges=edges,
                success=all(a.state.status == "completed" for a in agents if a.state.total_calls > 0)
            )
        except Exception as e:
            elapsed = time.time() - start_time
            return ArchitectureResult(
                architecture_name="graph",
                task_id=task_id,
                final_answer=f"ERROR: {str(e)}",
                execution_time_seconds=elapsed,
                total_calls=5,
                total_tokens=0,
                estimated_cost_usd=0.0,
                success=False,
                error_message=str(e)
            )

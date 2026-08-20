"""
Base Architecture Class and Execution Result Dataclass.
Standardizes execution interface, communication recording, and performance tracking across all 5 topologies.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple, Optional
import time
from app.llm.base import LLMProvider
from app.agents.base_agent import AgentMessage
from app.utils.guardrails import GuardrailTracker

@dataclass
class ArchitectureResult:
    """Standardized result schema produced by any coordination topology."""
    architecture_name: str
    task_id: str
    final_answer: str
    execution_time_seconds: float
    total_calls: int
    total_tokens: int
    estimated_cost_usd: float
    messages: List[Dict[str, Any]] = field(default_factory=list)
    agent_states: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    communication_edges: List[Tuple[str, str]] = field(default_factory=list)
    success: bool = True
    error_message: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert result object to dictionary for storage and analysis."""
        return {
            "architecture_name": self.architecture_name,
            "task_id": self.task_id,
            "final_answer": self.final_answer,
            "execution_time_seconds": round(self.execution_time_seconds, 4),
            "total_calls": self.total_calls,
            "total_tokens": self.total_tokens,
            "estimated_cost_usd": round(self.estimated_cost_usd, 6),
            "messages_count": len(self.messages),
            "communication_edges": self.communication_edges,
            "success": self.success,
            "error_message": self.error_message,
            "messages": self.messages,
            "agent_states": self.agent_states
        }

class BaseArchitecture(ABC):
    """Abstract interface for multi-agent coordination topologies."""

    def __init__(
        self,
        architecture_name: str,
        provider: LLMProvider,
        guardrails: Optional[GuardrailTracker] = None
    ):
        self.architecture_name = architecture_name
        self.provider = provider
        self.guardrails = guardrails or GuardrailTracker()
        self.messages_log: List[AgentMessage] = []
        self.communication_edges: List[Tuple[str, str]] = []

    def record_message(self, message: AgentMessage, receiver_role: str):
        """Logs inter-agent message communication and graph edge."""
        self.messages_log.append(message)
        edge = (message.sender_role, receiver_role)
        if edge not in self.communication_edges:
            self.communication_edges.append(edge)

    @abstractmethod
    def solve_task(self, task: Dict[str, Any]) -> ArchitectureResult:
        """
        Executes task solving pipeline for the given coordination topology.

        Args:
            task: Task dictionary containing task_id, category, prompt, constraints, expected_properties.

        Returns:
            ArchitectureResult object with final answer and complete metadata.
        """
        pass

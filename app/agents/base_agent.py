"""
Base Agent Class for MultiAgentBench.
Encapsulates agent state, role directives, execution metadata, message buffers, and LLM interaction.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import time
from app.llm.base import LLMProvider, LLMResponse

@dataclass
class AgentMessage:
    """Represents a message sent between agents or coordinator nodes."""
    sender_id: str
    sender_role: str
    receiver_id: str
    content: str
    timestamp: float = field(default_factory=time.time)
    message_type: str = "inform"  # inform, request, critique, plan, final

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sender_id": self.sender_id,
            "sender_role": self.sender_role,
            "receiver_id": self.receiver_id,
            "content": self.content,
            "timestamp": round(self.timestamp, 3),
            "message_type": self.message_type
        }

@dataclass
class AgentState:
    """State tracking container for an individual agent instance."""
    agent_id: str
    name: str
    role: str
    status: str = "idle"  # idle, running, completed, failed
    execution_time: float = 0.0
    input_context: str = ""
    output: str = ""
    messages_received: List[AgentMessage] = field(default_factory=list)
    messages_sent: List[AgentMessage] = field(default_factory=list)
    total_calls: int = 0
    token_usage: Dict[str, int] = field(default_factory=lambda: {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0})
    estimated_cost_usd: float = 0.0
    error_information: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "role": self.role,
            "status": self.status,
            "execution_time": round(self.execution_time, 4),
            "output_snippet": self.output[:150] + ("..." if len(self.output) > 150 else ""),
            "total_calls": self.total_calls,
            "token_usage": self.token_usage,
            "estimated_cost_usd": round(self.estimated_cost_usd, 6),
            "error_information": self.error_information
        }

class BaseAgent:
    """Base class for all multi-agent role implementations."""

    def __init__(
        self,
        agent_id: str,
        name: str,
        role: str,
        system_prompt: str,
        provider: LLMProvider
    ):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.provider = provider
        self.state = AgentState(agent_id=agent_id, name=name, role=role)

    def reset(self):
        """Resets agent state for a new task execution."""
        self.state = AgentState(agent_id=self.agent_id, name=self.name, role=self.role)

    def receive_message(self, message: AgentMessage):
        """Records incoming message from another agent."""
        self.state.messages_received.append(message)

    def execute(self, prompt: str, context: Optional[str] = None) -> AgentMessage:
        """
        Executes agent reasoning step using the underlying LLM provider.

        Args:
            prompt: User task or delegated instruction.
            context: Optional compiled context from prior agent interactions.

        Returns:
            AgentMessage containing structured agent response.
        """
        self.state.status = "running"
        start_time = time.time()

        # Build execution prompt including inter-agent context
        full_context = ""
        if self.state.messages_received:
            incoming = "\n".join([f"[{m.sender_role.upper()}]: {m.content}" for m in self.state.messages_received[-4:]])
            full_context += f"\n--- RECENT MESSAGES RECEIVED ---\n{incoming}\n"

        if context:
            full_context += f"\n--- CONTEXT ---\n{context}\n"

        combined_prompt = f"{full_context}\n--- CURRENT TASK ---\n{prompt}"
        self.state.input_context = combined_prompt

        response: LLMResponse = self.provider.generate(
            prompt=combined_prompt,
            system_prompt=self.system_prompt
        )

        elapsed = time.time() - start_time
        self.state.execution_time += elapsed
        self.state.total_calls += 1

        if response.success:
            self.state.status = "completed"
            self.state.output = response.content
            self.state.token_usage["input_tokens"] += response.input_tokens
            self.state.token_usage["output_tokens"] += response.output_tokens
            self.state.token_usage["total_tokens"] += response.total_tokens
            self.state.estimated_cost_usd += response.estimated_cost_usd
        else:
            self.state.status = "failed"
            self.state.error_information = response.error_message
            self.state.output = f"ERROR: {response.error_message}"

        msg = AgentMessage(
            sender_id=self.agent_id,
            sender_role=self.role,
            receiver_id="coordinator",
            content=self.state.output,
            message_type="inform"
        )
        self.state.messages_sent.append(msg)
        return msg

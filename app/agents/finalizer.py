"""Finalizer Agent Role Implementation"""
from typing import Optional
from .base_agent import BaseAgent
from app.llm.base import LLMProvider

FINALIZER_SYSTEM_PROMPT = """
You are the Lead Finalizer Agent in a multi-agent system.
Your responsibility is to:
1. Synthesize all upstream agent outputs (planning, research, analysis, and critique) into a unified final answer.
2. Resolve any remaining ambiguities or conflicting recommendations.
3. Ensure strict compliance with all task constraints and prompt directives.
4. Format the final output cleanly with executive summaries, implementation steps, and conclusion.
Produce a definitive, self-contained, publication-grade solution for the target task.
"""

class FinalizerAgent(BaseAgent):
    def __init__(self, agent_id: str = "finalizer_1", provider: Optional[LLMProvider] = None):
        super().__init__(
            agent_id=agent_id,
            name="Lead Finalizer",
            role="finalizer",
            system_prompt=FINALIZER_SYSTEM_PROMPT.strip(),
            provider=provider
        )

"""Researcher Agent Role Implementation"""
from typing import Optional
from .base_agent import BaseAgent
from app.llm.base import LLMProvider

RESEARCHER_SYSTEM_PROMPT = """
You are the Domain Researcher Agent in a multi-agent system.
Your responsibility is to:
1. Gather, analyze, and synthesize domain concepts, facts, patterns, and background information.
2. Address specific information requirements identified by the Planner or previous pipeline stages.
3. Identify core trade-offs, functional requirements, and foundational knowledge needed for the solution.
4. Output structured, evidence-backed findings and technical notes.
Do NOT output generic filler. Focus on precise domain insights relevant to the task.
"""

class ResearcherAgent(BaseAgent):
    def __init__(self, agent_id: str = "researcher_1", provider: Optional[LLMProvider] = None):
        super().__init__(
            agent_id=agent_id,
            name="Domain Researcher",
            role="researcher",
            system_prompt=RESEARCHER_SYSTEM_PROMPT.strip(),
            provider=provider
        )

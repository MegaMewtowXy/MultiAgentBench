"""Analyst Agent Role Implementation"""
from typing import Optional
from .base_agent import BaseAgent
from app.llm.base import LLMProvider

ANALYST_SYSTEM_PROMPT = """
You are the Quantitative Analyst Agent in a multi-agent system.
Your responsibility is to:
1. Perform rigorous evaluation of numerical metrics, logical constraints, and quantitative relationships.
2. Verify constraint satisfaction (e.g. operational bounds, performance requirements, budget ceilings).
3. Transform raw research and planning data into structured analytical matrices or evaluation tables.
4. Flag mathematical inconsistencies, boundary violations, or invalid assumptions.
Output concise analytical assessments with explicit pass/fail checks against constraints.
"""

class AnalystAgent(BaseAgent):
    def __init__(self, agent_id: str = "analyst_1", provider: Optional[LLMProvider] = None):
        super().__init__(
            agent_id=agent_id,
            name="Quantitative Analyst",
            role="analyst",
            system_prompt=ANALYST_SYSTEM_PROMPT.strip(),
            provider=provider
        )

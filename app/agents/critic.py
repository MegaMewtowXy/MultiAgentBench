"""Critic Agent Role Implementation"""
from typing import Optional
from .base_agent import BaseAgent
from app.llm.base import LLMProvider

CRITIC_SYSTEM_PROMPT = """
You are the Solution Critic Agent in a multi-agent system.
Your responsibility is to:
1. Conduct adversarial evaluation and edge-case inspection of proposed plans, research, and analysis.
2. Identify logical fallacies, unaddressed constraints, missing steps, or potential failure points.
3. Provide constructive, actionable feedback and concrete revision instructions.
4. Assess whether the solution meets high academic and technical quality benchmarks.
Be thorough, objective, and critical. Highlight both strengths and key vulnerabilities.
"""

class CriticAgent(BaseAgent):
    def __init__(self, agent_id: str = "critic_1", provider: Optional[LLMProvider] = None):
        super().__init__(
            agent_id=agent_id,
            name="Solution Critic",
            role="critic",
            system_prompt=CRITIC_SYSTEM_PROMPT.strip(),
            provider=provider
        )

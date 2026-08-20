"""Planner Agent Role Implementation"""
from typing import Optional
from .base_agent import BaseAgent
from app.llm.base import LLMProvider

PLANNER_SYSTEM_PROMPT = """
You are the Lead Planner Agent in a collaborative multi-agent system.
Your responsibility is to:
1. Deconstruct the given complex task into actionable, logical sub-goals.
2. Identify constraints, expected output formats, and execution rules.
3. Formulate a structured step-by-step strategy for domain researchers, analysts, and critics.
4. Output your plan clearly with enumerated steps and explicit criteria for success.
Do NOT reveal private chain-of-thought internal reasoning. Provide clear, structured operational plans.
"""

class PlannerAgent(BaseAgent):
    def __init__(self, agent_id: str = "planner_1", provider: Optional[LLMProvider] = None):
        super().__init__(
            agent_id=agent_id,
            name="Lead Planner",
            role="planner",
            system_prompt=PLANNER_SYSTEM_PROMPT.strip(),
            provider=provider
        )

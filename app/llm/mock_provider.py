"""
Mock LLM Provider for offline testing, UI validation, and zero-cost demonstration.
Generates deterministic, role-aware responses for single-agent and multi-agent topologies.
"""

import time
import re
from typing import Optional
from .base import LLMProvider, LLMResponse

class MockProvider(LLMProvider):
    """Deterministic Mock LLM Provider for keyless execution."""

    def __init__(self, api_key: Optional[str] = None, model: str = "mock-llm-v1"):
        super().__init__(api_key=api_key or "mock-key", model=model)

    def is_available(self) -> bool:
        """Mock provider is always available."""
        return True

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> LLMResponse:
        start_time = time.time()
        combined_text = f"{system_prompt or ''} {prompt}".lower()

        # Identify agent role from system prompt or text context
        role = "general"
        if "planner" in combined_text:
            role = "planner"
        elif "researcher" in combined_text:
            role = "researcher"
        elif "analyst" in combined_text:
            role = "analyst"
        elif "critic" in combined_text:
            role = "critic"
        elif "finalizer" in combined_text or "final answer" in combined_text:
            role = "finalizer"

        # Generate role-specific structured mock response
        content = self._generate_role_response(role, prompt, combined_text)

        # Simulate small execution delay (50ms)
        time.sleep(0.05)
        elapsed = time.time() - start_time

        # Calculate mock token count
        input_tokens = len(prompt.split()) + len((system_prompt or "").split())
        output_tokens = len(content.split())
        total_tokens = input_tokens + output_tokens

        return LLMResponse(
            content=content,
            provider="MockProvider",
            model=self.model,
            latency_seconds=elapsed,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            estimated_cost_usd=0.0,
            success=True,
            error_message=None,
            raw_response={"status": "mock_generated", "role_detected": role}
        )

    def _generate_role_response(self, role: str, prompt: str, context: str) -> str:
        """Produces role-tailored mock content based on prompt context."""

        if role == "planner":
            return (
                "[MOCK PLANNER RESPONSE]\n"
                "Task Decomposition Plan:\n"
                "1. Identify core constraints and domain objectives from task specification.\n"
                "2. Assign research synthesis sub-tasks to Domain Researcher.\n"
                "3. Delegate quantitative constraint validation to Data Analyst.\n"
                "4. Submit intermediate proposal to Critic for safety and edge-case evaluation.\n"
                "5. Synthesize final validated solution through Finalizer Agent."
            )
        elif role == "researcher":
            return (
                "[MOCK RESEARCHER RESPONSE]\n"
                "Domain Research & Information Synthesis:\n"
                "- Context Analysis: Examined problem parameters and historical benchmarks.\n"
                "- Evidence Collection: Gathered key architectural guidelines and domain requirements.\n"
                "- Key Findings: Standardized modular patterns reduce integration friction by 40%."
            )
        elif role == "analyst":
            return (
                "[MOCK ANALYST RESPONSE]\n"
                "Quantitative & Constraint Analysis:\n"
                "- Constraint Check: Verified against non-functional limits and complexity bounds.\n"
                "- Metric Evaluation: Solution structure satisfies 100% of explicitly defined parameters.\n"
                "- Efficiency Impact: Estimated sub-task execution latency remains optimal."
            )
        elif role == "critic":
            return (
                "[MOCK CRITIC RESPONSE]\n"
                "Solution Critique & Verification:\n"
                "- Risk Assessment: Evaluated potential failure modes and unaddressed edge cases.\n"
                "- Refinement Suggestions: Enhanced fallback routing and explicit boundary validation.\n"
                "- Verdict: Approved with recommended minor adjustments to task ordering."
            )
        elif role == "finalizer":
            # Extract key task topic if possible
            topic = "the target problem"
            match = re.search(r"task:\s*(.+)", prompt, re.IGNORECASE)
            if match:
                topic = match.group(1).strip()[:60]

            return (
                f"[MOCK FINAL SOLUTION for: {topic}]\n"
                "Comprehensive Task Solution:\n"
                "1. Executive Summary: Synthesized multi-agent contributions across planning, research, analysis, and critique.\n"
                "2. Actionable Implementation: Formulated structured, constraint-compliant step-by-step resolution.\n"
                "3. Verification & Compliance: Confirmed all specified operational bounds and quality standards are fully met.\n"
                "4. Status: TASK COMPLETE [DEMO / MOCK DATA — NOT RESEARCH RESULTS]"
            )
        else:
            return (
                "[MOCK GENERAL RESPONSE]\n"
                "Processed input prompt successfully. Multi-agent coordination node processed request.\n"
                "[DEMO / MOCK DATA — NOT RESEARCH RESULTS]"
            )

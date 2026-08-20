"""
Groq API Provider implementation.
Provides ultra-fast inference using Groq LLaMA models.
"""

import time
import os
from typing import Optional
from .base import LLMProvider, LLMResponse

class GroqProvider(LLMProvider):
    """LLM Provider for Groq Cloud API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.3-70b-versatile"):
        api_key = os.getenv("GROQ_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.client = None
        if self.api_key:
            try:
                from groq import Groq
                self.client = Groq(api_key=self.api_key)
            except ImportError:
                self.client = None

    def is_available(self) -> bool:
        """Returns True if API key is provided and Groq SDK client is initialized."""
        return bool(self.api_key and self.client)

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> LLMResponse:
        if not self.is_available():
            return LLMResponse(
                content="",
                provider="GroqProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="Groq API key missing or 'groq' package not installed."
            )

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        start_time = time.time()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            elapsed = time.time() - start_time

            choice = response.choices[0]
            content = choice.message.content or ""

            usage = getattr(response, "usage", None)
            input_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
            output_tokens = getattr(usage, "completion_tokens", 0) if usage else 0
            total_tokens = getattr(usage, "total_tokens", input_tokens + output_tokens) if usage else 0

            # Estimated cost for LLaMA 3.3 70B on Groq (~$0.59 / 1M tokens)
            estimated_cost = (total_tokens / 1_000_000) * 0.59

            return LLMResponse(
                content=content,
                provider="GroqProvider",
                model=self.model,
                latency_seconds=elapsed,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                total_tokens=total_tokens,
                estimated_cost_usd=estimated_cost,
                success=True,
                error_message=None
            )
        except Exception as e:
            elapsed = time.time() - start_time
            return LLMResponse(
                content="",
                provider="GroqProvider",
                model=self.model,
                latency_seconds=elapsed,
                success=False,
                error_message=f"Groq API Error: {str(e)}"
            )

"""
OpenAI API Provider implementation.
Provides inference using OpenAI GPT models (e.g. GPT-4o, GPT-4o-mini).
"""

import time
import os
from typing import Optional
from .base import LLMProvider, LLMResponse

class OpenAIProvider(LLMProvider):
    """LLM Provider for OpenAI API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o-mini"):
        api_key = os.getenv("OPENAI_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                self.client = None

    def is_available(self) -> bool:
        """Returns True if OpenAI API key is configured and SDK client is initialized."""
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
                provider="OpenAIProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="OpenAI API key missing or 'openai' package not installed."
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

            # Estimated cost for GPT-4o-mini ($0.15 / 1M input, $0.60 / 1M output)
            estimated_cost = ((input_tokens / 1_000_000) * 0.15) + ((output_tokens / 1_000_000) * 0.60)

            return LLMResponse(
                content=content,
                provider="OpenAIProvider",
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
                provider="OpenAIProvider",
                model=self.model,
                latency_seconds=elapsed,
                success=False,
                error_message=f"OpenAI API Error: {str(e)}"
            )

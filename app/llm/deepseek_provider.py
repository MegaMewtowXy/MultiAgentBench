"""
DeepSeek API Provider implementation.
Provides inference using official DeepSeek OpenAI-compatible API endpoints.
"""

import time
import os
from typing import Optional
from .base import LLMProvider, LLMResponse

from dotenv import load_dotenv
load_dotenv()

class DeepSeekProvider(LLMProvider):
    """LLM Provider for DeepSeek API using OpenAI-compatible client."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "deepseek-v4-flash",
        base_url: str = "https://api.deepseek.com"
    ):
        api_key = os.getenv("DEEPSEEK_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.base_url = base_url
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
            except ImportError:
                self.client = None

    def is_available(self) -> bool:
        """Returns True if DeepSeek API key is configured and OpenAI client is initialized."""
        return bool(self.api_key and self.client)

    def _sanitize_error(self, err_msg: str) -> str:
        """Redacts API key from error messages if present."""
        if not err_msg:
            return ""
        if self.api_key and self.api_key in err_msg:
            err_msg = err_msg.replace(self.api_key, "[REDACTED_API_KEY]")
        return err_msg

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
                provider="DeepSeekProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="DeepSeek API key missing or 'openai' SDK package not installed."
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
            msg = choice.message
            content = getattr(msg, "content", "") or ""
            if not content and hasattr(msg, "reasoning_content") and getattr(msg, "reasoning_content", None):
                content = getattr(msg, "reasoning_content")

            usage = getattr(response, "usage", None)
            input_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
            output_tokens = getattr(usage, "completion_tokens", 0) if usage else 0
            total_tokens = getattr(usage, "total_tokens", input_tokens + output_tokens) if usage else 0

            # Estimated cost for DeepSeek V4 Flash (~$0.14 / 1M input, $0.28 / 1M output)
            estimated_cost = ((input_tokens / 1_000_000) * 0.14) + ((output_tokens / 1_000_000) * 0.28)

            return LLMResponse(
                content=content,
                provider="DeepSeekProvider",
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
            clean_err = self._sanitize_error(str(e))
            return LLMResponse(
                content="",
                provider="DeepSeekProvider",
                model=self.model,
                latency_seconds=elapsed,
                success=False,
                error_message=f"DeepSeek API Error: {clean_err}"
            )

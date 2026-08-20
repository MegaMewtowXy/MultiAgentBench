"""
Google Gemini API Provider implementation.
Provides inference using Google Generative AI models.
"""

import time
import os
from typing import Optional
from .base import LLMProvider, LLMResponse

class GeminiProvider(LLMProvider):
    """LLM Provider for Google Gemini API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-3.1-flash-lite"):
        api_key = os.getenv("GEMINI_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.genai = None
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.genai = genai
            except ImportError:
                self.genai = None

    def is_available(self) -> bool:
        """Returns True if Gemini API key is configured and SDK is installed."""
        return bool(self.api_key and self.genai)

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
                provider="GeminiProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="Gemini API key missing or 'google-generativeai' package not installed."
            )

        start_time = time.time()
        try:
            model_inst = self.genai.GenerativeModel(
                model_name=self.model,
                system_instruction=system_prompt if system_prompt else None
            )
            config = self.genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
            response = model_inst.generate_content(prompt, generation_config=config)
            elapsed = time.time() - start_time

            content = response.text if hasattr(response, "text") else ""

            # Extract token usage metadata if provided
            input_tokens = 0
            output_tokens = 0
            if hasattr(response, "usage_metadata") and response.usage_metadata:
                input_tokens = getattr(response.usage_metadata, "prompt_token_count", 0) or 0
                output_tokens = getattr(response.usage_metadata, "candidates_token_count", 0) or 0
            total_tokens = input_tokens + output_tokens

            # Estimated cost for Gemini Flash Lite (~$0.15 / 1M tokens)
            estimated_cost = (total_tokens / 1_000_000) * 0.15

            return LLMResponse(
                content=content,
                provider="GeminiProvider",
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
                provider="GeminiProvider",
                model=self.model,
                latency_seconds=elapsed,
                success=False,
                error_message=f"Gemini API Error: {clean_err}"
            )

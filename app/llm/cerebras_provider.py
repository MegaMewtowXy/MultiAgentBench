"""
Cerebras API Provider implementation.
Provides inference using official Cerebras OpenAI-compatible API endpoints for gpt-oss-120b.
Implements rate-limiting (5 RPM / 30,000 TPM) and exponential backoff retry for HTTP 429.
"""

import time
import os
from typing import Optional, List
from .base import LLMProvider, LLMResponse
from dotenv import load_dotenv

load_dotenv()

class CerebrasProvider(LLMProvider):
    """LLM Provider for Cerebras API using OpenAI-compatible client."""

    # Class-level rate-limiter trackers for Cerebras quota (5 RPM, 30,000 TPM)
    _request_timestamps: List[float] = []
    _token_window: List[tuple] = []  # (timestamp, token_count)
    _last_request_time: float = 0.0

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-oss-120b",
        base_url: str = "https://api.cerebras.ai/v1",
        max_retries: int = 5,
        requests_per_minute: int = 5,
        tokens_per_minute: int = 30000
    ):
        api_key = os.getenv("CEREBRAS_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.base_url = base_url
        self.max_retries = max_retries
        self.rpm_limit = requests_per_minute
        self.tpm_limit = tokens_per_minute
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
            except ImportError:
                self.client = None

    def is_available(self) -> bool:
        """Returns True if Cerebras API key is configured and client initialized."""
        return bool(self.api_key and self.client)

    def _sanitize_error(self, err_msg: str) -> str:
        """Redacts API key from error messages if present."""
        if not err_msg:
            return ""
        if self.api_key and self.api_key in err_msg:
            err_msg = err_msg.replace(self.api_key, "[REDACTED_API_KEY]")
        return err_msg

    def _apply_rate_limiting(self, estimated_prompt_tokens: int = 500):
        """Enforces rate limits (5 RPM / 30,000 TPM) via controlled delay before request."""
        now = time.time()
        window = 60.0

        # Purge timestamps older than 60s
        CerebrasProvider._request_timestamps = [
            t for t in CerebrasProvider._request_timestamps if now - t < window
        ]
        CerebrasProvider._token_window = [
            (t, count) for (t, count) in CerebrasProvider._token_window if now - t < window
        ]

        # 1. Enforce RPM limit (5 RPM -> minimum 12 seconds per request window)
        if len(CerebrasProvider._request_timestamps) >= self.rpm_limit:
            oldest = CerebrasProvider._request_timestamps[0]
            wait_time = window - (now - oldest) + 0.5
            if wait_time > 0:
                time.sleep(wait_time)
                now = time.time()

        # Enforce inter-request spacing (~12 seconds) to avoid RPM spikes
        time_since_last = now - CerebrasProvider._last_request_time
        min_spacing = 60.0 / self.rpm_limit  # 12.0s for 5 RPM
        if time_since_last < min_spacing:
            sleep_needed = min_spacing - time_since_last
            time.sleep(sleep_needed)

        # 2. Enforce TPM limit (30,000 TPM)
        current_tokens = sum(count for _, count in CerebrasProvider._token_window)
        if current_tokens + estimated_prompt_tokens > self.tpm_limit and CerebrasProvider._token_window:
            oldest_t = CerebrasProvider._token_window[0][0]
            wait_time = window - (now - oldest_t) + 0.5
            if wait_time > 0:
                time.sleep(wait_time)

        # Update timestamps
        now_final = time.time()
        CerebrasProvider._request_timestamps.append(now_final)
        CerebrasProvider._last_request_time = now_final

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
                provider="CerebrasProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="Cerebras API key missing or 'openai' SDK package not installed."
            )

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        # Controlled rate-limiting throttle before sending
        self._apply_rate_limiting(estimated_prompt_tokens=len(prompt) // 4)

        start_time = time.time()
        retries = 0

        while retries <= self.max_retries:
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

                # Record token usage for TPM tracking
                CerebrasProvider._token_window.append((time.time(), total_tokens))

                # Estimated cost for Cerebras gpt-oss-120b ($0.10 / 1M input, $0.10 / 1M output)
                estimated_cost = ((input_tokens / 1_000_000) * 0.10) + ((output_tokens / 1_000_000) * 0.10)

                return LLMResponse(
                    content=content,
                    provider="CerebrasProvider",
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
                err_str = str(e)
                clean_err = self._sanitize_error(err_str)

                # Exponential backoff for HTTP 429 Rate Limits
                if ("429" in err_str or "rate limit" in err_str.lower()) and retries < self.max_retries:
                    retries += 1
                    backoff = min(60.0, (2 ** retries) * 5.0)
                    time.sleep(backoff)
                    continue

                elapsed = time.time() - start_time
                return LLMResponse(
                    content="",
                    provider="CerebrasProvider",
                    model=self.model,
                    latency_seconds=elapsed,
                    success=False,
                    error_message=f"Cerebras API Error: {clean_err}"
                )

"""
Cohere API Provider implementation.
Provides inference using Cohere V2 official API endpoints for command-a-plus-05-2026.
Implements rate-limiting (20 RPM) and exponential backoff retry for HTTP 429.
"""

import time
import os
import json
import urllib.request
import urllib.error
from typing import Optional, List, Any
from .base import LLMProvider, LLMResponse
from app.utils.config import Config, default_config, resolve_setting
from dotenv import load_dotenv

load_dotenv()

class CohereProvider(LLMProvider):
    """LLM Provider for Cohere API using official V2 REST endpoints."""

    # Class-level rate-limiter trackers for Cohere API calls
    _request_timestamps: List[float] = []
    _last_request_time: float = 0.0

    # Provider-specific explicit configuration overrides (None = inherit system default)
    OVERRIDE_TIMEOUT: Optional[int] = 90
    OVERRIDE_MAX_TOKENS: Optional[int] = 8192
    OVERRIDE_RPM: Optional[int] = 39

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "command-a-plus-05-2026",
        base_url: str = "https://api.cohere.com/v2/chat",
        max_retries: Optional[int] = None,
        requests_per_minute: Optional[int] = None,
        timeout: Optional[int] = None,
        max_tokens_override: Optional[int] = None,
        config: Optional[Config] = None
    ):
        api_key = os.getenv("COHERE_API_KEY") if api_key is None else api_key
        super().__init__(api_key=api_key, model=model)
        self.base_url = base_url

        cfg = config or default_config

        # Per-setting independent precedence resolution:
        # 1. Instance arg (if not None) -> 2. Provider explicit override (if not None) -> 3. System default config
        self.request_timeout = resolve_setting(timeout, getattr(self, "OVERRIDE_TIMEOUT", None), getattr(cfg, "request_timeout", 30))
        self.rpm_limit = resolve_setting(requests_per_minute, getattr(self, "OVERRIDE_RPM", None), getattr(cfg, "requests_per_minute", 20))
        self.max_tokens_floor = resolve_setting(max_tokens_override, getattr(self, "OVERRIDE_MAX_TOKENS", None), getattr(cfg, "max_tokens", 1024))
        self.max_retries = resolve_setting(max_retries, getattr(cfg, "retry_limit", 3), 3)

    def is_available(self) -> bool:
        """Returns True if Cohere API key is configured."""
        return bool(self.api_key and len(self.api_key.strip()) > 0)

    def _sanitize_error(self, err_msg: str) -> str:
        """Redacts API key from error messages if present."""
        if not err_msg:
            return ""
        if self.api_key and self.api_key in err_msg:
            err_msg = err_msg.replace(self.api_key, "[REDACTED_API_KEY]")
        return err_msg

    def _apply_rate_limiting(self):
        """Enforces rate limits via controlled delay before request."""
        now = time.time()
        window = 60.0

        # Purge timestamps older than 60s
        CohereProvider._request_timestamps = [
            t for t in CohereProvider._request_timestamps if now - t < window
        ]

        # Enforce RPM limit
        if len(CohereProvider._request_timestamps) >= self.rpm_limit:
            oldest = CohereProvider._request_timestamps[0]
            wait_time = window - (now - oldest) + 0.2
            if wait_time > 0:
                time.sleep(wait_time)
                now = time.time()

        # Inter-request spacing
        time_since_last = now - CohereProvider._last_request_time
        min_spacing = 60.0 / self.rpm_limit
        if time_since_last < min_spacing:
            sleep_needed = min_spacing - time_since_last
            time.sleep(sleep_needed)

        now_final = time.time()
        CohereProvider._request_timestamps.append(now_final)
        CohereProvider._last_request_time = now_final

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
                provider="CohereProvider",
                model=self.model,
                latency_seconds=0.0,
                success=False,
                error_message="Cohere API key missing or 'COHERE_API_KEY' not configured."
            )

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        # Ensure max_tokens accommodates thinking + user-visible response text (uses resolved max_tokens_floor)
        request_max_tokens = max(max_tokens, self.max_tokens_floor)
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": request_max_tokens
        }

        # Controlled rate-limiting throttle before sending
        self._apply_rate_limiting()

        start_time = time.time()
        retries = 0

        while retries <= self.max_retries:
            try:
                req_data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    self.base_url,
                    data=req_data,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    method="POST"
                )

                with urllib.request.urlopen(req, timeout=self.request_timeout) as resp:
                    raw_body = resp.read().decode("utf-8")
                    data = json.loads(raw_body)

                elapsed = time.time() - start_time

                # Parse V2 chat response content: strictly separate user-visible text from thinking metadata
                text_content = ""
                thinking_content = ""
                msg_data = data.get("message", {})
                content_list = msg_data.get("content", [])

                if isinstance(content_list, list):
                    for item in content_list:
                        if isinstance(item, dict):
                            b_type = item.get("type")
                            if b_type == "text":
                                text_content += item.get("text", "")
                            elif b_type == "thinking":
                                thinking_content += item.get("thinking", "")
                        elif isinstance(item, str):
                            text_content += item

                if not text_content and isinstance(msg_data.get("content"), str):
                    text_content = msg_data.get("content")

                if not text_content and "text" in data:
                    text_content = data.get("text", "")

                # Parse token usage
                usage_tokens = data.get("usage", {}).get("tokens", {})
                input_tokens = usage_tokens.get("input_tokens", 0)
                output_tokens = usage_tokens.get("output_tokens", 0)
                total_tokens = input_tokens + output_tokens

                # Estimated cost for Cohere Command A+ ($0.50 / 1M input, $1.50 / 1M output)
                estimated_cost = ((input_tokens / 1_000_000) * 0.50) + ((output_tokens / 1_000_000) * 1.50)

                # Strict research rule: user-visible text is required. Never use internal thinking as final answer.
                if not text_content:
                    err_msg = "Cohere API Error: Incomplete generation — response truncated during thinking phase before user-visible text block was produced."
                    return LLMResponse(
                        content="",
                        provider="CohereProvider",
                        model=self.model,
                        latency_seconds=elapsed,
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        total_tokens=total_tokens,
                        estimated_cost_usd=estimated_cost,
                        success=False,
                        error_message=err_msg
                    )

                return LLMResponse(
                    content=text_content,
                    provider="CohereProvider",
                    model=self.model,
                    latency_seconds=elapsed,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    total_tokens=total_tokens,
                    estimated_cost_usd=estimated_cost,
                    success=True,
                    error_message=None
                )

            except urllib.error.HTTPError as e:
                err_body = e.read().decode("utf-8") if hasattr(e, "read") else str(e)
                clean_err = self._sanitize_error(err_body)

                if e.code == 429 and retries < self.max_retries:
                    retries += 1
                    backoff = min(60.0, (2 ** retries) * 3.0)
                    time.sleep(backoff)
                    self._apply_rate_limiting()
                    continue

                elapsed = time.time() - start_time
                return LLMResponse(
                    content="",
                    provider="CohereProvider",
                    model=self.model,
                    latency_seconds=elapsed,
                    success=False,
                    error_message=f"Cohere API Error ({e.code}): {clean_err}"
                )

            except Exception as e:
                elapsed = time.time() - start_time
                clean_err = self._sanitize_error(str(e))
                return LLMResponse(
                    content="",
                    provider="CohereProvider",
                    model=self.model,
                    latency_seconds=elapsed,
                    success=False,
                    error_message=f"Cohere API Error: {clean_err}"
                )

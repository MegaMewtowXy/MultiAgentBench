"""
Base Abstract Interface for LLM Providers.
Standardizes inference calls, latency tracking, token measurement, safe connectivity testing, and error reporting.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class LLMResponse:
    """Standardized response container across all LLM providers."""
    content: str
    provider: str
    model: str
    latency_seconds: float
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost_usd: float = 0.0
    success: bool = True
    error_message: Optional[str] = None
    raw_response: Optional[Dict[str, Any]] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary for logging and serialization (excluding auth data)."""
        return {
            "content": self.content,
            "provider": self.provider,
            "model": self.model,
            "latency_seconds": round(self.latency_seconds, 4),
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "estimated_cost_usd": round(self.estimated_cost_usd, 6),
            "success": self.success,
            "error_message": self.error_message
        }

class LLMProvider(ABC):
    """Abstract Base Class for provider-independent LLM execution."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> LLMResponse:
        """Executes text generation request to the LLM."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Returns True if the provider credentials and network endpoints are ready."""
        pass

    def test_connection(self) -> Dict[str, Any]:
        """
        Executes a safe, minimal connectivity test request without revealing credentials.
        Returns dict with status ("API connection successful" or "API connection failed").
        """
        if not self.is_available():
            return {
                "success": False,
                "message": f"API connection failed: {self.__class__.__name__} credential is not configured.",
                "latency_seconds": 0.0
            }

        try:
            resp = self.generate(prompt="ping", max_tokens=5, temperature=0.0)
            if resp.success:
                return {
                    "success": True,
                    "message": "API connection successful",
                    "latency_seconds": resp.latency_seconds
                }
            else:
                return {
                    "success": False,
                    "message": f"API connection failed: {resp.error_message}",
                    "latency_seconds": resp.latency_seconds
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"API connection failed: {str(e)}",
                "latency_seconds": 0.0
            }

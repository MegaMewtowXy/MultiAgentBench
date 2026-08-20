"""
Configuration management for MultiAgentBench implementation.
Centralizes environment settings, API credentials, model configurations, and safety limits.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables if .env exists
load_dotenv()

@dataclass
class Config:
    # Provider Settings
    default_provider: str = os.getenv("DEFAULT_PROVIDER", "mock")
    mock_mode: bool = os.getenv("MOCK_MODE", "true").lower() in ("true", "1", "yes")

    # API Keys (loaded securely from environment)
    groq_api_key: Optional[str] = os.getenv("GROQ_API_KEY")
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    deepseek_api_key: Optional[str] = os.getenv("DEEPSEEK_API_KEY")
    cerebras_api_key: Optional[str] = os.getenv("CEREBRAS_API_KEY")
    cohere_api_key: Optional[str] = os.getenv("COHERE_API_KEY")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")

    # Default Model Identifiers per Provider
    provider_models: Dict[str, str] = field(default_factory=lambda: {
        "mock": "mock-llm-v1",
        "groq": "llama-3.3-70b-versatile",
        "gemini": "gemini-3.1-flash-lite",
        "deepseek": "deepseek-v4-flash",
        "cerebras": "gpt-oss-120b",
        "cohere": "command-a-plus-05-2026",
        "openai": "gpt-4o-mini"
    })

    # Model Parameters
    temperature: float = 0.7
    max_tokens: int = 1024

    # API Safety & Resource Limits (Api Cost Protection)
    max_calls_per_task: int = 15
    max_calls_per_experiment: int = 60
    max_agent_iterations: int = 5
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "30"))
    requests_per_minute: int = int(os.getenv("DEFAULT_RPM", "20"))
    retry_limit: int = 3

    # Storage Paths
    benchmark_data_path: str = os.path.join("data", "tasks", "benchmark_tasks.json")
    results_dir: str = os.path.join("data", "results")

    def get_api_key(self, provider_name: str) -> Optional[str]:
        """Returns API key for specified provider without logging secrets."""
        provider_name = provider_name.lower()
        if provider_name == "groq":
            return self.groq_api_key
        elif provider_name == "gemini":
            return self.gemini_api_key
        elif provider_name == "deepseek":
            return self.deepseek_api_key
        elif provider_name == "cerebras":
            return self.cerebras_api_key
        elif provider_name == "cohere":
            return self.cohere_api_key
        elif provider_name == "openai":
            return self.openai_api_key
        return None

    def get_model_name(self, provider_name: str) -> str:
        """Returns the configured model name for a provider."""
        return self.provider_models.get(provider_name.lower(), "mock-llm-v1")

    def to_dict(self) -> Dict[str, Any]:
        """Returns a sanitized dict representation (excluding secret API keys)."""
        return {
            "default_provider": self.default_provider,
            "mock_mode": self.mock_mode,
            "provider_models": self.provider_models,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "max_calls_per_task": self.max_calls_per_task,
            "max_calls_per_experiment": self.max_calls_per_experiment,
            "max_agent_iterations": self.max_agent_iterations,
            "request_timeout": self.request_timeout,
            "retry_limit": self.retry_limit,
            "has_groq_key": bool(self.groq_api_key),
            "has_gemini_key": bool(self.gemini_api_key),
            "has_deepseek_key": bool(self.deepseek_api_key),
            "has_cerebras_key": bool(self.cerebras_api_key),
            "has_cohere_key": bool(self.cohere_api_key),
            "has_openai_key": bool(self.openai_api_key)
        }

# Global default config instance
default_config = Config()

def resolve_setting(override_val: Any, default_val: Any, fallback_val: Any = None) -> Any:
    """
    Resolves configuration setting with explicit per-setting precedence:
      1. Explicit instance argument / provider override (if not None)
      2. Class-level / default configuration setting (if not None)
      3. Hardcoded safe fallback value
    """
    if override_val is not None:
        return override_val
    if default_val is not None:
        return default_val
    return fallback_val

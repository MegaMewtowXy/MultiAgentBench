"""
Structured logging module for MultiAgentBench implementation.
Ensures clean, trace-level debugging without leaking API credentials or sensitive keys.
"""

import logging
import os
import sys
import json
from datetime import datetime
from typing import Optional, Dict, Any

class SecurityFilter(logging.Filter):
    """Filter that masks API keys or secret strings from log outputs."""

    def __init__(self, secrets_to_mask: Optional[list] = None):
        super().__init__()
        self.secrets_to_mask = [s for s in (secrets_to_mask or []) if s]

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        for secret in self.secrets_to_mask:
            if secret and secret in message:
                message = message.replace(secret, "***MASKED_KEY***")
        record.msg = message
        record.args = ()
        return True

def setup_logger(name: str = "MultiAgentBench", log_file: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """Creates a configured logger instance with console and file output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    # Console Handler
    console_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%H:%M:%S"
    )
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(console_formatter)
    logger.addHandler(ch)

    # File Handler if log_file specified
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(file_formatter)
        logger.addHandler(fh)

    # Attach security filter for API keys in environment
    api_keys = [os.getenv("GROQ_API_KEY"), os.getenv("GEMINI_API_KEY"), os.getenv("OPENAI_API_KEY")]
    logger.addFilter(SecurityFilter(secrets_to_mask=api_keys))

    return logger

# Primary logger instance
logger = setup_logger()

def log_experiment_event(logger_inst: logging.Logger, event_type: str, experiment_id: str, data: Dict[str, Any]):
    """Logs structured experiment trace events as JSON strings."""
    payload = {
        "timestamp": datetime.now().isoformat(),
        "experiment_id": experiment_id,
        "event_type": event_type,
        "details": data
    }
    logger_inst.info(f"EVENT_{event_type} | {json.dumps(payload, default=str)}")

"""
API Cost Protection & Resource Guardrails.
Prevents uncontrolled agent loops, excessive token usage, API budget depletion, and timeouts.
"""

from typing import Dict, Any, Optional

class ResourceLimitExceededError(Exception):
    """Raised when an experiment exceeds max API calls, iterations, or cost budget."""
    pass

class GuardrailTracker:
    """Tracks resource consumption during single task or multi-task experiment runs."""

    def __init__(self, max_calls_per_task: int = 15, max_calls_per_experiment: int = 60, max_iterations: int = 5):
        self.max_calls_per_task = max_calls_per_task
        self.max_calls_per_experiment = max_calls_per_experiment
        self.max_iterations = max_iterations

        self.current_experiment_calls = 0
        self.current_task_calls = 0
        self.current_iteration = 0
        self.total_tokens_consumed = 0

    def reset_task(self):
        """Resets counters for a new task execution."""
        self.current_task_calls = 0
        self.current_iteration = 0

    def record_call(self, tokens_used: int = 0):
        """Increments call counters and validates against defined safety thresholds."""
        self.current_task_calls += 1
        self.current_experiment_calls += 1
        self.total_tokens_consumed += tokens_used

        if self.current_task_calls > self.max_calls_per_task:
            raise ResourceLimitExceededError(
                f"Task call limit exceeded: {self.current_task_calls} calls > max allowed ({self.max_calls_per_task})."
            )

        if self.current_experiment_calls > self.max_calls_per_experiment:
            raise ResourceLimitExceededError(
                f"Experiment budget exceeded: {self.current_experiment_calls} calls > max allowed ({self.max_calls_per_experiment})."
            )

    def record_iteration(self):
        """Increments agent step iteration and checks for potential circular loops."""
        self.current_iteration += 1
        if self.current_iteration > self.max_iterations:
            raise ResourceLimitExceededError(
                f"Max agent iteration limit reached: {self.current_iteration} iterations > limit ({self.max_iterations})."
            )

    def estimate_dry_run(self, num_agents: int, num_tasks: int, estimated_calls_per_agent: int = 2) -> Dict[str, Any]:
        """Pre-flight dry run estimating expected API calls and potential token consumption."""
        estimated_calls_per_task = num_agents * estimated_calls_per_agent
        total_estimated_calls = estimated_calls_per_task * num_tasks
        estimated_tokens = total_estimated_calls * 500  # avg 500 tokens per agent turn

        within_limits = (
            estimated_calls_per_task <= self.max_calls_per_task and
            total_estimated_calls <= self.max_calls_per_experiment
        )

        return {
            "num_agents": num_agents,
            "num_tasks": num_tasks,
            "estimated_calls_per_task": estimated_calls_per_task,
            "total_estimated_calls": total_estimated_calls,
            "estimated_tokens": estimated_tokens,
            "max_calls_per_task": self.max_calls_per_task,
            "max_calls_per_experiment": self.max_calls_per_experiment,
            "within_limits": within_limits,
            "warning": None if within_limits else "Estimated API calls exceed configured cost protection thresholds!"
        }

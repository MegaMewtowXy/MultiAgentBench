"""
Benchmark Task Loader and Schema Validation.
Loads benchmark tasks from JSON/JSONL datasets and provides filtering by category or task ID.
Enforces strict anti-leakage boundary separating agent execution inputs from evaluation ground truth.
"""

import json
import os
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TaskDefinition:
    """Schema representing a benchmark task item."""
    task_id: str
    category: str
    prompt: str
    constraints: List[str] = field(default_factory=list)
    expected_properties: List[str] = field(default_factory=list)
    reference_answer: Optional[str] = None
    evaluation_type: str = "constraint_validation"
    difficulty: str = "Medium"

    def to_dict(self) -> Dict[str, Any]:
        """Full representation including ground truth for evaluator use."""
        return {
            "task_id": self.task_id,
            "category": self.category,
            "prompt": self.prompt,
            "constraints": self.constraints,
            "expected_properties": self.expected_properties,
            "reference_answer": self.reference_answer,
            "evaluation_type": self.evaluation_type,
            "difficulty": self.difficulty
        }

    def to_agent_prompt_dict(self) -> Dict[str, Any]:
        """Sanitized representation for agent execution. Excludes reference answers & evaluation keywords to prevent leakage."""
        return {
            "task_id": self.task_id,
            "category": self.category,
            "prompt": self.prompt,
            "constraints": self.constraints
        }

class BenchmarkLoader:
    """Loader for benchmark task definitions with anti-leakage protection."""

    def __init__(self, data_path: Optional[str] = None):
        self.data_path = data_path or os.path.join("data", "tasks", "benchmark_tasks.json")
        self.tasks: List[TaskDefinition] = []
        self.load_tasks()

    def load_tasks(self) -> List[TaskDefinition]:
        """Loads and parses task dataset from disk."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Benchmark task file not found at: {self.data_path}")

        with open(self.data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        self.tasks = [
            TaskDefinition(
                task_id=item["task_id"],
                category=item["category"],
                prompt=item["prompt"],
                constraints=item.get("constraints", []),
                expected_properties=item.get("expected_properties", []),
                reference_answer=item.get("reference_answer"),
                evaluation_type=item.get("evaluation_type", "constraint_validation"),
                difficulty=item.get("difficulty", "Medium")
            )
            for item in raw_data
        ]
        return self.tasks

    def get_task_by_id(self, task_id: str) -> Optional[TaskDefinition]:
        """Returns task definition matching specified task_id."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_tasks_by_category(self, category: str) -> List[TaskDefinition]:
        """Returns list of tasks belonging to specified category."""
        return [t for t in self.tasks if t.category.lower() == category.lower()]

    def list_categories(self) -> List[str]:
        """Returns unique categories available in benchmark dataset."""
        return sorted(list(set(t.category for t in self.tasks)))

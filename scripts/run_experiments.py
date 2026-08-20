"""
CLI Script to execute benchmark matrix experiments from terminal.
Usage: python scripts/run_experiments.py --provider mock --archs single star chain tree graph
"""

import sys
import os
import argparse

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.experiments import ExperimentRunner
from app.utils.logger import logger

def main():
    parser = argparse.ArgumentParser(description="MultiAgentBench Experiment Matrix CLI Runner")
    parser.add_argument("--provider", type=str, default="mock", help="LLM Provider (mock, groq, gemini, openai)")
    parser.add_argument("--archs", nargs="+", default=["single", "star", "chain", "tree", "graph"], help="Architectures to evaluate")
    parser.add_argument("--tasks", nargs="+", default=None, help="Task IDs to evaluate")
    parser.add_argument("--model", type=str, default=None, help="Model override")

    args = parser.parse_args()

    runner = ExperimentRunner()
    logger.info(f"Starting CLI Experiment Matrix with provider={args.provider}...")

    res = runner.run_experiment_matrix(
        provider_name=args.provider,
        architectures=args.archs,
        task_ids=args.tasks,
        model_name=args.model
    )

    print(f"\n=======================================================")
    print(f"EXPERIMENT COMPLETE: {res['experiment_id']}")
    print(f"Total Runs Executed: {res['total_runs']}")
    print(f"Summary CSV: {res['csv_path']}")
    print(f"Detailed JSON: {res['json_path']}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    main()

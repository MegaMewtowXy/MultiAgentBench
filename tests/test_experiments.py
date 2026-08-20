"""
Integration test for Experiment Runner and Result Persistence.
Runs offline using MockProvider.
"""

import pytest
import os
from app.experiments import ExperimentRunner

def test_experiment_runner_mock_execution(tmp_path):
    results_dir = str(tmp_path / "results")
    runner = ExperimentRunner(results_dir=results_dir)

    # Run matrix with 2 topologies and 1 task
    exp_res = runner.run_experiment_matrix(
        provider_name="mock",
        architectures=["single", "star"],
        task_ids=["TASK_PLAN_001"]
    )

    assert exp_res["total_runs"] == 2
    assert os.path.exists(exp_res["json_path"])
    assert os.path.exists(exp_res["csv_path"])
    assert len(exp_res["summary_rows"]) == 2

    # Check content of summary rows
    row_single = exp_res["summary_rows"][0]
    assert row_single["architecture"] == "single"
    assert row_single["task_id"] == "TASK_PLAN_001"
    assert row_single["total_calls"] == 1

    row_star = exp_res["summary_rows"][1]
    assert row_star["architecture"] == "star"
    assert row_star["total_calls"] == 5

"""
Comparative Analytics and Charts Module for MultiAgentBench implementation.
Transforms raw experiment summary rows into structured DataFrames and chart metrics for Streamlit.
"""

import pandas as pd
from typing import List, Dict, Any, Tuple

def create_summary_charts(summary_rows: List[Dict[str, Any]]) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """
    Processes experiment summary rows into comparative DataFrames.

    Returns:
        Tuple of (Full DataFrame, Dictionary of grouped metric DataFrames).
    """
    if not summary_rows:
        empty_df = pd.DataFrame()
        return empty_df, {}

    df = pd.DataFrame(summary_rows)

    # Ensure required numerical columns are properly cast
    numeric_cols = [
        "task_score", "quality_score", "coordination_score",
        "constraint_satisfaction", "latency_seconds", "total_calls",
        "total_tokens", "estimated_cost_usd"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    if "task_success" in df.columns:
        df["task_success_int"] = df["task_success"].astype(int)

    # Grouped Metrics by Architecture
    arch_summary = df.groupby("architecture").agg(
        total_runs=("task_id", "count"),
        success_rate=("task_success_int", "mean"),
        avg_task_score=("task_score", "mean"),
        avg_quality_score=("quality_score", "mean"),
        avg_coordination_score=("coordination_score", "mean"),
        avg_constraint_satisfaction=("constraint_satisfaction", "mean"),
        avg_latency_seconds=("latency_seconds", "mean"),
        avg_total_calls=("total_calls", "mean"),
        avg_total_tokens=("total_tokens", "mean"),
        avg_cost_usd=("estimated_cost_usd", "mean")
    ).reset_index()

    # Format percentages and rounds for display
    arch_summary["success_rate_pct"] = (arch_summary["success_rate"] * 100).round(1)
    arch_summary["avg_quality_score"] = arch_summary["avg_quality_score"].round(2)
    arch_summary["avg_coordination_score"] = arch_summary["avg_coordination_score"].round(2)
    arch_summary["avg_latency_seconds"] = arch_summary["avg_latency_seconds"].round(3)
    arch_summary["avg_total_calls"] = arch_summary["avg_total_calls"].round(1)

    # Category-wise breakdown
    category_summary = pd.DataFrame()
    if "category" in df.columns:
        category_summary = df.groupby(["category", "architecture"]).agg(
            avg_quality_score=("quality_score", "mean"),
            avg_latency_seconds=("latency_seconds", "mean"),
            avg_calls=("total_calls", "mean")
        ).reset_index()

    grouped_dfs = {
        "architecture_summary": arch_summary,
        "category_summary": category_summary
    }

    return df, grouped_dfs

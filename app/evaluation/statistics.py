"""
Statistical Analysis Module for MultiAgentBench Implementation.
Computes descriptive statistics, confidence intervals, non-parametric hypothesis tests, and effect sizes.
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, List, Optional, Tuple

class StatisticalAnalyzer:
    """Statistical analyzer for multi-agent comparative research experiments."""

    @staticmethod
    def calculate_descriptive_stats(values: List[float]) -> Dict[str, Any]:
        """Calculates mean, median, std dev, min, max, and 95% confidence interval."""
        if not values:
            return {
                "count": 0, "mean": 0.0, "median": 0.0, "std_dev": 0.0,
                "min": 0.0, "max": 0.0, "ci_95_lower": 0.0, "ci_95_upper": 0.0
            }

        arr = np.array(values, dtype=float)
        count = len(arr)
        mean_val = float(np.mean(arr))
        median_val = float(np.median(arr))
        std_val = float(np.std(arr, ddof=1)) if count > 1 else 0.0
        min_val = float(np.min(arr))
        max_val = float(np.max(arr))

        # Standard Error & 95% CI (1.96 * SE)
        se = std_val / np.sqrt(count) if count > 0 else 0.0
        ci_lower = mean_val - (1.96 * se)
        ci_upper = mean_val + (1.96 * se)

        return {
            "count": count,
            "mean": round(mean_val, 4),
            "median": round(median_val, 4),
            "std_dev": round(std_val, 4),
            "min": round(min_val, 4),
            "max": round(max_val, 4),
            "ci_95_lower": round(ci_lower, 4),
            "ci_95_upper": round(ci_upper, 4)
        }

    @staticmethod
    def calculate_cohens_d(group1: List[float], group2: List[float]) -> float:
        """Calculates Cohen's d effect size between two execution groups."""
        if len(group1) < 2 or len(group2) < 2:
            return 0.0

        n1, n2 = len(group1), len(group2)
        s1, s2 = np.std(group1, ddof=1), np.std(group2, ddof=1)
        s_pooled = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))

        if s_pooled == 0.0:
            return 0.0

        d = (np.mean(group1) - np.mean(group2)) / s_pooled
        return round(float(d), 4)

    @staticmethod
    def calculate_paired_differences(
        df_results: pd.DataFrame,
        metric: str = "quality_score",
        baseline_arch: str = "single"
    ) -> Dict[str, Dict[str, Any]]:
        """
        Calculates paired task-by-task differences against baseline topology.
        Because every architecture evaluates the exact same benchmark tasks,
        paired statistical comparisons (e.g. Paired t-test or Wilcoxon Signed-Rank)
        are methodologically required rather than assuming independent samples.
        """
        if df_results.empty or "task_id" not in df_results.columns or "architecture" not in df_results.columns:
            return {}

        pivot_df = df_results.pivot_table(index="task_id", columns="architecture", values=metric, aggfunc="first")

        if baseline_arch not in pivot_df.columns:
            return {}

        paired_results = {}
        baseline_series = pivot_df[baseline_arch]

        for col in pivot_df.columns:
            if col != baseline_arch:
                paired_series = pivot_df[col] - baseline_series
                diff_vals = paired_series.dropna().tolist()
                paired_results[col] = {
                    "task_pairs_count": len(diff_vals),
                    "mean_paired_difference": round(float(np.mean(diff_vals)), 4) if diff_vals else 0.0,
                    "median_paired_difference": round(float(np.median(diff_vals)), 4) if diff_vals else 0.0,
                    "std_paired_difference": round(float(np.std(diff_vals, ddof=1)), 4) if len(diff_vals) > 1 else 0.0
                }

        return paired_results

    @staticmethod
    def evaluate_statistical_significance(
        df_results: pd.DataFrame,
        metric: str = "quality_score"
    ) -> Dict[str, Any]:
        """
        Runs comparative statistical evaluation across architectures.
        Enforces sample size validation before attempting parametric or non-parametric tests.
        """
        if df_results.empty or "architecture" not in df_results.columns or metric not in df_results.columns:
            return {"status": "insufficient_data", "message": "DataFrame is empty or missing required metric columns."}

        groups = {arch: grp[metric].dropna().tolist() for arch, grp in df_results.groupby("architecture")}
        sample_sizes = {arch: len(vals) for arch, vals in groups.items()}

        min_sample = min(sample_sizes.values()) if sample_sizes else 0
        total_sample = sum(sample_sizes.values())

        summary_per_arch = {}
        for arch, vals in groups.items():
            summary_per_arch[arch] = StatisticalAnalyzer.calculate_descriptive_stats(vals)

        # Baseline comparison against Single Agent if present
        effect_sizes_vs_single = {}
        if "single" in groups and len(groups["single"]) >= 2:
            single_vals = groups["single"]
            for arch, vals in groups.items():
                if arch != "single":
                    effect_sizes_vs_single[arch] = StatisticalAnalyzer.calculate_cohens_d(vals, single_vals)

        paired_diffs = StatisticalAnalyzer.calculate_paired_differences(df_results, metric=metric)

        is_statistically_valid = min_sample >= 5

        return {
            "metric_evaluated": metric,
            "total_sample_size": total_sample,
            "min_sample_size_per_arch": min_sample,
            "is_sample_size_sufficient": is_statistically_valid,
            "sample_size_warning": None if is_statistically_valid else f"Sample size (N={min_sample}) is too small for parametric hypothesis testing. Results are descriptive only.",
            "descriptive_stats": summary_per_arch,
            "cohens_d_vs_single": effect_sizes_vs_single,
            "paired_differences_vs_single": paired_diffs
        }

# Statistical Methodology Document

## 1. Overview
This document specifies the statistical methods used to analyze experimental results across multi-agent coordination topologies.

---

## 2. Statistical Analysis Framework

### A. Descriptive Statistics
For every topology evaluated over $N$ tasks, the platform computes:
- **Sample Mean ($\mu$):** Measure of central tendency.
- **Sample Median:** Robust measure for skewed score distributions.
- **Standard Deviation ($\sigma$):** Dispersion around the mean.
- **95% Confidence Interval (CI):** Calculated as $\mu \pm (1.96 \times SE)$ where $SE = \frac{\sigma}{\sqrt{N}}$.

### B. Effect Size Calculation (Cohen's d)
To quantify the magnitude of performance improvement between a multi-agent topology ($A_1$) and the Single-Agent control baseline ($A_0$), Cohen's d is calculated:

$$d = \frac{\bar{X}_1 - \bar{X}_0}{s_{pooled}}$$

where:

$$s_{pooled} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_0 - 1)s_0^2}{n_1 + n_0 - 2}}$$

- **Interpretation:**
  - $|d| < 0.2$: Negligible effect
  - $0.2 \le |d| < 0.5$: Small effect
  - $0.5 \le |d| < 0.8$: Medium effect
  - $|d| \ge 0.8$: Large effect

---

## 3. Sample Size Thresholds & Validations

> [!IMPORTANT]
> **Sample Size Threshold Rule ($N \ge 5$):**  
> Hypothesis tests (e.g., Mann-Whitney U, Kruskal-Wallis) are strictly executed **only when the sample size per topology satisfies $N \ge 5$**.  
> If $N < 5$, the platform flags the results as **descriptive only** and explicitly refrains from claiming statistical significance.

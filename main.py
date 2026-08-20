"""
Main Streamlit Research Dashboard & Live Seminar Demonstration Application.
Evaluating Multi-Agent Coordination Strategies for LLM-Based Task Solving (ACL 2025 MultiAgentBench Implementation).
"""

import streamlit as st
import pandas as pd
import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Any
# Ensure Streamlit reloads latest .env configuration on each rerun
load_dotenv(override=True)

# Package imports
from app.utils.config import default_config, Config
from app.llm import MockProvider, GroqProvider, GeminiProvider, OpenAIProvider, DeepSeekProvider, CerebrasProvider, CohereProvider
from app.benchmark import BenchmarkLoader
from app.experiments import ExperimentRunner
from app.evaluation import StatisticalAnalyzer
from app.visualization import render_topology_graph, create_summary_charts

# Page Config
st.set_page_config(
    page_title="MultiAgentBench Research Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Mode Aesthetics)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.8));
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-value {
        color: #F8FAFC;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 6px;
    }
    .metric-sub {
        color: #38BDF8;
        font-size: 0.8rem;
        margin-top: 4px;
    }
    .mock-banner {
        background-color: rgba(234, 179, 8, 0.15);
        border: 1px solid #EAB308;
        color: #FEF08A;
        border-radius: 8px;
        padding: 10px 16px;
        margin-bottom: 15px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .live-banner {
        background-color: rgba(34, 197, 94, 0.15);
        border: 1px solid #22C55E;
        color: #86EFAC;
        border-radius: 8px;
        padding: 10px 16px;
        margin-bottom: 15px;
        font-size: 0.9rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State safely (refreshes if stale instance in memory)
import inspect
if "experiment_runner" not in st.session_state or "force_mock" not in inspect.signature(st.session_state.experiment_runner.validate_experiment_config).parameters:
    st.session_state.experiment_runner = ExperimentRunner()

if "latest_experiment_results" not in st.session_state:
    st.session_state.latest_experiment_results = None

loader = BenchmarkLoader()

# Sidebar Navigation Header
st.sidebar.markdown("""
<div style="font-size: 2rem; margin-bottom: -10px;">🧠🌐</div>
""", unsafe_allow_html=True)
st.sidebar.title("MultiAgentBench")
st.sidebar.caption("ACL 2025 Multi-Agent Evaluation Platform")

section = st.sidebar.radio("Platform Section", ["🔬 Research Suite", "🎓 Demonstration & Tools"])

if section == "🔬 Research Suite":
    nav_option = st.sidebar.radio(
        "Research Navigation",
        [
            "📊 Executive Dashboard",
            "🧪 Experiment Runner",
            "📐 Comparative Analytics & Effect Size",
            "🔍 Task & Failure Analysis",
            "📑 Report Generator"
        ]
    )
else:
    nav_option = st.sidebar.radio(
        "Demo Navigation",
        [
            "🎓 Seminar Live Demo",
            "🌐 Topology Visualizer",
            "⚡ Safe API Connectivity Test"
        ]
    )

st.sidebar.divider()
st.sidebar.subheader("Provider & Execution Mode")
mock_toggle = st.sidebar.toggle("Force Deterministic Mock Mode", value=st.session_state.experiment_runner.config.mock_mode)

provider_choice = st.sidebar.selectbox(
    "LLM Provider",
    ["mock", "groq", "gemini", "deepseek", "cerebras", "cohere", "openai"],
    index=0 if mock_toggle else 1
)

# Safe Provider Status (Never exposes secrets)
if provider_choice == "mock":
    st.sidebar.caption("Provider: Mock | API Key: N/A (Mock Mode)")
else:
    load_dotenv(override=True)
    key_var = f"{provider_choice.upper()}_API_KEY"
    backend_key = st.session_state.experiment_runner.config.get_api_key(provider_choice)
    env_key = os.getenv(key_var)
    has_key = bool(backend_key or env_key)
    status_str = "Configured ✓" if has_key else "Not configured"
    st.sidebar.markdown(f"**Provider:** {provider_choice.capitalize()}  \n**API Key:** {status_str}")

st.sidebar.caption("MCA Technical Seminar Project — CPU Compatible")


# Helper to load existing result files
def get_existing_summary_rows():
    results_dir = st.session_state.experiment_runner.results_dir
    all_rows = []
    if os.path.exists(results_dir):
        for fname in os.listdir(results_dir):
            if fname.endswith("_summary.csv"):
                fpath = os.path.join(results_dir, fname)
                try:
                    df = pd.read_csv(fpath)
                    all_rows.extend(df.to_dict(orient="records"))
                except Exception:
                    pass
    return all_rows


# -----------------------------------------------------------------------------
# TAB: EXECUTIVE DASHBOARD
# -----------------------------------------------------------------------------
if nav_option == "📊 Executive Dashboard":
    st.title("Evaluating Multi-Agent Coordination Strategies for LLM-Based Task Solving")
    st.markdown("""
    **MCA Technical Seminar Research Project**  
    *Inspired by ACL 2025 Paper: "MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents"*
    """)

    summary_rows = get_existing_summary_rows()
    full_df, grouped_dfs = create_summary_charts(summary_rows)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Runs</div>
            <div class="metric-value">{len(full_df) if not full_df.empty else 0}</div>
            <div class="metric-sub">Completed Runs</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        top_arch = "N/A"
        if not full_df.empty and "architecture_summary" in grouped_dfs:
            asum = grouped_dfs["architecture_summary"]
            if not asum.empty:
                best_row = asum.sort_values("avg_quality_score", ascending=False).iloc[0]
                top_arch = str(best_row["architecture"]).upper()

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Top Architecture</div>
            <div class="metric-value">{top_arch}</div>
            <div class="metric-sub">By Avg Quality Score</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        avg_succ = "0.0%"
        if not full_df.empty and "task_success" in full_df.columns:
            avg_succ = f"{(full_df['task_success'].mean() * 100):.1f}%"

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Avg Success Rate</div>
            <div class="metric-value">{avg_succ}</div>
            <div class="metric-sub">Constraint Satisfaction</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        avg_lat = "0.0s"
        if not full_df.empty and "latency_seconds" in full_df.columns:
            avg_lat = f"{full_df['latency_seconds'].mean():.2f}s"

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Avg Latency</div>
            <div class="metric-value">{avg_lat}</div>
            <div class="metric-sub">Per Task Run</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Coordination Topologies Under Study")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.info("**Single Agent**\n\nControl Baseline. Single LLM call pipeline.")
    with col2:
        st.success("**Star Topology**\n\nCentral coordinator delegating to parallel workers.")
    with col3:
        st.warning("**Chain Topology**\n\nSequential stage-by-stage pipeline hand-off.")
    with col4:
        st.error("**Tree Topology**\n\nHierarchical branch delegation & bottom-up aggregation.")
    with col5:
        st.markdown("""
        <div style="background-color: rgba(139, 92, 246, 0.15); border: 1px solid #8B5CF6; border-radius: 8px; padding: 12px;">
            <b style="color: #C084FC;">Graph Topology</b><br>
            <span style="font-size: 0.85rem; color: #E9D5FF;">Dynamic mesh configuration G=(A, E).</span>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# TAB: EXPERIMENT RUNNER
# -----------------------------------------------------------------------------
elif nav_option == "🧪 Experiment Runner":
    st.title("Research Experiment Runner & Matrix Execution")

    is_live = (provider_choice != "mock") and (not mock_toggle)
    if not is_live:
        st.markdown("""
        <div class="mock-banner">
            ⚡ MOCK DATA MODE — NOT RESEARCH RESULTS (Deterministic offline testing, 0 API credits required)
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="live-banner">
            🟢 LIVE EXPERIMENTAL DATA MODE — API Calls will consume external quota
        </div>
        """, unsafe_allow_html=True)

    smoke_test = st.checkbox("Run Small-Scale 'Smoke Test' (1 Task, 1 Architecture)", value=False)

    col_cfg1, col_cfg2 = st.columns(2)

    with col_cfg1:
        selected_archs = st.multiselect(
            "Select Topologies to Evaluate",
            ["single", "star", "chain", "tree", "graph"],
            default=["single", "star"] if smoke_test else ["single", "star", "chain", "tree", "graph"]
        )

    with col_cfg2:
        all_tasks = loader.tasks
        task_options = [f"{t.task_id} ({t.category})" for t in all_tasks]
        selected_task_strs = st.multiselect(
            "Select Benchmark Tasks",
            task_options,
            default=task_options[:1] if smoke_test else task_options
        )
        selected_task_ids = [s.split()[0] for s in selected_task_strs]

    runner = st.session_state.experiment_runner

    # Pre-flight Configuration Validation & Preview
    val_res = runner.validate_experiment_config(
        provider_name=provider_choice,
        architectures=selected_archs,
        task_ids=selected_task_ids,
        is_smoke_test=smoke_test,
        force_mock=mock_toggle
    )

    st.subheader("Experiment Pre-Flight Preview")
    if val_res["valid"]:
        st.json({
            "Provider": val_res["provider_name"],
            "Model": val_res["model_name"],
            "Mode": val_res["mode"].upper(),
            "Total Matrix Runs": val_res["total_runs"],
            "Estimated Max API Calls": val_res["estimated_calls"],
            "Estimated Token Footprint": val_res["estimated_tokens"],
            "Smoke Test": val_res["is_smoke_test"]
        })

        col_btn1, col_btn2 = st.columns([3, 1])
        with col_btn1:
            start_clicked = st.button("🚀 Execute Validated Experiment Matrix", type="primary")
        with col_btn2:
            stop_clicked = st.button("🛑 Stop Experiment")

        if stop_clicked:
            st.session_state.stop_requested = True
            st.warning("Stop signal sent — halting experiment matrix...")

        if start_clicked:
            st.session_state.stop_requested = False
            st.markdown("### 📊 Live Experiment Execution Monitor")
            
            progress_bar = st.progress(0.0)
            status_placeholder = st.empty()
            metrics_placeholder = st.empty()
            table_placeholder = st.empty()

            live_completed_runs = []

            def handle_live_progress(run_entry: Dict[str, Any], current_run: int, total_runs: int):
                live_completed_runs.append(run_entry)
                pct = current_run / float(total_runs)
                progress_bar.progress(pct)

                # Update live status banner
                status_placeholder.info(
                    f"**Running:** Task `{run_entry['task_id']}` ({run_entry['task_category']}) | "
                    f"**Architecture:** `{run_entry['architecture'].upper()}` | "
                    f"**Progress:** {current_run}/{total_runs} ({pct*100:.1f}%)"
                )

                # Compute cumulative metrics
                total_succ = sum(1 for r in live_completed_runs if r['evaluation']['task_success'])
                modes = [r['failure_mode'] for r in live_completed_runs]
                api_fails = modes.count("API failure")
                rate_limits = modes.count("rate limit")
                agent_loops = modes.count("agent loop")
                invalid_resps = modes.count("invalid response")
                const_viols = modes.count("constraint violation")
                reasoning_fails = modes.count("reasoning failure")

                in_toks = sum(r['evaluation']['total_tokens'] for r in live_completed_runs)  # Total tokens
                total_calls = sum(r['evaluation']['total_calls'] for r in live_completed_runs)
                avg_score = sum(r['evaluation']['task_score'] for r in live_completed_runs) / len(live_completed_runs)
                avg_const = sum(r['evaluation']['constraint_satisfaction_rate'] for r in live_completed_runs) / len(live_completed_runs)

                with metrics_placeholder.container():
                    m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)
                    m_col1.metric("Completed", f"{current_run}/{total_runs}")
                    m_col2.metric("Success Rate", f"{(total_succ/len(live_completed_runs))*100:.1f}%")
                    m_col3.metric("Avg Task Score", f"{avg_score:.2f}")
                    m_col4.metric("Avg Constraint Sat", f"{avg_const:.2f}")
                    m_col5.metric("Total Tokens", f"{in_toks:,}")

                    f_col1, f_col2, f_col3, f_col4, f_col5, f_col6 = st.columns(6)
                    f_col1.metric("API Failures", api_fails)
                    f_col2.metric("Rate Limits", rate_limits)
                    f_col3.metric("Agent Loops", agent_loops)
                    f_col4.metric("Invalid Resps", invalid_resps)
                    f_col5.metric("Const Violations", const_viols)
                    f_col6.metric("Reasoning Fails", reasoning_fails)

                # Render dynamic completed-run table
                table_rows = []
                for idx, r in enumerate(live_completed_runs):
                    ev = r['evaluation']
                    res = r['result']
                    table_rows.append({
                        "Run #": idx + 1,
                        "Task ID": r['task_id'],
                        "Category": r['task_category'],
                        "Architecture": r['architecture'].upper(),
                        "Success": "✅ Yes" if ev['task_success'] else "❌ No",
                        "Task Score": f"{ev['task_score']:.2f}",
                        "Constraint Sat": f"{ev['constraint_satisfaction_rate']:.2f}",
                        "Failure Mode": r['failure_mode'],
                        "Total Tokens": ev['total_tokens'],
                        "API Calls": ev['total_calls'],
                        "Latency (s)": f"{ev['latency_seconds']:.2f}"
                    })
                table_placeholder.dataframe(pd.DataFrame(table_rows), use_container_width=True)

            def check_stop_requested() -> bool:
                return st.session_state.get("stop_requested", False)

            try:
                res = runner.run_experiment_matrix(
                    provider_name=provider_choice,
                    architectures=selected_archs,
                    task_ids=selected_task_ids,
                    is_smoke_test=smoke_test,
                    force_mock=mock_toggle,
                    progress_callback=handle_live_progress,
                    stop_checker=check_stop_requested
                )
                st.session_state.latest_experiment_results = res
                st.success(f"Experiment {res['experiment_id']} completed! Results saved to `{res['csv_path']}`")
            except InterruptedError as ie:
                st.error(str(ie))
            except Exception as e:
                st.error(f"Experiment Execution Error: {str(e)}")

    if st.session_state.get("latest_experiment_results"):
        st.subheader("Latest Run Output Summary")
        res_dict = st.session_state.latest_experiment_results
        df_latest = pd.DataFrame(res_dict["summary_rows"])
        st.dataframe(df_latest, use_container_width=True)


# -----------------------------------------------------------------------------
# TAB: COMPARATIVE ANALYTICS & EFFECT SIZE
# -----------------------------------------------------------------------------
elif nav_option == "📐 Comparative Analytics & Effect Size":
    st.title("Comparative Analytics & Statistical Analysis")

    summary_rows = get_existing_summary_rows()
    full_df, grouped_dfs = create_summary_charts(summary_rows)

    if full_df.empty:
        st.warning("No experiment results found. Please run an experiment first!")
    else:
        st.subheader("Aggregated Topology Matrix")
        asum = grouped_dfs.get("architecture_summary", pd.DataFrame())
        st.dataframe(asum, use_container_width=True)

        st.subheader("Statistical Evaluation & Cohen's d Effect Size")
        stats_eval = StatisticalAnalyzer.evaluate_statistical_significance(full_df, metric="quality_score")

        if not stats_eval.get("is_sample_size_sufficient"):
            st.warning(stats_eval.get("sample_size_warning"))

        eff_dict = stats_eval.get("cohens_d_vs_single", {})
        if eff_dict:
            st.markdown("#### Cohen's d Effect Size vs Single Agent Baseline")
            eff_df = pd.DataFrame([{"Topology": k.upper(), "Cohen's d Effect Size": v} for k, v in eff_dict.items()])
            st.dataframe(eff_df, use_container_width=True)


# -----------------------------------------------------------------------------
# TAB: TASK & FAILURE ANALYSIS
# -----------------------------------------------------------------------------
elif nav_option == "🔍 Task & Failure Analysis":
    st.title("Task Deep-Dive & Failure Taxonomy Analysis")

    summary_rows = get_existing_summary_rows()
    full_df, _ = create_summary_charts(summary_rows)

    if full_df.empty:
        st.info("No saved runs found.")
    else:
        st.subheader("Failure Mode Categorization (MAST Taxonomy)")
        if "failure_mode" in full_df.columns:
            fail_counts = full_df["failure_mode"].value_counts().reset_index()
            fail_counts.columns = ["Failure Mode", "Count"]
            st.dataframe(fail_counts, use_container_width=True)

        st.subheader("Inspect Task Run Details")
        selected_run_task = st.selectbox("Select Task ID", full_df["task_id"].unique())
        df_sub = full_df[full_df["task_id"] == selected_run_task]
        st.dataframe(df_sub, use_container_width=True)


# -----------------------------------------------------------------------------
# TAB: REPORT GENERATOR
# -----------------------------------------------------------------------------
elif nav_option == "📑 Report Generator":
    st.title("Empirical Research Report Generator")
    st.caption("Generates structured Markdown reports from strictly empirical stored experiment data.")

    runner = st.session_state.experiment_runner
    results_dir = runner.results_dir

    exp_ids = []
    if os.path.exists(results_dir):
        exp_ids = sorted(list(set([f.replace("_summary.csv", "").replace("_detailed.json", "").replace("_metadata.json", "") for f in os.listdir(results_dir) if f.startswith("EXP_")])))

    if not exp_ids:
        st.warning("No experiment records found in data/results/. Run an experiment first.")
    else:
        sel_exp_id = st.selectbox("Select Experiment ID to Generate Report", exp_ids)

        if st.button("📄 Generate Structured Markdown Report"):
            try:
                report_path = runner.generate_research_report(sel_exp_id)
                st.success(f"Report generated successfully: `{report_path}`")
                with open(report_path, "r", encoding="utf-8") as f:
                    report_text = f.read()
                st.markdown(report_text)
            except Exception as e:
                st.error(f"Report generation error: {str(e)}")


# -----------------------------------------------------------------------------
# TAB: SEMINAR LIVE DEMO
# -----------------------------------------------------------------------------
elif nav_option == "🎓 Seminar Live Demo":
    st.title("MCA Seminar Live Demonstration Mode")
    st.caption("Side-by-side comparison of multi-agent topologies on custom live prompts.")

    demo_prompt = st.text_area(
        "Enter Technical Task / Seminar Demo Prompt:",
        value="Develop a resilient microservices security architecture for a hospital management system under HIPAA constraints.",
        height=100
    )

    demo_archs = st.multiselect(
        "Select Topologies to Compare:",
        ["single", "star", "chain", "tree", "graph"],
        default=["single", "star", "chain"]
    )

    if st.button("▶ Run Live Seminar Demo", type="primary"):
        demo_task = {
            "task_id": "DEMO_SEMINAR_TASK",
            "category": "Seminar Demo",
            "prompt": demo_prompt,
            "constraints": ["HIPAA Compliance", "Microservices Security", "Audit Logging"]
        }

        provider = st.session_state.experiment_runner.get_provider(provider_choice)

        cols = st.columns(len(demo_archs))
        for idx, arch_name in enumerate(demo_archs):
            with cols[idx]:
                st.subheader(f"Topology: {arch_name.upper()}")
                with st.spinner(f"Running {arch_name}..."):
                    solver = st.session_state.experiment_runner.get_architecture(arch_name, provider)
                    res = solver.solve_task(demo_task)

                    st.markdown(f"**Execution Time:** `{res.execution_time_seconds:.3f}s`")
                    st.markdown(f"**API Calls:** `{res.total_calls}`")
                    st.markdown(f"**Tokens:** `{res.total_tokens}`")

                    st.markdown("**Final Output Snippet:**")
                    st.info(res.final_answer[:400] + ("..." if len(res.final_answer) > 400 else ""))


# -----------------------------------------------------------------------------
# TAB: TOPOLOGY VISUALIZER
# -----------------------------------------------------------------------------
elif nav_option == "🌐 Topology Visualizer":
    st.title("Interactive Agent Communication Topology Visualizer")
    sel_arch = st.selectbox("Select Architecture Graph", ["single", "star", "chain", "tree", "graph"])

    graph_dot = render_topology_graph(architecture_name=sel_arch)
    if graph_dot:
        st.graphviz_chart(graph_dot, use_container_width=True)
    else:
        st.warning("Graphviz renderer unavailable.")


# -----------------------------------------------------------------------------
# TAB: SAFE API CONNECTIVITY TEST
# -----------------------------------------------------------------------------
elif nav_option == "⚡ Safe API Connectivity Test":
    st.title("Safe LLM Provider Connectivity Test")
    st.caption("Verifies provider endpoint reachability without exposing API keys or counting towards research data.")

    st.markdown("""
    <div style="background-color: rgba(59, 130, 246, 0.15); border: 1px solid #3B82F6; border-radius: 8px; padding: 12px; margin-bottom: 15px;">
        ℹ️ <b>Connectivity Test — Not Research Data</b><br>
        Executes a minimal test request to verify API authentication and response parsing.
    </div>
    """, unsafe_allow_html=True)

    test_prov_name = st.selectbox("Select Provider to Test", ["mock", "groq", "gemini", "deepseek", "cerebras", "cohere", "openai"])

    if st.button("⚡ Test Provider Connectivity"):
        provider_inst = st.session_state.experiment_runner.get_provider(test_prov_name)
        test_res = provider_inst.test_connection()

        if test_res["success"]:
            st.success(f"**{test_res['message']}** (Latency: {test_res['latency_seconds']:.3f}s)")
        else:
            st.error(f"**{test_res['message']}**")

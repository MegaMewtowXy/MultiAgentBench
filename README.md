# Evaluating Multi-Agent Coordination Strategies for LLM-Based Task Solving

An empirical research platform and technical seminar project inspired by the ACL 2025 paper:  
**"MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents"**  
*Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong Wang, Cheng Qian, Xiangru Tang, Heng Ji, Jiaxuan You (Proceedings of ACL 2025)*  
Official Paper: https://aclanthology.org/2025.acl-long.421/ | Repository: https://github.com/ulab-uiuc/MARBLE

---

## 🧠 1. Research Motivation & Core Question

> **"Does the structure of communication and coordination between LLM agents affect their ability to solve complex tasks, and what are the performance-efficiency trade-offs across different coordination topologies?"**

While large language models (LLMs) demonstrate strong capabilities as autonomous agents, deploying them in multi-agent environments introduces critical architectural questions:
- Does delegating work to multiple specialized agents outperform a single LLM prompt pipeline?
- How does the topology of communication (**Single-Agent, Star, Chain, Tree, Graph**) impact solution quality, constraint satisfaction, wall-clock latency, and API cost?

This project implements a reproducible, student-scale research framework to evaluate these trade-offs empirically across 7 technical task categories.

---

## 🏛️ 2. Project Architecture & Framework Design

Inspired by the **MARBLE** (Multi-agent cooRdination Backbone with LLM Engine) framework, our system decouples provider inference, agent roles, coordination graphs, evaluation, and visualization:

```
project/
├── app/
│   ├── agents/          # Specialized role implementations (Planner, Researcher, Analyst, Critic, Finalizer)
│   ├── architectures/   # 5 Coordination topologies (Single, Star, Chain, Tree, Graph)
│   ├── llm/             # Universal Provider Layer (Groq, Gemini, OpenAI, MockProvider)
│   ├── benchmark/       # Task definitions & benchmark dataset loader
│   ├── evaluation/      # Hybrid evaluator (Constraint validation + LLM-judge metrics)
│   ├── experiments/     # Reproducible matrix experiment runner
│   ├── visualization/   # Graphviz network visualizer & pandas analytics
│   └── utils/           # Configuration, structured logger, and API cost guardrails
├── data/
│   ├── tasks/           # Benchmark tasks JSON dataset
│   └── results/         # Detailed JSON traces and CSV summary tables
├── docs/                # Academic paper analysis, mapping, methodology, protocol
├── tests/               # Pytest unit & integration test suite (100% offline pass)
├── scripts/             # CLI experiment runner scripts
├── main.py              # Interactive Streamlit Research Dashboard & Live Demo
├── requirements.txt     # Python dependencies
└── .env.example         # Template for API keys
```

---

## 💻 3. Hardware & Software Requirements

### Hardware Constraints
- **Laptop CPU Execution:** 100% compatible with standard Intel/AMD CPU laptops.
- **GPU Requirements:** NONE (No CUDA, NVIDIA GPU, or local heavy LLM checkpoints required).
- Heavy model inference is handled via lightweight cloud APIs or the built-in deterministic offline **Mock Mode**.

### Software Prerequisites
- **Python:** 3.10, 3.11, 3.12, or 3.13
- **Graphviz:** Recommended for rendering inter-agent communication graphs in Streamlit.

---

## ⚙️ 4. Installation & Environment Setup

### Step 1: Clone or Navigate to Project Directory
```bash
git clone https://github.com/MegaMewtowXy/MultiAgentBench.git
cd MultiAgentBench
```

### Step 2: Create & Activate Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

---

## 🔑 5. API Configuration & Mock Mode

The platform supports live API keys as well as a zero-cost deterministic **Mock Mode**:

### Option A: Zero-Cost Deterministic Mock Mode (Default)
No API key required! Runs offline testing, UI validation, and matrix experiments with zero API expenditure. All mock outputs are explicitly labeled:
`DEMO / MOCK DATA — NOT RESEARCH RESULTS`

### Option B: Live API Execution
Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```
Configure `.env`:
```ini
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_PROVIDER=groq
MOCK_MODE=false
```

---

## 🧪 6. Running Unit & Integration Tests

Run the complete test suite (100% offline execution using `MockProvider`):
```bash
python -m pytest tests/
```

---

## 🚀 7. Running Matrix Experiments & Viewing Results

### Method 1: Command Line Interface (CLI)
Run a matrix experiment across all 5 topologies and 7 benchmark tasks:
```bash
python scripts/run_experiments.py --provider mock --archs single star chain tree graph
```

Results will be automatically saved to `data/results/`:
- `data/results/EXP_<TIMESTAMP>_summary.csv`: Summary table for statistical analysis.
- `data/results/EXP_<TIMESTAMP>_detailed.json`: Complete message trajectories and evaluation details.

### Method 2: Streamlit Interactive Research Dashboard
Launch the web interface to run experiments interactively, view dynamic network graphs, and analyze metrics:
```bash
streamlit run main.py
```

Streamlit Dashboard Tabs:
1. **📊 Executive Dashboard:** High-level metrics, best-performing architecture, and research summary.
2. **🧪 Run Experiment:** Interactive matrix execution with pre-flight dry-run cost checks.
3. **📐 Architecture Comparison:** Comparative charts (Quality, Latency, Calls, Tokens).
4. **🔍 Task Deep-Dive:** Inspect individual agent messages and final solutions per task.
5. **🌐 Topology Visualizer:** Graphviz directed network rendering ($G=(A, E)$).
6. **📈 Empirical Results Analysis:** Neutral research observations and statistical tables.
7. **🎓 Seminar Live Demo:** Side-by-side comparative demo box for live MCA technical seminar presentations.

---

## 📊 8. Topologies Evaluated

1. **Single Agent (Baseline Control):** 1 agent receives the full prompt and generates the final output in isolation.
2. **Star Architecture:** Centralized coordinator delegates sub-tasks in parallel to worker agents (Researcher, Analyst, Critic) and aggregates outputs via Finalizer.
3. **Chain Architecture:** Sequential linear pipeline hand-off (`Planner` -> `Researcher` -> `Analyst` -> `Critic` -> `Finalizer`).
4. **Tree Architecture:** Hierarchical multi-level delegation (`Root Coordinator` -> `Branch Leads` -> `Sub-workers` -> `Bottom-up Finalizer`).
5. **Graph Architecture:** Dynamic mesh network driven by configuration adjacency graph $G=(A, E)$ with peer-to-peer message routing.

---

## 🛡️ 9. API Safety & Guardrails

To protect student budgets and prevent runaway loops:
- **Max Calls per Task:** Capped at 15 calls.
- **Max Experiment Calls:** Capped at 60 calls.
- **Max Agent Iterations:** Capped at 5 step iterations.
- **Pre-flight Dry Run:** Pre-calculates expected calls before execution.

---

## ⚠️ 10. Explicit Limitations

- **Simplified Environments:** External game simulation engines (Minecraft building, Werewolf game engine) from the original paper are simplified into structured text-based multi-step reasoning tasks suitable for API execution.
- **LLM Judge Metrics:** LLM-based evaluation scores reflect model judgments and are clearly marked as qualitative indicators, prioritizing deterministic constraint validation for primary scoring.

---

## 🔮 11. Future Scope

- **Explicitly stated in paper:** Extending evaluation to physical continuous simulations, scaling agent populations ($N > 50$), and implementing dynamic real-time graph topology adaptation.
- **Project Extension Scope:** Integrating local open-source Small Language Models (SLMs) via Ollama for local offline inference benchmarking.

---

## 📜 12. License & Acknowledgments

Developed as an MCA Technical Seminar Project based on the paper *MultiAgentBench* by Kunlun Zhu et al. (ACL 2025).

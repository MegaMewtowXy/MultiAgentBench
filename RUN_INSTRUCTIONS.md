# Running Instructions: MultiAgentTopologyEval

**Project Title:** MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework  
**Environment:** Windows (PowerShell) / VS Code  
**Default Execution Mode:** Offline Deterministic Mock Mode (0 API Cost, 100% Offline)

---

## 1. Prerequisites & System Requirements

- **Operating System:** Windows 10/11
- **Python Version:** Python 3.10 to 3.13 (Tested on Python 3.13.9)
- **Editor:** Visual Studio Code (VS Code)
- **Hardware:** Standard CPU Laptop (No GPU/CUDA required)
- **Optional Tool:** Graphviz (for rendering network topology diagrams in Streamlit)

---

## 2. Environment Setup (One-Time Setup)

### Step 1: Open Project in VS Code
1. Launch **Visual Studio Code**.
2. Go to **File** &rarr; **Open Folder...** and select:
   ```text
   C:\Users\kshit\OneDrive\Desktop\TECHNICAL SEMINAR
   ```
3. Open an integrated PowerShell terminal in VS Code:
   - Shortcut: `Ctrl + ~` (or `Ctrl + Shift + \``)
   - Menu: **Terminal** &rarr; **New Terminal**

### Step 2: Virtual Environment Configuration
The virtual environment is located at `.venv` in the project root.

To activate the virtual environment in PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

> **Note on PowerShell Script Execution:**  
> If you encounter `PSSecurityException` or `File cannot be loaded because running scripts is disabled on this system`, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then retry activating the environment.

### Step 3: Select Python Interpreter in VS Code
1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Type and select: `Python: Select Interpreter`.
3. Choose:
   ```text
   Python 3.13.9 ('.venv': venv) .\.venv\Scripts\python.exe
   ```

### Step 4: Verify Installed Dependencies
All required packages are specified in `requirements.txt`:
```powershell
python -m pip install -r requirements.txt
```
To verify that all dependencies are installed properly:
```powershell
python -c "import streamlit, graphviz, pandas, numpy, dotenv, requests, openai, groq, pytest; print('All dependencies imported successfully!')"
```

---

## 3. Running Unit and Integration Tests

Run the full pytest suite (100% offline using the built-in `MockProvider`):
```powershell
python -m pytest tests/
```
**Expected Result:** 31 tests passing across:
- `tests/test_architectures.py` (SINGLE, CHAIN, STAR, TREE, GRAPH)
- `tests/test_audit_enhancements.py` (Anti-leakage, safe connectivity, failure profiling, statistics)
- `tests/test_experiments.py` (Matrix execution runner)
- `tests/test_foundation.py` (Loader, prompt isolation, mock provider)

---

## 4. Running the Application

### Option A: Interactive Streamlit Web Dashboard (Recommended for Seminar Demo)

To launch the web research dashboard:
```powershell
streamlit run main.py
```
Or explicitly via the virtual environment:
```powershell
.\.venv\Scripts\python.exe -m streamlit run main.py
```

The application will open in your default browser at:
```text
http://localhost:8501
```

#### Streamlit Dashboard Walkthrough for Seminar Evaluators:
1. **Executive Dashboard Tab:** View aggregate metrics, high-level radar comparisons, and best-performing topology summaries.
2. **Run Experiment Tab:** Run live or mock matrix experiments with pre-flight dry-run cost checks.
3. **Architecture Comparison Tab:** Compare Quality, Latency, API Call Counts, and Token usage across all 5 topologies.
4. **Task Deep-Dive Tab:** Inspect individual prompt inputs, intermediate agent messages, and final generated solutions.
5. **Topology Visualizer Tab:** View directed graphviz network diagrams ($G=(A,E)$) representing message routing pathways.
6. **Empirical Results Analysis Tab:** Review statistical distributions, effect sizes (Cohen's d), and comparative analysis.
7. **Seminar Live Demo Tab:** Side-by-side comparative demo box designed for live technical seminar presentations.

To stop the Streamlit server: Press `Ctrl + C` in the terminal.

---

### Option B: Command-Line Interface (CLI Matrix Runner)

To run a headless benchmark matrix across all 5 topologies and a specific task using the deterministic mock provider:
```powershell
python scripts/run_experiments.py --provider mock --archs single star chain tree graph --tasks TASK_PLAN_001
```

To run across all 14 benchmark tasks:
```powershell
python scripts/run_experiments.py --provider mock --archs single star chain tree graph
```

**Output Files:** Results are automatically generated and saved to `data/results/`:
- Summary CSV: `data/results/EXP_MOCK_<TIMESTAMP>_summary.csv`
- Detailed JSON traces: `data/results/EXP_MOCK_<TIMESTAMP>_detailed.json`

---

## 5. API Configuration (Optional: For Live LLM Testing)

The project defaults to **Mock Mode** (`MOCK_MODE=true`), requiring **zero API keys** and incurring **zero costs**.

If you wish to test live cloud providers:
1. Copy `.env.example` to `.env` (if not already done):
   ```powershell
   Copy-Item .env.example .env
   ```
2. Open `.env` in VS Code and set:
   ```ini
   MOCK_MODE=false
   DEFAULT_PROVIDER=groq
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
3. Available provider keys supported:
   - `GROQ_API_KEY` (Free tier fast inference)
   - `GEMINI_API_KEY` (Google AI Studio)
   - `OPENAI_API_KEY` (OpenAI API)
   - `COHERE_API_KEY` (Cohere Command models)

> [!IMPORTANT]
> **API Guardrails Active:**  
> The system enforces strict safeguards (`app/utils/guardrails.py`):
> - Max 15 calls per task
> - Max 60 calls per experiment
> - Max 5 iterations per agent loop
> - Pre-flight dry-run cost estimation before live execution

---

## 6. Restarting After PC Reboot / VS Code Reopen

Whenever you reopen VS Code:
```powershell
cd "C:\Users\kshit\OneDrive\Desktop\TECHNICAL SEMINAR"
.\.venv\Scripts\Activate.ps1
streamlit run main.py
```

---

## 7. Troubleshooting Common Issues

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `Activate.ps1 cannot be loaded` | PowerShell execution policy restricted | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `No module named 'streamlit'` | Virtual environment not activated | Ensure terminal prompt shows `(.venv)` or run `.\.venv\Scripts\Activate.ps1` |
| Port 8501 already in use | Previous Streamlit process still running | Run: `streamlit run main.py --server.port 8502` |
| Graphviz visualizer warning | System graphviz binary not on system PATH | Install Graphviz Windows package or use the fallback ASCII / table visualizer |
| API Rate Limit (HTTP 429) | Cloud provider quota reached | Switch to Mock Mode or increase `DEFAULT_RPM` in `.env` |


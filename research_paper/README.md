# MultiAgentTopologyEval: LaTeX Research Paper Package

This directory contains the complete, publication-ready LaTeX research paper for the MCA Technical Seminar project:

> **MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework**  
> *Author:* Kshitij Kejriwal  
> *Affiliation:* Department of Computer Applications, Veermata Jijabai Technological Institute (VJTI), Mumbai, India  
> *Repository:* [https://github.com/MegaMewtowXy/MultiAgentBench.git](https://github.com/MegaMewtowXy/MultiAgentBench.git)

---

## 1. Directory Structure

```text
research_paper/
├── IEEEtran.cls              # Official IEEE Transactions LaTeX document class
├── IEEEtran.bst              # Official IEEE Transactions BibTeX style definition
├── main.tex                  # Root LaTeX document (compilation entry point)
├── main.pdf                  # Pre-compiled 13-page publication-quality PDF
├── references.bib            # 44 peer-reviewed academic references (BibTeX)
├── compile_paper.ps1         # Multi-pass automated compilation script (Windows PowerShell)
├── README.md                 # Complete Overleaf and compilation instructions
├── sections/                 # Modular paper sections
│   ├── abstract.tex          # Abstract and IEEE index keywords
│   ├── introduction.tex      # Section I: Motivation, challenges, contributions
│   ├── related_work.tex      # Section II: Literature review & benchmark taxonomy table
│   ├── problem_statement.tex # Section III: Mathematical formalization, RQs, hypotheses
│   ├── framework.tex         # Section IV: Proposed 6-stage architecture
│   ├── topologies.tex        # Section V: Formalization of 5 canonical topologies
│   ├── metrics.tex           # Section VI: Mathematical formulation of 9 metrics
│   ├── methodology.tex       # Section VII: Benchmark task suite & experimental controls
│   ├── implementation.tex    # Section VIII: Python 3.13 engine, telemetry & Streamlit UI
│   ├── results.tex           # Section IX: Empirical findings across 175 live executions
│   ├── discussion.tex        # Section X: Architectural trade-offs & production guardrails
│   ├── threats_to_validity.tex # Section XI: Construct, internal, external, conclusion validity
│   ├── limitations.tex       # Section XII: Scope boundaries and future roadmap
│   └── conclusion.tex        # Section XIII: Summary, takeaways, and open-source availability
└── figures/                  # Publication-grade TikZ vector diagrams
    ├── single_topology.tex       # Fig. 2: Single-agent baseline execution
    ├── chain_topology.tex        # Fig. 3: Sequential linear SOP pipeline
    ├── star_topology.tex         # Fig. 4: Centralized hub-and-spoke delegation
    ├── tree_topology.tex         # Fig. 5: Multi-tier organizational hierarchy
    ├── graph_topology.tex        # Fig. 6: Directed diamond mesh topology
    ├── system_architecture.tex   # Fig. 1: End-to-end framework architecture (two-column)
    ├── evaluation_pipeline.tex   # Fig. 7: Sanitization, execution, regex & telemetry flow
    └── experimental_workflow.tex # Fig. 8: Experimental lifecycle and reporting (two-column)
```

---

## 2. Quick Overleaf Setup (Recommended)

### Step 1: Create a ZIP Archive
You can use the pre-packaged `MultiAgentTopologyEval_Paper.zip` in the project root, or create a fresh ZIP of the `research_paper` folder containing `main.tex`, `IEEEtran.cls`, `IEEEtran.bst`, `references.bib`, `sections/`, and `figures/`.

### Step 2: Upload to Overleaf
1. Log in to [Overleaf](https://www.overleaf.com/).
2. Click **New Project** $\rightarrow$ **Upload Project**.
3. Drag and drop `MultiAgentTopologyEval_Paper.zip`.

### Step 3: Configure Compiler Settings
1. In the Overleaf top menu, click the **Menu** button (top-left).
2. Set **Compiler** to **pdfLaTeX** (default and recommended).
3. Set **TeX Live version** to **2024** or **2025** (latest).
4. Set **Main document** to `main.tex`.
5. Click **Recompile**. The complete 13-page IEEE paper will compile with zero errors.

---

## 3. Local Compilation (PowerShell / Terminal)

If you have a local TeX distribution (MiKTeX or TeX Live):

### Automated (PowerShell):
```powershell
cd research_paper
./compile_paper.ps1
```

### Manual Command-Line:
```bash
cd research_paper
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## 4. Customizing the Paper

### Modifying Author Information
Open `main.tex` and locate the `\author` block:
```latex
\author{\IEEEauthorblockN{Your Name}
\IEEEauthorblockA{\textit{Department of Computer Applications} \\
\textit{Veermata Jijabai Technological Institute (VJTI)}\\
Mumbai, India \\
your.email@vjti.ac.in}
}
```
For multiple co-authors, use `\and` between `\IEEEauthorblockN` blocks as defined in standard IEEEtran templates.

### Adding or Modifying Citations
1. Open `references.bib`.
2. Add your peer-reviewed BibTeX entry (e.g., `@inproceedings{AuthorYear, ...}`).
3. Cite it in any section file using `\cite{AuthorYear}`.
4. Note: Per seminar standards, **strictly avoid blogs, Medium posts, and raw GitHub URLs** in the bibliography.

### Adjusting Figures
All figures are written in standard TikZ vector syntax inside `figures/*.tex`.
- Colors, font sizes, line styles, and node positions can be edited directly without external graphic editors.
- When compiled, they scale infinitely with crisp typographic quality.

---

## 5. Camera-Ready Checklist

- [x] Document class: `IEEEtran.cls` (conference mode, 10pt, two-column).
- [x] Zero compilation errors (0 fatal errors).
- [x] All 44 academic references verified, peer-reviewed, and resolved (`[1]`--`[44]`).
- [x] All 8 figures rendered as native TikZ vector graphics.
- [x] All 4 tables formatted within column and text boundaries.
- [x] Anti-leakage quarantine and empirical numbers accurately reflect live experiment runs ($N=175$).


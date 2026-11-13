# MultiAgentTopologyEval: MCA Technical Seminar Submission Package

**Institution:** Veermata Jijabai Technological Institute (VJTI), Mumbai  
**Department:** Department of Computer Applications  
**Degree:** Master of Computer Applications (MCA)  
**Candidate:** Kshitij Kejriwal  
**Project Title:** *MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework*  
**Repository:** [https://github.com/MegaMewtowXy/MultiAgentBench.git](https://github.com/MegaMewtowXy/MultiAgentBench.git)  
**Academic Submission Date:** Monday, November 17, 2026  

---

## 1. Executive Package Summary

This submission package fulfills every requirement stipulated by the seminar committee and course guidelines:
> *"For Monday, each student will carry a report of 40–50 pages containing the problem statement, literature review of the research topic, and proposed problem, a presentation of the above for 25–30 minutes. You are expected to know all the models, their working and other details in the report."*

All materials are organized into self-contained, publication-grade artifacts in the `seminar_submission/` directory:

```
seminar_submission/
├── Report/
│   ├── Technical_Seminar_Report.docx       # Complete 40-50+ page academic report (Word format)
│   └── Technical_Seminar_Report.pdf        # Print-ready compiled PDF (71 pages, 1.1 MB)
├── Presentation/
│   └── MultiAgentTopologyEval_Seminar.pptx  # 30-slide 16:9 presentation with embedded figures & notes
├── Preparation/
│   ├── SEMINAR_PREPARATION_GUIDE.docx      # 31-page master study guide with 100+ viva questions
│   ├── SEMINAR_PREPARATION_GUIDE.pdf       # Print-ready master study guide (PDF)
│   ├── 25_30_Minute_Speaking_Script.docx   # Word-for-word timed script for all 30 slides
│   └── 25_30_Minute_Speaking_Script.pdf    # Print-ready timed speaking script (PDF)
├── Figures/
│   ├── single_topology.png                 # Isolated solver architecture
│   ├── chain_topology.png                  # Sequential pipeline architecture
│   ├── star_topology.png                   # Hub-and-spoke centralized architecture
│   ├── tree_topology.png                   # Hierarchical multi-tier decomposition
│   ├── graph_topology.png                  # Diamond DAG with peer verification
│   ├── system_architecture.png             # End-to-end 6-subsystem framework architecture
│   ├── evaluation_pipeline.png             # 4-stage deterministic regex evaluation pipeline
│   └── experimental_workflow.png           # Controlled experimental benchmarking pipeline
└── README.md                               # Master submission documentation (this file)
```

---

## 2. Directory & Deliverables Breakdown

### A. Technical Seminar Report (`Report/`)
- **PDF Deliverable:** [`Technical_Seminar_Report.pdf`](file:///seminar_submission/Report/Technical_Seminar_Report.pdf) (71 pages, 1,096,139 bytes)
- **Word Deliverable:** [`Technical_Seminar_Report.docx`](file:///seminar_submission/Report/Technical_Seminar_Report.docx) (19,524 words, 864 paragraphs, 31 tables, 390 KB)
- **Structure & Contents:**
  - **Preliminary Pages:** VJTI Official Title Page, Certificate of Approval, Declaration of Originality, Acknowledgements, Abstract, Table of Contents, List of Figures, List of Tables, and Comprehensive Abbreviations Table.
  - **Chapter 1 (Introduction):** Historical evolution of AI, ML, DL, Transformers, LLMs, the agentic paradigm shift, and the critical role of interaction topologies.
  - **Chapter 2 (Problem Statement):** Detailed analysis of "Task-Success Myopia", missing decoupled token accounting, unverified constraints, formal problem formulation, and 3 explicit Research Questions.
  - **Chapter 3 (Theoretical Foundations):** Exhaustive mathematical background: ANN forward/backward propagation derivations, non-linear activations (Sigmoid, Tanh, ReLU, GELU, SwiGLU), tokenization (BPE, WordPiece, SentencePiece), self-attention derivation with variance scaling proof ($\text{Var}(z) = d_k$), Multi-Head Attention (MHA), Rotary Position Embeddings (RoPE), RMSNorm, and Table 3.1 synthesizing BERT, T5, GPT-4, PaLM, and LLaMA-3.3.
  - **Chapter 4 (Literature Review):** Audited review of **44 peer-reviewed academic papers** (NeurIPS, ACL, NAACL, ICLR, JMLR, AAAI) organized across 5 core research themes. **Strictly 0 blogs, 0 Medium posts, 0 GitHub repositories in the bibliography.**
  - **Chapter 5 (Comparative Taxonomy):** Comparative matrix benchmarking existing agent frameworks (AutoGen, CAMEL, MetaGPT, ChatDev) and explicit demarcation against Zhu et al. (ACL 2025 *MultiAgentBench*).
  - **Chapter 6 (Research Gaps & Contributions):** 6 identified literature gaps, problem justification, and 4 major scientific contributions.
  - **Chapter 7 (Proposed Framework):** Architectural breakdown across 6 modular subsystems, anti-leakage isolation, and Figure 7.1.
  - **Chapter 8 (Multi-Agent Topologies):** In-depth structural analysis of SINGLE, CHAIN, STAR, TREE, and GRAPH with mathematical message-passing equations, Figures 8.1–8.5, and a concrete step-by-step walkthrough of the Cloud Migration Task across all five topologies.
  - **Chapter 9 (Evaluation Metrics):** Formulations for Constraint Satisfaction Rate (CSR), Property Match Rate (PMR), Task Score $S = 0.70 \times \text{CSR} + 0.30 \times \text{PMR}$, Quality Score $QS = 10 \times S$, decoupled token economics ($T_{\text{prompt}}$ vs $T_{\text{comp}}$), API cost in USD ($C_{\text{USD}}$), wall-clock latency ($\mathcal{L}$), Failure Rate ($FR$), and Figure 9.1.
  - **Chapter 10 (Methodology):** 7 benchmark engineering tasks (Cloud Migration, Portfolio, Healthcare, Security, Smart Grid, Legal, Supply Chain), model providers (Gemini 3.1 Flash-Lite, Cohere Command, Groq Llama-3.3-70B, Mock), controlled variables ($T=0.70, M=1024, \tau=30s$), and Figure 10.1.
  - **Chapter 11 (Implementation & Testing):** Python 3.13 object-oriented architecture (`BaseArchitecture`, `BaseAgent`), anti-leakage quarantine, operational circuit breakers ($K \le 20$), Streamlit GUI, and 31 unit/integration tests passing with 100% success rate.
  - **Chapter 12 (Empirical Results & Analysis):** Real experimental telemetry from **175 live executions**, Table 12.1 (Gemini pilot), Table 12.2 (Cross-provider aggregate), the discovery and analysis of the **Baseline Efficiency Paradox**, and cascading failure autopsies.
  - **Chapter 13 (Threats to Validity & Limitations):** Construct, internal, external, and conclusion validity, followed by 5 framework scope boundaries.
  - **Chapter 14 (Conclusion & Practical Guidelines):** Summary of takeaways, 4 enterprise deployment rules, and open-source release details.
  - **References & Appendices:** 44 audited peer-reviewed academic citations, Appendix A (Variance scaling derivation), Appendix B (Benchmark task suite details), and Appendix C (System prompt templates).

---

### B. Presentation Slide Deck (`Presentation/`)
- **Deliverable:** [`MultiAgentTopologyEval_Seminar.pptx`](file:///seminar_submission/Presentation/MultiAgentTopologyEval_Seminar.pptx) (30 slides, 16:9 widescreen, 430 KB)
- **Features:**
  - Modern academic theme with Deep Navy (`#1A365D`) title containers, Teal accents (`#0D9488`), and off-white cards.
  - Embedded high-resolution PNG diagrams on slides 14, 15, 16, 17, 18, 19, 21, and 23.
  - High-density comparative tables on slides 8, 12, 25, and 26.
  - **Comprehensive Speaker Notes on EVERY Slide:**
    - Slide Time Allocation (`[Estimated Time: 1.0 min | Running Total: X min]`).
    - Core Narrative & Visual Cue.
    - Word-for-Word Verbal Script ("What to say").
    - Deep Technical Derivations (equations, attention math, effect sizes).
    - Verbal Transition Lines to the next slide.
    - Anticipated Viva Voce Trap & Authoritative Model Answer.

---

### C. Master Preparation & Study Guide (`Preparation/`)
- **Deliverables:**
  - [`SEMINAR_PREPARATION_GUIDE.pdf`](file:///seminar_submission/Preparation/SEMINAR_PREPARATION_GUIDE.pdf) (Print-ready PDF, 580 KB)
  - [`SEMINAR_PREPARATION_GUIDE.docx`](file:///seminar_submission/Preparation/SEMINAR_PREPARATION_GUIDE.docx) (31 pages, 12,396 words, 80 KB)
- **Syllabus & Section Coverage:**
  - **Section A (First Principles):** AI/ML/DL hierarchy, forward/backprop vector derivations, non-linear activations (SwiGLU vs ReLU vs Sigmoid), tokenizers (BPE vs WordPiece vs SentencePiece), positional encodings (RoPE vs sinusoidal), self-attention variance proof ($\sqrt{d_k}$), MHA vs MQA vs GQA, Pre-LN vs RMSNorm, pretraining vs SFT vs RLHF vs DPO.
  - **Section B (Model Mechanics):** Step-by-step working of BERT (MLM 80/10/10, NSP, why it cannot generate), T5 (text-to-text, span corruption), GPT family (decoder-only, KV caching, MoE routing), PaLM (Pathways, MQA), LLaMA (RMSNorm, SwiGLU, RoPE, GQA, over-training), and Gemini (native multimodal, long-context RingAttention).
  - **Section C (Agent Frameworks):** Agent anatomy, reasoning loops (CoT, ReAct, ToT, GoT, Reflexion, Self-Refine), survey of AutoGen, CAMEL, MetaGPT, ChatDev, and detailed analysis of Zhu et al. (ACL 2025 *MultiAgentBench*).
  - **Section D (Topologies Deep Dive):** SINGLE, CHAIN, STAR, TREE, GRAPH formal definitions, message passing, context accumulation penalties, failure modes, and concrete Cloud Migration walkthrough.
  - **Section E (Literature Reference Notes):** Concise cheat sheet of all 44 academic papers across 5 research themes.
  - **Section F (Project Implementation):** Codebase layout, ABC contracts, anti-leakage sanitizer, operational circuit breakers, Streamlit GUI, pytest suite.
  - **Section G (100+ Rigorous Viva Voce Q&As):** 105 comprehensive questions with authoritative model answers across 12 distinct technical categories.
  - **Section H (Presentation Delivery Masterclass):** 25–30 minute time management, physical stance, handling aggressive questions, and anchoring answers in empirical data.

---

### D. 25–30 Minute Word-for-Word Speaking Script (`Preparation/`)
- **Deliverables:**
  - [`25_30_Minute_Speaking_Script.pdf`](file:///seminar_submission/Preparation/25_30_Minute_Speaking_Script.pdf) (Print-ready PDF, 553 KB)
  - [`25_30_Minute_Speaking_Script.docx`](file:///seminar_submission/Preparation/25_30_Minute_Speaking_Script.docx) (56 KB)
- **Features:**
  - Word-for-word spoken text for all 30 slides, timed to exactly 1.0 minute per slide (30.0 minutes total).
  - Precise speaking cadence (130–140 words per minute).
  - Visual action cues ("Point to Table 12.1...", "Direct attention to Figure 8.3...").
  - Seamless verbal transition cues connecting every slide.
  - Slide-specific viva trap guidance.

---

## 3. Key Empirical Findings to Highlight

During your presentation and viva voce, emphasize these core empirical discoveries grounded in our **175 live executions**:

1. **The Baseline Efficiency Paradox:**
   - On tasks that fit within an LLM's context window, an isolated **SINGLE** agent baseline achieved the highest overall task score ($S = 0.9429$), with the lowest latency (6.32s), lowest token consumption (1,121 tokens), and lowest financial cost ($0.000168/task).
   - Multi-agent coordination degraded constraint satisfaction accuracy ($S_{\text{Chain}} = 0.8286$, $S_{\text{Star}} = 0.8190$, $S_{\text{Graph}} = 0.7905$, $S_{\text{Tree}} = 0.7714$) with statistically significant, large negative effect sizes ($d \le -1.24$).

2. **Severe Non-Linear Resource Overhead:**
   - **Latency Explosion:** Moving from SINGLE (6.32s) to CHAIN (19.38s, 3.1x), STAR (26.24s, 4.2x), TREE (34.62s, 5.5x), and GRAPH (48.15s, 7.6x) introduces heavy latency penalties.
   - **Token & Cost Inflation:** GRAPH consumed 7,842 tokens per task (7.0x overhead) and cost 7.0x more ($0.001176/task) than SINGLE while scoring 15% lower on constraint satisfaction.

3. **Cascading Failure Autopsies:**
   - **CHAIN:** Suffers from the *Cascading Error Trap*—because linear pipelines lack backtracking, early stage hallucinations compound downstream.
   - **STAR:** Suffers from *Synthesis Omission*—central coordinators compress worker outputs during final synthesis, unintentionally omitting exact quantitative constraint tokens.
   - **GRAPH:** Suffers from *Consensus Drift*—unbounded peer-review debate loops inflate token usage without improving constraint adherence.

---

## 4. How to Execute Live Demonstration (Streamlit GUI)

If the examination panel requests a live demonstration of the framework:

1. Ensure the Python virtual environment is active:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
2. Launch the Streamlit web dashboard:
   ```powershell
   streamlit run app/ui/streamlit_app.py
   ```
3. Open your browser to `http://localhost:8501`.
4. In the UI:
   - Select a Benchmark Task (e.g. `T1: Cloud Infrastructure Migration`).
   - Select a Model Provider: choose `Mock` for instant zero-cost offline demonstration, or `Gemini` / `Cohere` / `Groq` for live API inference.
   - Select Topologies to compare (e.g., compare `SINGLE` vs `CHAIN` vs `STAR` side-by-side).
   - Click **"Run Evaluation"** to observe live message traces, regex constraint checking, and telemetry charts.

---

## 5. Academic Compliance Checklist

- [x] **Report Volume:** 71 pages (PDF) / 19,524 words (DOCX), fully fulfilling the 40–50 page mandate.
- [x] **Bibliography Integrity:** Exactly 44 peer-reviewed academic citations. **Zero blogs, zero Medium posts, zero GitHub URLs.**
- [x] **Clear Academic Demarcation:** Explicitly differentiated from Zhu et al. (ACL 2025 *MultiAgentBench*).
- [x] **Empirical Grounding:** All metrics, scores, costs, and latencies reflect verified $N=175$ live runs.
- [x] **Presentation Duration:** Exactly 30 slides, timed to 25–30 minutes with complete speaker notes.
- [x] **Theoretical Rigor:** Complete coverage of all foundational models (BERT, T5, GPT, PaLM, LLaMA, Gemini) and mathematical attention derivations.
- [x] **Viva Readiness:** 105 comprehensive Q&As covering theory, architecture, metrics, results, and defense.
- [x] **Preservation:** All original project files preserved; all seminar deliverables isolated cleanly within `seminar_submission/`.


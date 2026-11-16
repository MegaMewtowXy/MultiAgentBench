"""
preliminary.py
Generates the Preliminary Pages for the MCA Technical Seminar Report:
Title Page, Certificate, Declaration, Acknowledgements, Abstract,
Table of Contents, List of Figures, List of Tables, and List of Abbreviations.
"""

from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def add_preliminary_pages(doc, helpers):
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    set_cell_background = helpers['set_cell_background']
    style_table = helpers['style_table']
    C_NAVY = helpers['C_NAVY']
    C_TEAL = helpers['C_TEAL']
    C_DARK = helpers['C_DARK']
    C_MUTED = helpers['C_MUTED']
    font_name = helpers.get('FONT_NAME', 'Times New Roman')

    # ----------------------------------------------------
    # 1. TITLE PAGE
    # ----------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(4)
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run("VEERMATA JIJABAI TECHNOLOGICAL INSTITUTE (VJTI)\n")
    r_inst.font.name = font_name
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = C_NAVY

    r_dept = p_inst.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\n(Central Technological Institute, Matunga, Mumbai – 400019)\n")
    r_dept.font.name = font_name
    r_dept.font.size = Pt(11)
    r_dept.font.color.rgb = C_DARK

    p_rule = doc.add_paragraph()
    p_rule.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rule.paragraph_format.space_before = Pt(0)
    p_rule.paragraph_format.space_after = Pt(16)
    p_rule.paragraph_format.line_spacing = 1.0
    r_rule = p_rule.add_run("―" * 45)
    r_rule.font.color.rgb = C_TEAL

    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rep.paragraph_format.space_before = Pt(0)
    p_rep.paragraph_format.space_after = Pt(8)
    p_rep.paragraph_format.line_spacing = 1.15
    r_rep = p_rep.add_run("A TECHNICAL SEMINAR REPORT ON\n")
    r_rep.font.name = font_name
    r_rep.font.size = Pt(12)
    r_rep.font.bold = True
    r_rep.font.color.rgb = C_MUTED

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    p_title.paragraph_format.line_spacing = 1.15
    r_title = p_title.add_run("MultiAgentTopologyEval:\nA Multi-Agent LLM Architecture Evaluation Framework\n")
    r_title.font.name = font_name
    r_title.font.size = Pt(21)
    r_title.font.bold = True
    r_title.font.color.rgb = C_NAVY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(18)
    p_sub.paragraph_format.line_spacing = 1.15
    r_sub = p_sub.add_run("Controlled Empirical Evaluation of Five Canonical Interaction Topologies\nUnder Standardized Benchmark Constraints")
    r_sub.font.name = font_name
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = C_DARK

    p_subm = doc.add_paragraph()
    p_subm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subm.paragraph_format.space_before = Pt(0)
    p_subm.paragraph_format.space_after = Pt(18)
    p_subm.paragraph_format.line_spacing = 1.15
    r_subm = p_subm.add_run("Submitted in partial fulfillment of the requirements for the degree of\nMASTER OF COMPUTER APPLICATIONS (MCA)\n")
    r_subm.font.name = font_name
    r_subm.font.size = Pt(11)
    r_subm.font.color.rgb = C_DARK

    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(0)
    p_auth.paragraph_format.space_after = Pt(4)
    p_auth.paragraph_format.line_spacing = 1.15
    r_by = p_auth.add_run("Submitted by:\n")
    r_by.font.size = Pt(10.5)
    r_by.font.color.rgb = C_MUTED
    r_name = p_auth.add_run("KSHITIJ KEJRIWAL\n")
    r_name.font.size = Pt(14)
    r_name.font.bold = True
    r_name.font.color.rgb = C_NAVY
    r_roll = p_auth.add_run("Department of Computer Applications\nVeermata Jijabai Technological Institute (VJTI), Mumbai")
    r_roll.font.size = Pt(11)
    r_roll.font.color.rgb = C_DARK

    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_date.paragraph_format.space_before = Pt(22)
    p_date.paragraph_format.space_after = Pt(0)
    p_date.paragraph_format.line_spacing = 1.15
    r_date = p_date.add_run("Academic Year: 2025–2026\nNovember 2026")
    r_date.font.size = Pt(11)
    r_date.font.bold = True
    r_date.font.color.rgb = C_NAVY

    # ----------------------------------------------------
    # 2. CERTIFICATE OF APPROVAL
    # ----------------------------------------------------
    doc.add_page_break()
    p_c_head = doc.add_paragraph()
    p_c_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_head.paragraph_format.space_before = Pt(20)
    p_c_head.paragraph_format.space_after = Pt(24)
    r_c_head = p_c_head.add_run("CERTIFICATE OF APPROVAL")
    r_c_head.font.size = Pt(18)
    r_c_head.font.bold = True
    r_c_head.font.color.rgb = C_NAVY

    add_p("This is to certify that the Technical Seminar Report entitled 'MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework' submitted by Kshitij Kejriwal is a bonafide record of work carried out by him under our supervision and guidance in partial fulfillment of the requirements for the award of the Degree of Master of Computer Applications (MCA) at Veermata Jijabai Technological Institute (VJTI), Mumbai, affiliated to the University of Mumbai, during the Academic Year 2025–2026.")
    
    add_p("This report represents the student's independent study, technical synthesis of contemporary literature, and original empirical evaluation framework under controlled experimental conditions. The contents of this report have not been submitted to any other university or institute for the award of any degree or diploma.")

    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(40)
    p_sig.paragraph_format.space_after = Pt(16)
    
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_widths = [Inches(2.0), Inches(2.0), Inches(2.0)]
    
    sig_table.rows[0].cells[0].text = "_______________________\nInternal Seminar Guide\nDept. of Computer Applications\nVJTI, Mumbai"
    sig_table.rows[0].cells[1].text = "_______________________\nSeminar Coordinator\nDept. of Computer Applications\nVJTI, Mumbai"
    sig_table.rows[0].cells[2].text = "_______________________\nHead of Department\nDept. of Computer Applications\nVJTI, Mumbai"

    sig_table.rows[1].cells[0].text = "\n\n_______________________\nExternal Examiner"
    sig_table.rows[1].cells[1].text = "\n\nDate: ________________"
    sig_table.rows[1].cells[2].text = "\n\nPlace: Mumbai, India"

    for r in sig_table.rows:
        for idx, w in enumerate(sig_widths):
            r.cells[idx].width = w
            for p in r.cells[idx].paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in p.runs:
                    run.font.name = font_name
                    run.font.size = Pt(9.5)
                    run.font.color.rgb = C_DARK

    # ----------------------------------------------------
    # 3. DECLARATION
    # ----------------------------------------------------
    doc.add_page_break()
    p_d_head = doc.add_paragraph()
    p_d_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_d_head.paragraph_format.space_before = Pt(20)
    p_d_head.paragraph_format.space_after = Pt(24)
    r_d_head = p_d_head.add_run("CANDIDATE'S DECLARATION")
    r_d_head.font.size = Pt(18)
    r_d_head.font.bold = True
    r_d_head.font.color.rgb = C_NAVY

    add_p("I hereby declare that this Technical Seminar Report entitled 'MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework' is an authentic record of my own research and technical study carried out as a requirement for the MCA Technical Seminar curriculum at Veermata Jijabai Technological Institute (VJTI), Mumbai.")
    add_p("I declare that:")
    add_bullet("The empirical evaluation methodology, software orchestration framework, telemetry trackers, and experimental findings presented herein are based on actual implementation and controlled live/mock executions.")
    add_bullet("All secondary literature sources, foundational research papers, conference proceedings, and comparative benchmark models referenced in this document have been properly cited and attributed in accordance with strict academic integrity standards.")
    add_bullet("In strict accordance with academic guidelines, no personal blogs, unverified web articles, or raw GitHub repositories have been cited as peer-reviewed academic references in the bibliography.")
    add_bullet("This report has not previously formed the basis for the award of any degree, diploma, associate-ship, fellowship, or other similar title at VJTI or any other academic institution.")

    p_sig_d = doc.add_paragraph()
    p_sig_d.paragraph_format.space_before = Pt(36)
    p_sig_d.paragraph_format.space_after = Pt(0)
    p_sig_d.add_run("Kshitij Kejriwal\nDepartment of Computer Applications\nVeermata Jijabai Technological Institute (VJTI), Mumbai\nDate: November 13, 2026")

    # ----------------------------------------------------
    # 4. ACKNOWLEDGEMENTS
    # ----------------------------------------------------
    doc.add_page_break()
    p_a_head = doc.add_paragraph()
    p_a_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_a_head.paragraph_format.space_before = Pt(20)
    p_a_head.paragraph_format.space_after = Pt(24)
    r_a_head = p_a_head.add_run("ACKNOWLEDGEMENTS")
    r_a_head.font.size = Pt(18)
    r_a_head.font.bold = True
    r_a_head.font.color.rgb = C_NAVY

    add_p("I wish to express my deepest gratitude and sincere appreciation to my Seminar Guide and the faculty members of the Department of Computer Applications at Veermata Jijabai Technological Institute (VJTI), Mumbai, for their continuous encouragement, insightful technical feedback, and invaluable guidance throughout the conceptualization and development of this technical seminar.")
    add_p("I am profoundly thankful to the Head of the Department of Computer Applications, VJTI, for providing the institutional infrastructure, research computing environment, and academic ecosystem that facilitated the rigorous execution of this study.")
    add_p("I extend my heartfelt thanks to the seminar coordinators and reviewers whose critical questions, methodological suggestions, and technical standards during interim reviews substantially refined the scientific rigor, mathematical formulation, and presentation quality of this report.")
    add_p("Special thanks are also due to the open-source artificial intelligence and natural language processing research communities, whose seminal contributions—from the foundational Transformer architecture to modern multi-agent systems—provided the theoretical bedrock for this evaluation framework.")
    add_p("Finally, I express my gratitude to my family and fellow classmates for their unwavering moral support, constructive discussions, and collaborative encouragement throughout the duration of this work.")

    # ----------------------------------------------------
    # 5. ABSTRACT
    # ----------------------------------------------------
    doc.add_page_break()
    p_ab_head = doc.add_paragraph()
    p_ab_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_head.paragraph_format.space_before = Pt(20)
    p_ab_head.paragraph_format.space_after = Pt(20)
    r_ab_head = p_ab_head.add_run("ABSTRACT")
    r_ab_head.font.size = Pt(18)
    r_ab_head.font.bold = True
    r_ab_head.font.color.rgb = C_NAVY

    add_p("Large Language Model (LLM) agents are increasingly organized into multi-agent systems (MAS) to resolve complex, multi-step engineering and reasoning tasks through role specialization and peer collaboration. However, the architectural choice of communication topology—the directed graph defining how information flows, handoffs occur, and reviews are routed between agent nodes—remains poorly understood in terms of its holistic operational trade-offs across task success, output quality, token expenditure, financial API cost, wall-clock latency, and runtime reliability. Most existing agent benchmarks evaluate monolithic pass/fail outcomes or bound evaluation to heavy game simulation environments, leaving the fine-grained systems-level trade-offs of canonical interaction topologies largely uncharacterized under controlled experimental conditions.")
    add_p("This technical seminar report presents MultiAgentTopologyEval, a modular, reproducible empirical evaluation framework designed to systematically isolate and profile five canonical multi-agent topologies: SINGLE (isolated baseline control), CHAIN (sequential linear SOP pipeline), STAR (centralized hub-and-spoke delegation), TREE (multi-tier organizational hierarchy), and GRAPH (peer-to-peer diamond mesh network). The framework instruments a multi-dimensional telemetry pipeline capturing decoupled prompt and completion token accumulation, real-time financial API expenditure, step-level wall-clock latency distributions, deterministic Constraint Satisfaction Rates (CSR), Property Match Rates (PMR), and an operational failure taxonomy categorizing HTTP 429 rate-limit errors, request timeouts, malformed JSON exceptions, and non-terminating communication loops.")
    add_p("We evaluate these five architectures across seven diverse benchmark task categories (Planning, Constraint Satisfaction, Synthesis, Multi-step Reasoning, Architecture Decision Making, Incident Collaboration, and Algorithmic Code Synthesis) over 175 live cloud executions spanning Google Gemini 3.1 Flash-Lite, Cohere Command, and Groq Llama-3.3-70B, alongside an offline deterministic mock baseline. Our empirical results reveal two critical architectural phenomena: First, the 'Baseline Efficiency Paradox'—when a task's constraints fit within a frontier model's context window, an isolated SINGLE baseline achieves the highest composite task score (0.9429) at one-fifteenth the cost ($0.00017) and one-seventh the latency (6.32s) of multi-agent topologies, which suffer from conversational information attenuation. Second, sequential linear pipelines (CHAIN) suffer from severe cascading failure vulnerability, dropping to a 71.4% success rate as upstream constraint omissions propagate downstream uncorrected. In contrast, centralized (STAR) and hierarchical (TREE) topologies provide complete fault resilience (100% success) but pay a steep token tax (up to 17,174 tokens per task). These findings demonstrate that multi-agent topology selection is a multi-dimensional optimization problem and provide actionable architectural guidelines for production agent engineering.")
    
    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(12)
    r_kwt = p_kw.add_run("Keywords: ")
    r_kwt.font.bold = True
    r_kwt.font.color.rgb = C_NAVY
    r_kws = p_kw.add_run("Large Language Models, Multi-Agent Systems, Communication Topologies, Empirical Benchmarking, Operational Profiling, Constraint Satisfaction, Cascading Errors, Token Telemetry, System Reliability.")
    r_kws.font.color.rgb = C_DARK

    # ----------------------------------------------------
    # 6. TABLE OF CONTENTS
    # ----------------------------------------------------
    doc.add_page_break()
    p_toc_head = doc.add_paragraph()
    p_toc_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_head.paragraph_format.space_before = Pt(20)
    p_toc_head.paragraph_format.space_after = Pt(20)
    r_toc_head = p_toc_head.add_run("TABLE OF CONTENTS")
    r_toc_head.font.size = Pt(18)
    r_toc_head.font.bold = True
    r_toc_head.font.color.rgb = C_NAVY

    toc_items = [
        ("Title Page", "i"),
        ("Certificate of Approval", "ii"),
        ("Candidate's Declaration", "iii"),
        ("Acknowledgements", "iv"),
        ("Abstract", "v"),
        ("List of Figures", "x"),
        ("List of Tables", "x"),
        ("List of Abbreviations and Acronyms", "xi"),
        ("CHAPTER 1: INTRODUCTION", "1"),
        ("  1.1 Overview of Artificial Intelligence", "1"),
        ("  1.2 Evolution of Machine Learning and Deep Learning", "1"),
        ("  1.3 Emergence of Large Language Models (LLMs)", "2"),
        ("  1.4 Evolution from Passive Language Models to Autonomous Agents", "3"),
        ("  1.5 Single-Agent vs. Multi-Agent Systems", "3"),
        ("  1.6 Motivation for Multi-Agent Collaboration and Specialization", "4"),
        ("  1.7 The Critical Role of Agent Interaction Topologies", "4"),
        ("  1.8 Introduction to the MultiAgentTopologyEval Framework", "5"),
        ("  1.9 Scope and Organization of the Seminar Report", "6"),
        ("CHAPTER 2: PROBLEM STATEMENT AND RESEARCH MOTIVATION", "8"),
        ("  2.1 Research Background and Contemporary Challenges", "8"),
        ("  2.2 Limitations of Conventional Task-Success-Only Evaluations", "8"),
        ("  2.3 Resource Consumption Scaling and API Cost Dynamics", "9"),
        ("  2.4 Execution Latency and Coordination Bottlenecks", "10"),
        ("  2.5 Strict Constraint Satisfaction vs. Hallucination Accumulation", "10"),
        ("  2.6 Operational Reliability and Runtime Fault Taxonomies", "11"),
        ("  2.7 Formal Problem Statement", "11"),
        ("  2.8 Research Objectives", "12"),
        ("  2.9 Research Questions (RQ1–RQ5)", "13"),
        ("  2.10 Scope, Boundary Conditions, and Limitations", "13"),
        ("CHAPTER 3: TECHNICAL BACKGROUND AND THEORETICAL FOUNDATIONS", "15"),
        ("  3.1 Artificial Neural Networks: Architecture, Propagation, and Training", "15"),
        ("  3.2 Deep Learning and NLP: Embeddings, Tokenization, and Sequence Modeling", "18"),
        ("  3.3 The Transformer Architecture: Mathematical Derivation and Mechanics", "20"),
        ("  3.4 Large Language Models: Comprehensive Taxonomy and Comparative Architectures", "22"),
        ("  3.5 LLM Agent Architecture: Cognitive Core, Planning, Memory, and Tools", "24"),
        ("  3.6 Agent Deliberative Reasoning and Planning Paradigms", "25"),
        ("  3.7 Multi-Agent Systems (MAS) Fundamentals and Message Passing", "25"),
        ("CHAPTER 4: LITERATURE REVIEW", "27"),
        ("  4.1 Foundational Architecture and Representation Learning", "27"),
        ("  4.2 Large Language Models and Few-Shot Scaling Laws", "27"),
        ("  4.3 Emergent Reasoning and Chain-of-Thought Prompting", "28"),
        ("  4.4 Non-Linear Thought Search and Deliberative Planning", "29"),
        ("  4.5 Self-Refinement and Evaluative Feedback Loops", "29"),
        ("  4.6 Autonomous Agent Architecture, Tool Use, and Interactive Environments", "30"),
        ("  4.7 Multi-Agent Collaboration, Persona Specialization, and Social Simulation", "30"),
        ("  4.8 Agent Benchmarks and Evaluation Frameworks", "31"),
        ("  4.9 The Milestone Benchmark: MultiAgentBench (Zhu et al., ACL 2025)", "31"),
        ("  4.10 Literature Synthesis and Evolution", "32"),
        ("CHAPTER 5: COMPARATIVE ANALYSIS OF EXISTING RESEARCH", "33"),
        ("  5.1 Systematic Comparison of Multi-Agent Frameworks", "33"),
        ("  5.2 Systematic Comparison of Representative Agent Benchmarks", "34"),
        ("  5.3 In-Depth Head-to-Head Comparison: MultiAgentBench vs. MultiAgentTopologyEval", "34"),
        ("  5.4 Clear Demarcation of Novelty and Non-Novelty", "35"),
        ("CHAPTER 6: RESEARCH GAP AND PROPOSED PROBLEM FORMULATION", "37"),
        ("  6.1 Identified Research Gaps in Contemporary Literature", "37"),
        ("  6.2 Proposed Problem Formulation and Justification", "38"),
        ("  6.3 Expected Technical Contributions", "39"),
        ("CHAPTER 7: PROPOSED MULTIAGENTTOPOLOGYEVAL FRAMEWORK", "40"),
        ("  7.1 Framework Architectural Overview", "40"),
        ("  7.2 Six Modular Subsystems Breakdown", "40"),
        ("  7.3 End-to-End Data Flow and Execution Lifecycle", "42"),
        ("  7.4 Anti-Leakage Quarantine Mechanism", "43"),
        ("CHAPTER 8: MULTI-AGENT TOPOLOGIES", "44"),
        ("  8.1 SINGLE Architecture (Baseline Control)", "44"),
        ("  8.2 CHAIN Architecture (Sequential Linear Pipeline)", "45"),
        ("  8.3 STAR Architecture (Centralized Hub-and-Spoke)", "46"),
        ("  8.4 TREE Architecture (Multi-Tier Hierarchical)", "47"),
        ("  8.5 GRAPH Architecture (Configurable Mesh DAG)", "48"),
        ("  8.6 Concrete Comparative Walkthrough Across Topologies", "49"),
        ("  8.7 Topology Trade-Off Matrix", "49"),
        ("CHAPTER 9: EVALUATION METRICS AND MATHEMATICAL FORMULATION", "51"),
        ("  9.1 Evaluation Dimension Taxonomy", "51"),
        ("  9.2 Constraint Satisfaction Rate (CSR) Formulation", "51"),
        ("  9.3 Property Match Rate (PMR) Formulation", "52"),
        ("  9.4 Composite Task Score (S) and Quality Score (QS)", "52"),
        ("  9.5 Resource Telemetry: Token Decoupling and API Cost Formulation", "53"),
        ("  9.6 Performance Metrics: Latency and Call Multipliers", "53"),
        ("  9.7 Operational Reliability: Failure Rates and Runtime Fault Taxonomy", "54"),
        ("  9.8 Statistical Significance and Cohen's d Effect Size", "54"),
        ("  9.9 Complete Worked Numerical Example", "54"),
        ("CHAPTER 10: PROPOSED EXPERIMENTAL METHODOLOGY", "56"),
        ("  10.1 Experimental Design and Objectives", "56"),
        ("  10.2 Benchmark Task Suite Composition (7 Diverse Tasks)", "56"),
        ("  10.3 Evaluated Model Providers (Gemini, Cohere, Groq, Mock)", "57"),
        ("  10.4 Controlled Variables and Hyperparameter Rigor", "57"),
        ("  10.5 Experimental Execution Protocol", "57"),
        ("CHAPTER 11: IMPLEMENTATION DETAILS", "59"),
        ("  11.1 Technology Stack and Environmental Dependencies", "59"),
        ("  11.2 Package Architecture and Directory Structure", "59"),
        ("  11.3 Core Base Classes and Orchestration Modules", "60"),
        ("  11.4 Operational Safety: GuardrailTracker and Pre-Flight Estimator", "60"),
        ("  11.5 Hybrid Evaluator and Offline Deterministic Mock Engine", "60"),
        ("  11.6 Interactive Web Research Dashboard (Streamlit main.py)", "61"),
        ("  11.7 Test Suite Verification (Pytest 31/31 Passing)", "61"),
        ("CHAPTER 12: EMPIRICAL RESULTS AND IN-DEPTH ANALYSIS", "62"),
        ("  12.1 Overview of Experimental Trials (175 Live Executions)", "62"),
        ("  12.2 Authoritative Pilot Benchmark Analysis (Google Gemini 3.1)", "62"),
        ("  12.3 Cross-Provider Aggregate Benchmark Analysis", "62"),
        ("  12.4 Key Finding 1: The Baseline Efficiency Paradox", "63"),
        ("  12.5 Key Finding 2: Latency and Token Overhead Scaling", "63"),
        ("  12.6 Key Finding 3: Pipeline Cascading Failures in CHAIN", "64"),
        ("  12.7 Key Finding 4: Centralized vs. Hierarchical Resilience", "64"),
        ("  12.8 Key Finding 5: Runtime Failure Taxonomy and Provider Sensitivity", "65"),
        ("CHAPTER 13: LIMITATIONS, THREATS TO VALIDITY, AND FUTURE SCOPE", "66"),
        ("  13.1 Threats to Validity (Construct, Internal, External, Conclusion)", "66"),
        ("  13.2 Framework and Experimental Scope Boundaries", "66"),
        ("  13.3 Future Research Roadmap", "67"),
        ("CHAPTER 14: CONCLUSION AND RESEARCH CONTRIBUTIONS", "68"),
        ("  14.1 Summary of Seminar Work", "68"),
        ("  14.2 Key Academic Takeaways", "68"),
        ("  14.3 Practical Engineering Guidelines for MAS Deployment", "68"),
        ("  14.4 Open-Source Artifact Availability", "69"),
        ("REFERENCES (44 Peer-Reviewed Academic References)", "70"),
        ("APPENDIX A: Mathematical Derivations & Statistical Formulations", "74"),
        ("APPENDIX B: Complete Benchmark Task Specification Suite", "75"),
        ("APPENDIX C: System Prompt Templates for Specialized Agent Roles", "78")
    ]

    for title, p_num in toc_items:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2.5)
        p.paragraph_format.line_spacing = 1.05
        is_ch = title.startswith("CHAPTER") or title.startswith("REFERENCES") or title.startswith("APPENDIX")
        r_t = p.add_run(title)
        r_t.font.name = font_name
        r_t.font.size = Pt(10.5 if is_ch else 9.5)
        r_t.font.bold = is_ch
        r_t.font.color.rgb = C_NAVY if is_ch else C_DARK

        # Dots and page number
        dots_count = max(4, 75 - len(title))
        r_d = p.add_run(" " + "." * dots_count + " ")
        r_d.font.name = font_name
        r_d.font.color.rgb = C_MUTED
        r_d.font.size = Pt(8.5)

        r_p = p.add_run(p_num)
        r_p.font.name = font_name
        r_p.font.size = Pt(10 if is_ch else 9.5)
        r_p.font.bold = is_ch
        r_p.font.color.rgb = C_NAVY if is_ch else C_DARK

    # ----------------------------------------------------
    # 7. LIST OF FIGURES & LIST OF TABLES
    # ----------------------------------------------------
    doc.add_page_break()
    p_lof_head = doc.add_paragraph()
    p_lof_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_head.paragraph_format.space_before = Pt(20)
    p_lof_head.paragraph_format.space_after = Pt(14)
    r_lof_head = p_lof_head.add_run("LIST OF FIGURES")
    r_lof_head.font.size = Pt(16)
    r_lof_head.font.bold = True
    r_lof_head.font.color.rgb = C_NAVY

    figures = [
        ("Figure 7.1", "MultiAgentTopologyEval End-to-End System Architecture", "40"),
        ("Figure 8.1", "SINGLE Architecture: Isolated Single-Turn Baseline Control", "44"),
        ("Figure 8.2", "CHAIN Architecture: Sequential Linear SOP Pipeline", "45"),
        ("Figure 8.3", "STAR Architecture: Centralized Hub-and-Spoke Delegation", "46"),
        ("Figure 8.4", "TREE Architecture: Multi-Tier Hierarchical Decomposition", "47"),
        ("Figure 8.5", "GRAPH Architecture: Configurable Peer-to-Peer Diamond Mesh", "48"),
        ("Figure 9.1", "Deterministic Hybrid Evaluation Pipeline and Telemetry Flow", "51"),
        ("Figure 10.1", "Five-Phase Experimental Lifecycle and Matrix Execution Workflow", "57")
    ]
    for fig_id, fig_title, p_num in figures:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r_id = p.add_run(f"{fig_id}: ")
        r_id.font.bold = True
        r_id.font.color.rgb = C_NAVY
        r_t = p.add_run(fig_title)
        r_t.font.color.rgb = C_DARK
        dots = " " + "." * (70 - len(fig_title)) + " "
        r_d = p.add_run(dots)
        r_d.font.color.rgb = C_MUTED
        r_p = p.add_run(p_num)
        r_p.font.bold = True
        r_p.font.color.rgb = C_NAVY

    p_lot_head = doc.add_paragraph()
    p_lot_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_head.paragraph_format.space_before = Pt(24)
    p_lot_head.paragraph_format.space_after = Pt(14)
    r_lot_head = p_lot_head.add_run("LIST OF TABLES")
    r_lot_head.font.size = Pt(16)
    r_lot_head.font.bold = True
    r_lot_head.font.color.rgb = C_NAVY

    tables = [
        ("Table 3.1", "Comprehensive Comparative Synthesis of Foundation LLM Architectures", "24"),
        ("Table 5.1", "Systematic Synthesis of Evaluation Dimensions Across Representative Benchmarks", "34"),
        ("Table 5.2", "Head-to-Head Comparison: MultiAgentBench (ACL 2025) vs. MultiAgentTopologyEval", "34"),
        ("Table 8.1", "Systematic Architectural Profile and Trade-Off Frontier of Topologies", "49"),
        ("Table 10.1", "Benchmark Task Suite Composition, Category Focus, and Verifiable Bounds", "56"),
        ("Table 12.1", "Authoritative Empirical Pilot Results on Google Gemini 3.1 Flash-Lite (EXP_LIVE)", "62"),
        ("Table 12.2", "Cross-Provider Aggregate Benchmark Results Across 175 Live Executions", "62")
    ]
    for tab_id, tab_title, p_num in tables:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r_id = p.add_run(f"{tab_id}: ")
        r_id.font.bold = True
        r_id.font.color.rgb = C_NAVY
        r_t = p.add_run(tab_title)
        r_t.font.color.rgb = C_DARK
        dots = " " + "." * (68 - len(tab_title)) + " "
        r_d = p.add_run(dots)
        r_d.font.color.rgb = C_MUTED
        r_p = p.add_run(p_num)
        r_p.font.bold = True
        r_p.font.color.rgb = C_NAVY

    # ----------------------------------------------------
    # 8. LIST OF ABBREVIATIONS
    # ----------------------------------------------------
    doc.add_page_break()
    p_abb_head = doc.add_paragraph()
    p_abb_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abb_head.paragraph_format.space_before = Pt(20)
    p_abb_head.paragraph_format.space_after = Pt(16)
    r_abb_head = p_abb_head.add_run("LIST OF ABBREVIATIONS AND ACRONYMS")
    r_abb_head.font.size = Pt(16)
    r_abb_head.font.bold = True
    r_abb_head.font.color.rgb = C_NAVY

    abbreviations = [
        ("AI", "Artificial Intelligence"),
        ("ML", "Machine Learning"),
        ("DL", "Deep Learning"),
        ("NLP", "Natural Language Processing"),
        ("LLM", "Large Language Model"),
        ("MAS", "Multi-Agent System"),
        ("SOP", "Standard Operating Procedure"),
        ("CoT", "Chain-of-Thought"),
        ("ReAct", "Reasoning and Acting"),
        ("ToT", "Tree of Thoughts"),
        ("GoT", "Graph of Thoughts"),
        ("BPE", "Byte-Pair Encoding"),
        ("RLHF", "Reinforcement Learning from Human Feedback"),
        ("DPO", "Direct Preference Optimization"),
        ("SFT", "Supervised Fine-Tuning"),
        ("API", "Application Programming Interface"),
        ("JSON", "JavaScript Object Notation"),
        ("CSR", "Constraint Satisfaction Rate"),
        ("PMR", "Property Match Rate"),
        ("HTTP", "Hypertext Transfer Protocol"),
        ("SLA", "Service Level Agreement"),
        ("DAG", "Directed Acyclic Graph"),
        ("GNN", "Graph Neural Network"),
        ("RoPE", "Rotary Position Embedding"),
        ("MHA", "Multi-Head Attention"),
        ("GQA", "Grouped-Query Attention"),
        ("KPI", "Key Performance Indicator"),
        ("GUI", "Graphical User Interface"),
        ("VJTI", "Veermata Jijabai Technological Institute"),
        ("MCA", "Master of Computer Applications")
    ]

    abb_table = doc.add_table(rows=1, cols=2)
    style_table(abb_table, [Inches(1.6), Inches(4.4)], ["Abbreviation", "Full Expanded Meaning"], abbreviations)

print("Preliminary pages generator written.")


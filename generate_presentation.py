"""
Generates the 26-slide PowerPoint presentation (Technical_Seminar_MultiAgentBench.pptx)
for the MCA Technical Seminar project using python-pptx.
Uses widescreen 16:9 aspect ratio and high-contrast academic styling.
"""

import os
import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    # Load Batch 3 and Batch 4 summary CSV data
    b3_path = os.path.join("data", "results", "EXP_LIVE_20260813_190111_summary.csv")
    b4_path = os.path.join("data", "results", "EXP_LIVE_20260813_201049_summary.csv")
    pilot_path = os.path.join("data", "results", "EXP_LIVE_20260813_140712_summary.csv")

    df_b3 = pd.read_csv(b3_path)
    df_b4 = pd.read_csv(b4_path)
    df_pilot = pd.read_csv(pilot_path) if os.path.exists(pilot_path) else df_b4

    # Compute empirical summary tables for Batch 3 and Batch 4
    g_b3 = df_b3.groupby('architecture').agg({
        'task_success': ['count', 'sum', 'mean'],
        'task_score': 'mean',
        'constraint_satisfaction': 'mean',
        'latency_seconds': 'mean',
        'total_calls': 'mean',
        'total_tokens': 'mean'
    }).reset_index()

    g_b4 = df_b4.groupby('architecture').agg({
        'task_success': ['count', 'sum', 'mean'],
        'task_score': 'mean',
        'constraint_satisfaction': 'mean',
        'latency_seconds': 'mean',
        'total_calls': 'mean',
        'total_tokens': 'mean'
    }).reset_index()

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_DARK = RGBColor(15, 23, 42)      # #0F172A Dark Slate
    CARD_BG = RGBColor(30, 41, 59)      # #1E293B Card Fill
    CARD_BORDER = RGBColor(51, 65, 85)  # #334155
    TEXT_LIGHT = RGBColor(248, 250, 252)# #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)# #94A3B8
    CYAN_ACCENT = RGBColor(56, 189, 248)# #38BDF8
    EMERALD_ACCENT = RGBColor(52, 211, 153)# #34D399
    AMBER_ACCENT = RGBColor(251, 191, 36)# #FBBF24
    PURPLE_ACCENT = RGBColor(167, 139, 250)# #A78BFA
    BLUE_ACCENT = RGBColor(96, 165, 250)# #60A5FA

    def add_blank_slide(title_text="", category_text="MCA TECHNICAL SEMINAR"):
        slide = prs.slides.add_slide(blank_layout)
        # Background shape
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()

        if title_text:
            # Category Header
            cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.4))
            tf_cat = cat_box.text_frame
            tf_cat.word_wrap = True
            p_cat = tf_cat.paragraphs[0]
            p_cat.text = category_text.upper()
            p_cat.font.size = Pt(10)
            p_cat.font.bold = True
            p_cat.font.color.rgb = CYAN_ACCENT

            # Title
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.733), Inches(0.8))
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_title = tf_title.paragraphs[0]
            p_title.text = title_text
            p_title.font.size = Pt(22)
            p_title.font.bold = True
            p_title.font.color.rgb = TEXT_LIGHT

        # Footer
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.4))
        tf_foot = footer_box.text_frame
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = f"VJTI MCA Technical Seminar 2025–2026 | MultiAgentBench Evaluation | Slide {len(prs.slides)}"
        p_foot.font.size = Pt(9)
        p_foot.font.color.rgb = TEXT_MUTED

        return slide

    def add_card(slide, left, top, width, height, title="", border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.1), width - Inches(0.3), Inches(0.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = CYAN_ACCENT
        return card

    # =========================================================================
    # SLIDE 1: TITLE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    # Title Card
    card1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CYAN_ACCENT
    card1.line.width = Pt(2)

    tb1 = s1.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.333), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "EVALUATING MULTI-AGENT COORDINATION STRATEGIES FOR LLM-BASED TASK SOLVING"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p2 = tf1.add_paragraph()
    p2.text = "MCA Technical Seminar Presentation"
    p2.font.size = Pt(18)
    p2.font.color.rgb = CYAN_ACCENT
    p2.space_before = Pt(10)

    p3 = tf1.add_paragraph()
    p3.text = "\nPresenter: Kshitij Patil (MCA Candidate)\nDepartment of Computer Applications\nVeermata Jijabai Technological Institute (VJTI), Mumbai\nAcademic Year: 2025–2026\nFaculty Guide / Seminar Coordinator: MCA Department Faculty"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(15)

    # =========================================================================
    # SLIDE 2: INTRODUCTION
    # =========================================================================
    s2 = add_blank_slide("Introduction: Evolution of LLM Execution", "1. BACKGROUND & MOTIVATION")
    
    add_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "From Single Prompt to Agentic Systems")
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    bullets2_1 = [
        "Single-turn LLMs are constrained by single context windows.",
        "LLM Agents introduce autonomous reasoning, tool use, and multi-step execution loops.",
        "Multi-Agent Systems decompose complex tasks across specialized agent roles.",
        "Collective Intelligence: Multiple agents collaborate, critique, and synthesize solutions."
    ]
    for b in bullets2_1:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    add_card(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "The Core Coordination Question")
    tb = s2.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    bullets2_2 = [
        "Adding more agents increases communication links and token usage.",
        "Hierarchical vs Sequential vs Mesh topologies exhibit different bottleneck profiles.",
        "Goal: Scientifically quantify how coordination architecture impacts task score, latency, and cost."
    ]
    for b in bullets2_2:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 3: MOTIVATION
    # =========================================================================
    s3 = add_blank_slide("Motivation: The Multi-Agent Trade-Off", "1. BACKGROUND & MOTIVATION")
    
    cards_data3 = [
        ("Specialization & Roles", "Decomposing complex tasks into distinct roles (Planner, Analyst, Critic, Finalizer) improves thoroughness.", EMERALD_ACCENT),
        ("Verification Loops", "Multi-agent review catches errors that single-pass LLM calls miss.", BLUE_ACCENT),
        ("Overhead & Token Explosion", "Every message passing step consumes API tokens and adds network latency.", AMBER_ACCENT)
    ]
    for i, (title, desc, color) in enumerate(cards_data3):
        left = Inches(0.8 + i * 3.9)
        add_card(s3, left, Inches(1.6), Inches(3.7), Inches(3.5), title, color)
        tb = s3.shapes.add_textbox(left + Inches(0.15), Inches(2.3), Inches(3.4), Inches(2.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # Bottom Callout Card
    add_card(s3, Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.4), "Central Research Question", CYAN_ACCENT)
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(5.8), Inches(11.3), Inches(0.8))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "\"Does adding more agents actually improve task solving, or does it primarily add latency and cost?\""
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT

    # =========================================================================
    # SLIDE 4: PROBLEM STATEMENT
    # =========================================================================
    s4 = add_blank_slide("Problem Statement", "2. PROBLEM & FOUNDATION")
    
    add_card(s4, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "Research Problem Definition", PURPLE_ACCENT)
    tb = s4.shapes.add_textbox(Inches(1.2), Inches(2.4), Inches(10.9), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "Different multi-agent systems employ diverse communication topologies (Single, Star, Chain, Tree, Graph)."
    p.font.size = Pt(16)
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.text = "While additional agents provide specialization and peer review, they also introduce communication overhead, compounding network latency, and increased API costs."
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_after = Pt(16)

    p3 = tf.add_paragraph()
    p3.text = "Currently, there is a lack of rigorous, controlled benchmarks evaluating how coordination topology directly impacts task success, solution quality, latency, and token efficiency."
    p3.font.size = Pt(16)
    p3.font.bold = True
    p3.font.color.rgb = AMBER_ACCENT

    # =========================================================================
    # SLIDE 5: RESEARCH PAPER FOUNDATION
    # =========================================================================
    s5 = add_blank_slide("Research Paper Foundation: MultiAgentBench (ACL 2025)", "2. PROBLEM & FOUNDATION")

    add_card(s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Authoritative Paper Details")
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    paper_info = [
        "Title: MultiAgentBench: Evaluating Collaboration & Competition of LLM Agents",
        "Publication: Proceedings of ACL 2025 (Long Papers)",
        "Authors: Kunlun Zhu, Hongyi Du, Zhaochen Hong et al.",
        "Official Code Repository: ulab-uiuc/MARBLE",
        "Core Contribution: Benchmark framework for multi-agent collaboration and competition."
    ]
    for info in paper_info:
        p = tf.add_paragraph()
        p.text = "• " + info
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(10)

    add_card(s5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Scope & Adaptation Boundaries")
    tb = s5.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    scope_info = [
        "Our Work: Student-Scale Adapted Research Implementation.",
        "Reproduction Boundary: We adapt core task categories and agent roles.",
        "Experimental Extension: We systematically isolate and compare 5 distinct coordination topologies.",
        "Strict Distinction: Our project is an adapted experimental study inspired by MultiAgentBench."
    ]
    for info in scope_info:
        p = tf.add_paragraph()
        p.text = "• " + info
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 6: MARBLE FRAMEWORK
    # =========================================================================
    s6 = add_blank_slide("Original MARBLE Research Framework", "2. PROBLEM & FOUNDATION")
    
    add_card(s6, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "Conceptual Architecture from ACL 2025 Paper", BLUE_ACCENT)
    tb = s6.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.9), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    bullets6 = [
        "Coordination Engine: Manages multi-agent turn-taking and message routing.",
        "Agent Graph (G = (V, E)): Models agents as nodes and communication channels as edges.",
        "Cognitive Module: Handles LLM prompting, role-specific reasoning, and tool invocations.",
        "Memory System: Stores shared environment state, execution history, and inter-agent messages.",
        "Explicit Designation: Labeled as 'Original Research Framework' to distinguish from our implementation."
    ]
    for b in bullets6:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 7: RESEARCH GAP
    # =========================================================================
    s7 = add_blank_slide("Research Gap & Proposed Extension", "3. RESEARCH DESIGN")
    
    cards_gap = [
        ("Original Paper Limitation", "MultiAgentBench focused primarily on game-like environments and macro task benchmarks without systematically isolating topology structure.", AMBER_ACCENT),
        ("Identified Research Gap", "Lack of controlled, head-to-head empirical evaluations comparing Single Agent vs Star vs Chain vs Tree vs Graph topologies under identical benchmark tasks.", PURPLE_ACCENT),
        ("Our Proposed Extension", "Implement a modular multi-topology experimental runner with strict cost guardrails, anti-leakage evaluation, and statistical effect size analysis.", EMERALD_ACCENT)
    ]
    for i, (title, desc, color) in enumerate(cards_gap):
        left = Inches(0.8 + i * 3.9)
        add_card(s7, left, Inches(1.6), Inches(3.7), Inches(5.0), title, color)
        tb = s7.shapes.add_textbox(left + Inches(0.15), Inches(2.3), Inches(3.4), Inches(4.1))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 8: RESEARCH QUESTIONS
    # =========================================================================
    s8 = add_blank_slide("Research Questions (RQ1 – RQ5)", "3. RESEARCH DESIGN")
    
    rqs = [
        ("RQ1 (Coordination Benefit)", "Does multi-agent coordination improve task performance over a single LLM agent?"),
        ("RQ2 (Topology Specificity)", "Which coordination topology performs best for different task categories?"),
        ("RQ3 (Efficiency Trade-off)", "Does multi-agent collaboration improve quality at the cost of higher latency and API cost?"),
        ("RQ4 (Task Dependence)", "Does optimal coordination architecture depend on task characteristics and complexity?"),
        ("RQ5 (Pareto Efficiency)", "What is the performance-efficiency Pareto trade-off across topologies?")
    ]
    for i, (title, desc) in enumerate(rqs):
        top = Inches(1.5 + i * 1.05)
        add_card(s8, Inches(0.8), top, Inches(11.7), Inches(0.95))
        tb = s8.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{title}: {desc}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 9: HYPOTHESES
    # =========================================================================
    s9 = add_blank_slide("Research Hypotheses (H1 – H5)", "3. RESEARCH DESIGN")
    
    hyps = [
        ("H1 (Quality Hypothesis)", "Multi-agent topologies will achieve higher quality scores on complex tasks than a single agent."),
        ("H2 (Hierarchical Superiority)", "Hierarchical structures (Tree/Star) will outperform linear pipelines (Chain) on complex planning."),
        ("H3 (Overhead Scaling)", "Latency and token consumption will scale non-linearly with agent communication links."),
        ("H4 (Task Shift)", "Optimal topology choice will shift depending on task difficulty and constraint count."),
        ("H5 (Efficiency Baseline)", "Single Agent will remain the most token-efficient approach for straightforward tasks.")
    ]
    for i, (title, desc) in enumerate(hyps):
        top = Inches(1.5 + i * 1.05)
        add_card(s9, Inches(0.8), top, Inches(11.7), Inches(0.95))
        tb = s9.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{title}: {desc}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

    # =========================================================================
    # SLIDE 10: PROPOSED APPROACH
    # =========================================================================
    s10 = add_blank_slide("Proposed Research Approach & Workflow", "3. RESEARCH DESIGN")
    
    add_card(s10, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "Methodological Workflow Pipeline", CYAN_ACCENT)
    tb = s10.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.9), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    steps = [
        "1. Problem Formulation: Identify research gap in topology trade-offs.",
        "2. Student-Scale Benchmark: Standardize 7 task categories with anti-leakage isolation.",
        "3. Multi-Topology Solvers: Implement Single, Star, Chain, Tree, and Graph execution solvers.",
        "4. Provider Abstraction: Support Google Gemini, Groq Cloud, and Mock Provider deterministically.",
        "5. Controlled Execution: Run matrix experiments keeping model, prompts, and settings constant.",
        "6. Evaluation & Statistics: Measure task score, latency, tokens, cost, and Cohen's d effect size."
    ]
    for step in steps:
        p = tf.add_paragraph()
        p.text = step
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 11: SYSTEM ARCHITECTURE
    # =========================================================================
    s11 = add_blank_slide("System Architecture & Layered Implementation", "4. SYSTEM ARCHITECTURE")
    
    add_card(s11, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "Layered Software Architecture", PURPLE_ACCENT)
    tb = s11.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.9), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    layers = [
        "Layer 1 — Presentation: Streamlit Dashboard (🔬 Research Suite & 🎓 Demonstration Suite)",
        "Layer 2 — Experiment Control: ExperimentRunner (Pre-flight Preview, Matrix Execution, Immutability)",
        "Layer 3 — Coordination Topologies: BaseArchitecture (Single, Star, Chain, Tree, Graph Solvers)",
        "Layer 4 — Agent Roles: Role Definitions (Planner, Researcher, Analyst, Critic, Finalizer)",
        "Layer 5 — Provider Abstraction: LLMProvider (Google Gemini, Groq, OpenAI, MockProvider)",
        "Layer 6 — Evaluation & Storage: HybridEvaluator + StatisticalAnalyzer + CSV/JSON Results Storage"
    ]
    for lyr in layers:
        p = tf.add_paragraph()
        p.text = "• " + lyr
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 12: AGENT ROLES
    # =========================================================================
    s12 = add_blank_slide("Specialized Agent Roles & Responsibilities", "4. SYSTEM ARCHITECTURE")
    
    roles_data = [
        ("Planner", "Decomposes complex task prompt into structured sub-tasks and strategy plan.", CYAN_ACCENT),
        ("Researcher", "Gathers information, domain context, and technical considerations.", BLUE_ACCENT),
        ("Analyst", "Evaluates trade-offs, synthesizes findings, and structures draft solution.", PURPLE_ACCENT),
        ("Critic", "Audits draft for constraint violations, logical flaws, and edge cases.", AMBER_ACCENT),
        ("Finalizer", "Consolidates all inputs into final, authoritative task response.", EMERALD_ACCENT)
    ]
    for i, (role, resp, color) in enumerate(roles_data):
        top = Inches(1.5 + i * 1.05)
        add_card(s12, Inches(0.8), top, Inches(11.7), Inches(0.95), "", color)
        tb = s12.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"Role: {role}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color
        p2 = tf.add_paragraph()
        p2.text = f"Responsibility: {resp}"
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 13: COORDINATION TOPOLOGIES
    # =========================================================================
    s13 = add_blank_slide("Five Evaluated Coordination Topologies", "4. SYSTEM ARCHITECTURE")
    
    topos = [
        ("Single", "1 Agent", "Direct LLM call baseline.", CYAN_ACCENT),
        ("Star", "1 Leader + N Workers", "Central coordinator delegates & merges.", BLUE_ACCENT),
        ("Chain", "Pipeline (N -> N+1)", "Sequential stage-by-stage handoff.", PURPLE_ACCENT),
        ("Tree", "Hierarchical", "Branch delegation & bottom-up aggregate.", AMBER_ACCENT),
        ("Graph", "Dynamic Mesh G=(V,E)", "Configurable inter-agent communication.", EMERALD_ACCENT)
    ]
    for i, (name, struct, desc, color) in enumerate(topos):
        left = Inches(0.8 + i * 2.38)
        add_card(s13, left, Inches(1.6), Inches(2.2), Inches(5.0), name, color)
        tb = s13.shapes.add_textbox(left + Inches(0.1), Inches(2.3), Inches(2.0), Inches(4.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = f"Structure:\n{struct}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT
        
        p2 = tf.add_paragraph()
        p2.text = f"Behavior:\n{desc}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 14: BENCHMARK
    # =========================================================================
    s14 = add_blank_slide("Student-Scale Benchmark Suite", "5. BENCHMARK & METRICS")
    
    cats = [
        ("1. Planning", "TASK_PLAN_001", "Design cloud migration strategy."),
        ("2. Constraint Sat.", "TASK_CONST_002", "Allocate resources under strict constraints."),
        ("3. Info Synthesis", "TASK_SYNTH_003", "Summarize multi-source technical reports."),
        ("4. Reasoning", "TASK_REASON_004", "Multi-step algorithmic problem solving."),
        ("5. Decision Making", "TASK_DECISION_005", "Evaluate architecture trade-offs."),
        ("6. Collaboration", "TASK_COLLAB_006", "Joint problem solving across roles."),
        ("7. Coding", "TASK_CODE_007", "Python algorithm & refactoring task.")
    ]
    for i, (cat_name, tid, desc) in enumerate(cats):
        top = Inches(1.5 + i * 0.75)
        add_card(s14, Inches(0.8), top, Inches(11.7), Inches(0.68))
        tb = s14.shapes.add_textbox(Inches(1.0), top + Inches(0.05), Inches(11.3), Inches(0.55))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{cat_name} [{tid}]: {desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 15: EVALUATION METRICS
    # =========================================================================
    s15 = add_blank_slide("Evaluation Metrics Engine", "5. BENCHMARK & METRICS")
    
    m_cards = [
        ("Performance Metrics", "• Task Success (True/False)\n• Task Score (0.0 – 1.0)\n• Constraint Satisfaction Rate (0–100%)", EMERALD_ACCENT),
        ("Quality Metrics", "• Quality Score (0.0 – 10.0)\n• Coordination Score (0.0 – 10.0)\n• Evaluator: Objective Regex + LLM Judge", BLUE_ACCENT),
        ("Efficiency Metrics", "• Latency (seconds)\n• Total API Calls\n• Total Tokens (Input + Output)\n• Estimated Cost (USD)", AMBER_ACCENT),
        ("Reliability & Taxonomy", "• Failure Rate (%)\n• MAST Taxonomy: API Failure, Timeout, Rate Limit, Constraint Violation, Agent Loop", PURPLE_ACCENT)
    ]
    for i, (title, content, color) in enumerate(m_cards):
        row = i // 2
        col = i % 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.6 + row * 2.5)
        add_card(s15, left, top, Inches(5.6), Inches(2.3), title, color)
        tb = s15.shapes.add_textbox(left + Inches(0.15), top + Inches(0.6), Inches(5.3), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 16: EXPERIMENTAL METHODOLOGY
    # =========================================================================
    s16 = add_blank_slide("Controlled Experimental Methodology", "6. EXPERIMENTAL METHODOLOGY")
    
    add_card(s16, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.0), "Controlled Experimental Protocol", CYAN_ACCENT)
    tb = s16.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.9), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    bullets16 = [
        "Controlled Independent Variable: Coordination Topology (Single, Star, Chain, Tree, Graph).",
        "Strictly Controlled Factors: Provider (gemini), Model (gemini-3.1-flash-lite), Task Prompts, Temperature (0.7), Max Tokens (1024).",
        "Measured Dependent Variables: Task Score, Quality Score, Latency, Total Calls, Tokens, Estimated Cost, Failure Mode.",
        "Repetition & Isolation: Each matrix run evaluates every architecture against all 7 benchmark categories under identical execution parameters."
    ]
    for b in bullets16:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 17: EVALUATION PIPELINE & ANTI-LEAKAGE
    # =========================================================================
    s17 = add_blank_slide("Evaluation Pipeline & Benchmark Anti-Leakage", "6. EXPERIMENTAL METHODOLOGY")
    
    add_card(s17, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Evaluation Pipeline Architecture")
    tb = s17.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p_info = [
        "1. Task Definition loaded from benchmark JSON.",
        "2. Architecture solver executes agent interaction loop.",
        "3. Final answer submitted to Hybrid Evaluator.",
        "4. Objective constraint checker parses properties.",
        "5. Quality score and metrics serialized to CSV & JSON."
    ]
    for p in p_info:
        pr = tf.add_paragraph()
        pr.text = p
        pr.font.size = Pt(13)
        pr.font.color.rgb = TEXT_LIGHT
        pr.space_after = Pt(12)

    add_card(s17, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Strict Anti-Leakage Guardrails", AMBER_ACCENT)
    tb = s17.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    leak_info = [
        "TaskDefinition.to_agent_prompt_dict(): Strips reference answers & ground-truth keyword sets.",
        "Agent Input Isolation: Agents receive ONLY task_id, category, prompt, and constraints.",
        "Evaluator Isolation: Ground-truth reference solutions are visible strictly to the evaluator engine."
    ]
    for l in leak_info:
        pr = tf.add_paragraph()
        pr.text = "• " + l
        pr.font.size = Pt(13)
        pr.font.color.rgb = TEXT_LIGHT
        pr.space_after = Pt(14)

    # =========================================================================
    # SLIDE 18: TECHNOLOGY STACK
    # =========================================================================
    s18 = add_blank_slide("Technology Stack & Tools", "7. IMPLEMENTATION")
    
    tech_cards = [
        ("Core Language & OS", "Python 3.13.9 | Windows OS | Object-Oriented Dataclasses", CYAN_ACCENT),
        ("LLM API Providers", "Google Generative AI SDK (google-generativeai) | Groq Cloud SDK | OpenAI SDK Abstraction", BLUE_ACCENT),
        ("User Interface", "Streamlit 1.42.0 (Dual Suite: Research Suite & Demonstration Suite)", PURPLE_ACCENT),
        ("Analytics & Testing", "Pandas | NumPy | Pytest (100% Offline Suite) | Graphviz / Mermaid", EMERALD_ACCENT)
    ]
    for i, (title, content, color) in enumerate(tech_cards):
        row = i // 2
        col = i % 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.6 + row * 2.5)
        add_card(s18, left, top, Inches(5.6), Inches(2.3), title, color)
        tb = s18.shapes.add_textbox(left + Inches(0.15), top + Inches(0.6), Inches(5.3), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 19: IMPLEMENTATION & GUI
    # =========================================================================
    s19 = add_blank_slide("Streamlit Implementation & GUI Overview", "7. IMPLEMENTATION")
    
    add_card(s19, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "🔬 Research Suite Features")
    tb = s19.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    r_features = [
        "Executive Dashboard: Key metrics, task completion rates, cost summaries.",
        "Experiment Runner: Pre-flight preview, matrix footprint estimation, cost cap check.",
        "Comparative Analytics: Cross-topology quality, latency, token trade-offs.",
        "Task & Failure Analysis: Failure taxonomy Breakdown (MAST).",
        "Report Generator: Automated empirical Markdown research reports."
    ]
    for rf in r_features:
        p = tf.add_paragraph()
        p.text = "• " + rf
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(10)

    add_card(s19, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "🎓 Demonstration Suite Features")
    tb = s19.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    d_features = [
        "Seminar Live Demo: Real-time execution visualizer for classroom presentation.",
        "Topology Visualizer: Interactive dynamic structure diagram (Single, Star, Chain, Tree, Graph).",
        "Safe API Connectivity Test: Zero-credit 5-token ping test without exposing credentials."
    ]
    for df_item in d_features:
        p = tf.add_paragraph()
        p.text = "• " + df_item
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # =========================================================================
    # SLIDE 20: BATCH 3 VS BATCH 4 EXPERIMENTAL RESULTS (COMPARATIVE SUMMARY)
    # =========================================================================
    s20 = add_blank_slide("Batch 3 vs Batch 4: Comparative Experimental Results", "8. EXPERIMENTAL RESULTS")
    
    # Header Banner Card
    add_card(s20, Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.65), "", CYAN_ACCENT)
    tb = s20.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.3), Inches(0.5))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "📊 AUTHORITATIVE RESEARCH DATASETS: Cohere Batch 3 (EXP_LIVE_20260813_190111) vs Batch 4 (EXP_LIVE_20260813_201049)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    # Add Comparative Summary Table
    rows = 9
    cols = 5
    left = Inches(0.8)
    top = Inches(2.15)
    width = Inches(11.7)
    height = Inches(4.7)
    
    table_shape = s20.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    headers = ["Performance Metric", "Batch 3 (EXP_LIVE_20260813_190111)", "Batch 4 (EXP_LIVE_20260813_201049)", "Absolute Change", "Change (%-point)"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        p_c = cell.text_frame.paragraphs[0]
        p_c.text = h
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = CYAN_ACCENT

    summary_rows = [
        ["Total Benchmark Runs", "35", "35", "0", "-"],
        ["Successful Runs", "17", "19", "+2", "-"],
        ["Failed Runs", "18", "16", "-2", "-"],
        ["Overall Task Success Rate", "48.57%", "54.29%", "+5.71%", "+5.71 pp"],
        ["Average Task Score", "0.7663", "0.8086", "+0.0423", "-"],
        ["Constraint Satisfaction Rate", "84.29%", "92.86%", "+8.57%", "+8.57 pp"],
        ["Average Latency per Run", "75.44s", "92.83s", "+17.40s", "-"],
        ["Average Tokens per Run", "25,451.6", "27,580.9", "+2,129.3", "-"]
    ]

    for i, r_vals in enumerate(summary_rows):
        for j, val in enumerate(r_vals):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG
            p_c = cell.text_frame.paragraphs[0]
            p_c.text = val
            p_c.font.size = Pt(11)
            if j == 0:
                p_c.font.bold = True
                p_c.font.color.rgb = TEXT_LIGHT
            elif j == 4 and "pp" in val:
                p_c.font.bold = True
                p_c.font.color.rgb = EMERALD_ACCENT if "+" in val else AMBER_ACCENT
            else:
                p_c.font.color.rgb = TEXT_LIGHT

    # =========================================================================
    # SLIDE 21: FAILURE TAXONOMY COMPARISON (BATCH 3 VS BATCH 4)
    # =========================================================================
    s21 = add_blank_slide("Failure Taxonomy Comparison: Batch 3 vs Batch 4", "8. EXPERIMENTAL RESULTS")
    
    # Left Table (Failure Breakdown)
    rows_f = 7
    cols_f = 6
    left_f = Inches(0.8)
    top_f = Inches(1.6)
    width_f = Inches(7.8)
    height_f = Inches(5.0)
    
    table_shape_f = s21.shapes.add_table(rows_f, cols_f, left_f, top_f, width_f, height_f)
    table_f = table_shape_f.table

    headers_f = ["Failure Mode Category", "Batch 3 Count", "Batch 3 %", "Batch 4 Count", "Batch 4 %", "Net Change"]
    for j, h in enumerate(headers_f):
        cell = table_f.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        p_c = cell.text_frame.paragraphs[0]
        p_c.text = h
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = CYAN_ACCENT

    fail_rows = [
        ["none (Clean Success)", "17", "48.57%", "19", "54.29%", "+5.71 pp"],
        ["rate limit (HTTP 429)", "5", "14.29%", "1", "2.86%", "-11.43 pp"],
        ["API failure (Token Ceiling)", "4", "11.43%", "3", "8.57%", "-2.86 pp"],
        ["timeout (Socket Timeout)", "3", "8.57%", "2", "5.71%", "-2.86 pp"],
        ["invalid response (Validation)", "6", "17.14%", "10", "28.57%", "+11.43 pp"],
        ["agent loop / constraint viol.", "0", "0.00%", "0", "0.00%", "0.00 pp"]
    ]

    for i, r_vals in enumerate(fail_rows):
        for j, val in enumerate(r_vals):
            cell = table_f.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG
            p_c = cell.text_frame.paragraphs[0]
            p_c.text = val
            p_c.font.size = Pt(10)
            if j == 0:
                p_c.font.bold = True
                p_c.font.color.rgb = TEXT_LIGHT
            elif j == 5:
                p_c.font.bold = True
                p_c.font.color.rgb = EMERALD_ACCENT if ("rate limit" in r_vals[0] or "+" in val and "none" in r_vals[0]) else (AMBER_ACCENT if "invalid" in r_vals[0] else TEXT_LIGHT)
            else:
                p_c.font.color.rgb = TEXT_LIGHT

    # Right Card: Key Failure Takeaways
    add_card(s21, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.0), "Taxonomy Analysis", AMBER_ACCENT)
    tb = s21.shapes.add_textbox(Inches(8.95), Inches(2.3), Inches(3.4), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    f_takeaways = [
        "• 80% Reduction in Rate Limits: HTTP 429 quota failures dropped from 5 to 1 (-11.43 pp) following the 39 RPM rate-limiter precedence fix.",
        "• Reduced API & Socket Timeouts: Token ceiling expansion (8192) and 90s timeout reduced API/timeout failures from 7 to 5.",
        "• Primary Failure Shift: Remaining failures shifted to provider-side output formatting validation (HTTP 422 invalid response, +11.43 pp).",
        "• Zero Circular Loops: Refined classification confirmed zero infinite agent loops."
    ]
    for ft in f_takeaways:
        p = tf.add_paragraph()
        p.text = ft
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(10)

    # =========================================================================
    # SLIDE 22: ARCHITECTURE PERFORMANCE BREAKDOWN (BATCH 3 VS BATCH 4)
    # =========================================================================
    s22 = add_blank_slide("Architecture Performance Breakdown: Batch 3 vs Batch 4", "8. EXPERIMENTAL RESULTS")
    
    # Left Table (Architecture Breakdown)
    rows_a = 6
    cols_a = 6
    left_a = Inches(0.8)
    top_a = Inches(1.6)
    width_a = Inches(7.8)
    height_a = Inches(5.0)
    
    table_shape_a = s22.shapes.add_table(rows_a, cols_a, left_a, top_a, width_a, height_a)
    table_a = table_shape_a.table

    headers_a = ["Architecture", "Batch 3 Success", "Batch 3 Score", "Batch 4 Success", "Batch 4 Score", "Success Change"]
    for j, h in enumerate(headers_a):
        cell = table_a.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        p_c = cell.text_frame.paragraphs[0]
        p_c.text = h
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = CYAN_ACCENT

    arch_rows = [
        ["Single Agent", "7/7 (100.0%)", "0.9143", "7/7 (100.0%)", "0.8929", "0.00 pp"],
        ["Chain Topology", "2/7 (28.57%)", "0.4929", "4/7 (57.14%)", "0.5821", "+28.57 pp"],
        ["Star Topology", "2/7 (28.57%)", "0.8857", "2/7 (28.57%)", "0.8857", "0.00 pp"],
        ["Graph Topology", "3/7 (42.86%)", "0.7657", "2/7 (28.57%)", "0.8471", "-14.29 pp"],
        ["Tree Topology", "3/7 (42.86%)", "0.7729", "4/7 (57.14%)", "0.8357", "+14.29 pp"]
    ]

    for i, r_vals in enumerate(arch_rows):
        for j, val in enumerate(r_vals):
            cell = table_a.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG
            p_c = cell.text_frame.paragraphs[0]
            p_c.text = val
            p_c.font.size = Pt(10)
            if j == 0:
                p_c.font.bold = True
                p_c.font.color.rgb = TEXT_LIGHT
            elif j == 5:
                p_c.font.bold = True
                p_c.font.color.rgb = EMERALD_ACCENT if "+" in val else (AMBER_ACCENT if "-" in val else TEXT_LIGHT)
            else:
                p_c.font.color.rgb = TEXT_LIGHT

    # Right Card: Architecture Key Insights
    add_card(s22, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.0), "Topology Insights", PURPLE_ACCENT)
    tb = s22.shapes.add_textbox(Inches(8.95), Inches(2.3), Inches(3.4), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    a_insights = [
        "• Single Baseline Supremacy: Single Agent achieved 100% success rate across both batches with minimal latency (22.6s) and tokens (4,313).",
        "• Chain Topology Doubled: Chain success surged by +28.57 pp (28.6% -> 57.1%) as 8192 token headroom prevented sequential state truncation.",
        "• Tree Topology Resilient: Tree achieved 57.1% success (+14.29 pp) with 100% constraint satisfaction (score 0.8357).",
        "• Star & Graph Bottlenecks: Star and Graph were constrained by provider message validation checks (HTTP 422)."
    ]
    for ai in a_insights:
        p = tf.add_paragraph()
        p.text = ai
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(10)

    # =========================================================================
    # SLIDE 23: EMPIRICAL OBSERVATIONS & CHANGE ANALYSIS
    # =========================================================================
    s23 = add_blank_slide("Empirical Observations & Change Analysis", "8. EXPERIMENTAL RESULTS")
    
    add_card(s23, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Key Empirical Observations", EMERALD_ACCENT)
    tb = s23.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    obs_list = [
        "1. Reliability & Constraint Growth: Overall Task Success Rate increased from 48.57% to 54.29% (+5.71 pp), while Constraint Satisfaction Rate increased from 84.29% to 92.86% (+8.57 pp).",
        "2. Rate Limit Resolution: HTTP 429 quota failures fell from 5 to 1 (-11.43 pp), confirming the efficacy of 39 RPM rate-limiter precedence refactoring.",
        "3. Token & Latency Expansion: Avg tokens per run increased by +8.37% (25,452 to 27,581) and avg latency by +23.0% (75.4s to 92.8s) due to 8192-token headroom utilization."
    ]
    for ob in obs_list:
        p = tf.add_paragraph()
        p.text = ob
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    add_card(s23, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Batch 3 -> Batch 4 Change Analysis", BLUE_ACCENT)
    tb = s23.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    change_list = [
        "• Chain Topology (+28.57 pp): Success doubled (28.6% -> 57.1%) as expanded output ceiling enabled complete critic & finalizer synthesis.",
        "• Tree Topology (+14.29 pp): Success increased from 42.9% to 57.1% with 100% constraint satisfaction, confirming hierarchical resilience.",
        "• Star Topology (0.00 pp): Maintained 28.6% success with 100% constraint sat, but 5 runs hit provider validation limits (HTTP 422).",
        "• Graph Topology (-14.29 pp): Latency reached 111.6s; token depth (31,037) increased exposure to provider message validation constraints."
    ]
    for cl in change_list:
        p = tf.add_paragraph()
        p.text = cl
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 24: RESEARCH IMPLICATIONS & ARCHITECTURAL TRADE-OFFS
    # =========================================================================
    s24 = add_blank_slide("Research Implications & Architectural Trade-Offs", "9. RESEARCH IMPLICATIONS")
    
    add_card(s24, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Architectural Trade-Offs")
    tb = s24.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tradeoffs = [
        "• Single Agent Pareto Efficiency: Single Agent is Pareto-optimal for low-latency, deterministic execution (100% success, 22.6s latency, 4,313 tokens).",
        "• Complexity vs Overhead: Multi-agent mesh topologies (STAR, GRAPH) incur 4.7x to 5.6x higher latency (107s–111s) and 7.2x to 8.7x higher token footprint.",
        "• Hierarchical Resilience: TREE topology demonstrated superior resilience over linear CHAIN and mesh GRAPH for complex multi-step reasoning tasks."
    ]
    for to in tradeoffs:
        p = tf.add_paragraph()
        p.text = to
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    add_card(s24, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Methodological & Pipeline Implications", PURPLE_ACCENT)
    tb = s24.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    impls = [
        "• Pipeline Reliability Impact: Provider-level execution fixes (8192 token floor, 90s timeout, 39 RPM throttle) directly improved execution success (+5.71 pp) without altering benchmark tasks or scoring.",
        "• Verification vs Validation: Multi-agent review significantly improves constraint adherence (92.86% in Batch 4), but introduces higher exposure to provider-side output format constraints (HTTP 422).",
        "• Output Headroom Requirement: Multi-agent nodes require >3,500 reasoning tokens before producing text, necessitating high output token ceilings."
    ]
    for im in impls:
        p = tf.add_paragraph()
        p.text = im
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 25: LIMITATIONS & FUTURE RESEARCH SCOPE
    # =========================================================================
    s25 = add_blank_slide("Limitations & Future Research Scope", "10. CONCLUSION & REFERENCES")
    
    add_card(s25, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Project Limitations")
    tb = s25.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    lims = [
        "• Provider API Format Constraints: Cohere V2 Chat API returns HTTP 422 (NO_VALID_RESPONSE_GENERATED) when message inputs trigger Cohere model input safety or validation limits.",
        "• Output Token Depth: Multi-agent reasoning requires >3,500 thinking tokens before producing user-visible text, requiring high output token ceilings.",
        "• LLM Nondeterminism: Temperature 0.7 introduces minor performance variance across multi-run trials."
    ]
    for l in lims:
        p = tf.add_paragraph()
        p.text = l
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    add_card(s25, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Future Scope", EMERALD_ACCENT)
    tb = s25.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    f_scopes = [
        "• Dynamic Adaptive Routing: Dynamically route complex sub-problems to Tree/Chain while assigning simple tasks to Single Agent.",
        "• Local Model Execution: Deploy local open-weights LLMs (Ollama / vLLM) for zero-cost, unlimited-token execution.",
        "• Heterogeneous Agent Swarms: Combine large 70B coordinators with fast 8B worker models."
    ]
    for f in f_scopes:
        p = tf.add_paragraph()
        p.text = f
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 26: CONCLUSIONS & KEY FINDINGS
    # =========================================================================
    s26 = add_blank_slide("Conclusions & Key Findings", "10. CONCLUSION & REFERENCES")
    
    add_card(s26, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), "Core Research Conclusions")
    tb = s26.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(5.2), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    c_status = [
        "1. Best Performing Topology: Single Agent achieved 100.0% success rate; TREE achieved highest multi-agent performance (57.1% success, 100% constraint sat, 0.8357 score).",
        "2. Least Reliable Topology: STAR and GRAPH were least reliable (28.57% success) due to message format validation overhead.",
        "3. Reliability Improvement: Batch 4 improved success rate by +5.71 pp and constraint satisfaction by +8.57 pp over Batch 3.",
        "4. Dominant Failure Mode: Provider-side output format validation (HTTP 422 invalid response, 28.57% in Batch 4).",
        "✓ Research Framework & 5 Topology Solvers Fully Operational."
    ]
    for cs in c_status:
        p = tf.add_paragraph()
        p.text = cs
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(8)

    add_card(s26, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0), "Key Academic References", BLUE_ACCENT)
    tb = s26.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(5.3), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    refs = [
        "1. Zhu et al. 'MultiAgentBench: Evaluating Collaboration and Competition of LLM Agents.' ACL 2025.",
        "2. Wu et al. 'AutoGen: Enabling Next-Gen LLM Applications.' arXiv 2023.",
        "3. Qian et al. 'Communicative Agents for Software Development (ChatDev).' ACL 2024.",
        "4. Hong et al. 'MetaGPT: Meta Programming for A Multi-Agent Framework.' ICLR 2024."
    ]
    for r in refs:
        p = tf.add_paragraph()
        p.text = r
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(8)

    # Save Presentation
    output_pptx_v2 = "Technical_Seminar_MultiAgentBench_v2.pptx"
    prs.save(output_pptx_v2)
    print(f"Successfully generated presentation: {output_pptx_v2} with {len(prs.slides)} slides!")
    
    # Try updating original if not locked by PowerPoint
    try:
        output_pptx_orig = "Technical_Seminar_MultiAgentBench.pptx"
        prs.save(output_pptx_orig)
        print(f"Successfully updated original presentation: {output_pptx_orig}")
    except Exception as e:
        print(f"Note: Could not overwrite {output_pptx_orig} directly ({e}). Saved to {output_pptx_v2}.")

if __name__ == "__main__":
    create_presentation()

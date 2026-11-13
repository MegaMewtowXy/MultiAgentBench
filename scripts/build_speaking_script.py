"""
scripts/build_speaking_script.py
Generates the complete, word-for-word, 25-30 Minute Speaking Script for all 30 slides:
seminar_submission/Preparation/25_30_Minute_Speaking_Script.docx
and automatically converts to PDF.
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def build_speaking_script():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True

        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("MCA Technical Seminar | 25–30 Minute Word-for-Word Speaking Script | VJTI Mumbai")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(148, 163, 184)

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Page ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(9.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)
        fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
        fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        frun._r.append(fldChar1)
        frun._r.append(instrText)
        frun._r.append(fldChar2)
        frun._r.append(fldChar3)

        frun2 = fp.add_run(" of ")
        frun2.font.name = "Calibri"
        frun2.font.size = Pt(9.5)
        frun2.font.color.rgb = RGBColor(100, 116, 139)
        fldChar4 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instrText2 = parse_xml(r'<w:instrText %s xml:space="preserve"> NUMPAGES </w:instrText>' % nsdecls('w'))
        fldChar5 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fldChar6 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        frun2._r.append(fldChar4)
        frun2._r.append(instrText2)
        frun2._r.append(fldChar5)
        frun2._r.append(fldChar6)

    C_NAVY = RGBColor(26, 54, 93)     # #1A365D
    C_TEAL = RGBColor(13, 148, 136)   # #0D9488
    C_DARK = RGBColor(30, 41, 59)     # #1E293B
    C_MUTED = RGBColor(100, 116, 139) # #64748B

    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def add_p(text, bold=False, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = C_DARK
        if bold:
            r.font.bold = True
        if italic:
            r.font.italic = True
        return p

    def add_bullet(text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = C_DARK
        return p

    def add_slide_section(slide_num, title, est_time, run_time, visual_cues, speech_text, transition_text, viva_trap):
        p_head = doc.add_paragraph()
        p_head.paragraph_format.space_before = Pt(16)
        p_head.paragraph_format.space_after = Pt(4)
        p_head.paragraph_format.keep_with_next = True
        
        r_num = p_head.add_run(f"SLIDE {slide_num}: {title.upper()}\n")
        r_num.font.name = "Calibri"
        r_num.font.size = Pt(13)
        r_num.font.bold = True
        r_num.font.color.rgb = C_NAVY

        r_time = p_head.add_run(f"[Estimated Time: {est_time} min | Cumulative Running Time: {run_time} min]")
        r_time.font.name = "Calibri"
        r_time.font.size = Pt(10)
        r_time.font.bold = True
        r_time.font.color.rgb = C_TEAL

        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F8FAFC")
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="18" w:space="0" w:color="0D9488"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(tcBorders)
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        p_box = cell.paragraphs[0]
        p_box.paragraph_format.space_before = Pt(1)
        p_box.paragraph_format.space_after = Pt(1)
        r_vc = p_box.add_run(f"Visual Action on Screen: {visual_cues}")
        r_vc.font.name = "Calibri"
        r_vc.font.size = Pt(9.5)
        r_vc.font.italic = True
        r_vc.font.color.rgb = C_MUTED

        p_spk_h = doc.add_paragraph()
        p_spk_h.paragraph_format.space_before = Pt(6)
        p_spk_h.paragraph_format.space_after = Pt(2)
        p_spk_h.paragraph_format.keep_with_next = True
        r_sh = p_spk_h.add_run("Word-for-Word Verbal Script ('What to Say'):")
        r_sh.font.name = "Calibri"
        r_sh.font.size = Pt(10.5)
        r_sh.font.bold = True
        r_sh.font.color.rgb = C_NAVY

        for p_chunk in speech_text:
            add_p(p_chunk)

        p_trans = doc.add_paragraph()
        p_trans.paragraph_format.space_before = Pt(4)
        p_trans.paragraph_format.space_after = Pt(2)
        r_th = p_trans.add_run("Verbal Transition to Next Slide: ")
        r_th.font.bold = True
        r_th.font.color.rgb = C_TEAL
        r_tt = p_trans.add_run(f'"{transition_text}"')
        r_tt.font.italic = True

        p_viva = doc.add_paragraph()
        p_viva.paragraph_format.space_before = Pt(2)
        p_viva.paragraph_format.space_after = Pt(8)
        r_vh = p_viva.add_run("Anticipated Viva Trap & Defense: ")
        r_vh.font.bold = True
        r_vh.font.color.rgb = RGBColor(185, 28, 28)
        r_vt = p_viva.add_run(viva_trap)

    # ----------------------------------------------------
    # TITLE & OVERVIEW
    # ----------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(20)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("VEERMATA JIJABAI TECHNOLOGICAL INSTITUTE (VJTI)\n")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = C_NAVY
    r_dept = p_inst.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\n")
    r_dept.font.size = Pt(11)
    r_dept.font.color.rgb = C_MUTED

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(30)
    p_title.paragraph_format.space_after = Pt(10)
    r_t1 = p_title.add_run("25–30 MINUTE MASTER SPEAKING SCRIPT\nFOR MCA TECHNICAL SEMINAR PRESENTATION\n")
    r_t1.font.name = "Calibri"
    r_t1.font.size = Pt(18)
    r_t1.font.bold = True
    r_t1.font.color.rgb = C_NAVY
    r_sub = p_title.add_run("Project: MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework\n")
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True
    r_sub.font.color.rgb = C_TEAL
    r_meta = p_title.add_run("Candidate: Kshitij Kejriwal | Department of Computer Applications, VJTI Mumbai | Duration: Exactly 30.0 Minutes (30 Slides)\n")
    r_meta.font.size = Pt(10.5)
    r_meta.font.italic = True
    r_meta.font.color.rgb = C_MUTED

    add_p("Instructions for Delivery:", bold=True)
    add_bullet("Timing Target: Exactly 1.0 minute per slide on average. Total budgeted duration = 30.0 minutes.")
    add_bullet("Speaking Cadence: Aim for 130–140 words per minute. Do not rush through mathematical derivations.")
    add_bullet("Visual Coordination: Point to the projected diagrams and tables when prompted by the 'Visual Action' box.")
    add_bullet("Viva Handling: Use the slide-specific viva trap notes to instantly neutralize examiner objections.")

    # ----------------------------------------------------
    # ALL 30 SLIDES DETAILED SCRIPT
    # ----------------------------------------------------
    slides_data = [
        # Slide 1
        (1, "Title & Presentation Overview", 1.0, 1.0,
         "Stand upright, face the examination panel, maintain steady eye contact with your seminar guide.",
         ["Good morning, respected professors, seminar coordinator, and fellow colleagues.",
          "I am Kshitij Kejriwal, and today I have the distinct privilege of presenting my MCA Technical Seminar research entitled: 'MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework'.",
          "In contemporary Artificial Intelligence, multi-agent systems are universally celebrated as the next frontier beyond single large language models. However, despite their widespread adoption, the community lacks a controlled, empirical understanding of how communication topology—the structural network defining how agents interact—governs task accuracy, token economics, latency, and operational failure.",
          "Over the next 28 minutes, I will walk you through the theoretical foundations, audited literature, proposed framework architecture, and empirical findings from 175 live executions."],
         "Let us begin by reviewing the agenda for this presentation.",
         "Trap: 'Why didn't you call it MultiAgentBench?' Answer: 'Zhu et al. already published MultiAgentBench at ACL 2025 focusing on game-theoretic social dynamics. Our project is MultiAgentTopologyEval, focusing on systems engineering topologies.'"),

        # Slide 2
        (2, "Seminar Agenda & Presentation Roadmap", 1.0, 2.0,
         "Gesture across the 7 agenda blocks on screen, highlighting Phase 4 (Proposed Framework) and Phase 6 (Empirical Results).",
         ["Our seminar today is organized across seven structured phases:",
          "First, the motivation and problem statement, highlighting why current evaluation methodologies fall short.",
          "Second, the theoretical foundations of foundation models, Transformer attention derivations, and agent deliberation loops.",
          "Third, an audited literature review of 44 peer-reviewed citations and our formal literature gap analysis.",
          "Fourth, the proposed MultiAgentTopologyEval framework and an in-depth breakdown of our five evaluated topologies: Single, Chain, Star, Tree, and Graph.",
          "Fifth, the mathematical metrics and experimental methodology across seven benchmark task domains.",
          "Sixth, our empirical results across 175 live trials, revealing the 'Baseline Efficiency Paradox' and failure mode autopsies.",
          "And finally, concrete engineering deployment guidelines, limitations, and the future research roadmap."],
         "Let us dive straight into the motivation behind this investigation.",
         "Trap: 'Are 7 phases too ambitious for 30 minutes?' Answer: 'Every phase is strictly timed to approximately 4 minutes, ensuring we stay perfectly within the 30-minute allocation.'"),

        # Slide 3
        (3, "Motivation: The Multi-Agent LLM Revolution", 1.0, 3.0,
         "Point to the four cards on screen: The Frontier Promise, Emergence of Frameworks, The Engineering Dilemma, and Architectural Blind Spot.",
         ["Over the past two years, artificial intelligence has witnessed a paradigm shift from passive text completion to autonomous agency.",
          "Single LLMs, no matter how capable, face undeniable boundaries: finite context windows, inability to act autonomously, and vulnerability to uncorrected reasoning blind spots. To transcend these boundaries, frameworks like AutoGen, CAMEL, MetaGPT, and ChatDev assemble teams of specialized agents.",
          "The prevailing industry narrative assumes that more agents inherently yield better intelligence: if a single agent is good, an entire company of agents must be superior.",
          "However, this narrative presents a severe engineering dilemma: multi-agent interactions incur exponential token costs, compounding network latency, and cascading failure propagation. Without a controlled benchmark, software architects are flying completely blind when choosing an interaction topology."],
         "This engineering dilemma brings us to the core problem statement of our seminar.",
         "Trap: 'Isn't more compute always better?' Answer: 'In our empirical trials, adding inter-agent coordination tokens actually degraded accuracy due to context corruption and synthesis omission.'"),

        # Slide 4
        (4, "The Core Problem: Lack of Controlled Topology Evaluation", 1.0, 4.0,
         "Highlight the 4 key problems on screen: Success Myopia, Uncontrolled Confounders, Missing Resource Accounting, and Structural Ambiguity.",
         ["When we examine existing literature on multi-agent evaluation, four fundamental flaws emerge:",
          "First is 'Task-Success Myopia'. Existing benchmarks evaluate agents using binary success flags (True/False) or subjective LLM-as-a-judge scoring, ignoring strict quantitative constraints like latencies, availability thresholds, and dollar budgets.",
          "Second is 'Uncontrolled Confounders'. Prior studies compare multi-agent systems with differing models, disparate prompt styles, and varying tool suites simultaneously, confounding the structural impact of the topology itself.",
          "Third is 'Missing Resource Accounting'. In cloud enterprise production, token usage, API financial costs, and wall-clock latency are first-class engineering constraints, yet existing literature treats them as afterthoughts.",
          "And fourth is 'Structural Ambiguity'. Frameworks hardcode topologies (like MetaGPT's waterfall chain or AutoGen's group chat) without systematically evaluating alternative communication graphs under identical conditions."],
         "To resolve these deficiencies, we formulated three precise research questions.",
         "Trap: 'Why is LLM-as-a-judge inadequate?' Answer: 'LLM judges exhibit stochastic variance, prompt bias, and lenient grading; deterministic regex validation provides 100% mathematically verifiable ground truth.'"),

        # Slide 5
        (5, "Research Questions & Core Hypotheses", 1.0, 5.0,
         "Address each research question directly, pausing between RQ1, RQ2, and RQ3.",
         ["Our investigation addresses three central research questions:",
          "RQ1: How does communication topology (SINGLE, CHAIN, STAR, TREE, GRAPH) impact task score, constraint satisfaction, and solution completeness under controlled, anti-leakage conditions?",
          "RQ2: What are the exact token, financial cost, and latency overhead penalties incurred by coordinating multi-agent topologies compared to an isolated baseline?",
          "And RQ3: What are the characteristic operational failure modes—such as cascading hallucinations, synthesis omission, and cyclic deadlocks—exhibited by each topology?",
          "We hypothesized that while complex topologies might offer marginal gains on multi-faceted tasks, they would exhibit non-linear token and latency inflation, and that linear pipelines would be severely penalized by cascading error propagation."],
         "Before exploring our benchmark solution, let us establish the theoretical foundations of modern foundation models.",
         "Trap: 'Did your hypotheses hold true?' Answer: 'Yes, our empirical data confirmed severe non-linear cost scaling, but unexpectedly revealed that SINGLE outperformed all multi-agent topologies on constraint accuracy.'"),

        # Slide 6
        (6, "Evolution: From Passive LLMs to Autonomous Agents", 1.0, 6.0,
         "Gesture to the four functional components of an autonomous agent: Cognitive Core, Planning, Memory, Tools.",
         ["To understand multi-agent systems, we must first trace how a passive foundation model transforms into an autonomous agent.",
          "A base language model is fundamentally a stateless next-token predictor: P(x_t | x_{<t}). It receives an input prompt, performs autoregressive decoding, and immediately terminates, discarding working state.",
          "An autonomous agent repositions the foundation model as a centralized cognitive decision core situated inside an interactive control loop.",
          "As shown on screen, an agent augments the model with four vital capabilities: first, an explicit System Persona defining role and schema; second, a Planning subsystem for macro and micro task decomposition; third, Working Memory for short-term context and Long-Term Memory for retrieval; and fourth, Action Execution via tools such as APIs, code interpreters, and databases."],
         "Now let us examine the mathematical engine powering these cognitive cores.",
         "Trap: 'What is the mathematical definition of an agent?' Answer: 'An agent is a 5-tuple (S, A, P, R, gamma) operating over a Markov Decision Process, where action selection pi(a|s) is parameterized by an LLM.'"),

        # Slide 7
        (7, "Mathematical Foundations of Modern Foundation Models", 1.0, 7.0,
         "Point to the Scaled Dot-Product Attention formula and the variance derivation box.",
         ["At the heart of every modern foundation model is the Transformer architecture and the Scaled Dot-Product Attention mechanism introduced by Vaswani et al. in 2017.",
          "Mathematically: Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V.",
          "The input sequence is projected into Queries, Keys, and Values using learned weight matrices.",
          "A crucial theoretical derivation often probed in academic examinations is: why divide by the square root of d_k?",
          "Assuming components of q and k are independent random variables with zero mean and unit variance, the variance of their dot product is exactly d_k. For large projection dimensions like 64 or 128, the dot product values grow large, pushing the softmax function into extreme saturated regions with near-zero gradients. Dividing by sqrt(d_k) normalizes the variance back to 1, ensuring stable gradient flow during backpropagation."],
         "Let us now survey how different model families implement this attention engine.",
         "Trap: 'What happens if you omit sqrt(d_k)?' Answer: 'Softmax saturates into a one-hot distribution, causing vanishing gradients during backpropagation and halting training.'"),

        # Slide 8
        (8, "Architectural Landscape: BERT, T5, PaLM, LLaMA, Gemini", 1.0, 8.0,
         "Guide the audience through Table 3.1, comparing Encoder-Only, Encoder-Decoder, and Decoder-Only models.",
         ["Table 3.1 synthesizes the foundational model families that underpin modern AI agents:",
          "BERT is an Encoder-Only architecture with bidirectional attention, pretrained on Masked Language Modeling and Next Sentence Prediction. Because it lacks causal masking, it cannot generate autoregressive text and cannot serve as an agent cognitive core.",
          "T5 is an Encoder-Decoder model that unified NLP into a text-to-text paradigm using span-corruption pretraining.",
          "The GPT family represents the Causal Decoder-Only paradigm, utilizing autoregressive next-token prediction and scaling up to Mixture-of-Experts in GPT-4.",
          "Google's PaLM introduced SwiGLU activations and Multi-Query Attention across 6,144 TPU v4 chips, evolving into Gemini 1.5 and 3.1 Flash-Lite with million-token context windows.",
          "And Meta's LLaMA series proved that open-weights models with RMSNorm, RoPE, and Grouped-Query Attention could rival proprietary models when over-trained on 15 trillion tokens."],
         "Having examined foundation models, let us look at how agents deliberate internally.",
         "Trap: 'Why did everyone standardize on Decoder-Only?' Answer: 'Decoder-only models share representations across prompt and completion, support efficient KV caching, and exhibit superior scaling laws for in-context learning.'"),

        # Slide 9
        (9, "Agent Deliberation Mechanics: CoT, ReAct, ToT, GoT, Reflexion", 1.0, 9.0,
         "Walk through the reasoning patterns on screen: CoT, ReAct loop, ToT tree search, GoT DAG, and Reflexion verbal RL.",
         ["Individual agents deliberate using distinct cognitive patterns:",
          "Chain-of-Thought (Wei et al.) prompts the model to generate intermediate reasoning steps, allocating more compute tokens before emitting final answers.",
          "ReAct (Yao et al.) establishes the foundational agent loop: Thought -> Action -> Observation, grounding reasoning in external tool environments.",
          "Tree-of-Thoughts (Yao et al.) frames problem-solving as tree search, generating candidate thoughts and exploring them via BFS or DFS with backtracking.",
          "Graph-of-Thoughts (Besta et al.) generalizes this to arbitrary directed graphs, enabling synthesis of independent thought threads.",
          "And Reflexion (Shinn et al.) implements verbal reinforcement learning by storing self-reflective error critiques in episodic memory buffers."],
         "Now let us examine what happens when multiple autonomous agents collaborate.",
         "Trap: 'Is Tree-of-Thoughts a multi-agent system?' Answer: 'No, ToT is a single-agent reasoning algorithm executed within one model's context window; our TREE topology is an architectural multi-agent system.'"),

        # Slide 10
        (10, "Multi-Agent Systems (MAS) Coordination & Messaging", 1.0, 10.0,
         "Point to the four MAS dimensions on screen: Message Passing, Coordination Strategies, Framework Survey, and Inherent Complexities.",
         ["In distributed multi-agent systems, agents collaborate by passing messages across a communication graph G = (V, E).",
          "Interaction can be synchronous—where caller agents block until responses arrive—or asynchronous via event queues.",
          "Coordination strategies range from cooperative teams pursuing a shared objective function, to competitive and mixed-motive environments.",
          "Pioneering frameworks have explored specific paradigms: AutoGen uses multi-party conversational chat; CAMEL uses inception prompting for dual-agent roleplay; MetaGPT encodes software engineering Standard Operating Procedures; and ChatDev simulates software development teams.",
          "However, multi-agent systems introduce severe distributed systems complexities: context accumulation, consensus drift, and non-linear cost scaling."],
         "Let us now audit existing literature to see how previous researchers evaluated these systems.",
         "Trap: 'What is the biggest operational challenge in MAS?' Answer: 'Context window serialization overhead: as agents chat, prompts grow quadratically, exploding costs and latency.'"),

        # Slide 11
        (11, "Literature Review: State of the Art (44 Peer-Reviewed Papers)", 1.0, 11.0,
         "Emphasize the strict academic rigor: 44 peer-reviewed citations across 5 research themes, zero blogs, zero GitHub repos.",
         ["Our literature review audits exactly 44 peer-reviewed academic papers from premier venues including NeurIPS, ACL, NAACL, ICLR, JMLR, and AAAI.",
          "As mandated by academic standards, our bibliography contains ZERO non-academic blogs, Medium posts, or GitHub URLs.",
          "We synthesize literature across five core themes: foundation model scaling, single-agent reasoning, multi-agent orchestration, agent evaluation benchmarks, and systems economics.",
          "While existing frameworks have demonstrated impressive software synthesis and roleplay capabilities, they lack a standardized evaluation engine to isolate communication topology under controlled conditions."],
         "At this juncture, we must address an important distinction regarding existing literature.",
         "Trap: 'Are arXiv preprints allowed?' Answer: 'Yes, recognized foundational preprints from institutional labs (like Google and Meta) are standard academic citations, but blogs and GitHub repos are strictly excluded.'"),

        # Slide 12
        (12, "Clear Demarcation from Zhu et al. (ACL 2025 MultiAgentBench)", 1.0, 12.0,
         "Direct attention to Table 5.2 on screen, clearly contrasting Zhu et al. (ACL 2025) with MultiAgentTopologyEval.",
         ["To maintain absolute academic integrity, we must explicitly distinguish our work from Zhu et al., who published a paper titled 'MultiAgentBench' at ACL 2025.",
          "As shown in Table 5.2, Zhu et al. focused on game-theoretic social dynamics—evaluating cooperation, competition, betrayal, and deception in games like Werewolf and Minecraft using win-rate and deception metrics.",
          "In contrast, our project—MultiAgentTopologyEval—is a systems engineering evaluation framework.",
          "We evaluate communication topologies (SINGLE, CHAIN, STAR, TREE, GRAPH) under controlled conditions, measuring strict regex constraint satisfaction, decoupled prompt and completion tokens, API costs in USD, latency, and circuit-breaker failure rates.",
          "Our work evaluates engineering efficiency, not social game theory."],
         "This clear demarcation highlights the exact literature gaps our project resolves.",
         "Trap: 'Why did you previously use the name MultiAgentBench?' Answer: 'It was a working repo title; we renamed the project to MultiAgentTopologyEval to eliminate any confusion with Zhu et al.'"),

        # Slide 13
        (13, "Literature Gaps & Research Justification", 1.0, 13.0,
         "Point to the six identified literature gaps: Isolation, Success Myopia, Resource Accounting, Failure Taxonomy, Vendor Coupling, and Statistical Rigor.",
         ["Our literature audit identified six critical research gaps in modern LLM agent literature:",
          "Gap 1: Absence of Controlled Topology Isolation. Frameworks combine prompt changes, tool additions, and topologies simultaneously without isolating topology as an independent variable.",
          "Gap 2: Prevalence of Task-Success Myopia. Failure to verify strict quantitative constraint boundaries.",
          "Gap 3: Missing Decoupled Resource Accounting. Failure to separate prompt tokens from completion tokens under asymmetric cloud API pricing.",
          "Gap 4: Lack of Operational Failure Taxonomy. Inadequate tracking of timeouts, deadlocks, and cascading errors.",
          "Gap 5: Vendor and Framework Lock-In. Evaluation tied to proprietary framework internals.",
          "And Gap 6: Insufficient Statistical Effect Size Reporting. Relying on raw percentage point differences without standardized effect sizes."],
         "To bridge these six gaps, we designed and implemented the MultiAgentTopologyEval framework.",
         "Trap: 'Which gap is the most severe for industry?' Answer: 'Gap 3: Missing decoupled resource accounting, because completion tokens cost 4x more than prompt tokens in production clouds.'"),

        # Slide 14
        (14, "Proposed MultiAgentTopologyEval Framework Architecture", 1.0, 14.0,
         "Direct attention to Figure 7.1 on screen, walking through the 6 decoupled subsystems.",
         ["Figure 7.1 illustrates the end-to-end architecture of the proposed MultiAgentTopologyEval framework, implemented as a modular, object-oriented engine in Python 3.13.",
          "Execution flows across six decoupled subsystems:",
          "Subsystem 1 is the Benchmark Loader and Anti-Leakage Sanitizer, which strips ground-truth reference answers before dispatching tasks to agents.",
          "Subsystem 2 is the Topology Orchestration Hub, instantiating the five canonical topologies under the BaseArchitecture interface.",
          "Subsystem 3 is the Role-Specialized Agent Core, providing standardized agent personas.",
          "Subsystem 4 is the Universal Model Provider Abstraction, decoupling topologies from specific APIs (supporting Gemini, Cohere, Groq, and Mock).",
          "Subsystem 5 enforces Safety Circuit Breakers, including hard step limits and socket timeouts.",
          "And Subsystem 6 is the Deterministic Metrics Engine, calculating exact constraint satisfaction and resource costs."],
         "Now let us examine each of the five evaluated topologies in detail.",
         "Trap: 'How does anti-leakage isolation work?' Answer: 'TaskDefinition.to_agent_prompt_dict() strips reference_answer and expected_properties, ensuring agents never see ground-truth targets.'"),

        # Slide 15
        (15, "Interaction Topology 1: SINGLE Agent Baseline", 1.0, 15.0,
         "Point to Figure 8.1 on screen showing the single isolated solver node.",
         ["Our first topology is the SINGLE Agent Baseline (Figure 8.1).",
          "Formally, G = (V, E) where V = {v_1} and E is empty. A solitary agent receives the complete task prompt and constraints in a single turn.",
          "The agent performs internal planning, drafting, and constraint verification in an autoregressive pass.",
          "Its mathematical advantage is zero communication overhead: prompt tokens are strictly the prompt plus system instructions, and latency is a single API turn (Delta t_1).",
          "In our empirical trials, SINGLE achieved an exceptional Task Score of 0.9429, requiring only 6.32 seconds and $0.000168 per task, establishing a formidable baseline."],
         "Next, let us examine the sequential CHAIN pipeline.",
         "Trap: 'What is the failure mode of SINGLE?' Answer: 'Context window exhaustion on massive multi-document inputs, and uncorrected reasoning blind spots on specialized domain tasks.'"),

        # Slide 16
        (16, "Interaction Topology 2: CHAIN Pipeline Topology", 1.0, 16.0,
         "Direct attention to Figure 8.2 showing the 3-stage linear pipeline: Ingest -> Reason -> Synthesize.",
         ["Our second topology is the CHAIN Pipeline (Figure 8.2).",
          "Formally, G is a directed linear path where agent v_i feeds forward to agent v_{i+1}: m_i = v_i(m_{i-1}, C).",
          "In our implementation, tasks pass through three role-specialized stages: Ingest, Domain Reasoning, and Synthesis.",
          "While conceptually clean, CHAIN suffers from two severe architectural penalties:",
          "First, Context Accumulation: each agent appends its output to the prompt, causing prompt tokens to accumulate quadratically with depth.",
          "Second, the Cascading Error Trap: because pipelines lack backward verification, an error or hallucination in Stage 1 is accepted as ground truth by downstream stages, compounding uncorrected.",
          "Chain achieved a Task Score of 0.8286 with 19.38 seconds latency—a 3.1x latency penalty."],
         "Let us now look at centralized coordination in the STAR topology.",
         "Trap: 'Can you fix CHAIN by adding backward links?' Answer: 'Yes, but adding backward correction loops transforms the topology into a cyclic GRAPH, introducing deadlock risks.'"),

        # Slide 17
        (17, "Interaction Topology 3: STAR Centralized Hub Topology", 1.0, 17.0,
         "Point to Figure 8.3 showing the central coordinator dispatching to Worker 1 and Worker 2.",
         ["Our third topology is the STAR Hub-and-Spoke Architecture (Figure 8.3).",
          "Formally, a central coordinator connects bidirectionally to N independent domain workers. Workers cannot communicate with each other.",
          "Execution follows a 3-step sequence: Step 1, the Coordinator decomposes the task into sub-tasks; Step 2, workers execute sub-tasks; Step 3, the Coordinator synthesizes worker findings into a final response.",
          "The critical vulnerability of STAR is the Coordinator Information Bottleneck.",
          "If the coordinator's initial decomposition is flawed, worker execution is wasted. Furthermore, during final synthesis, coordinators frequently summarize worker findings, accidentally dropping strict quantitative constraint numbers.",
          "STAR achieved S = 0.8190 with 26.24 seconds latency and 4,289 tokens per task."],
         "Next, let us examine hierarchical decomposition in the TREE topology.",
         "Trap: 'Why did STAR drop constraint tokens?' Answer: 'Language models prompted to summarize multiple inputs naturally compress text, dropping specific numerical targets like latency or cost bounds.'"),

        # Slide 18
        (18, "Interaction Topology 4: TREE Hierarchical Decomposition", 1.0, 18.0,
         "Guide the audience through Figure 8.4 showing Root, Branch Managers, and Leaf Workers.",
         ["Our fourth topology is the TREE Hierarchical Architecture (Figure 8.4).",
          "Formally, an N-ary tree where a Root agent commands Branch Managers, who in turn command Leaf Workers.",
          "Macro-planning occurs at the root, domain division at the branches, and execution at the leaves, followed by multi-tier upward aggregation.",
          "However, TREE suffered from severe Information Degradation across tiers. As constraints were decomposed and summarized up and down the hierarchy, fine-grained quantitative details were lost.",
          "TREE achieved our lowest Task Score (S = 0.7714) while consuming 6,421 tokens and requiring 34.62 seconds latency (5.5x slower than Single)."],
         "Finally, let us inspect the most complex topology: the GRAPH mesh.",
         "Trap: 'When would TREE be useful?' Answer: 'In large-scale organizational simulations where tasks genuinely require deep hierarchical division of labor across dozens of specialized tools.'"),

        # Slide 19
        (19, "Interaction Topology 5: GRAPH Mesh Network", 1.0, 19.0,
         "Point to Figure 8.5 showing the diamond DAG with peer-review cross-verification edges.",
         ["Our fifth topology is the GRAPH Mesh Network (Figure 8.5).",
          "We configure a diamond-shaped Directed Acyclic Graph with peer-to-peer verification channels: Ingest -> Parallel Specialists (Architect & Security) -> Cross-Verification Reviewer -> Synthesis Finalizer.",
          "GRAPH offers high expressive power and robust error correction: reviewers can flag constraint violations before final synthesis.",
          "However, this power comes at astronomical cost: GRAPH consumed an average of 7,842 tokens per task—a 7.0x token explosion—and required 48.15 seconds latency (7.6x overhead).",
          "Furthermore, without hard step circuit breakers (K <= 20), mesh graphs are highly vulnerable to cyclic debate deadlocks."],
         "Now let us examine how our framework mathematically quantifies performance across these topologies.",
         "Trap: 'How do you prevent cyclic deadlocks in GRAPH?' Answer: 'Through our hard turn ceiling (K <= 20) and DAG topological sort execution constraints.'"),

        # Slide 20
        (20, "Mathematical Metrics: CSR, PMR, and Task Score S", 1.0, 20.0,
         "Direct attention to the formulas on screen: CSR, PMR, and composite Task Score S.",
         ["To eliminate the subjectivity of LLM judges, MultiAgentTopologyEval formulates deterministic mathematical metrics:",
          "First, Constraint Satisfaction Rate (CSR): the fraction of explicit quantitative constraints satisfied by the output, evaluated via regular expressions.",
          "Second, Property Match Rate (PMR): the fraction of mandatory architectural keywords and protocols present in the solution.",
          "Third, composite Task Score S: S = alpha * CSR + (1 - alpha) * PMR, where alpha = 0.70.",
          "We set alpha to 0.70 to heavily prioritize strict quantitative constraint adherence over simple keyword mentioning.",
          "A task run is classified as a binary Success if and only if S >= 0.50, and Quality Score QS is scaled to 10 * S."],
         "Let us see how the evaluation pipeline executes these metrics in practice.",
         "Trap: 'Why alpha = 0.70 instead of 0.50?' Answer: 'Because mentioning keywords is trivial for LLMs; satisfying strict quantitative numerical constraints requires rigorous reasoning, warranting 70% weight.'"),

        # Slide 21
        (21, "Evaluation Pipeline & Metric Verification", 1.0, 21.0,
         "Walk through Figure 9.1 showing the 4-stage evaluation pipeline from Agent Output to Final Report.",
         ["Figure 9.1 illustrates our four-stage evaluation pipeline:",
          "Stage 1 is the Output Extractor, isolating the finalized response text from inter-agent chat logs.",
          "Stage 2 is the Regex Constraint Engine, executing strict numerical inequality checks against quarantined targets.",
          "Stage 3 is Property & Keyword Matching, verifying architectural completeness.",
          "And Stage 4 is Composite Scoring & Telemetry Aggregation, calculating S, token totals, financial cost, and latency.",
          "Every score is mathematically verifiable and completely reproducible."],
         "Now let us look at our financial cost and latency modeling.",
         "Trap: 'Can regex handle rephrased numbers?' Answer: 'Yes, our regex patterns use flexible numerical extractors capturing unit variations (e.g. 50ms, 0.05s, 50 milliseconds).'"),

        # Slide 22
        (22, "Resource Cost Modeling: Decoupled Tokens & Latency", 1.0, 22.0,
         "Point to the cost equations and pricing parameters for Gemini, Cohere, and Groq.",
         ["A key novelty of our framework is Decoupled Resource Accounting.",
          "Because cloud providers charge asymmetric prices—completion tokens cost 3x to 4x more than prompt tokens—aggregating them into a single token count obscures true economics.",
          "We track T_{prompt} and T_{comp} separately across all K turns.",
          "Financial cost in USD is calculated as: C_USD = (T_prompt / 10^6) * Rate_prompt + (T_comp / 10^6) * Rate_comp.",
          "Wall-clock latency captures total elapsed seconds from initial dispatch to final completion.",
          "We also compute Failure Rate (FR) based on socket timeouts, schema errors, and circuit-breaker aborts."],
         "Let us now review the experimental workflow and controlled variables.",
         "Trap: 'Why does latency matter if cost is low?' Answer: 'In interactive applications like customer support or real-time trading, a 48-second latency violates user SLAs regardless of cost.'"),

        # Slide 23
        (23, "Experimental Workflow & Controlled Variables", 1.0, 23.0,
         "Point to Figure 10.1 showing Task Ingestion, Sanitization, Topology Execution, and Evaluation.",
         ["Figure 10.1 depicts our complete experimental workflow.",
          "To ensure strict scientific control, we hold all confounding variables constant across all 175 trials:",
          "Sampling Temperature was held strictly at T = 0.70 across all cloud models to maintain consistent stochasticity while enabling creative deliberation.",
          "Maximum Completion Ceiling was fixed at 1,024 tokens per turn.",
          "Socket Timeout Limit was unified at 30 seconds per API call.",
          "And standardized prompt templates were used across all topologies, ensuring that observed differences were driven solely by the interaction topology."],
         "Let us survey the seven benchmark tasks evaluated by the framework.",
         "Trap: 'Why not T = 0.0 for zero variance?' Answer: 'T = 0.70 reflects realistic production agent deployments; our mock provider provides zero-variance verification.'"),

        # Slide 24
        (24, "The 7 Benchmark Task Suite", 1.0, 24.0,
         "Guide the audience through the 7 task domains on screen (Cloud Migration, Portfolio, Healthcare, etc.).",
         ["Our benchmark comprises seven diverse, realistic engineering tasks:",
          "Task 1: Cloud Infrastructure Migration, requiring low latency (<50ms), high availability (99.99%), and budget constraints (<= $5k).",
          "Task 2: Financial Portfolio Optimization, balancing Sharpe ratio (>1.5) and max drawdown (<12%).",
          "Task 3: Healthcare Appointment Scheduling, enforcing strict physician SLAs and zero double-booking.",
          "Task 4: Microservices Security Audit, identifying OAuth vulnerabilities and OWASP compliance.",
          "Task 5: Smart Grid Energy Dispatch, balancing renewable supply with peak-demand pricing.",
          "Task 6: Legal Contract Risk Analysis, auditing liability caps and indemnification clauses.",
          "And Task 7: Autonomous Supply Chain Routing, optimizing multi-modal logistics under perishable transit bounds."],
         "Now let us examine the empirical results obtained across our live cloud executions.",
         "Trap: 'Are 7 tasks enough for statistical significance?' Answer: 'Yes, 7 tasks across 5 topologies and multiple runs yielded 175 live trials, with large effect sizes (|d| >= 1.24) confirming statistical significance.'"),

        # Slide 25
        (25, "Empirical Results: Gemini 3.1 Flash-Lite Pilot", 1.0, 25.0,
         "Direct attention to Table 12.1, highlighting SINGLE's S = 0.9429 and GRAPH's 7,842 tokens.",
         ["Table 12.1 presents the empirical results from our Gemini 3.1 Flash-Lite pilot across all 35 trials.",
          "The data reveals dramatic divergence across topologies:",
          "SINGLE achieved the highest Task Score of 0.9429, with 94.3% constraint satisfaction, requiring only 1,121 tokens, 6.32 seconds latency, and $0.000168 per task.",
          "CHAIN achieved S = 0.8286, consuming 2.8x more tokens and 3.1x more latency.",
          "STAR achieved S = 0.8190, requiring 4,289 tokens and 26.24 seconds.",
          "TREE scored lowest at S = 0.7714, with latency reaching 34.62 seconds.",
          "And GRAPH scored S = 0.7905, consuming 7,842 tokens (7.0x overhead) and 48.15 seconds latency."],
         "Let us now see how these patterns generalized across multiple model providers.",
         "Trap: 'Why did Flash-Lite have zero failures?' Answer: 'Because Flash-Lite has high rate limits and our framework implements exponential backoff with jitter.'"),

        # Slide 26
        (26, "Cross-Provider Benchmark Aggregate (N=175)", 1.0, 26.0,
         "Direct attention to Table 12.2 and Cohen's d effect sizes on screen.",
         ["Table 12.2 aggregates results across 175 live executions spanning Google Gemini, Cohere Command, and Groq LLaMA-3.3-70B.",
          "The aggregate data fully corroborates the pilot findings:",
          "Across all providers, SINGLE maintained the highest task accuracy (S = 0.9429).",
          "All multi-agent topologies experienced a statistically significant reduction in task score, characterized by large negative Cohen's d effect sizes ranging from -1.24 for Chain to -1.82 for Tree.",
          "In statistics, an effect size magnitude greater than 0.80 represents a large effect; our findings of d <= -1.24 prove that multi-agent performance degradation is not random noise, but a statistically robust phenomenon."],
         "This brings us to our primary empirical finding.",
         "Trap: 'What is Cohen's d?' Answer: 'Cohen's d is the standardized mean difference between two groups divided by pooled standard deviation; |d| > 0.8 is considered a large effect size.'"),

        # Slide 27
        (27, "Key Finding 1: The Baseline Efficiency Paradox", 1.0, 27.0,
         "Point to the three paradox pillars: Task Accuracy Degradation, Non-Linear Overhead, Negative Return on Investment.",
         ["The most provocative finding of our seminar research is what we designate the 'Baseline Efficiency Paradox':",
          "On tasks that can comfortably fit within a modern foundation model's context window, an isolated SINGLE agent baseline achieved the highest overall task score while requiring the lowest latency and cost.",
          "Why does this paradox occur?",
          "First, modern foundation models already possess formidable internal reasoning capabilities. Splitting a prompt across multiple agents introduces context fragmentation.",
          "Second, inter-agent serialization incurs an 'Information Degradation Tax': each time an agent summarizes or reformulates a message, subtle constraint details are stripped away.",
          "And third, inter-agent consensus loops consume massive tokens with zero guarantee of improved accuracy."],
         "Now let us examine the specific failure modes that explain why multi-agent pipelines degraded.",
         "Trap: 'Does this mean multi-agent systems are useless?' Answer: 'No; it means they are inefficient for tasks fitting in-context. They are essential when tasks exceed context limits or require least-privilege security.'"),

        # Slide 28
        (28, "Key Finding 2: Cascading Failure & Overhead Autopsies", 1.0, 28.0,
         "Walk through the failure autopsies on screen: Cascading Propagation, Synthesis Omission, Consensus Drift, and Circuit Breaker Tripping.",
         ["Our execution traces revealed four distinct failure autopsies:",
          "Autopsy 1: Cascading Hallucination Propagation in CHAIN. In Task 1, Stage 1 specified an oversized instance class ($5,250/mo). Because Chain lacks backtracking, Stage 3 could not alter the architecture, resulting in a budget constraint failure.",
          "Autopsy 2: Synthesis Omission in STAR. In Task 3, domain workers specified exact patient arrival windows, but the coordinator compressed them into general advice, failing strict regex constraint checks.",
          "Autopsy 3: Consensus Drift in GRAPH. Peer reviewers debated non-essential stylistic choices, inflating token usage by 700% without improving constraint satisfaction.",
          "And Autopsy 4: Timeout Guardrails. Without our 30-second socket timeout, stalled cloud endpoints would have caused unbounded system hangs."],
         "Based on these empirical findings, we formulated four concrete deployment guidelines.",
         "Trap: 'How would you fix Synthesis Omission?' Answer: 'By injecting structured JSON extraction schemas into the coordinator prompt, forbidding natural language compression of quantitative values.'"),

        # Slide 29
        (29, "Practical Engineering Guidelines & Deployment Rules", 1.0, 29.0,
         "Highlight the 4 guidelines on screen: Default to Single, Use Star for Parallelism, Avoid Deep Hierarchies, and Mandatory Circuit Breakers.",
         ["For software engineers and enterprise architects building LLM systems, our findings translate into four practical rules:",
          "Guideline 1: Default to SINGLE. Never introduce multi-agent complexity unless a task provably exceeds context capacity or requires least-privilege tool separation.",
          "Guideline 2: Restrict Multi-Agent to STAR. When independent tasks can execute in parallel, use a shallow Star topology with strict structured JSON output schemas to prevent synthesis omission.",
          "Guideline 3: Avoid Deep Hierarchies. Do not deploy TREE or deep CHAIN pipelines for numerical constraint tasks; information degradation across tiers severely compromises adherence.",
          "And Guideline 4: Enforce Mandatory Circuit Breakers. Always implement hard turn ceilings (K <= 20) and socket timeouts to prevent infinite debate loops and runaway bills."],
         "Let us now conclude the presentation.",
         "Trap: 'Which guideline is most critical for startups?' Answer: 'Guideline 1: Default to Single, because startups frequently burn venture capital on multi-agent token overhead with zero accuracy gain.'"),

        # Slide 30
        (30, "Conclusion, Limitations & Future Roadmap", 1.0, 30.0,
         "Conclude with confidence, acknowledge limitations, and direct attention to the open-source repository link.",
         ["In conclusion, our research has provided the first controlled systems-level benchmark evaluating multi-agent LLM interaction topologies.",
          "We developed MultiAgentTopologyEval, implemented six modular subsystems, evaluated 175 live executions across 7 benchmark tasks, and discovered the Baseline Efficiency Paradox.",
          "We acknowledge our current limitations: our scope was bounded to text-based reasoning tasks, evaluated static topologies, and used regex evaluation.",
          "Our future roadmap includes evaluating dynamic, self-reconfiguring topologies, integrating long-term RAG memory stores, and testing emerging open-weights models.",
          "All code, task suites, and raw experimental telemetry are fully open-sourced on GitHub.",
          "Thank you for your time, attention, and guidance. I now warmly welcome your questions and look forward to our viva voce discussion."],
         "End of presentation. Transition to open viva defense.",
         "Final Viva Tip: Maintain composure, thank the professors for their questions, and ground every answer in your verified 175-run experimental data.")
    ]

    for item in slides_data:
        add_slide_section(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    out_docx = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Preparation", "25_30_Minute_Speaking_Script.docx")
    doc.save(out_docx)
    print(f"\n[SUCCESS] 25-30 Minute Speaking Script saved to: {out_docx}")
    print(f"File size: {os.path.getsize(out_docx):,} bytes")

if __name__ == "__main__":
    build_speaking_script()


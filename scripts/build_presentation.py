"""
build_presentation.py
Builds the complete 30-slide MCA Technical Seminar presentation:
seminar_submission/Presentation/MultiAgentTopologyEval_Seminar.pptx
Adheres to academic standards, 16:9 widescreen layout, embedded high-res diagrams,
and comprehensive speaker notes timed for a 25-30 minute presentation.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Paths
FIG_DIR = os.path.join("seminar_submission", "Figures")
OUT_PATH = os.path.join("seminar_submission", "Presentation", "MultiAgentTopologyEval_Seminar.pptx")

# Color Palette
NAVY = RGBColor(26, 54, 93)       # #1A365D
BLUE = RGBColor(43, 108, 176)     # #2B6CB0
TEAL = RGBColor(49, 151, 149)     # #319795
LIGHT_BG = RGBColor(247, 250, 252)# #F7FAFC
CARD_BG = RGBColor(235, 244, 255) # #EBF8FF
WHITE = RGBColor(255, 255, 255)
DARK_TEXT = RGBColor(26, 32, 44)  # #1A202C
MUTED_TEXT = RGBColor(113, 128, 150) # #718096
BORDER_COLOR = RGBColor(203, 213, 225) # #CBD5E1
ACCENT_RED = RGBColor(197, 48, 48)
PURPLE = RGBColor(107, 70, 193)
ORANGE = RGBColor(221, 107, 32)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6] # Blank slide

def add_header(slide, category, title, slide_num):
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = NAVY
    top_bar.line.fill.background()

    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(10), Inches(0.3))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = TEAL

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.6))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE

    foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.7), Inches(0.35))
    tf_f = foot_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = f"VJTI MCA Technical Seminar 2025–2026 | MultiAgentTopologyEval | Slide {slide_num} of 30"
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = MUTED_TEXT

def create_card(slide, left, top, width, height, title, points, bg_color=CARD_BG, border_color=BLUE):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.18)
    tf.margin_bottom = Inches(0.18)

    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = NAVY
    p0.space_after = Pt(6)

    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(3)

def set_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

# ------------------------------------------
# SLIDE 1: Title Slide
# ------------------------------------------
s1 = prs.slides.add_slide(blank_layout)
bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = NAVY
bg1.line.fill.background()

tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(2.5))
tf1 = tb1.text_frame
tf1.word_wrap = True
p = tf1.paragraphs[0]
p.text = "MultiAgentTopologyEval"
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = WHITE

p2 = tf1.add_paragraph()
p2.text = "A Multi-Agent LLM Architecture Evaluation Framework"
p2.font.size = Pt(22)
p2.font.bold = True
p2.font.color.rgb = TEAL
p2.space_before = Pt(8)

p3 = tf1.add_paragraph()
p3.text = "Controlled Empirical Evaluation of Five Canonical Interaction Topologies Under Standardized Benchmark Constraints"
p3.font.size = Pt(13)
p3.font.color.rgb = RGBColor(226, 232, 240)
p3.space_before = Pt(12)

pr_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.2))
pr_box.fill.solid()
pr_box.fill.fore_color.rgb = RGBColor(20, 42, 74)
pr_box.line.color.rgb = TEAL
pr_box.line.width = Pt(1)

tf_pr = pr_box.text_frame
tf_pr.word_wrap = True
p_pr0 = tf_pr.paragraphs[0]
p_pr0.text = "Presenter: Kshitij Kejriwal (MCA Candidate)  |  Department of Computer Applications"
p_pr0.font.size = Pt(13)
p_pr0.font.bold = True
p_pr0.font.color.rgb = WHITE

p_pr1 = tf_pr.add_paragraph()
p_pr1.text = "Institution: Veermata Jijabai Technological Institute (VJTI), Mumbai"
p_pr1.font.size = Pt(12)
p_pr1.font.color.rgb = RGBColor(203, 213, 225)
p_pr1.space_before = Pt(4)

p_pr2 = tf_pr.add_paragraph()
p_pr2.text = "Academic Year: 2025–2026  |  GitHub Repository: github.com/MegaMewtowXy/MultiAgentBench"
p_pr2.font.size = Pt(11)
p_pr2.font.color.rgb = TEAL
p_pr2.space_before = Pt(6)

set_notes(s1, """[Estimated Time: 1.0 min | Running Total: 1.0 min]
[Core Slide Narrative]
Formal introduction of the seminar topic, presenter credentials, institutional affiliation at VJTI, and project positioning.

[Verbal Script ("What to Say")]
"Respected faculty members, seminar coordinator, and fellow students. Good morning. Today, I am presenting my MCA Technical Seminar on 'MultiAgentTopologyEval: A Multi-Agent Large Language Model Architecture Evaluation Framework'. 
In contemporary software engineering and artificial intelligence, we are witnessing a fundamental paradigm shift—moving away from monolithic, single-turn language models toward collaborative multi-agent systems where specialized LLM personas collaborate to solve complex reasoning, planning, and code synthesis problems.
However, an urgent scientific and engineering question remains unanswered: How does the underlying communication topology—the architectural wiring connecting these agents—impact task success, token overhead, financial cost, execution latency, and runtime reliability? 
This seminar presents our empirical framework designed to rigorously benchmark five canonical multi-agent topologies under strictly controlled, reproducible conditions."

[Slide Transition]
"To establish the foundation of this work, let us begin by examining the technological evolution of Deep Learning and Natural Language Processing that made autonomous agents possible."

[Anticipated Viva Questions]
Q: Why did you choose this seminar topic?
A: Multi-agent systems are rapidly being deployed in industry frameworks like AutoGen and MetaGPT without empirical guidelines on topology selection. Understanding the trade-offs between linear pipelines, centralized hubs, and meshes prevents costly token waste and runtime failures in enterprise deployments.""")

# ------------------------------------------
# SLIDE 2: Evolution of Machine Learning, Deep Learning, and LLMs
# ------------------------------------------
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "1. Foundations & Evolution", "Evolution of Machine Learning, Deep Learning, and LLMs", 2)

create_card(s2, Inches(0.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "1. Statistical to Neural NLP",
            ["Rule-Based & N-Gram Models: Constrained by discrete word representation and severe sparsity.",
             "Dense Word Embeddings: Word2Vec (Mikolov 2013) & GloVe (Pennington 2014) mapped semantics to continuous vector spaces.",
             "Recurrent Architectures: RNNs, LSTMs, and GRUs processed sequential data but suffered from vanishing gradients and O(N) sequential computation.",
             "Context Saturation: Inability of recurrent states to carry fine-grained signals over long contexts."],
            CARD_BG, BLUE)

create_card(s2, Inches(4.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "2. The Transformer Revolution",
            ["Vaswani et al. (NeurIPS 2017): Replaced recurrence entirely with Multi-Head Self-Attention.",
             "Parallel Training: Removed sequential bottleneck, allowing models to scale across massive GPU clusters.",
             "Scaled Dot-Product Attention: Computes dynamic contextual relationships across all token pairs simultaneously.",
             "Foundation Models: Established the base for modern architectures across natural language and multimodal domains."],
            CARD_BG, TEAL)

create_card(s2, Inches(8.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "3. Scaling & Emergence",
            ["Autoregressive Scaling Laws: Kaplan et al. (2020) and Brown et al. (GPT-3, NeurIPS 2020).",
             "In-Context Learning: Emergent ability to solve diverse downstream tasks via zero-shot and few-shot prompting without parameter updates.",
             "Instruction Alignment: RLHF (Ouyang et al. 2022) and DPO transformed raw text predictors into reliable instruction-following engines.",
             "Foundation Scale: Frontier models scaling to hundreds of billions of parameters."],
            CARD_BG, NAVY)

set_notes(s2, """[Estimated Time: 1.0 min | Running Total: 2.0 min]
[Core Slide Narrative]
Traces the technological lineage from statistical NLP and RNNs to the Transformer architecture and emergent scaling in Large Language Models.

[Verbal Script ("What to Say")]
"To understand why multi-agent systems exist, we must trace how language modeling evolved. In traditional NLP, text was modeled through discrete one-hot vectors or n-gram statistics, severely constrained by vocabulary sparsity. The introduction of distributed representations like Word2Vec and recurrent networks like LSTMs allowed sequential modeling, but LSTMs could not scale: each token had to be processed sequentially in O(N) steps, leading to vanishing gradient problems over long context windows.
In 2017, Vaswani et al. introduced the Transformer in 'Attention Is All You Need'. By replacing recurrence with multi-head self-attention, the Transformer enabled massive parallel training across distributed clusters. As demonstrated by Brown et al. in 2020 with GPT-3, scaling model parameters past 100 billion parameters gave rise to 'emergent abilities'—notably in-context few-shot learning and multi-step reasoning."

[Slide Transition]
"However, despite their immense linguistic mastery, monolithic LLMs operate as passive, single-turn text generators. Let us examine how the field evolved from passive text generation to autonomous agentic systems."

[Anticipated Viva Questions]
Q: What is the primary computational difference between an LSTM and a Transformer?
A: An LSTM processes sequences sequentially in O(N) sequential time steps where hidden state h_t depends on h_{t-1}, preventing parallelization. A Transformer computes self-attention across all tokens simultaneously in O(1) sequential operations, enabling massive GPU parallelization.""")

# ------------------------------------------
# SLIDE 3: Evolution from LLMs to Autonomous Agents
# ------------------------------------------
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "1. Foundations & Evolution", "Evolution from Passive LLMs to Autonomous Agents", 3)

create_card(s3, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Limitations of Passive LLM Generation",
            ["Single-Turn Statelessness: The model receives an input prompt, outputs a completion, and discards state; no iterative problem solving.",
             "Absence of Environmental Grounding: LLMs cannot observe external state changes, verify intermediate calculations, or interact with databases or APIs.",
             "Unchecked Hallucination: Autoregressive decoding lacks native self-correction mechanisms; an early error compounds across subsequent tokens.",
             "Context Window Saturation: Monolithic prompts attempting to contain system instructions, examples, tools, and background saturate the attention context."],
            CARD_BG, BLUE)

create_card(s3, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "The Agentic Paradigm Shift",
            ["Reasoning & Acting Duality: Grounding cognitive thought traces with external tool actions (ReAct, Yao et al. 2023).",
             "Autonomous Execution Loops: Introducing iterative execution cycles (Sense -> Plan -> Act -> Reflect) until completion criteria are met.",
             "External Tool Integration: Invoking calculators, Python interpreters, search engines, and web APIs dynamically (Toolformer, Schick et al. 2023).",
             "Working & Episodic Memory: Maintaining dynamic scratchpads, execution logs, and vector database embeddings across multi-step tasks."],
            CARD_BG, TEAL)

set_notes(s3, """[Estimated Time: 1.0 min | Running Total: 3.0 min]
[Core Slide Narrative]
Explains the limitations of raw, single-turn LLM generation and motivates the paradigm shift toward autonomous agents with reasoning, memory, and tools.

[Verbal Script ("What to Say")]
"While frontier LLMs exhibit extraordinary general knowledge, raw foundation models are inherently passive and stateless. In a conventional API call, the model takes a prompt, generates a single completion, and terminates. It has no capacity to inspect whether its answer actually executed, no mechanism to call an external API, and no ability to correct errors mid-flight.
This led to the emergence of LLM Agents. Instead of treating the language model as an oracle that provides an immediate answer, agentic architectures treat the LLM as a central reasoning engine inside an iterative control loop. By equipping the model with memory, planning mechanisms, and external tools—such as Python execution environments or SQL databases—an agent can autonomously decompose goals, observe intermediate results, and iteratively refine its solution."

[Slide Transition]
"Let us formalize the architectural anatomy of an autonomous LLM agent."

[Anticipated Viva Questions]
Q: What distinguishes an LLM prompt from an LLM Agent?
A: An LLM prompt is a single-turn input-output mapping. An LLM agent encapsulates the model within an autonomous control loop featuring perception, planning, tool execution, working memory, and multi-step self-correction.""")

# ------------------------------------------
# SLIDE 4: What Are LLM Agents? Core Architecture
# ------------------------------------------
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "2. Agent Foundations", "Anatomy of an Autonomous LLM Agent", 4)

create_card(s4, Inches(0.8), Inches(1.4), Inches(2.7), Inches(5.4),
            "1. Cognitive Core",
            ["Foundation Model: The LLM serves as the central brain and reasoning engine.",
             "System Prompt: Defines persona, role boundaries, capabilities, and output formatting rules.",
             "In-Context Reasoning: Performs inductive, deductive, and abductive inference over inputs."],
            CARD_BG, BLUE)

create_card(s4, Inches(3.8), Inches(1.4), Inches(2.7), Inches(5.4),
            "2. Planning Engine",
            ["Task Decomposition: Breaks complex goals into manageable sub-tasks.",
             "Multi-Step Strategy: Employs CoT, Plan-and-Solve, or branching search (ToT).",
             "Self-Reflection: Evaluates previous actions and dynamically adjusts plan."],
            CARD_BG, TEAL)

create_card(s4, Inches(6.8), Inches(1.4), Inches(2.7), Inches(5.4),
            "3. Memory System",
            ["Short-Term Working Memory: In-context message history and active scratchpads.",
             "Long-Term Episodic Memory: Vector database indexing past experiences via embeddings.",
             "State Serialization: Maintains execution context across API boundaries."],
            CARD_BG, PURPLE)

create_card(s4, Inches(9.8), Inches(1.4), Inches(2.7), Inches(5.4),
            "4. Tool Integration",
            ["API Function Calling: Generates structured JSON tool calls.",
             "Execution Environment: Runs code, queries databases, and browses web.",
             "Observation Feedback: Integrates tool outputs back into context for next reasoning turn."],
            CARD_BG, NAVY)

set_notes(s4, """[Estimated Time: 1.0 min | Running Total: 4.0 min]
[Core Slide Narrative]
Deconstructs the four core subsystems that constitute a modern autonomous LLM agent: Cognitive Core, Planning, Memory, and Tool Integration.

[Verbal Script ("What to Say")]
"An autonomous agent consists of four interconnected subsystems:
First, the Cognitive Core—the foundation LLM configured with a system prompt that enforces role persona, behavioral boundaries, and reasoning style.
Second, the Planning Subsystem—responsible for goal decomposition, step sequencing, and error reflection.
Third, the Memory Subsystem—distinguished into short-term working memory within the context window, and long-term memory indexed via vector stores like ChromaDB or FAISS for retrieval-augmented context.
Fourth, the Tool Execution Subsystem—which uses function calling schemas to produce structured arguments, dispatch calls to external tools like compilers or APIs, and ingest the output observations back into the agent's context."

[Slide Transition]
"Next, let us look at the dynamic execution cycle that brings these four components together."

[Anticipated Viva Questions]
Q: How does tool invocation work in an LLM?
A: The LLM does not execute code directly; it emits a structured schema (typically JSON) containing function name and arguments. The host application intercepts the JSON, runs the actual tool, and injects the output back into the agent context as an observation token sequence.""")

# ------------------------------------------
# SLIDE 5: How LLM Agents Work: The Execution Loop
# ------------------------------------------
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "2. Agent Foundations", "How LLM Agents Work: The Execution Loop", 5)

create_card(s5, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "The Sense-Plan-Act Cycle (ReAct Paradigm)",
            ["1. Task Ingestion: Agent receives user objective p and operational constraints C.",
             "2. Thought Generation (Reasoning): Generates explicit natural language deliberation: 'Thought: I need to calculate X before proceeding.'",
             "3. Action Formulation: Generates structured tool invocation: 'Action: python_calc(query=\"...\")'.",
             "4. Observation (Perception): Host environment executes tool and returns raw result into context: 'Observation: 42.5ms'.",
             "5. Iterative Refinement: Agent inspects observation, detects errors, and refines next thought until goal is solved."],
            CARD_BG, BLUE)

create_card(s5, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Termination & Guardrail Mechanics",
            ["Stopping Conditions: Goal satisfaction markers, constraint checks, iteration ceilings (K <= 20).",
             "Failure Traps: Infinite reasoning loops, hallucinatory tool calls, context window drift.",
             "Engineering Guardrails: Circuit breakers, schema validators, exponential retry backoff."],
            CARD_BG, ACCENT_RED)

set_notes(s5, """[Estimated Time: 1.0 min | Running Total: 5.0 min]
[Core Slide Narrative]
Explains the ReAct (Reasoning + Acting) execution cycle and highlights essential runtime guardrails to prevent non-terminating loops and hallucinated actions.

[Verbal Script ("What to Say")]
"The standard operational loop of an agent follows the ReAct framework established by Yao et al. in 2023. Rather than outputting an answer directly, the agent alternates between generating 'Thoughts'—internal deliberative tokens—and 'Actions'—external tool calls. Upon receiving the observation from the tool execution, the agent synthesizes the new evidence, updates its internal hypothesis, and decides the next step.
Crucially, production agents require strict termination mechanics. If an agent encounters an unhandled exception or an edge case, it can fall into an infinite loop, endlessly re-attempting failed queries and draining API budgets. In our framework, we enforce explicit step bounds, timeout budgets, and JSON schema validators."

[Slide Transition]
"Now, what happens when a task becomes too complex for a single agent to handle? This brings us to Multi-Agent Systems."

[Anticipated Viva Questions]
Q: What is the main vulnerability of the ReAct execution loop?
A: Cascading hallucination and infinite looping. If an observation does not match the model's expectations, it may repeatedly generate identical invalid actions unless circuit-breaker guardrails are enforced.""")

# ------------------------------------------
# SLIDE 6: Single-Agent vs. Multi-Agent Systems
# ------------------------------------------
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "3. Multi-Agent Paradigm", "Single-Agent vs. Multi-Agent Systems", 6)

create_card(s6, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Single-Agent Systems",
            ["Monolithic Cognitive Load: A single agent must parse requirements, plan, execute, audit, and format solutions simultaneously.",
             "Context Crowding: Stacking multiple complex system instructions, guidelines, and tool schemas causes context confusion and instruction omission.",
             "Uncorrected Bias & Blindspots: A single model tends to confirm its own hallucinations; self-refinement without external critique frequently fails.",
             "Efficiency Advantage: Zero communication serialization overhead, lowest token consumption, and minimal wall-clock latency."],
            CARD_BG, BLUE)

create_card(s6, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Multi-Agent Systems (MAS)",
            ["Persona Specialization: Decomposes cognitive duties across distinct expert personas (e.g. Planner, Researcher, Analyst, Critic, Finalizer).",
             "Peer Review & Dialectic Critique: Independent Critic agents inspect drafts, catching subtle logical fallacies and constraint violations.",
             "Modular Extensibility: Individual agents can be updated, swapped, or routed to different specialized model backends.",
             "Coordination Overhead Penalty: Substantial token inflation from message serialization, accumulated latency, and potential communication deadlocks."],
            CARD_BG, TEAL)

set_notes(s6, """[Estimated Time: 1.0 min | Running Total: 6.0 min]
[Core Slide Narrative]
Contrasts the monolithic single-agent architecture with multi-agent systems, balancing persona specialization against coordination overhead.

[Verbal Script ("What to Say")]
"When tackling complex industrial tasks—such as migrating a legacy monolith or conducting a medical compliance audit—a single agent faces cognitive overload. Trying to instruct a single prompt to simultaneously act as a software architect, security auditor, and financial analyst leads to 'context crowding', where the LLM drops subtle negative constraints.
Multi-Agent Systems solve this by distributing cognitive labor across specialized roles—such as MetaGPT's Standard Operating Procedures or AutoGen's conversational dialogues. A Planner decomposes the task, a Researcher retrieves context, an Analyst formulates the architecture, a Critic reviews compliance, and a Finalizer synthesizes the report. 
However, this specialization comes at a steep engineering cost: inter-agent communication inflates token usage and introduces multiple points of failure."

[Slide Transition]
"This brings us to the core technical question: How should these agents be connected? Why does interaction topology matter?"

[Anticipated Viva Questions]
Q: Does a multi-agent system always outperform a single agent?
A: No. In our empirical results, if the task fits comfortably within a modern LLM's context window, a single agent baseline often achieves higher constraint adherence at one-fifteenth the cost and one-seventh the latency.""")

# ------------------------------------------
# SLIDE 7: Why Multi-Agent Topology Matters
# ------------------------------------------
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "3. Multi-Agent Paradigm", "Why Agent Interaction Topology Matters", 7)

create_card(s7, Inches(0.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "1. Communication Topologies",
            ["Definition: The directed graph G = (V, E) defining which agents can exchange messages and in what order.",
             "Structural Diversity:\n• Linear Pipeline (Chain)\n• Centralized Hub (Star)\n• Hierarchical Tree (Tree)\n• Fully Connected Mesh (Graph)",
             "Decisive Impact: Topology determines information diffusion, context accumulation, and bottleneck locations."],
            CARD_BG, BLUE)

create_card(s7, Inches(4.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "2. Latency & Token Footprint",
            ["Sequential Hops: In a linear chain, wall-clock latency is strictly additive across stages: L = sum(L_i).",
             "Context Window Bloat: Aggregator nodes in Star or Tree topologies must ingest transcripts from all subordinates, leading to token explosion.",
             "Message Serialization: Every inter-agent dialogue hop requires formatting, JSON serialization, and API request-response round-trips."],
            CARD_BG, PURPLE)

create_card(s7, Inches(8.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "3. Cascading Failure Dynamics",
            ["Pipeline Fragility: If an upstream agent drops a constraint, downstream agents inherit the flaw, leading to cascading failure.",
             "Coordinator Bottlenecks: A central manager can misroute sub-tasks, corrupting parallel worker threads.",
             "Deadlock Risks: Cyclic communication in mesh networks risks non-terminating ping-pong debates.",
             "Need for Benchmarking: No prior benchmark rigorously isolated topology under controlled tasks."],
            CARD_BG, ACCENT_RED)

set_notes(s7, """[Estimated Time: 1.0 min | Running Total: 7.0 min]
[Core Slide Narrative]
Demonstrates why communication topology is the decisive design parameter governing latency, token consumption, and cascading fault propagation.

[Verbal Script ("What to Say")]
"The interaction topology—the directed graph G = (V, E) defining the communication pathways between agents—is arguably the most critical architectural decision in multi-agent engineering. 
If you choose a linear chain, your execution is strictly sequential: each stage must wait for the preceding agent to finish, compounding latency. If you choose a centralized star, your central coordinator becomes a token bottleneck as all subordinate messages converge upon it. If you choose an open mesh graph, you invite circular debate loops and runaway financial costs.
Furthermore, topologies exhibit starkly different failure modes. In sequential pipelines, an error in stage 1 propagates downstream uncorrected. Despite these profound implications, existing research lacked a controlled benchmark to evaluate these topologies head-to-head."

[Slide Transition]
"This brings us directly to our formal Problem Statement."

[Anticipated Viva Questions]
Q: Can you define communication topology formally?
A: Formally, an interaction topology is a directed graph G = (V, E, R), where V is the set of agent nodes, E is the set of directed communication edges, and R represents the specialized functional role assigned to each node.""")

# ------------------------------------------
# SLIDE 8: Problem Statement
# ------------------------------------------
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "4. Research Problem", "Problem Statement & Contemporary Challenges", 8)

create_card(s8, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Existing Evaluation Blindspots",
            ["1. Task-Success Myopia: Most agent benchmarks measure only a binary success flag (True/False), ignoring whether strict numerical constraints were satisfied.",
             "2. Resource Telemetry Deficit: Total token counts are rarely decoupled into prompt vs. completion tokens, obscuring where token waste occurs.",
             "3. Latency Ignorance: End-to-end wall-clock latency and API turn serialization bottlenecks are systematically ignored.",
             "4. Runtime Fault Invisibility: Lack of categorization for HTTP 429 rate limits, request timeouts, JSON parse exceptions, and loop deadlocks."],
            CARD_BG, ACCENT_RED)

create_card(s8, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Formal Problem Formulation",
            ["Given:\n• A set of complex technical tasks T = <p, C, P, y*>\n• A foundation model provider M with parameters theta\n• Five canonical interaction topologies G in {Single, Chain, Star, Tree, Graph}\n\nObjective:\nScientifically isolate, measure, and analyze the empirical trade-offs across:\n• Task Score S and Constraint Satisfaction Rate (CSR)\n• Wall-Clock Latency L and API Call Multipliers\n• Decoupled Token Usage (T_prompt, T_comp) & Financial Cost C_USD\n• Operational Failure Taxonomy FR under controlled conditions."],
            CARD_BG, BLUE)

set_notes(s8, """[Estimated Time: 1.0 min | Running Total: 8.0 min]
[Core Slide Narrative]
Articulates the formal problem statement, exposing the limitations of existing binary benchmarks and defining our multi-dimensional evaluation objective.

[Verbal Script ("What to Say")]
"Let us define the core problem. Contemporary LLM benchmarks suffer from 'task-success myopia'. They evaluate an agent based on a simple binary pass/fail check. However, in enterprise deployment, an agent that solves a task in 5 seconds with 1,000 tokens is vastly superior to a multi-agent system that takes 50 seconds, consumes 18,000 tokens, costs 15 times more, and violates two subtle budgetary constraints while producing a verbose answer.
Our formal problem statement is therefore formulated as follows: Given a standardized task suite with explicit constraints, and an identical foundation model backend, we systematically isolate and evaluate five canonical topologies—Single, Chain, Star, Tree, and Graph—across task score, constraint satisfaction, decoupled prompt and completion tokens, real-time cost, wall-clock latency, and runtime failure taxonomies."

[Slide Transition]
"To investigate this problem systematically, we formulated five research questions and four testable hypotheses."

[Anticipated Viva Questions]
Q: Why is separating prompt tokens from completion tokens important?
A: In cloud LLMs, prompt and completion tokens have different pricing tiers (completion is typically 2x to 4x more expensive). Furthermore, prompt token growth indicates context accumulation across hops, while completion token growth reflects agent verbosity.""")

# ------------------------------------------
# SLIDE 9: Research Questions & Hypotheses
# ------------------------------------------
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "4. Research Problem", "Research Questions (RQ1–RQ5) and Hypotheses (H1–H4)", 9)

create_card(s9, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Research Questions (RQs)",
            ["RQ1 (Task Quality): How does interaction topology impact overall task score and strict constraint satisfaction?",
             "RQ2 (Resource Scaling): What is the quantitative amplification factor of prompt and completion tokens across topologies?",
             "RQ3 (Latency Bottlenecks): How severely does sequential communication serialize execution and inflate wall-clock latency?",
             "RQ4 (Fault Vulnerability): Which topologies are vulnerable to cascading failure propagation and API rate-limit stalls?",
             "RQ5 (Efficiency Frontier): Under what task complexity conditions does multi-agent coordination justify its operational overhead?"],
            CARD_BG, BLUE)

create_card(s9, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Testable Hypotheses (H1–H4)",
            ["H1 (Resource Overhead Scaling): Multi-agent topologies will exhibit super-linear token amplification (>5x) and latency inflation compared to Single baseline.",
             "H2 (Linear Pipeline Fragility): The Chain topology will suffer from cascading error propagation, resulting in lower success rates on multi-constraint tasks.",
             "H3 (Hierarchical Resilience): Centralized (Star) and hierarchical (Tree) topologies will demonstrate superior constraint adherence due to explicit aggregation sinks.",
             "H4 (Baseline Efficiency Paradox): On tasks fitting within context bounds, the Single agent baseline will match or exceed multi-agent quality at a fraction of the cost."],
            CARD_BG, TEAL)

set_notes(s9, """[Estimated Time: 1.0 min | Running Total: 9.0 min]
[Core Slide Narrative]
Details the five guiding Research Questions and the four testable Hypotheses that drove our experimental benchmark design.

[Verbal Script ("What to Say")]
"We established five formal Research Questions. RQ1 assesses task quality and constraint adherence. RQ2 measures the precise scaling of tokens and financial cost. RQ3 investigates wall-clock latency. RQ4 categorizes runtime failure modes. RQ5 seeks the Pareto efficiency frontier.
From these, we formulated four testable hypotheses. H1 posits super-linear token and latency overhead. H2 hypothesizes that sequential Chain pipelines will be fragile due to error cascading. H3 predicts that centralized Star and Tree architectures will resist failure via aggregation nodes. And H4—our most provocative hypothesis—posits the 'Baseline Efficiency Paradox': that for tasks fitting within modern context windows, a single-agent baseline will rival or outperform multi-agent architectures at far lower cost."

[Slide Transition]
"Now, let us examine the existing academic literature and see how prior research approached this domain."

[Anticipated Viva Questions]
Q: Were your hypotheses confirmed by the experimental results?
A: Yes, all four hypotheses were strongly corroborated: H1 saw 10x-15x token scaling; H2 saw Chain drop to 71.4% success; H3 saw Star and Tree achieve 100% success; and H4 was validated as Single achieved the highest overall score (0.9429) at 1/15th the cost.""")

# ------------------------------------------
# SLIDE 10: Literature Review: Foundational Evolution
# ------------------------------------------
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "5. Literature Review", "Literature Review: Foundations & Deliberative Prompting", 10)

create_card(s10, Inches(0.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "1. Foundational Architectures",
            ["Vaswani et al. (NeurIPS 2017): Transformer self-attention foundation.",
             "Devlin et al. (NAACL 2019): BERT bidirectional masked representations.",
             "Raffel et al. (JMLR 2020): T5 unified text-to-text sequence modeling.",
             "Brown et al. (NeurIPS 2020): Few-shot in-context learning in GPT-3.",
             "Touvron et al. (2023): Open-weights foundation models with LLaMA."],
            CARD_BG, BLUE)

create_card(s10, Inches(4.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "2. Deliberative Reasoning",
            ["Wei et al. (NeurIPS 2022): Chain-of-Thought (CoT) prompting eliciting intermediate reasoning steps.",
             "Kojima et al. (NeurIPS 2022): Zero-shot CoT ('Let's think step by step').",
             "Yao et al. (NeurIPS 2023): Tree of Thoughts (ToT) enabling deliberate state space exploration and backtracking.",
             "Besta et al. (AAAI 2024): Graph of Thoughts (GoT) generalizing thought graphs."],
            CARD_BG, TEAL)

create_card(s10, Inches(8.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "3. Self-Refinement & Verification",
            ["Shinn et al. (NeurIPS 2023): Reflexion using verbal reinforcement feedback.",
             "Madaan et al. (NeurIPS 2023): Self-Refine iteratively auditing and correcting outputs.",
             "Gou et al. (ICLR 2024): CRITIC conditioning self-refinement on external tool feedback.",
             "Du et al. (ICML 2024): Multi-agent debate reducing individual hallucinations."],
            CARD_BG, NAVY)

set_notes(s10, """[Estimated Time: 1.0 min | Running Total: 10.0 min]
[Core Slide Narrative]
Summarizes foundational papers in the literature review covering Transformer origins, in-context learning, deliberate reasoning search, and self-refinement loops.

[Verbal Script ("What to Say")]
"Our literature review traces 44 peer-reviewed academic papers across three major phases. 
Phase 1 established architectural foundations: Vaswani's Transformer, Devlin's BERT, and Brown's demonstration of few-shot emergent learning in GPT-3.
Phase 2 introduced single-agent deliberative reasoning. Wei et al. demonstrated in 2022 that forcing the model to generate intermediate Chain-of-Thought tokens unlocks multi-step arithmetic and symbolic reasoning. Yao et al. with Tree of Thoughts and Besta et al. with Graph of Thoughts generalized this from linear sequences to branching graph state search.
Phase 3 introduced self-refinement: Shinn's Reflexion and Madaan's Self-Refine showed that asking an LLM to critique its own past outputs can eliminate obvious mistakes. However, single models frequently suffer from blindspots, motivating multi-agent debate protocols."

[Slide Transition]
"Let us now look at the landmark 2025 ACL paper in this field: MultiAgentBench by Zhu et al."

[Anticipated Viva Questions]
Q: What is the fundamental difference between Tree of Thoughts (ToT) and Multi-Agent Systems?
A: Tree of Thoughts is a single-agent search heuristic that explores branches of thought tokens using BFS or DFS. Multi-Agent Systems distribute cognitive tasks across distinct specialized personas that communicate via message passing.""")

# ------------------------------------------
# SLIDE 11: Foundation Paper: MultiAgentBench (ACL 2025)
# ------------------------------------------
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, "5. Literature Review", "Landmark Benchmark: MultiAgentBench (Zhu et al., ACL 2025)", 11)

create_card(s11, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "The MARBLE Coordination Framework",
            ["Authors & Venue: Kunlun Zhu, Hongyi Du, Zhaochen Hong et al., ACL 2025.",
             "Core Innovation: First comprehensive benchmark for collaborative and competitive LLM multi-agent systems.",
             "MARBLE Coordination Engine: Orchestrates multi-agent execution via:\n• Agent Graph G = (V, E) defining message routes\n• Turn-taking coordination engine\n• Shared environment memory & state updates",
             "Diverse Environments: Evaluated across Research, Software Engineering, Werewolf, Bargaining, and Minecraft."],
            CARD_BG, BLUE)

create_card(s11, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "MultiAgentBench Evaluation Dimensions",
            ["Milestone-Based KPIs: Tracks task completion by checking whether predefined environment milestones were unlocked.",
             "Coordination Metrics: Computes task-specific coordination and competition scores.",
             "MAST Profiling: Behavioral profiling across cooperation, communication, and strategy.",
             "Boundaries & Limitations:\n• Heavy reliance on complex game simulators and digital sandboxes.\n• High compute/setup barrier for academic reproduction.\n• Did not isolate communication topology as an independent controlled variable."],
            CARD_BG, TEAL)

set_notes(s11, """[Estimated Time: 1.0 min | Running Total: 11.0 min]
[Core Slide Narrative]
Analyzes the landmark ACL 2025 paper 'MultiAgentBench' by Zhu et al., detailing its MARBLE coordination architecture, strengths, and operational boundaries.

[Verbal Script ("What to Say")]
"The most significant recent milestone in this research area is the paper titled 'MultiAgentBench: Evaluating Collaboration and Competition of LLM Agents', published by Zhu et al. in ACL 2025.
Zhu et al. introduced MARBLE, a coordination framework that evaluates agents across both collaborative environments—like multi-agent coding and research—and competitive environments—such as Werewolf social deduction and bargaining games. They evaluated systems using milestone-based KPIs and behavioral interaction profiles.
However, MultiAgentBench has clear boundaries. Its environments are computationally heavy simulation engines (e.g., Minecraft and complex games). Most importantly, MultiAgentBench did not systematically isolate interaction topology as an independent controlled variable across standardized engineering tasks."

[Slide Transition]
"This brings us to how our work, MultiAgentTopologyEval, positions itself relative to MultiAgentBench."

[Anticipated Viva Questions]
Q: Are you copying or reproducing MultiAgentBench?
A: No. We cite Zhu et al. as the foundational benchmark inspiration. Our framework, MultiAgentTopologyEval, addresses complementary operational dimensions: strictly isolating five canonical topologies, tracking decoupled token and latency telemetry, and profiling systems-level runtime failures in a lightweight, 100% reproducible testbed.""")

# ------------------------------------------
# SLIDE 12: Research Gap & Scope Differentiation
# ------------------------------------------
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, "5. Literature Review", "Research Gap & Comparative Benchmark Synthesis", 12)

create_card(s12, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Identified Research Gaps",
            ["Gap 1: Absence of Topology Isolation: Existing works confound agent count, prompts, and topologies without controlled baseline comparisons.",
             "Gap 2: Decoupled Token & Cost Telemetry Deficit: Failure to separate prompt token inflation from completion token volume in multi-hop systems.",
             "Gap 3: Step-Level Latency Blindness: Lack of empirical profiling of wall-clock serialization delay across sequential vs. parallel topologies.",
             "Gap 4: Superficial Constraint Validation: Relying on binary success rather than rigorous mathematical constraint satisfaction.",
             "Gap 5: Runtime Failure Invisibility: Neglect of API rate-limit errors, request timeouts, and malformed schema exceptions."],
            CARD_BG, ACCENT_RED)

create_card(s12, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Benchmark Comparison Matrix",
            ["AgentBench (Liu 2024): Single-agent focus; coarse token tracking; no topology isolation.",
             "SWE-bench (Jimenez 2024): Monolithic software issue solver; unit test validation; no topology comparison.",
             "AgentVerse (Chen 2024): Group discussion focus; partial topology evaluation; game-centric.",
             "MultiAgentBench (Zhu 2025 ACL): Simulation/game environments; milestone KPIs; heavy simulator dependency.",
             "MultiAgentTopologyEval (Our Work):\n• Controlled isolation of 5 canonical topologies\n• Decoupled prompt/completion token & USD cost telemetry\n• Strict deterministic Constraint Satisfaction Rates (CSR)\n• Comprehensive runtime fault & loop taxonomy\n• 100% reproducible, zero-cost offline mock engine."],
            CARD_BG, BLUE)

set_notes(s12, """[Estimated Time: 1.0 min | Running Total: 12.0 min]
[Core Slide Narrative]
Summarizes the systematic comparative synthesis across major benchmarks, defining our explicit niche: controlled topology isolation with fine-grained operational profiling.

[Verbal Script ("What to Say")]
"Here we see the research gap crystallized in our comparative synthesis. Previous benchmarks like AgentBench and SWE-bench focused exclusively on single agents. While AgentVerse and MultiAgentBench pioneered multi-agent evaluation, they bound execution to complex simulation games and macro milestone completion.
MultiAgentTopologyEval establishes a complementary, engineering-focused evaluation bed. We isolate the topology variable—keeping prompts, models, and budgets strictly identical. We instrument decoupled token telemetry, step-level latency profiling, strict mathematical constraint satisfaction, and an operational fault taxonomy. Furthermore, we provide a zero-cost, deterministic mock engine that enables 100% reproducible regression testing without spending cloud API credits."

[Slide Transition]
"Let us now examine the architectural design of the proposed MultiAgentTopologyEval framework."

[Anticipated Viva Questions]
Q: Why is a zero-cost mock engine academically valuable?
A: LLM cloud APIs are non-deterministic, subject to rate limits, and incur financial costs. A deterministic mock provider enables instant, reproducible regression testing, verifying pipeline logic, metrics, and error handlers without variance or expense.""")

# ------------------------------------------
# SLIDE 13: Proposed Framework Architecture
# ------------------------------------------
s13 = prs.slides.add_slide(blank_layout)
add_header(s13, "6. Proposed Framework", "MultiAgentTopologyEval: System Architecture Overview", 13)

create_card(s13, Inches(0.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "1. Ingestion & Orchestration",
            ["Subsystem 1: Benchmark Loader & Anti-Leakage Sanitizer\n• Ingests 35 curated tasks\n• Strips ground-truth reference answers and expected properties from agent prompts.",
             "Subsystem 2: Topology Orchestration Hub\n• Instantiates Single, Chain, Star, Tree, or Graph solver classes.",
             "Subsystem 3: Agent Core\n• BaseAgent abstraction managing state, queues, and execution logs."],
            CARD_BG, BLUE)

create_card(s13, Inches(4.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "2. Execution & Safety",
            ["Subsystem 4: Universal Model Provider Layer\n• Unified adapter supporting Google Gemini 3.1, Cohere Command, Groq Llama-3.3, and Mock engine.",
             "Subsystem 5: Guardrails & Fault Engine\n• Step limit breaker (K <= 20)\n• Financial cost ceiling ($0.50/run)\n• Exponential backoff & retry\n• Runtime failure taxonomy logger (HTTP 429, timeouts, schema errors)."],
            CARD_BG, TEAL)

create_card(s13, Inches(8.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "3. Evaluation & Reporting",
            ["Subsystem 6: Hybrid Evaluation Engine\n• Deterministic regular expression constraint verifier\n• Architectural property matching (PMR)\n• Optional LLM-as-a-Judge semantic auditor.",
             "Statistical Analytics:\n• Computes Cohen's d effect sizes\n• Aggregates JSON traces and summary CSV matrices.",
             "Interactive Research Dashboard:\n• Streamlit GUI for live inspection."],
            CARD_BG, NAVY)

set_notes(s13, """[Estimated Time: 1.0 min | Running Total: 13.0 min]
[Core Slide Narrative]
Presents the six decoupled subsystems of the MultiAgentTopologyEval framework, explaining the separation of concerns across ingestion, execution, safety, and evaluation.

[Verbal Script ("What to Say")]
"The MultiAgentTopologyEval framework is organized into six decoupled subsystems.
Subsystem 1 handles task ingestion and enforces anti-leakage isolation by stripping ground-truth answers from agent prompts.
Subsystem 2 is the Topology Orchestration Hub, which instantiates the five architecture solvers.
Subsystem 3 encapsulates the specialized agent core—providing Planner, Researcher, Analyst, Critic, and Finalizer agents.
Subsystem 4 is our Universal Provider Layer, allowing identical execution across Gemini, Cohere, Groq, and Mock engines.
Subsystem 5 provides operational safety guardrails, enforcing step limits, cost caps, and logging system-level faults.
Finally, Subsystem 6 is the Hybrid Evaluation Pipeline, which audits outputs using deterministic regex rules, property matching, and statistical effect size calculations."

[Slide Transition]
"Let us view the complete end-to-end architectural diagram illustrating how these subsystems interact."

[Anticipated Viva Questions]
Q: How does the framework ensure that agents do not cheat by seeing the answer?
A: Through anti-leakage quarantine in Subsystem 1: TaskDefinition.to_agent_prompt_dict() strips reference_answer and expected_properties. Only the prompt and constraints are dispatched to the agents; the ground truth is passed exclusively to the evaluator.""")

# ------------------------------------------
# SLIDE 14: System Architecture Diagram Slide
# ------------------------------------------
s14 = prs.slides.add_slide(blank_layout)
add_header(s14, "6. Proposed Framework", "Detailed System Architecture & Data Flow", 14)

sys_img_path = os.path.join(FIG_DIR, "system_architecture.png")
if os.path.exists(sys_img_path):
    s14.shapes.add_picture(sys_img_path, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.2))

set_notes(s14, """[Estimated Time: 1.0 min | Running Total: 14.0 min]
[Core Slide Narrative]
Walks through the high-resolution system architecture diagram, highlighting data flow, provider interaction, and anti-leakage quarantine.

[Verbal Script ("What to Say")]
"This diagram illustrates the complete end-to-end data flow. On the left, benchmark tasks containing prompts and operational constraints are ingested. Notice the orange dashed line at the bottom: this represents our strict anti-leakage quarantine. The ground-truth reference answers bypass the topology execution engine entirely and are delivered directly to the downstream evaluation engine.
In the center, the selected topology orchestrates the role-specialized agents. Each agent calls the universal LLM provider adapter, while the guardrail tracker monitors token accumulation, costs, and API status codes in real time. 
Upon task termination, the synthesized response, wall-clock latency, token usage, and inter-agent message traces are transmitted to the Hybrid Evaluator, which computes objective constraint scores and logs telemetry to disk."

[Slide Transition]
"Now let us examine each of the five canonical topologies in detail, beginning with our baseline control: the Single Agent."

[Anticipated Viva Questions]
Q: Why is the guardrail tracker placed between the agent core and the provider layer?
A: By intercepting every LLM call before execution, the guardrail tracker can enforce budget caps, prevent runaway loops, and inject exponential backoff retries when encountering HTTP 429 rate limits.""")

# ------------------------------------------
# SLIDE 15: SINGLE Topology: Baseline Control
# ------------------------------------------
s15 = prs.slides.add_slide(blank_layout)
add_header(s15, "7. Multi-Agent Topologies", "SINGLE Architecture: Baseline Control", 15)

single_img_path = os.path.join(FIG_DIR, "single_topology.png")
if os.path.exists(single_img_path):
    s15.shapes.add_picture(single_img_path, Inches(0.8), Inches(1.4), Inches(7.2), Inches(5.4))

create_card(s15, Inches(8.3), Inches(1.4), Inches(4.2), Inches(5.4),
            "SINGLE Architecture Specs",
            ["Mathematical Formulation:\ny_hat = M(p, C; theta)\n\n• Single Agent Node (a_single)\n• Execution Style: Isolated 1-turn direct prompt inference\n• Inter-Agent Edges: |E| = 0\n• API Calls: Exactly 1 per task\n\nKey Strengths:\n• Zero inter-agent serialization delay\n• Lowest execution latency (6.32s avg)\n• Lowest token consumption (~1.1k tokens)\n• Extremely cost effective ($0.00017/task)\n\nInherent Vulnerabilities:\n• No peer review or critique loop\n• Prone to uncorrected hallucination\n• Context crowding on high-constraint prompts."],
            CARD_BG, BLUE)

set_notes(s15, """[Estimated Time: 1.0 min | Running Total: 15.0 min]
[Core Slide Narrative]
Explains the Single Agent architecture, its mathematical formalization, its operational characteristics, and its role as the baseline control.

[Verbal Script ("What to Say")]
"The first topology is the SINGLE architecture, which acts as our baseline control. Here, a solitary agent receives the user prompt and constraints and generates the complete solution in an isolated single turn: y_hat = M(p, C).
Because there are zero inter-agent communication channels (|E| = 0), this architecture completely avoids message passing, serialization overhead, and intermediate state parsing. In our empirical pilot on Gemini 3.1 Flash-Lite, it achieved an average execution latency of just 6.32 seconds and consumed only 1,121 tokens, costing less than two ten-thousandths of a dollar per task.
However, its vulnerability is that it operates without peer review. If the model hallucinates or overlooks a constraint during generation, there is no second agent to catch the flaw."

[Slide Transition]
"Next, let us look at the most common industrial multi-agent workflow: the sequential linear Chain."

[Anticipated Viva Questions]
Q: Why is Single included in a multi-agent evaluation framework?
A: In scientific benchmarking, a baseline control is mandatory. Without a single-agent baseline, one cannot prove whether multi-agent coordination actually adds value or merely inflates cost and latency.""")

# ------------------------------------------
# SLIDE 16: CHAIN Topology: Sequential Linear Pipeline
# ------------------------------------------
s16 = prs.slides.add_slide(blank_layout)
add_header(s16, "7. Multi-Agent Topologies", "CHAIN Architecture: Sequential Linear Pipeline", 16)

chain_img_path = os.path.join(FIG_DIR, "chain_topology.png")
if os.path.exists(chain_img_path):
    s16.shapes.add_picture(chain_img_path, Inches(0.8), Inches(1.4), Inches(7.2), Inches(5.4))

create_card(s16, Inches(8.3), Inches(1.4), Inches(4.2), Inches(5.4),
            "CHAIN Architecture Specs",
            ["Mathematical Formulation:\nm_i = a_i(p, m_{i-1}; M),  for i in {1..n}\ny_hat = m_n\n\n• Linear Pipeline Sequence:\nPlanner -> Researcher -> Analyst -> Critic -> Finalizer\n• Inter-Agent Edges: |E| = n - 1 = 4 edges\n• Sequential Handoffs: 5 API turns\n\nKey Strengths:\n• Clear functional stage boundaries\n• Mirrors industrial SOPs (MetaGPT)\n• Progressive refinement across roles\n\nCritical Vulnerabilities:\n• Strictly additive latency: L = sum(L_i) (42.2s)\n• Cascading Error Propagation: An uncorrected upstream error cascades to the end\n• Dropped to 71.4% success in pilot runs."],
            CARD_BG, ACCENT_RED)

set_notes(s16, """[Estimated Time: 1.0 min | Running Total: 16.0 min]
[Core Slide Narrative]
Explains the sequential Chain topology, its alignment with industrial Standard Operating Procedures, and its critical vulnerability to cascading failure propagation.

[Verbal Script ("What to Say")]
"The CHAIN topology organizes agents into a strictly linear pipeline: Planner to Researcher, to Analyst, to Critic, to Finalizer. This directly reflects industrial Standard Operating Procedure frameworks, such as MetaGPT.
At each stage, agent a_i receives the original prompt and the output of the preceding agent m_{i-1}, producing message m_i.
While conceptually intuitive, our experiments revealed that Chain is the most fragile multi-agent topology. Because communication is strictly forward-flowing with no backward feedback loops, any mistake or constraint omission in an early stage cascades downstream. In our pilot benchmark, Chain was the ONLY topology that failed tasks, dropping to a 71.4% success rate, while its latency jumped to 42.2 seconds due to sequential turn serialization."

[Slide Transition]
"To avoid sequential fragility, many architectures adopt centralized delegation. Let us look at the STAR topology."

[Anticipated Viva Questions]
Q: Why did Chain drop to 71.4% success while Single achieved 100%?
A: In tasks with multiple quantitative constraints, intermediate agents paraphrased the problem, inadvertently dropping constraints like sub-second latency bounds. Downstream agents optimized the paraphrased draft, resulting in cascading constraint failure.""")

# ------------------------------------------
# SLIDE 17: STAR Topology: Centralized Hub-and-Spoke
# ------------------------------------------
s17 = prs.slides.add_slide(blank_layout)
add_header(s17, "7. Multi-Agent Topologies", "STAR Architecture: Centralized Hub-and-Spoke", 17)

star_img_path = os.path.join(FIG_DIR, "star_topology.png")
if os.path.exists(star_img_path):
    s17.shapes.add_picture(star_img_path, Inches(0.8), Inches(1.4), Inches(7.2), Inches(5.4))

create_card(s17, Inches(8.3), Inches(1.4), Inches(4.2), Inches(5.4),
            "STAR Architecture Specs",
            ["Mathematical Formulation:\nm_{work,i} = a_i(m_{coord,i}; M)\ny_hat = a_{final}(Union_{i=1}^k m_{work,i}; M)\n\n• Hub-and-Spoke Organization:\nCentral Coordinator delegates sub-tasks to Researcher, Analyst, Critic; Finalizer aggregates.\n• Edges: Hub-to-Worker & Worker-to-Sink\n• API Invocations: 5 calls\n\nKey Strengths:\n• Strong centralized oversight\n• Eliminates uncoordinated worker chatter\n• Highly resilient: 100% success in pilot\n\nCritical Limitations:\n• Massive Token Explosion: Accumulates 17,174 tokens (15.3x vs Single)\n• Coordinator Context Bottleneck: Hub must ingest all worker transcripts."],
            CARD_BG, BLUE)

set_notes(s17, """[Estimated Time: 1.0 min | Running Total: 17.0 min]
[Core Slide Narrative]
Presents the Star topology, emphasizing centralized task delegation, high execution robustness, and the resulting coordinator token accumulation bottleneck.

[Verbal Script ("What to Say")]
"The STAR topology deploys a centralized Coordinator/Manager node surrounded by specialized satellite workers—Researcher, Analyst, and Critic—with outputs aggregated into a Finalizer sink.
The coordinator decomposes the objective, delegates targeted sub-prompts, gathers worker findings, and synthesizes the authoritative answer.
The major advantage of Star is its robustness: by eliminating uncoordinated chatter and maintaining strong central control, Star achieved a 100% success rate on the pilot benchmark.
However, its critical limitation is token explosion. Because all intermediate findings converge upon the coordinator and finalizer, Star consumed 17,174 tokens per task—a 15.3-fold increase over the single agent—making it the most token-intensive architecture evaluated."

[Slide Transition]
"To scale task delegation without bottlenecking a single central node, organizations use hierarchies. Let us look at the TREE topology."

[Anticipated Viva Questions]
Q: Why did Star consume more tokens than Tree and Graph?
A: In Star, the central coordinator and the finalizer sink accumulate full conversational history from all satellite workers, resulting in massive prompt token duplication during the aggregation turn.""")

# ------------------------------------------
# SLIDE 18: TREE Topology: Multi-Tier Hierarchical
# ------------------------------------------
s18 = prs.slides.add_slide(blank_layout)
add_header(s18, "7. Multi-Agent Topologies", "TREE Architecture: Multi-Tier Hierarchical", 18)

tree_img_path = os.path.join(FIG_DIR, "tree_topology.png")
if os.path.exists(tree_img_path):
    s18.shapes.add_picture(tree_img_path, Inches(0.8), Inches(1.4), Inches(7.2), Inches(5.4))

create_card(s18, Inches(8.3), Inches(1.4), Inches(4.2), Inches(5.4),
            "TREE Architecture Specs",
            ["Mathematical Formulation:\nV_tree = {a_root} U V_leads U V_workers U {a_final}\n\n• Multi-Tier Organization:\n• Tier 1: Root Coordinator\n• Tier 2: Research Lead & Analysis Lead\n• Tier 3: Research Worker & Critic Worker\n• Tier 4: Bottom-Up Finalizer Sink\n• API Invocations: 6 calls\n\nKey Strengths:\n• Scalable division of labor across branches\n• Localized sub-task context boundaries\n• 100% success rate in pilot evaluations\n\nCritical Limitations:\n• Highest Wall Latency: 47.38s average due to multi-tier depth traversal\n• Aggregation complexity at final sink."],
            CARD_BG, PURPLE)

set_notes(s18, """[Estimated Time: 1.0 min | Running Total: 18.0 min]
[Core Slide Narrative]
Explains the multi-tier Tree hierarchy, localized branch delegation, bottom-up aggregation, and latency accumulation across hierarchical depth.

[Verbal Script ("What to Say")]
"The TREE topology models a corporate multi-tier hierarchy. At Tier 1, a Root Coordinator decomposes the high-level objective into two operational branches: a Research branch and an Analysis branch. At Tier 2, intermediate branch leads supervise leaf execution workers at Tier 3. Finally, at Tier 4, worker syntheses are aggregated bottom-up into a Finalizer sink.
Tree structures provide clean localization: research workers don't see analysis chatter, keeping context concise. In our pilot, Tree achieved 100% success with 12,789 tokens.
However, because execution must traverse down the tree and then aggregate back up, Tree incurred the highest execution latency of all architectures—averaging 47.38 seconds per task across six API invocations."

[Slide Transition]
"Finally, let us examine the most flexible coordination architecture: the configurable GRAPH mesh."

[Anticipated Viva Questions]
Q: Why is Tree useful if it has the highest latency?
A: For extremely large, multi-faceted engineering projects where sub-tasks have disjoint domains (e.g., front-end UI vs. database indexing), localized branch hierarchy prevents context cross-contamination.""")

# ------------------------------------------
# SLIDE 19: GRAPH Topology: Peer-to-Peer Diamond Mesh
# ------------------------------------------
s19 = prs.slides.add_slide(blank_layout)
add_header(s19, "7. Multi-Agent Topologies", "GRAPH Architecture: Peer-to-Peer Diamond Mesh", 19)

graph_img_path = os.path.join(FIG_DIR, "graph_topology.png")
if os.path.exists(graph_img_path):
    s19.shapes.add_picture(graph_img_path, Inches(0.8), Inches(1.4), Inches(7.2), Inches(5.4))

create_card(s19, Inches(8.3), Inches(1.4), Inches(4.2), Inches(5.4),
            "GRAPH Architecture Specs",
            ["Mathematical Formulation:\nG = (V, E), where E defines permitted directed messaging channels:\nPlanner -> {Researcher, Analyst}\n{Researcher, Analyst} -> Critic\nCritic -> Finalizer\n\n• Peer-to-Peer Cross-Verification:\nCritic receives inputs from multiple peer nodes simultaneously.\n• API Invocations: 5 calls\n\nKey Strengths:\n• Maximum topological routing flexibility\n• Facilitates multi-agent debate and cross-examination\n• 100% success rate, Score: 0.8000\n\nCritical Limitations:\n• High token usage (13,843 tokens)\n• Vulnerable to non-terminating communication loops if cyclic edges exist."],
            CARD_BG, TEAL)

set_notes(s19, """[Estimated Time: 1.0 min | Running Total: 19.0 min]
[Core Slide Narrative]
Details the Graph mesh topology, dynamic adjacency configurations, peer-to-peer verification channels, and guardrails against cyclic deadlocks.

[Verbal Script ("What to Say")]
"The GRAPH topology generalizes inter-agent interaction to an arbitrary directed graph G = (V, E). In our benchmark implementation, we configure a diamond-shaped DAG: Planner dispatches to both Researcher and Analyst in parallel; both converge upon an independent Critic agent for multi-perspective auditing; and the Critic routes to the Finalizer.
The defining strength of Graph is peer-to-peer verification: the Critic can cross-examine the Researcher's findings against the Analyst's quantitative constraints, reducing bias. In our pilot, Graph achieved 100% success with an average score of 0.80.
Its trade-off is computational cost (13,843 tokens) and the potential risk of infinite cyclic loops if reciprocal feedback edges are introduced, requiring strict iteration breakers."

[Slide Transition]
"Let us synthesize all five topologies in a comprehensive side-by-side comparative matrix."

[Anticipated Viva Questions]
Q: How does Graph differ from Star?
A: In Star, communication is restricted to hub-to-spoke channels. In Graph, peer agents can communicate directly (e.g. Researcher and Analyst both feeding into Critic), enabling peer review without routing through a central manager.""")

# ------------------------------------------
# SLIDE 20: Comparative Topology Analysis
# ------------------------------------------
s20 = prs.slides.add_slide(blank_layout)
add_header(s20, "7. Multi-Agent Topologies", "Comparative Topology Analysis & Trade-Off Frontier", 20)

create_card(s20, Inches(0.8), Inches(1.4), Inches(2.2), Inches(5.4),
            "SINGLE",
            ["Style: 1-Turn Direct",
             "Latency: 6.32s (1.0x)",
             "Tokens: 1,121 (1.0x)",
             "Cost: $0.00017",
             "Success: 100%",
             "Score: 0.9429",
             "Strength: Fastest, lowest cost, zero overhead.",
             "Weakness: Single point of failure; no review.",
             "Best Use: Low-latency API tasks, focused queries."],
            CARD_BG, BLUE)

create_card(s20, Inches(3.2), Inches(1.4), Inches(2.2), Inches(5.4),
            "CHAIN",
            ["Style: Linear SOP",
             "Latency: 42.21s (6.7x)",
             "Tokens: 11,555 (10.3x)",
             "Cost: $0.00173",
             "Success: 71.4%",
             "Score: 0.6914",
             "Strength: Staged refinement; clear boundaries.",
             "Weakness: Cascading error propagation.",
             "Best Use: Document formatting, translation."],
            CARD_BG, ACCENT_RED)

create_card(s20, Inches(5.6), Inches(1.4), Inches(2.2), Inches(5.4),
            "STAR",
            ["Style: Hub-Spoke",
             "Latency: 43.62s (6.9x)",
             "Tokens: 17,174 (15.3x)",
             "Cost: $0.00258",
             "Success: 100%",
             "Score: 0.8329",
             "Strength: Strong central oversight.",
             "Weakness: Maximum token explosion.",
             "Best Use: Enterprise manager-worker workflows."],
            CARD_BG, TEAL)

create_card(s20, Inches(8.0), Inches(1.4), Inches(2.2), Inches(5.4),
            "TREE",
            ["Style: Hierarchy",
             "Latency: 47.38s (7.5x)",
             "Tokens: 12,789 (11.4x)",
             "Cost: $0.00192",
             "Success: 100%",
             "Score: 0.7571",
             "Strength: Localized context; scalable.",
             "Weakness: Highest latency across tiers.",
             "Best Use: Complex engineering decomposition."],
            CARD_BG, PURPLE)

create_card(s20, Inches(10.4), Inches(1.4), Inches(2.2), Inches(5.4),
            "GRAPH",
            ["Style: Mesh DAG",
             "Latency: 47.31s (7.5x)",
             "Tokens: 13,843 (12.3x)",
             "Cost: $0.00208",
             "Success: 100%",
             "Score: 0.8000",
             "Strength: Peer review & multi-debate.",
             "Weakness: High token burn; cycle risk.",
             "Best Use: Open-ended scientific research."],
            CARD_BG, NAVY)

set_notes(s20, """[Estimated Time: 1.0 min | Running Total: 20.0 min]
[Core Slide Narrative]
Comprehensive comparative synthesis of all five topologies, highlighting empirical scores, token scaling, latency inflation, and optimal production use cases.

[Verbal Script ("What to Say")]
"This slide provides the central comparative summary of our empirical research.
Looking across the columns, the architectural trade-offs become immediately apparent:
The Single agent represents the absolute peak of operational efficiency: 6.32 seconds latency, 1,121 tokens, and the highest pilot score of 0.9429.
Chain is computationally expensive (11,555 tokens, 42 seconds) but fragile, dropping to 71.4% success due to error cascading.
Star provides total reliability (100% success) but pays a severe token tax—17,174 tokens—due to coordinator context convergence.
Tree and Graph provide structured decomposition and peer critique, achieving 100% success, but suffer from high latency (47 seconds) across multi-turn handoffs.
There is no single 'best' topology: the optimal choice represents a deliberate trade-off between latency, token budget, and fault tolerance."

[Slide Transition]
"Let us now look at the evaluation metrics engine and mathematical formulas used to quantify these dimensions."

[Anticipated Viva Questions]
Q: Why does Single have a higher score than Star or Tree?
A: Modern frontier LLMs have massive attention windows. When a task can be solved within a single prompt, multi-agent conversational hops introduce information attenuation and paraphrasing loss, slightly degrading constraint adherence.""")

# ------------------------------------------
# SLIDE 21: Evaluation Metrics Engine
# ------------------------------------------
s21 = prs.slides.add_slide(blank_layout)
add_header(s21, "8. Metrics & Formulation", "Multi-Dimensional Evaluation Metrics Engine", 21)

eval_img_path = os.path.join(FIG_DIR, "evaluation_pipeline.png")
if os.path.exists(eval_img_path):
    s21.shapes.add_picture(eval_img_path, Inches(0.8), Inches(1.4), Inches(6.8), Inches(5.4))

create_card(s21, Inches(7.8), Inches(1.4), Inches(4.7), Inches(5.4),
            "Four Evaluation Pillars",
            ["1. Task Performance & Quality:\n• Task Success: Boolean flag (Score >= 0.5)\n• Constraint Satisfaction Rate (CSR): Strict percentage of numerical/logical constraints met\n• Property Match Rate (PMR): Inclusion of mandatory architectural components.",
             "2. Resource Telemetry:\n• Prompt Tokens (T_prompt): Ingested context\n• Completion Tokens (T_comp): Generated text\n• Total Tokens: T_total = T_prompt + T_comp\n• Financial Cost (C_USD): Real API expenditure.",
             "3. Execution Performance:\n• Wall-Clock Latency (L): End-to-end seconds\n• API Invocations: Total turn multiplier.",
             "4. Operational Reliability:\n• Failure Rate (FR): Percentage of aborted runs\n• Fault Taxonomy: HTTP 429, timeouts, schema errors."],
            CARD_BG, BLUE)

set_notes(s21, """[Estimated Time: 1.0 min | Running Total: 21.0 min]
[Core Slide Narrative]
Outlines the four evaluation pillars of our telemetry engine and illustrates the deterministic data flow from raw execution traces to multi-metric persistence.

[Verbal Script ("What to Say")]
"Our framework replaces ad-hoc subjective evaluation with a multi-dimensional evaluation engine based on four pillars:
Pillar 1 is Task Performance and Quality—anchored by deterministic Constraint Satisfaction Rates, which verify exact numerical thresholds via regex engines.
Pillar 2 is Resource Telemetry—decoupling prompt token accumulation from completion tokens and computing financial cloud costs.
Pillar 3 is Execution Performance—profiling end-to-end wall-clock latency in real seconds.
Pillar 4 is Operational Reliability—capturing runtime failures, rate-limit stalls, and loop deadlocks.
As shown in the flow diagram on the left, ground-truth constraints remain strictly quarantined until output auditing."

[Slide Transition]
"Let us review the exact mathematical formulations governing these metrics."

[Anticipated Viva Questions]
Q: Why is regex used for constraint evaluation instead of asking an LLM judge?
A: LLM judges exhibit subjective drift, self-preference bias, and non-determinism. Regular expression matching against numerical thresholds (e.g. latency < 50ms, budget <= $5000) provides 100% deterministic, mathematically reproducible verification.""")

# ------------------------------------------
# SLIDE 22: Mathematical Formulations
# ------------------------------------------
s22 = prs.slides.add_slide(blank_layout)
add_header(s22, "8. Metrics & Formulation", "Mathematical Metrics Formulation", 22)

create_card(s22, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Constraint & Score Formulations",
            ["Constraint Satisfaction Rate (CSR):\nCSR(y, C) = (1 / |C|) * Sum_{i=1}^{|C|} 1{c_i(y) = 1}\nWhere c_i(y) in {0, 1} evaluates deterministic compliance of constraint c_i.\n\nProperty Match Rate (PMR):\nPMR(y, P) = (1 / |P|) * Sum_{j=1}^{|P|} 1{rho_j in y}\nWhere rho_j represents mandatory architectural terms.\n\nComposite Task Score (S):\nS = alpha * CSR + (1 - alpha) * PMR\n(In benchmark: alpha = 0.70, weighting strict constraints).\n\nNormalized Quality Score (QS):\nQS = 10 * S  in [0.0, 10.0]"],
            CARD_BG, CARD_BG)

create_card(s22, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Resource, Latency & Statistical Formulas",
            ["Financial Cloud API Cost (C_USD):\nC_USD = (T_prompt / 10^6) * r_prompt + (T_comp / 10^6) * r_comp\nCalculated using live provider pricing tiers.\n\nWall-Clock Execution Latency (L):\nL = t_completion - t_start = Sum_{k=1}^K (Delta t_k)\n\nFailure Rate (FR):\nFR = (N_failed / N_total) * 100%\n\nStandardized Effect Size (Cohen's d):\nd = (x_bar_topology - x_bar_single) / s_pooled\nQuantifies statistical magnitude of performance delta relative to baseline."],
            CARD_BG, TEAL)

set_notes(s22, """[Estimated Time: 1.0 min | Running Total: 22.0 min]
[Core Slide Narrative]
Walks through the formal mathematical definitions of CSR, PMR, composite score S, API cost C_USD, latency L, and Cohen's d effect size.

[Verbal Script ("What to Say")]
"This slide details the mathematical formulations implemented in our HybridEvaluator.
Equation 1 defines the Constraint Satisfaction Rate (CSR) as the normalized sum of indicator functions evaluating whether each constraint c_i is satisfied by the generated output y.
Equation 2 defines the Property Match Rate (PMR) over mandatory architectural components.
Equation 3 combines these into a composite Task Score S with alpha = 0.70, prioritizing strict constraint adherence over mere keyword inclusion.
Equation 4 calculates financial cost by decoupling prompt and completion token counts and applying provider price schedules.
Finally, Equation 7 computes Cohen's d effect sizes, allowing us to quantify whether score differences between topologies are statistically meaningful or mere noise."

[Slide Transition]
"Let us now look at the experimental methodology and benchmark task suite."

[Anticipated Viva Questions]
Q: What does a Cohen's d of -1.64 mean between Single and Star?
A: In statistics, an absolute Cohen's d greater than 0.8 represents a large effect size. A d of -1.64 indicates that the Single agent outperformed Star by more than 1.6 pooled standard deviations—a statistically massive difference.""")

# ------------------------------------------
# SLIDE 23: Experimental Methodology & Task Suite
# ------------------------------------------
s23 = prs.slides.add_slide(blank_layout)
add_header(s23, "9. Experimental Design", "Experimental Methodology & Benchmark Task Suite", 23)

exp_img_path = os.path.join(FIG_DIR, "experimental_workflow.png")
if os.path.exists(exp_img_path):
    s23.shapes.add_picture(exp_img_path, Inches(0.8), Inches(1.4), Inches(6.8), Inches(5.4))

create_card(s23, Inches(7.8), Inches(1.4), Inches(4.7), Inches(5.4),
            "Seven Benchmark Task Archetypes",
            ["1. TASK_PLAN_001 (Planning): Monolith to microservices phased migration under zero downtime.\n2. TASK_CONST_002 (Constraints): Cloud architecture (Latency < 50ms, 99.99% availability, budget <= $5k).\n3. TASK_SYNTH_003 (Synthesis): GNN vs Relational Transformer asymptotic complexity analysis.\n4. TASK_REASON_004 (Reasoning): Deadlock cycle detection in concurrent financial clearing.\n5. TASK_DECISION_005 (Decision): HIPAA-compliant database selection for 500M records.\n6. TASK_COLLAB_006 (Collaboration): Cyber incident response & subnet isolation protocol.\n7. TASK_CODE_007 (Coding): Thread-safe Leaky Bucket rate limiter in Python (O(1) time).\n\nControlled Variables: T=0.70, Max Tokens=1024, Timeout=30s."],
            CARD_BG, BLUE)

set_notes(s23, """[Estimated Time: 1.0 min | Running Total: 23.0 min]
[Core Slide Narrative]
Details the experimental methodology, the five-stage lifecycle, the seven diverse benchmark tasks, and strict experimental controls.

[Verbal Script ("What to Say")]
"To ensure rigorous scientific validity, we constructed a benchmark suite of seven complex technical tasks, spanning planning, numerical constraints, complexity synthesis, reasoning, database decision making, incident collaboration, and algorithmic coding.
Every task features explicit, verifiable constraints—such as HIPAA compliance, 99.99% availability, or O(1) time complexity.
All experiments were conducted under identical sampling hyper-parameters: sampling temperature fixed at 0.70, maximum generation capped at 1024 tokens, and request timeouts set to 30 seconds.
The experiment runner follows the five-phase lifecycle shown on the left: Ingestion, Topology Execution, Telemetry Harvesting, Hybrid Evaluation, and Statistical Persistence."

[Slide Transition]
"Let us briefly review the software implementation and research dashboard."

[Anticipated Viva Questions]
Q: Why were these specific 7 tasks chosen?
A: They represent the core operational archetypes that LLM agents encounter in enterprise software engineering: long-term planning, multi-criteria decision making, strict mathematical bounds, and algorithmic code synthesis.""")

# ------------------------------------------
# SLIDE 24: Implementation & Streamlit GUI
# ------------------------------------------
s24 = prs.slides.add_slide(blank_layout)
add_header(s24, "10. Implementation", "Implementation Architecture & Research Dashboard", 24)

create_card(s24, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Software Architecture & Codebase",
            ["Language & Stack: Python 3.13, Pydantic, Streamlit, Plotly, Graphviz.\n• BaseArchitecture: Abstract base class enforcing solve_task() interface and unified telemetry logging.\n• BaseAgent: Abstract agent class managing prompt queues, memory, and LLM provider invocation.\n• GuardrailTracker: Tracks API invocation counts, token budgets, and intercepts HTTP 429 exceptions.\n• MockProvider: Deterministic offline engine for 100% reproducible zero-cost regression tests.\n• Test Suite: 31/31 unit tests passing with pytest."],
            CARD_BG, BLUE)

create_card(s24, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Interactive Streamlit Dashboard (main.py)",
            ["Seven Dedicated Research Modules:\n1. Executive Dashboard: High-level KPIs, radar charts, and best-performing topology badges.\n2. Experiment Runner: Pre-flight dry-run cost previews and matrix sweep execution.\n3. Architecture Comparison: Interactive Plotly comparisons of score, latency, and tokens.\n4. Task Deep-Dive: Message-by-message inspection of intermediate plans and drafts.\n5. Topology Visualizer: Dynamic Graphviz network rendering of active communication edges.\n6. Empirical Results Analysis: Effect size tables and failure mode distributions.\n7. Seminar Demonstration Suite: Side-by-side live comparative testing."],
            CARD_BG, TEAL)

set_notes(s24, """[Estimated Time: 1.0 min | Running Total: 24.0 min]
[Core Slide Narrative]
Highlights the Python 3.13 object-oriented implementation, robust test coverage, and the feature-rich Streamlit interactive research dashboard.

[Verbal Script ("What to Say")]
"The framework is implemented in Python 3.13 following clean object-oriented architecture. Core logic is organized around BaseArchitecture, BaseAgent, and GuardrailTracker abstractions. The codebase includes a full pytest suite with 31 out of 31 passing unit tests.
In addition to headless CLI execution, we built an interactive web dashboard in Streamlit. The dashboard features seven specialized modules—allowing researchers to run pre-flight budget checks, view live Graphviz network graphs of active agent communication, inspect message-by-message intermediate reasoning traces, and run live side-by-side demonstrations during technical seminars."

[Slide Transition]
"Now, let us examine the empirical results obtained across 175 live cloud executions."

[Anticipated Viva Questions]
Q: What does the Pre-flight Dry-Run feature do?
A: Before invoking paid cloud APIs, the pre-flight estimator calculates the maximum possible token consumption and estimated dollar expenditure across the selected matrix, ensuring that the experiment will not exceed predefined budget limits.""")

# ------------------------------------------
# SLIDE 25: Empirical Results: Pilot Benchmark
# ------------------------------------------
s25 = prs.slides.add_slide(blank_layout)
add_header(s25, "11. Results & Findings", "Empirical Results: Pilot Benchmark & Aggregate Matrix", 25)

create_card(s25, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Authoritative Pilot Results (Gemini 3.1 Flash-Lite)",
            ["Dataset: EXP_LIVE_20260813_140712 (35 Runs)\n\n• SINGLE:\nSuccess: 100.0% | Score: 0.9429 | Latency: 6.32s | Tokens: 1,121.6 | Cost: $0.00017 | Cohen's d: Baseline\n\n• STAR:\nSuccess: 100.0% | Score: 0.8329 | Latency: 43.62s | Tokens: 17,174.1 | Cost: $0.00258 | Cohen's d: -1.64\n\n• CHAIN:\nSuccess: 71.4% | Score: 0.6914 | Latency: 42.21s | Tokens: 11,555.4 | Cost: $0.00173 | Cohen's d: -1.24\n\n• TREE:\nSuccess: 100.0% | Score: 0.7571 | Latency: 47.38s | Tokens: 12,789.3 | Cost: $0.00192 | Cohen's d: -1.98\n\n• GRAPH:\nSuccess: 100.0% | Score: 0.8000 | Latency: 47.31s | Tokens: 13,843.1 | Cost: $0.00208 | Cohen's d: -1.79"],
            CARD_BG, CARD_BG)

create_card(s25, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Cross-Provider Aggregate Results (175 Runs)",
            ["Evaluated across Gemini, Cohere, and Groq (N = 35 runs each):\n\n• SINGLE:\nSuccess: 82.9% | Mean Score: 0.6521 | Latency: 10.25s | Tokens: 4,322 | Cost: $0.0857\n\n• CHAIN:\nSuccess: 54.3% | Mean Score: 0.4426 | Latency: 44.20s | Tokens: 12,854 | Cost: $0.3980\n\n• STAR:\nSuccess: 54.3% | Mean Score: 0.6171 | Latency: 46.56s | Tokens: 18,687 | Cost: $0.5048\n\n• TREE:\nSuccess: 60.0% | Mean Score: 0.5286 | Latency: 56.09s | Tokens: 16,243 | Cost: $0.5361\n\n• GRAPH:\nSuccess: 54.3% | Mean Score: 0.5517 | Latency: 50.17s | Tokens: 15,571 | Cost: $0.5006"],
            CARD_BG, TEAL)

set_notes(s25, """[Estimated Time: 1.0 min | Running Total: 25.0 min]
[Core Slide Narrative]
Presents empirical tables from the authoritative Gemini pilot and the 175-run cross-provider aggregate matrix, establishing ground-truth numbers.

[Verbal Script ("What to Say")]
"Here are the core empirical findings of our research.
Table 1 on the left presents our authoritative pilot run on Google Gemini 3.1 Flash-Lite. Notice the stark contrasts: Single agent achieved 100% success with an average score of 0.9429, executing in just 6.32 seconds and using 1,121 tokens.
In contrast, Star, Tree, and Graph achieved 100% success, but at 6.7 to 7.5 times higher latency (43 to 47 seconds) and 10 to 15 times more tokens. Chain dropped to 71.4% success.
Table 2 on the right extends this across 175 live executions spanning Gemini, Cohere Command, and Groq Llama-3.3. Across all providers, Single maintained the highest success rate (82.9%) and lowest latency (10.25s), while multi-agent systems averaged 44 to 56 seconds and over 15,000 tokens."

[Slide Transition]
"Let us analyze the first major finding: The Baseline Efficiency Paradox."

[Anticipated Viva Questions]
Q: Why are the cross-provider aggregate success rates lower than the Gemini pilot?
A: Different LLM providers exhibit varying adherence to strict JSON formatting and system prompts. Cohere and Groq encountered occasional schema truncation and rate-limit retries on complex multi-turn topologies, lowering their aggregate success rates.""")

# ------------------------------------------
# SLIDE 26: Finding 1: Baseline Efficiency Paradox
# ------------------------------------------
s26 = prs.slides.add_slide(blank_layout)
add_header(s26, "11. Results & Findings", "Key Finding 1: The Baseline Efficiency Paradox", 26)

create_card(s26, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "The Paradox Defined",
            ["Prevailing Industry Assumption:\nAdding more LLM agents and multi-stage peer review inherently improves reasoning accuracy and task quality.\n\nEmpirical Reality:\nIn tasks that fit within a frontier LLM's context window, an isolated SINGLE agent baseline achieved:\n• Highest overall Task Score (0.9429 on Gemini)\n• 1/15th the financial cost of Star ($0.00017 vs $0.00258)\n• 1/7th the execution latency (6.32s vs 43.62s)\n• Large negative effect sizes for multi-agent systems (d <= -1.24)."],
            CARD_BG, CARD_BG)

create_card(s26, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Root Causes: Information Attenuation",
            ["1. Information Attenuation Effect: Each conversational handoff acts as a lossy semantic channel; intermediate agents paraphrase prompts and inadvertently drop subtle negative constraints.\n2. Context Dilution: As transcripts grow across hops, the model's attention is distributed over hundreds of conversational tokens rather than the core prompt constraints.\n3. Latency Compounding: Synchronous turn-taking forces human users to wait 45+ seconds for answers that a single agent generates in 6 seconds.\n4. Engineering Takeaway: Multi-agent coordination should only be deployed when tasks strictly exceed single-agent context limits."],
            CARD_BG, BLUE)

set_notes(s26, """[Estimated Time: 1.0 min | Running Total: 26.0 min]
[Core Slide Narrative]
Explains the 'Baseline Efficiency Paradox' and details why single-agent baselines often outperform multi-agent systems on context-bounded tasks.

[Verbal Script ("What to Say")]
"Key Finding 1 is what we term the 'Baseline Efficiency Paradox'. A pervasive assumption in contemporary AI is that multi-agent delegation inherently yields superior accuracy. Our empirical data directly challenges this.
When a task's context and constraints comfortably fit within the attention window of a modern foundation model, an isolated single agent consistently outperforms multi-agent configurations.
Why does this occur? We identified the 'Information Attenuation Effect': each intermediate serialization step acts as a lossy compression channel. When the Planner summarizes the task for the Researcher, and the Researcher passes notes to the Analyst, subtle negative constraints—such as 'latency must remain below 50ms'—are frequently dropped or diluted. The single agent, processing the raw constraints directly in one turn, exhibits no paraphrasing loss."

[Slide Transition]
"Let us now look at Key Finding 2: Cascading Failure Propagation in sequential pipelines."

[Anticipated Viva Questions]
Q: Does this mean multi-agent systems are useless?
A: Absolutely not. Multi-agent systems become essential when tasks exceed context windows, require heterogeneous model specializations, or involve distinct external tool authorizations (e.g. read-only vs write permissions). However, for self-contained reasoning tasks, they introduce unnecessary overhead.""")

# ------------------------------------------
# SLIDE 27: Finding 2: Pipeline Cascading Failures
# ------------------------------------------
s27 = prs.slides.add_slide(blank_layout)
add_header(s27, "11. Results & Findings", "Key Finding 2: Cascading Pipeline Failures in CHAIN", 27)

create_card(s27, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Pipeline Failure Autopsy: TASK_SYNTH_003",
            ["Task Objective: Synthesize Graph Neural Network O(V+E) spatial complexity vs. Relational Transformer O(N^2) memory footprint.\nMandatory Constraints: Explicitly contrast O(V+E) vs O(N^2) and justify graph sparsity bounds.\n\nCascade Trajectory:\n• Stage 1 (Planner): Correctly noted both complexity terms.\n• Stage 2 (Researcher): Focused heavily on message passing, omitting the explicit O(V+E) asymptotic notation.\n• Stage 3 (Analyst): Inherited Researcher's notes, analyzing matrix operations without restoring the complexity formula.\n• Stage 4 & 5 (Critic & Finalizer): Validated the text as coherent, failing to recognize that the core constraint had vanished.\nResult: Constraint Omission Failure (Task Failed)."],
            CARD_BG, ACCENT_RED)

create_card(s27, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Architectural Lessons on Resilience",
            ["1. Forward-Only Fragility: Without backward critique loops (e.g. Critic -> Planner), sequential pipelines lack error correction.\n2. Illusion of Validation: Downstream critics evaluate coherence rather than compliance with the original quarantined ground truth.\n3. Contrast with STAR & TREE:\n• Star succeeded because the Coordinator independently retained the master task specification throughout.\n• Tree succeeded because localized branches preserved domain constraints.\n4. Architectural Remedy: In production chains, the original prompt and constraints must be explicitly re-injected into every stage's system prompt."],
            CARD_BG, TEAL)

set_notes(s27, """[Estimated Time: 1.0 min | Running Total: 27.0 min]
[Core Slide Narrative]
Presents a forensic trace autopsy of a cascading failure in the Chain topology on TASK_SYNTH_003, explaining the vulnerability of forward-only pipelines.

[Verbal Script ("What to Say")]
"Key Finding 2 explains why the Chain topology dropped to 71.4% success. On this slide, we present an actual forensic trace autopsy from our pilot data on TASK_SYNTH_003.
The task required contrasting the O(V+E) complexity of Graph Neural Networks against the O(N^2) footprint of Transformers.
In Stage 1, the Planner included both formulas. But in Stage 2, the Researcher paraphrased the discussion, omitting the explicit O(V+E) mathematical notation. In Stage 3, the Analyst worked solely from the Researcher's notes. By Stages 4 and 5, the Critic and Finalizer praised the draft for high coherence, completely oblivious to the fact that a mandatory constraint had been dropped two stages earlier.
This illustrates the fundamental flaw of linear pipelines: they lack backward feedback loops. To make chains resilient in production, system designers must enforce constraint re-injection protocols at every hop."

[Slide Transition]
"Let us now address Threats to Validity and study limitations."

[Anticipated Viva Questions]
Q: How could the Chain architecture be modified to prevent this cascade?
A: By implementing a 'skip-connection' or constraint re-injection mechanism where the original task prompt and constraints are appended to every agent's input context alongside the previous agent's output.""")

# ------------------------------------------
# SLIDE 28: Threats to Validity & Limitations
# ------------------------------------------
s28 = prs.slides.add_slide(blank_layout)
add_header(s28, "12. Discussion & Validity", "Threats to Validity & Experimental Limitations", 28)

create_card(s28, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Threats to Validity",
            ["1. Construct Validity: Does regex constraint checking truly reflect solution quality? (Mitigated by combining regex with property matching and manual trace verification).\n2. Internal Validity: Model sampling non-determinism and temperature variance. (Mitigated by fixing T=0.70 across all 175 runs and using deterministic mock baselines).\n3. External Validity: Generalizability across diverse model scales. (Evaluated across Google Gemini, Cohere Command, and Groq Llama-3.3-70B).\n4. Conclusion Validity: Statistical significance of topology differences verified using Cohen's d effect sizes."],
            CARD_BG, BLUE)

create_card(s28, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Framework & Study Limitations",
            ["1. Homogeneous Model Assignment: All agents within a topology shared the same model family; did not evaluate heterogeneous architectures (e.g. GPT-4 Planner + Flash Workers).\n2. Synthetic Benchmark Suite: 35 curated tasks across 7 domains; does not cover multi-day, open-ended real-world repository development.\n3. Static Topologies: Topologies were fixed prior to run; did not explore dynamic runtime reconfiguration.\n4. Tool Constraints: Focused on pure LLM reasoning, planning, and code synthesis; excluded multi-modal and web browsing tools."],
            CARD_BG, CARD_BG)

set_notes(s28, """[Estimated Time: 1.0 min | Running Total: 28.0 min]
[Core Slide Narrative]
Transparently discusses Threats to Validity (Construct, Internal, External, Conclusion) and explicitly acknowledges framework scope boundaries.

[Verbal Script ("What to Say")]
"A rigorous academic study must critically examine its own validity threats and limitations.
In terms of construct validity, regex constraint checking may miss nuanced prose, which is why we combined it with property matching and trace audits.
In terms of internal validity, LLM non-determinism was strictly controlled by unifying temperature, token caps, and timeouts across all 175 trials.
We also acknowledge four key limitations: First, we evaluated homogeneous model assignments where all agents used the same model backend. Second, our tasks are curated benchmark problems rather than multi-week software projects. Third, our topologies were statically configured rather than dynamically evolving during execution. And fourth, we focused on core textual and algorithmic reasoning rather than multimodal tools."

[Slide Transition]
"These limitations directly illuminate promising pathways for future research."

[Anticipated Viva Questions]
Q: Why did you use homogeneous models instead of assigning GPT-4 to the planner and a smaller model to the workers?
A: To isolate topology as the sole independent variable. If we used heterogeneous models, performance differences could be attributed to model disparities rather than communication graph structure.""")

# ------------------------------------------
# SLIDE 29: Future Research Directions
# ------------------------------------------
s29 = prs.slides.add_slide(blank_layout)
add_header(s29, "13. Future Roadmap", "Future Research Directions & Roadmap", 29)

create_card(s29, Inches(0.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "1. Dynamic Reconfiguration",
            ["Adaptive Routing: Agents dynamically spawn or dissolve communication channels based on intermediate task difficulty.",
             "Confidence-Gated Topologies: Start as Single; escalate to Star or Tree only when model confidence falls below threshold.",
             "Reinforcement Learning: Training meta-controllers to learn optimal topology graphs."],
            CARD_BG, BLUE)

create_card(s29, Inches(4.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "2. Heterogeneous Architectures",
            ["Tiered Model Routing: Pair frontier reasoning models (e.g. Gemini 1.5 Pro / GPT-4o) as Planners with lightweight models (Flash-Lite / Haiku) as leaf workers.",
             "Cost-Optimized Ensembles: Maximize constraint satisfaction per dollar spent.",
             "Cross-Provider Resilience: Mitigating single-provider API outages."],
            CARD_BG, TEAL)

create_card(s29, Inches(8.8), Inches(1.4), Inches(3.6), Inches(5.4),
            "3. Multimodal & Live Tooling",
            ["Real-World OS & Terminal: Integrating bash execution, Docker sandboxes, and git repositories.",
             "Multimodal Vision Agents: Evaluating diagrams, architecture schematics, and UI screenshots.",
             "Human-in-the-Loop: Topology nodes that can query human experts for approval."],
            CARD_BG, NAVY)

set_notes(s29, """[Estimated Time: 1.0 min | Running Total: 29.0 min]
[Core Slide Narrative]
Outlines three promising research avenues: dynamic topology reconfiguration, heterogeneous model allocation, and live environment tool execution.

[Verbal Script ("What to Say")]
"Our findings point toward three exciting frontiers for future multi-agent research.
First, Dynamic Topology Reconfiguration. Instead of fixing a topology beforehand, an adaptive meta-controller could evaluate task difficulty: simple queries remain as Single agents, while complex, multi-constraint problems dynamically spawn into a Star or Graph.
Second, Heterogeneous Model Tiering. By assigning a large frontier model as the central Planner and smaller, high-throughput models as leaf workers, systems can dramatically reduce financial cost while preserving reasoning rigor.
Third, Real-World Tooling Integration. Extending the framework into live Linux terminal environments, git repositories, and multimodal vision agents will expand empirical topology benchmarking into full software engineering workflows."

[Slide Transition]
"Let us conclude our seminar presentation with a summary of contributions and open-source availability."

[Anticipated Viva Questions]
Q: How would a confidence-gated topology work?
A: The single agent generates an initial answer and a self-assessed log-probability confidence score. If confidence is above 0.90, the answer is returned immediately in 6 seconds. If confidence is low, the task is escalated to a Star or Tree architecture for multi-agent peer review.""")

# ------------------------------------------
# SLIDE 30: Conclusion & References
# ------------------------------------------
s30 = prs.slides.add_slide(blank_layout)
add_header(s30, "14. Conclusion & Q&A", "Conclusions, Academic References & Q&A", 30)

create_card(s30, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Core Seminar Takeaways",
            ["1. Controlled Empirical Benchmark: Built and verified MultiAgentTopologyEval, isolating 5 canonical topologies across 175 live executions.\n2. The Baseline Efficiency Paradox: Single agent baseline achieved highest score (0.9429) at 1/15th cost and 1/7th latency for context-bounded tasks.\n3. Pipeline Vulnerability: Sequential Chain topology suffered from cascading constraint omission, dropping to 71.4% success.\n4. Production Guardrails: Real-time telemetry, step limits (K <= 20), and regex constraint checking are critical for MAS reliability.\n5. Open-Source Artifacts: Complete codebase, test suite, and research paper available on GitHub."],
            CARD_BG, TEAL)

create_card(s30, Inches(6.8), Inches(1.4), Inches(5.6), Inches(5.4),
            "Academic References & Acknowledgments",
            ["Key Peer-Reviewed Literature (Zero Blogs / Repos):\n• Vaswani et al. (NeurIPS 2017) Attention Is All You Need\n• Brown et al. (NeurIPS 2020) Language Models Few-Shot Learners\n• Wei et al. (NeurIPS 2022) Chain-of-Thought Prompting\n• Yao et al. (ICLR 2023) ReAct: Synergizing Reasoning & Acting\n• Hong et al. (ICLR 2024) MetaGPT: Multi-Agent Metaprogramming\n• Zhu et al. (ACL 2025) MultiAgentBench: Collab & Competition\n\nAcknowledgments:\nDepartment of Computer Applications, VJTI Mumbai\nFaculty Seminar Coordinator & Peer Reviewers\n\nThank You! Open for Questions & Viva Examination."],
            CARD_BG, CARD_BG)

set_notes(s30, """[Estimated Time: 1.0 min | Running Total: 30.0 min]
[Core Slide Narrative]
Summarizes core seminar contributions, acknowledges faculty and department at VJTI, cites key academic literature, and invites committee questions.

[Verbal Script ("What to Say")]
"To conclude: This technical seminar presented MultiAgentTopologyEval, an empirical evaluation framework that systematically characterizes the trade-offs of multi-agent communication topologies.
Our core conclusions are threefold: First, multi-agent systems incur a heavy operational penalty—amplifying latency by up to 7.5x and token consumption by up to 15x. Second, the single-agent baseline paradoxically outperforms multi-agent systems when tasks fit within the context window, avoiding information attenuation. Third, linear pipelines are fragile due to cascading constraint omissions, while centralized Star and Tree topologies provide superior fault resilience.
All experimental tools, benchmark suites, and documentation are open-source and reproducible.
I express my sincere gratitude to the faculty members of the Department of Computer Applications at VJTI for their guidance.
Thank you for your time. I am now open for questions and discussion."

[Anticipated Viva Questions]
Committee may ask deep questions on:
1. Transformer attention math
2. The exact mechanism of cascading failure in Chain
3. Why Star consumed 17k tokens
4. Differences with Zhu et al. (ACL 2025)
Refer to the SEMINAR_PREPARATION_GUIDE for comprehensive technical answers.""")

# Save complete presentation
prs.save(OUT_PATH)
print(f"Presentation successfully built and saved to: {OUT_PATH}")
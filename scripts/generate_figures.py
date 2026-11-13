"""
generate_figures.py
Generates publication-quality, high-resolution PNG diagrams for MultiAgentTopologyEval:
1. single_topology.png
2. chain_topology.png
3. star_topology.png
4. tree_topology.png
5. graph_topology.png
6. system_architecture.png
7. evaluation_pipeline.png
8. experimental_workflow.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join("seminar_submission", "Figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color Palette
NAVY = (26, 54, 93)
BLUE = (43, 108, 176)
LIGHT_BLUE = (235, 244, 255)
TEAL = (49, 151, 149)
LIGHT_TEAL = (230, 255, 250)
PURPLE = (107, 70, 193)
LIGHT_PURPLE = (250, 245, 255)
ORANGE = (221, 107, 32)
LIGHT_ORANGE = (255, 240, 222)
GRAY = (74, 85, 104)
LIGHT_GRAY = (247, 250, 252)
BORDER_GRAY = (203, 213, 225)
WHITE = (255, 255, 255)
DARK_TEXT = (26, 32, 44)
MUTED_TEXT = (113, 128, 150)

def get_font(size, bold=False):
    # Try system fonts on Windows
    candidates = [
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\calibri.ttf"
    ]
    if bold:
        candidates = [
            "C:\\Windows\\Fonts\\segoeuib.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",
            "C:\\Windows\\Fonts\\calibrib.ttf"
        ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_rounded_rect(draw, xy, fill, outline, width=2, radius=8):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_arrow(draw, start, end, color=BLUE, width=3, arrow_size=10):
    draw.line([start, end], fill=color, width=width)
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    length = (dx*dx + dy*dy)**0.5
    if length == 0:
        return
    ux = dx / length
    uy = dy / length
    # Perpendicular unit vector
    px = -uy
    py = ux
    # Arrow head points
    p1 = (x2, y2)
    p2 = (x2 - ux * arrow_size + px * (arrow_size * 0.5), y2 - uy * arrow_size + py * (arrow_size * 0.5))
    p3 = (x2 - ux * arrow_size - px * (arrow_size * 0.5), y2 - uy * arrow_size - py * (arrow_size * 0.5))
    draw.polygon([p1, p2, p3], fill=color)

# 1. SINGLE TOPOLOGY
def make_single():
    img = Image.new("RGBA", (1000, 350), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(15, False)
    f_sub = get_font(13, False)

    # Title
    draw.text((50, 30), "SINGLE Architecture (Baseline Control)", fill=NAVY, font=f_title)
    draw.text((50, 60), "Isolated single-turn execution: direct prompt-to-response generation without peer review", fill=MUTED_TEXT, font=f_sub)

    # Box 1: Input
    draw_rounded_rect(draw, (80, 130, 280, 230), LIGHT_GRAY, BORDER_GRAY, 2, 8)
    draw.text((100, 150), "Task Prompt p", fill=DARK_TEXT, font=f_body)
    draw.text((100, 175), "Constraints C", fill=DARK_TEXT, font=f_body)
    draw.text((100, 200), "Category Info", fill=MUTED_TEXT, font=f_sub)

    # Arrow 1
    draw_arrow(draw, (280, 180), (370, 180), BLUE, 3, 12)

    # Box 2: Single Agent
    draw_rounded_rect(draw, (370, 110, 630, 250), LIGHT_BLUE, BLUE, 3, 10)
    draw.text((410, 140), "Single Agent (a_single)", fill=NAVY, font=f_title)
    draw.text((410, 170), "• Direct model inference", fill=DARK_TEXT, font=f_body)
    draw.text((410, 195), "• Zero communication overhead", fill=DARK_TEXT, font=f_body)
    draw.text((410, 220), "• Lowest token and latency cost", fill=DARK_TEXT, font=f_body)

    # Arrow 2
    draw_arrow(draw, (630, 180), (720, 180), BLUE, 3, 12)

    # Box 3: Output
    draw_rounded_rect(draw, (720, 130, 920, 230), LIGHT_TEAL, TEAL, 2, 8)
    draw.text((740, 150), "Synthesized Answer y", fill=TEAL, font=f_body)
    draw.text((740, 175), "• Fast execution (6.3s)", fill=DARK_TEXT, font=f_sub)
    draw.text((740, 195), "• Minimal tokens (~1.1k)", fill=DARK_TEXT, font=f_sub)

    img.save(os.path.join(OUTPUT_DIR, "single_topology.png"), "PNG")

# 2. CHAIN TOPOLOGY
def make_chain():
    img = Image.new("RGBA", (1100, 360), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "CHAIN Architecture (Linear SOP Pipeline)", fill=NAVY, font=f_title)
    draw.text((50, 52), "Sequential stage-by-stage handoff reflecting industrial Standard Operating Procedures", fill=MUTED_TEXT, font=get_font(13))

    roles = [
        ("Planner (a1)", "Decompose & Plan", LIGHT_BLUE, BLUE),
        ("Researcher (a2)", "Domain Synthesis", LIGHT_TEAL, TEAL),
        ("Analyst (a3)", "Algorithmic Analysis", LIGHT_PURPLE, PURPLE),
        ("Critic (a4)", "Constraint Audit", LIGHT_ORANGE, ORANGE),
        ("Finalizer (a5)", "Synthesized Solution", LIGHT_BLUE, NAVY)
    ]

    x_start = 50
    box_w = 160
    box_h = 130
    gap = 45
    y = 130

    for i, (role, desc, fill, border) in enumerate(roles):
        x = x_start + i * (box_w + gap)
        draw_rounded_rect(draw, (x, y, x + box_w, y + box_h), fill, border, 2, 8)
        draw.text((x + 12, y + 20), role, fill=NAVY, font=f_body)
        draw.text((x + 12, y + 50), desc, fill=DARK_TEXT, font=f_sub)
        draw.text((x + 12, y + 80), f"Stage {i+1} Handoff", fill=MUTED_TEXT, font=f_sub)

        if i < len(roles) - 1:
            arr_start = (x + box_w, y + box_h // 2)
            arr_end = (x + box_w + gap, y + box_h // 2)
            draw_arrow(draw, arr_start, arr_end, BLUE, 3, 10)
            draw.text((arr_start[0] + 12, arr_start[1] - 20), f"m_{i+1}", fill=BLUE, font=f_sub)

    # Footnote warning
    draw.text((50, 290), "Vulnerability Alert: Linear cascades exhibit cumulative context attenuation; early omissions propagate downstream uncorrected.", fill=(197, 48, 48), font=get_font(12, True))

    img.save(os.path.join(OUTPUT_DIR, "chain_topology.png"), "PNG")

# 3. STAR TOPOLOGY
def make_star():
    img = Image.new("RGBA", (1000, 520), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(14, True)
    f_sub = get_font(12, False)

    draw.text((50, 25), "STAR Architecture (Centralized Hub-and-Spoke)", fill=NAVY, font=f_title)
    draw.text((50, 52), "Central Coordinator delegates in parallel to satellite workers, aggregating into a Finalizer sink", fill=MUTED_TEXT, font=get_font(13))

    # Center Hub (Coordinator)
    cx, cy = 500, 160
    draw_rounded_rect(draw, (cx - 150, cy - 45, cx + 150, cy + 45), LIGHT_BLUE, BLUE, 3, 10)
    draw.text((cx - 130, cy - 30), "Central Coordinator (Planner)", fill=NAVY, font=f_body)
    draw.text((cx - 130, cy - 5), "Task decomposition & worker prompt dispatch", fill=DARK_TEXT, font=f_sub)

    # Satellite Workers
    workers = [
        ("Researcher (a_res)", 180, 310, LIGHT_TEAL, TEAL),
        ("Analyst (a_ana)", 500, 310, LIGHT_PURPLE, PURPLE),
        ("Critic (a_crit)", 820, 310, LIGHT_ORANGE, ORANGE)
    ]

    for name, wx, wy, fill, border in workers:
        draw_rounded_rect(draw, (wx - 110, wy - 35, wx + 110, wy + 35), fill, border, 2, 8)
        draw.text((wx - 95, wy - 20), name, fill=NAVY, font=f_body)
        draw.text((wx - 95, wy + 5), "Targeted sub-task execution", fill=DARK_TEXT, font=f_sub)

        # Arrow down from Hub to Worker
        draw_arrow(draw, (cx + (wx - cx) * 0.35, cy + 45), (wx, wy - 35), BLUE, 2, 8)

    # Finalizer Sink at Bottom
    fx, fy = 500, 450
    draw_rounded_rect(draw, (fx - 140, fy - 35, fx + 140, fy + 35), (254, 235, 226), (197, 48, 48), 2, 8)
    draw.text((fx - 110, fy - 20), "Finalizer Aggregation Sink", fill=(155, 44, 44), font=f_body)
    draw.text((fx - 110, fy + 5), "Consolidates parallel worker outputs into y", fill=DARK_TEXT, font=f_sub)

    # Arrows from workers to sink
    for _, wx, wy, _, _ in workers:
        draw_arrow(draw, (wx, wy + 35), (fx + (wx - fx) * 0.45, fy - 35), (155, 44, 44), 2, 8)

    img.save(os.path.join(OUTPUT_DIR, "star_topology.png"), "PNG")

# 4. TREE TOPOLOGY
def make_tree():
    img = Image.new("RGBA", (1000, 560), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "TREE Architecture (Multi-Tier Hierarchical)", fill=NAVY, font=f_title)
    draw.text((50, 52), "Multi-level organizational hierarchy with branch delegation and bottom-up aggregation", fill=MUTED_TEXT, font=get_font(13))

    # Tier 1: Root
    rx, ry = 500, 120
    draw_rounded_rect(draw, (rx - 130, ry - 30, rx + 130, ry + 30), LIGHT_BLUE, BLUE, 2, 8)
    draw.text((rx - 110, ry - 15), "Tier 1: Root Coordinator", fill=NAVY, font=f_body)
    draw.text((rx - 110, ry + 5), "High-level goal decomposition", fill=DARK_TEXT, font=f_sub)

    # Tier 2: Leads
    l1_x, l1_y = 280, 240
    l2_x, l2_y = 720, 240
    draw_rounded_rect(draw, (l1_x - 110, l1_y - 30, l1_x + 110, l1_y + 30), LIGHT_TEAL, TEAL, 2, 8)
    draw.text((l1_x - 90, l1_y - 15), "Tier 2: Research Lead", fill=NAVY, font=f_body)
    draw.text((l1_x - 90, l1_y + 5), "Domain investigation branch", fill=DARK_TEXT, font=f_sub)

    draw_rounded_rect(draw, (l2_x - 110, l2_y - 30, l2_x + 110, l2_y + 30), LIGHT_PURPLE, PURPLE, 2, 8)
    draw.text((l2_x - 90, l2_y - 15), "Tier 2: Analysis Lead", fill=NAVY, font=f_body)
    draw.text((l2_x - 90, l2_y + 5), "Quantitative verification branch", fill=DARK_TEXT, font=f_sub)

    draw_arrow(draw, (rx - 60, ry + 30), (l1_x, l1_y - 30), BLUE, 2, 8)
    draw_arrow(draw, (rx + 60, ry + 30), (l2_x, l2_y - 30), BLUE, 2, 8)

    # Tier 3: Workers
    w1_x, w1_y = 280, 360
    w2_x, w2_y = 720, 360
    draw_rounded_rect(draw, (w1_x - 110, w1_y - 30, w1_x + 110, w1_y + 30), LIGHT_GRAY, BORDER_GRAY, 2, 8)
    draw.text((w1_x - 90, w1_y - 15), "Tier 3: Research Worker", fill=DARK_TEXT, font=f_body)
    draw.text((w1_x - 90, w1_y + 5), "Detailed factual synthesis", fill=MUTED_TEXT, font=f_sub)

    draw_rounded_rect(draw, (w2_x - 110, w2_y - 30, w2_x + 110, w2_y + 30), LIGHT_GRAY, BORDER_GRAY, 2, 8)
    draw.text((w2_x - 90, w2_y - 15), "Tier 3: Critic Worker", fill=DARK_TEXT, font=f_body)
    draw.text((w2_x - 90, w2_y + 5), "Constraint compliance audit", fill=MUTED_TEXT, font=f_sub)

    draw_arrow(draw, (l1_x, l1_y + 30), (w1_x, w1_y - 30), TEAL, 2, 8)
    draw_arrow(draw, (l2_x, l2_y + 30), (w2_x, w2_y - 30), PURPLE, 2, 8)

    # Tier 4: Aggregation Finalizer
    fx, fy = 500, 480
    draw_rounded_rect(draw, (fx - 140, fy - 30, fx + 140, fy + 30), LIGHT_ORANGE, ORANGE, 2, 8)
    draw.text((fx - 120, fy - 15), "Tier 4: Bottom-Up Finalizer", fill=(194, 65, 12), font=f_body)
    draw.text((fx - 120, fy + 5), "Hierarchical convergence to final solution", fill=DARK_TEXT, font=f_sub)

    draw_arrow(draw, (w1_x + 60, w1_y + 30), (fx - 60, fy - 30), ORANGE, 2, 8)
    draw_arrow(draw, (w2_x - 60, w2_y + 30), (fx + 60, fy - 30), ORANGE, 2, 8)

    img.save(os.path.join(OUTPUT_DIR, "tree_topology.png"), "PNG")

# 5. GRAPH TOPOLOGY
def make_graph():
    img = Image.new("RGBA", (1000, 520), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "GRAPH Architecture (Configurable Mesh Topology)", fill=NAVY, font=f_title)
    draw.text((50, 52), "General directed graph G=(V,E) enabling multi-agent debate and peer-to-peer verification", fill=MUTED_TEXT, font=get_font(13))

    # Diamond / Mesh Layout
    # Planner Top
    px, py = 500, 120
    draw_rounded_rect(draw, (px - 100, py - 30, px + 100, py + 30), LIGHT_BLUE, BLUE, 2, 8)
    draw.text((px - 75, py - 12), "Planner (v1)", fill=NAVY, font=f_body)
    draw.text((px - 75, py + 8), "Entry Point Dispatch", fill=DARK_TEXT, font=f_sub)

    # Researcher Left
    rx, ry = 260, 250
    draw_rounded_rect(draw, (rx - 100, ry - 30, rx + 100, ry + 30), LIGHT_TEAL, TEAL, 2, 8)
    draw.text((rx - 75, ry - 12), "Researcher (v2)", fill=NAVY, font=f_body)
    draw.text((rx - 75, ry + 8), "Domain Synthesis", fill=DARK_TEXT, font=f_sub)

    # Analyst Right
    ax, ay = 740, 250
    draw_rounded_rect(draw, (ax - 100, ay - 30, ax + 100, ay + 30), LIGHT_PURPLE, PURPLE, 2, 8)
    draw.text((ax - 75, ay - 12), "Analyst (v3)", fill=NAVY, font=f_body)
    draw.text((ax - 75, ay + 8), "Constraint Modeling", fill=DARK_TEXT, font=f_sub)

    # Critic Middle-Bottom
    cx, cy = 500, 360
    draw_rounded_rect(draw, (cx - 100, cy - 30, cx + 100, cy + 30), LIGHT_ORANGE, ORANGE, 2, 8)
    draw.text((cx - 75, cy - 12), "Critic (v4)", fill=NAVY, font=f_body)
    draw.text((cx - 75, cy + 8), "Cross-Peer Verification", fill=DARK_TEXT, font=f_sub)

    # Finalizer Bottom
    fx, fy = 500, 465
    draw_rounded_rect(draw, (fx - 100, fy - 25, fx + 100, fy + 25), LIGHT_GRAY, BORDER_GRAY, 2, 8)
    draw.text((fx - 70, fy - 12), "Finalizer (v5)", fill=DARK_TEXT, font=f_body)
    draw.text((fx - 70, fy + 6), "Authoritative Sink", fill=MUTED_TEXT, font=f_sub)

    # Edges
    draw_arrow(draw, (px - 50, py + 30), (rx + 40, ry - 30), BLUE, 2, 8)
    draw_arrow(draw, (px + 50, py + 30), (ax - 40, ay - 30), BLUE, 2, 8)
    draw_arrow(draw, (rx + 40, ry + 30), (cx - 50, cy - 30), TEAL, 2, 8)
    draw_arrow(draw, (ax - 40, ay + 30), (cx + 50, cy - 30), PURPLE, 2, 8)
    draw_arrow(draw, (cx, cy + 30), (fx, fy - 25), ORANGE, 2, 8)

    img.save(os.path.join(OUTPUT_DIR, "graph_topology.png"), "PNG")

# 6. SYSTEM ARCHITECTURE
def make_system_architecture():
    img = Image.new("RGBA", (1200, 520), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(22, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "MultiAgentTopologyEval: End-to-End System Architecture", fill=NAVY, font=f_title)
    draw.text((50, 55), "Modular six-layer architecture isolating benchmark tasks, topology orchestration, providers, guardrails, and deterministic evaluation", fill=MUTED_TEXT, font=get_font(13))

    layers = [
        ("1. Benchmark Suite", "35 Benchmark Tasks\n5 Task Categories\nStrict Constraints C\nAnti-Leakage Strip", LIGHT_ORANGE, ORANGE),
        ("2. Topology Hub", "Single (Control)\nChain (Linear SOP)\nStar (Hub-Spoke)\nTree (Hierarchy)\nGraph (Mesh)", LIGHT_BLUE, BLUE),
        ("3. Agent Core", "BaseAgent Abstraction\nPlanner & Researcher\nAnalyst & Critic\nFinalizer Sink\nState & Message Log", LIGHT_TEAL, TEAL),
        ("4. Provider Layer", "Google Gemini 3.1\nCohere Command A+\nGroq Llama-3.3-70B\nDeterministic Mock\nUniversal Adapter", LIGHT_PURPLE, PURPLE),
        ("5. Guardrails & Safety", "Step Limit (K <= 20)\nCost Cap ($0.50/run)\nRetry & Exponential Backoff\nError Taxonomy Engine", (254, 235, 226), (197, 48, 48)),
        ("6. Hybrid Evaluator", "Deterministic Regex Audit\nProperty Matching (PMR)\nToken & Latency Telemetry\nStatistical Tests (Cohen's d)\nStreamlit UI & CSV Logs", (240, 253, 244), (22, 163, 74))
    ]

    box_w = 170
    box_h = 240
    gap = 25
    x_start = 35
    y = 120

    for i, (title, content, fill, border) in enumerate(layers):
        x = x_start + i * (box_w + gap)
        draw_rounded_rect(draw, (x, y, x + box_w, y + box_h), fill, border, 2, 8)
        draw.text((x + 10, y + 15), title, fill=NAVY, font=f_body)
        
        lines = content.split("\n")
        line_y = y + 50
        for line in lines:
            draw.text((x + 10, line_y), f"• {line}", fill=DARK_TEXT, font=f_sub)
            line_y += 24

        if i < len(layers) - 1:
            arr_start = (x + box_w, y + box_h // 2)
            arr_end = (x + box_w + gap, y + box_h // 2)
            draw_arrow(draw, arr_start, arr_end, BLUE, 3, 10)

    # Anti-leakage quarantined reference link
    draw.line([(x_start + box_w // 2, y + box_h), (x_start + box_w // 2, y + box_h + 60), 
               (x_start + 5 * (box_w + gap) + box_w // 2, y + box_h + 60), (x_start + 5 * (box_w + gap) + box_w // 2, y + box_h)],
              fill=ORANGE, width=2)
    draw.text((400, y + box_h + 68), "Quarantined Ground-Truth References (y*, P) Dispatched Solely to Evaluator (Anti-Leakage)", fill=ORANGE, font=get_font(12, True))

    img.save(os.path.join(OUTPUT_DIR, "system_architecture.png"), "PNG")

# 7. EVALUATION PIPELINE
def make_eval_pipeline():
    img = Image.new("RGBA", (1000, 500), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "Deterministic Evaluation Pipeline & Scoring Flow", fill=NAVY, font=f_title)
    draw.text((50, 52), "Data flow from raw architecture execution through deterministic regex auditing to multi-metric scoring", fill=MUTED_TEXT, font=get_font(13))

    steps = [
        ("1. Architecture Execution", "ArchitectureResult Dataclass:\n• Synthesized Answer y_hat\n• Step Latency Delta t\n• Token Usage (Prompt & Comp)\n• Chronological AgentMessage Log", 70, 120, 240, 180, LIGHT_BLUE, BLUE),
        ("2. Hybrid Evaluator", "Deterministic Rule Engine:\n• Regex Numerical Extraction\n• Boundary Compliance Check\n• Mandatory Keyword Audit\n• Optional LLM-as-a-Judge", 380, 120, 240, 180, LIGHT_TEAL, TEAL),
        ("3. Statistical Analytics", "Scoring & Persistence:\n• CSR = Sum(1{c_i}) / |C|\n• PMR = Sum(1{rho_j}) / |P|\n• Composite Score S = a*CSR + (1-a)*PMR\n• Effect Size d & CSV Export", 690, 120, 240, 180, (240, 253, 244), (22, 163, 74))
    ]

    for title, content, x, y, w, h, fill, border in steps:
        draw_rounded_rect(draw, (x, y, x + w, y + h), fill, border, 2, 8)
        draw.text((x + 12, y + 15), title, fill=NAVY, font=f_body)
        lines = content.split("\n")
        line_y = y + 45
        for line in lines:
            draw.text((x + 12, line_y), line, fill=DARK_TEXT, font=f_sub)
            line_y += 22

    draw_arrow(draw, (310, 210), (380, 210), BLUE, 3, 10)
    draw_arrow(draw, (620, 210), (690, 210), TEAL, 3, 10)

    # Anti-leakage annotation
    draw_rounded_rect(draw, (380, 340, 620, 440), LIGHT_ORANGE, ORANGE, 2, 6)
    draw.text((395, 355), "Anti-Leakage Quarantine", fill=(194, 65, 12), font=f_body)
    draw.text((395, 380), "Ground-truth answers are strictly quarantined\nand injected ONLY at Step 2.", fill=DARK_TEXT, font=f_sub)
    draw_arrow(draw, (500, 340), (500, 300), ORANGE, 2, 8)

    img.save(os.path.join(OUTPUT_DIR, "evaluation_pipeline.png"), "PNG")

# 8. EXPERIMENTAL WORKFLOW
def make_exp_workflow():
    img = Image.new("RGBA", (1100, 380), WHITE)
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_body = get_font(13, True)
    f_sub = get_font(11, False)

    draw.text((50, 25), "Controlled Experimental Workflow & Matrix Execution", fill=NAVY, font=f_title)
    draw.text((50, 52), "Standardized execution lifecycle guaranteeing reproducibility across cloud models and baselines", fill=MUTED_TEXT, font=get_font(13))

    phases = [
        ("Phase 1: Ingestion", "Select Task Suite\nAnti-Leakage Strip\nBudget Preview", LIGHT_ORANGE, ORANGE),
        ("Phase 2: Execution", "Instantiate Topology\nDispatch Channel\nEnforce Guardrails", LIGHT_BLUE, BLUE),
        ("Phase 3: Telemetry", "Prompt/Comp Tokens\nReal Latency Profiling\nFault Classification", LIGHT_PURPLE, PURPLE),
        ("Phase 4: Evaluation", "Regex Constraint Audit\nProperty Matching\nTask Score S", LIGHT_TEAL, TEAL),
        ("Phase 5: Reporting", "JSON/CSV Serialization\nStreamlit Dashboard\nHypothesis Testing", (240, 253, 244), (22, 163, 74))
    ]

    x_start = 50
    w = 175
    h = 160
    gap = 30
    y = 120

    for i, (title, content, fill, border) in enumerate(phases):
        x = x_start + i * (w + gap)
        draw_rounded_rect(draw, (x, y, x + w, y + h), fill, border, 2, 8)
        draw.text((x + 12, y + 18), title, fill=NAVY, font=f_body)
        lines = content.split("\n")
        line_y = y + 55
        for line in lines:
            draw.text((x + 12, line_y), f"• {line}", fill=DARK_TEXT, font=f_sub)
            line_y += 24

        if i < len(phases) - 1:
            draw_arrow(draw, (x + w, y + h // 2), (x + w + gap, y + h // 2), BLUE, 3, 10)

    img.save(os.path.join(OUTPUT_DIR, "experimental_workflow.png"), "PNG")

if __name__ == "__main__":
    make_single()
    make_chain()
    make_star()
    make_tree()
    make_graph()
    make_system_architecture()
    make_eval_pipeline()
    make_exp_workflow()
    print("All 8 high-resolution diagram PNGs generated successfully in seminar_submission/Figures/")


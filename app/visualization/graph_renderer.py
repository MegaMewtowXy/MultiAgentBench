"""
Graph Visualization Module for Agent Communication Topologies.
Renders Graphviz directed graphs illustrating agent nodes, roles, and inter-agent message edges.
"""

from typing import List, Tuple, Optional, Dict, Any

def render_topology_graph(
    architecture_name: str,
    communication_edges: Optional[List[Tuple[str, str]]] = None,
    agent_states: Optional[Dict[str, Any]] = None
):
    """
    Constructs a Graphviz Digraph object representing the execution topology.

    Returns:
        graphviz.Digraph object suitable for st.graphviz_chart rendering.
    """
    try:
        import graphviz
    except ImportError:
        return None

    dot = graphviz.Digraph(comment=f"{architecture_name.upper()} Topology Graph")
    dot.attr(rankdir='LR', size='8,5', bgcolor='transparent')
    dot.attr('node', shape='box', style='filled,rounded', fontname='Inter', fontsize='11')

    # Color palette for agent roles
    role_colors = {
        "planner": "#3B82F6",    # Blue
        "researcher": "#10B981", # Emerald Green
        "analyst": "#F59E0B",    # Amber/Yellow
        "critic": "#EF4444",     # Red
        "finalizer": "#8B5CF6",  # Purple
        "user": "#6B7280",       # Gray
        "workers": "#0D9488"     # Teal
    }

    arch_name = architecture_name.lower()

    if arch_name == "single":
        dot.node("single_agent", "Single Agent\n(Baseline Solver)", fillcolor="#8B5CF6", fontcolor="white")
        dot.node("user", "User / Benchmark", fillcolor="#6B7280", fontcolor="white")
        dot.edge("user", "single_agent", label="task prompt")
        dot.edge("single_agent", "user", label="final solution")

    elif arch_name == "star":
        dot.node("planner", "Central Coordinator\n(Planner)", fillcolor="#3B82F6", fontcolor="white")
        dot.node("researcher", "Domain Researcher", fillcolor="#10B981", fontcolor="white")
        dot.node("analyst", "Quantitative Analyst", fillcolor="#F59E0B", fontcolor="white")
        dot.node("critic", "Solution Critic", fillcolor="#EF4444", fontcolor="white")
        dot.node("finalizer", "Output Finalizer", fillcolor="#8B5CF6", fontcolor="white")

        # Edges
        dot.edge("planner", "researcher", label="delegate research")
        dot.edge("planner", "analyst", label="delegate analysis")
        dot.edge("planner", "critic", label="delegate review")

        dot.edge("researcher", "finalizer", label="research output")
        dot.edge("analyst", "finalizer", label="analysis output")
        dot.edge("critic", "finalizer", label="critique output")

    elif arch_name == "chain":
        dot.node("planner", "Stage 1: Planner", fillcolor="#3B82F6", fontcolor="white")
        dot.node("researcher", "Stage 2: Researcher", fillcolor="#10B981", fontcolor="white")
        dot.node("analyst", "Stage 3: Analyst", fillcolor="#F59E0B", fontcolor="white")
        dot.node("critic", "Stage 4: Critic", fillcolor="#EF4444", fontcolor="white")
        dot.node("finalizer", "Stage 5: Finalizer", fillcolor="#8B5CF6", fontcolor="white")

        dot.edge("planner", "researcher", label="plan context")
        dot.edge("researcher", "analyst", label="findings")
        dot.edge("analyst", "critic", label="quant analysis")
        dot.edge("critic", "finalizer", label="critique")

    elif arch_name == "tree":
        dot.node("root", "Root Coordinator", fillcolor="#3B82F6", fontcolor="white")
        dot.node("r_lead", "Research Lead", fillcolor="#10B981", fontcolor="white")
        dot.node("a_lead", "Analysis Lead", fillcolor="#F59E0B", fontcolor="white")
        dot.node("r_sub", "Research Worker", fillcolor="#0D9488", fontcolor="white")
        dot.node("c_sub", "Critic Worker", fillcolor="#EF4444", fontcolor="white")
        dot.node("finalizer", "Finalizer Sink", fillcolor="#8B5CF6", fontcolor="white")

        dot.edge("root", "r_lead")
        dot.edge("root", "a_lead")
        dot.edge("r_lead", "r_sub")
        dot.edge("a_lead", "c_sub")
        dot.edge("r_sub", "finalizer")
        dot.edge("c_sub", "finalizer")

    elif arch_name == "graph":
        roles = ["planner", "researcher", "analyst", "critic", "finalizer"]
        for r in roles:
            color = role_colors.get(r, "#3B82F6")
            dot.node(r, f"Node: {r.capitalize()}", fillcolor=color, fontcolor="white")

        edges = communication_edges or [
            ("planner", "researcher"),
            ("planner", "analyst"),
            ("researcher", "critic"),
            ("analyst", "critic"),
            ("critic", "finalizer")
        ]
        for src, dst in edges:
            dot.edge(src, dst, label="mesh message")

    return dot

# Implementation Mapping: MultiAgentBench vs. Our Project

This document maps components of the ACL 2025 paper **"MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents"** to our project implementation, ensuring clear academic transparency regarding what is reproduced, simplified, modified, extended, or added as new features.

## Mapping Table

| Paper Component | Original Paper (ACL 2025) | Our Implementation | Status | Notes / Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Coordination Topologies** | Evaluates Star, Chain, Tree, and Graph topologies in MARBLE | Implements Single-Agent baseline, Star, Chain, Tree, and configurable Graph topologies | **REPRODUCED** | Preserves core topology definitions $G=(A, E)$ for comparative analysis. |
| **Agent Roles** | Planners, Actors, Critics, Domain Specialists | Role-based agents: Planner, Researcher, Analyst, Critic, Finalizer | **REPRODUCED** | Specialized prompts and functional responsibilities assigned to each role node. |
| **Benchmark Tasks** | Minecraft, Werewolf, Bargaining, Research, SQL, Coding | API-driven benchmark across 7 task categories: Planning, Constraint Satisfaction, Synthesis, Multi-step Reasoning, Decision Making, Collaboration, Coding | **SIMPLIFIED** | Simplified from heavy domain engines (Minecraft/Werewolf) to API-executable structured reasoning tasks for CPU/laptop execution. |
| **LLM Provider Abstraction** | OpenAI API & local open-source models via custom wrappers | Universal Provider abstraction: Groq, Gemini, OpenAI, and MockProvider | **EXTENDED** | Adds multi-provider support with fallback engineering and keyless offline testing. |
| **Offline Testing / Mock Mode** | Requires live model checkpoints or API calls for all runs | Deterministic Mock Mode producing realistic agent logs and metrics without API keys | **NEW** | Enables offline demonstration, UI validation, and cost-free student experimentation. |
| **Evaluation Engine** | Milestone-based KPIs, LLM judges, failure mode profiling (MAST) | Hybrid Evaluation: Deterministic constraint/pattern matching + LLM-based coordination scoring | **MODIFIED** | Retains objective evaluation priority while adapting milestone tracking for text-based tasks. |
| **Safety & Cost Guardrails** | Configurable step limits | Comprehensive protection: Call limits, token caps, timeout limits, dry-run estimates, and emergency loops break | **EXTENDED** | Designed specifically for student budget protection and laptop resource constraints. |
| **Visualization & UI** | Python scripts generating static matplotlib/seaborn plots | Interactive Streamlit dashboard with dynamic Graphviz interaction graphs and comparative analytics | **EXTENDED** | Provides real-time experiment execution, topology rendering, and interactive results analysis. |
| **Demonstration Mode** | CLI / script execution | Live seminar demo interface comparing all topologies side-by-side on custom user prompts | **NEW** | Added for MCA technical seminar live presentation. |
| **Memory & Context** | Shared blackboard, short-term message logs | Private message memory, explicit inter-agent message passing buffers, trajectory logging | **SIMPLIFIED** | Clean, lightweight memory structure preventing token bloat on API context windows. |

## Status Summary Definitions

- **REPRODUCED:** Core research concepts and architectural structures directly implemented as described in the paper.
- **SIMPLIFIED:** Complex multi-domain external environments adapted into lightweight, API-friendly task formats suitable for CPU execution.
- **MODIFIED:** Evaluation routines tailored for multi-provider API interaction and deterministic baseline comparison.
- **EXTENDED:** Capabilities added beyond the original paper scope (multi-provider support, cost guardrails, interactive Streamlit UI).
- **NEW:** Features unique to our MCA project (Mock Mode, Live Seminar Demonstration UI).

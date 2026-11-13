"""
sec_h_presentation_defense.py
Section H: Seminar Presentation Delivery & Defense Masterclass.
Timing breakdown, slide-by-slide choreography, non-verbal presence,
and tactical techniques for handling challenging viva questions.
"""

from docx.shared import Pt, Inches

def add_section_h(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_main_sec("SECTION H", "SEMINAR PRESENTATION DELIVERY & VIVA DEFENSE MASTERCLASS")

    add_p("A technically brilliant project can receive mediocre marks if delivered poorly, while a well-structured, confident presentation commands respect. This section provides an actionable blueprint for pacing your 25–30 minute seminar talk, navigating tricky examiner interactions, and defending your research with poise.")

    add_sub_sec("H.1", "25–30 Minute Presentation Time Allocation Matrix")
    add_p("To avoid running overtime (a common penalty in academic seminars), rehearse to the following strict timing budget across the 30 slides:")
    add_bullet("Phase 1: Introduction & Motivation (Slides 1–5) -> 4.5 Minutes (Running: 4.5m). Establish the agentic revolution, multi-agent coordination, and the core research question.")
    add_bullet("Phase 2: Theoretical Foundations & Models (Slides 6–10) -> 5.0 Minutes (Running: 9.5m). Demonstrate deep mastery of Transformers, Scaled Dot-Product Attention, and foundation models (BERT, T5, GPT, PaLM, LLaMA, Gemini).")
    add_bullet("Phase 3: Literature Review & Gap Analysis (Slides 11–13) -> 3.5 Minutes (Running: 13.0m). Cover 44 peer-reviewed citations, distinguish from Zhu et al. (ACL 2025 MultiAgentBench), and identify the 6 research gaps.")
    add_bullet("Phase 4: Proposed Framework & 5 Topologies (Slides 14–19) -> 6.0 Minutes (Running: 19.0m). Present the 6 subsystems, Figure 7.1 architecture, and deep dive into SINGLE, CHAIN, STAR, TREE, GRAPH with Figure diagrams.")
    add_bullet("Phase 5: Metrics & Experimental Methodology (Slides 20–24) -> 4.5 Minutes (Running: 23.5m). Detail CSR, PMR, Task Score S, cost models, the 7 benchmark tasks, and controlled variables (T=0.70).")
    add_bullet("Phase 6: Empirical Results & Analysis (Slides 25–28) -> 4.5 Minutes (Running: 28.0m). Present the 175 live executions, Table 12.1 and 12.2 data, the Baseline Efficiency Paradox, and cascading failure autopsies.")
    add_bullet("Phase 7: Practical Guidelines & Conclusion (Slides 29–30) -> 2.0 Minutes (Running: 30.0m). Deliver the 4 engineering deployment guidelines, acknowledge limitations, and conclude firmly.")

    add_sub_sec("H.2", "Tactical Verbal Script: How to Handle Difficult Questions")
    add_p("When an examiner challenges you or asks a complex question, use structured response templates:", bold=True)
    add_bullet("Technique 1: The 'Direct Answer First' Rule. Never begin with background fluff. State your conclusion in the first 5 words, then elaborate: 'Yes, sir, in our empirical trials that was indeed observed...' or 'No, sir, that is mathematically prevented because...'")
    add_bullet("Technique 2: The 'Empirical Grounding' Anchor. When faced with subjective opinions ('Don't you think tree topologies are always better?'), anchor your response in real numbers: 'Intuitively one might expect that, sir, but across our 175 live cloud executions with Gemini, Cohere, and Groq, Tree topologies consistently scored lower (S = 0.7714 vs 0.9429) due to information degradation across hierarchical tiers.'")
    add_bullet("Technique 3: Handling Gaps Honestly. If asked about something not in your scope (e.g. 'Did you test multi-modal video agents?'): 'That is an insightful question, sir. In this seminar, we bounded our scope strictly to natural language reasoning and code synthesis tasks to maintain controlled regex evaluation. Extending MultiAgentTopologyEval to multi-modal video pipelines is an active item in our future research roadmap.'")
    add_bullet("Technique 4: Defending Against the Zhu et al. Ambiguity. If an examiner says 'Isn't this already done in the ACL 2025 paper?': 'We are glad you brought up Zhu et al., sir. We explicitly cite Zhu et al. (ACL 2025) as reference [6]. However, Zhu et al. focused on game-theoretic social dynamics—evaluating deception and betrayal in Werewolf and Minecraft. In contrast, our work evaluates systems engineering trade-offs of communication topologies under strict quantitative constraints, token economics, and operational failure modes.'")

    add_sub_sec("H.3", "Physical Stance, Projection, and Presentation Presence")
    add_bullet("1. Eye Contact Distribution: Divide your audience into three zones (Left panel, Center professors, Right audience). Spend 60% of eye contact on the evaluators, rotating smoothly every 20–30 seconds.")
    add_bullet("2. Slide Pointing: Do not read slides verbatim. Look at the slide for 1 second to register the key diagram or bullet, then turn fully back to the audience to deliver your verbal explanation.")
    add_bullet("3. Pacing & Vocal Variety: Slow down deliberately during mathematical formulations (e.g. attention scaling factor sqrt(d_k) or Task Score S equation). This signals confidence and deep technical mastery.")

    add_callout("Final Seminar Mindset",
                "You have executed 175 live experiments, built an extensible object-oriented framework with 100% test pass rate, audited 44 academic papers, and documented an exhaustive 50+ page report. You know this codebase and data better than anyone in the room. Deliver your findings with humility, scientific rigor, and unshakeable confidence.")

print("Section H module written.")


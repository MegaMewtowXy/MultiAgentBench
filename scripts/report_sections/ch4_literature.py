"""
ch4_literature.py
Generates Chapter 4: Literature Review for the MCA Technical Seminar Report.
Synthesizes 44 audited peer-reviewed academic references across 10 structured sections.
"""

def add_chapter_4(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_chapter_heading(4, "LITERATURE REVIEW")

    add_sec("4.1", "Foundational Architecture and Representation Learning")
    add_p("The modern era of deep learning for natural language processing began with the introduction of the Transformer architecture by Vaswani et al. (NeurIPS 2017) [2]. In 'Attention Is All You Need', the authors eliminated recurrent and convolutional layers entirely, demonstrating that a sequence-to-sequence model relying exclusively on multi-head self-attention could achieve state-of-the-art translation performance while reducing training time by orders of magnitude through parallelization.")
    add_p("Devlin et al. (NAACL 2019) [3] established the paradigm of pre-trained contextualized representations with BERT (Bidirectional Encoder Representations from Transformers). By training deep bidirectional representations via Masked Language Modeling (MLM) and Next Sentence Prediction (NSP), BERT demonstrated that a single pre-trained model could achieve state-of-the-art results across eleven downstream NLP tasks via lightweight fine-tuning, cementing transfer learning as the standard NLP methodology.")
    add_p("Raffel et al. (JMLR 2020) [4] unified the field with T5 (Text-to-Text Transfer Transformer). The authors formalized every NLP task—whether classification, translation, summarization, or question answering—as a text-to-text mapping within an encoder-decoder architecture, introducing span-corruption pretraining and establishing comprehensive empirical scaling benchmarks.")

    add_sec("4.2", "Large Language Models and Few-Shot Scaling Laws")
    add_p("In 2020, Brown et al. (NeurIPS 2020) [1] published 'Language Models are Few-Shot Learners', introducing GPT-3 (175 billion parameters). The authors demonstrated that scaling autoregressive language models yields remarkable 'emergent abilities'. Without modifying weights or performing task-specific gradient fine-tuning, GPT-3 demonstrated in-context learning, matching or outperforming fine-tuned models on complex translation, arithmetic, and reasoning tasks purely through natural language prompting and few-shot demonstrations.")
    add_p("To resolve the misalignment between pre-training next-token prediction and user intent, Ouyang et al. (NeurIPS 2022) [5] introduced InstructGPT. Utilizing Reinforcement Learning from Human Feedback (RLHF), the authors trained reward models on human preference rankings and fine-tuned GPT-3 via Proximal Policy Optimization (PPO), dramatically reducing toxicity and hallucination while improving instruction adherence.")
    add_p("Chowdhery et al. (JMLR 2023) [7] presented PaLM (Pathways Language Model), scaling dense decoder-only Transformers to 540 billion parameters across 6,144 TPU chips. PaLM demonstrated discontinuous emergent reasoning jumps on multi-step arithmetic (GSM8K) and code synthesis, introducing SwiGLU activations and Multi-Query Attention (MQA).")
    add_p("Touvron et al. (Meta 2023) [8] released LLaMA, open-sourcing competitive foundation models (7B to 65B) trained on trillions of publicly available tokens, proving that efficient, publicly accessible models could democratize LLM research. The Gemini Team (Google 2024) [9] extended foundation models to native multimodality, establishing highly optimized reasoning engines across Flash and Pro tiers.")

    add_sec("4.3", "Emergent Reasoning and Chain-of-Thought Prompting")
    add_p("While scaled models excelled at factual retrieval, multi-step symbolic and mathematical reasoning remained challenging under standard few-shot prompting. Wei et al. (NeurIPS 2022) [10] resolved this with 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models'. By providing demonstrations where intermediate natural language reasoning steps preceded final answers, the authors unlocked latent multi-step problem-solving abilities on mathematical benchmarks (GSM8K, SVAMP) and symbolic manipulation tasks.")
    add_p("Kojima et al. (NeurIPS 2022) [11] showed in 'Large Language Models are Zero-Shot Reasoners' that chain-of-thought is an inherent latent capability: simply appending the prompt 'Let's think step by step' induced zero-shot multi-step reasoning without requiring few-shot exemplars.")
    add_p("Wang et al. (ICLR 2023) [12] introduced Self-Consistency, demonstrating that sampling diverse reasoning paths from an LLM at non-zero temperature and taking the marginal majority vote significantly boosts reasoning accuracy over greedy decoding. Zhou et al. (ICLR 2023) [13] proposed Least-to-Most prompting, decomposing complex problems into sequential sub-questions solved sequentially.")
    add_p("Gao et al. (ICML 2023) [14] introduced PAL (Program-Aided Language Models), and Chen et al. (EMNLP 2023) [15] introduced PoT (Program-of-Thoughts), offloading symbolic arithmetic steps to a Python interpreter to eliminate calculation errors.")

    add_sec("4.4", "Non-Linear Thought Search and Deliberative Planning")
    add_p("Recognizing that linear Chain-of-Thought cannot perform lookahead, state evaluation, or backtracking, Yao et al. (NeurIPS 2023) [16] introduced Tree of Thoughts (ToT). ToT formalizes reasoning as a search over a tree where each node represents a coherent thought unit. By evaluating the heuristic promise of candidate branches via self-assessment prompts, agents execute Breadth-First Search (BFS) or Depth-First Search (DFS) with backtracking, dramatically outperforming CoT on combinatorial problems like the Game of 24 and Creative Writing.")
    add_p("Besta et al. (AAAI 2024) [17] generalized this to Graph of Thoughts (GoT), modeling deliberative reasoning as an arbitrary directed graph. GoT allows distinct thought branches to be merged, enables cyclic feedback refinement, and provides fine-grained control over cognitive graph operations.")

    add_sec("4.5", "Self-Refinement and Evaluative Feedback Loops")
    add_p("Shinn et al. (NeurIPS 2023) [18] presented Reflexion, a verbal reinforcement framework where agents evaluate past trajectory failures, generate linguistic reflections, and store them in an episodic memory buffer to condition subsequent attempts, achieving substantial gains on HumanEval and AlfWorld.")
    add_p("Madaan et al. (NeurIPS 2023) [19] introduced Self-Refine, demonstrating that LLMs can iteratively critique and refine their own outputs across code optimization, math reasoning, and dialogue generation without external training signals.")
    add_p("Gou et al. (ICLR 2024) [20] proposed CRITIC, conditioning the critique process on external tool feedback (search engines and code linters) to prevent self-refinement from confirming hallucinated premises.")

    add_sec("4.6", "Autonomous Agent Architecture, Tool Use, and Interactive Environments")
    add_p("Schick et al. (NeurIPS 2023) [22] introduced Toolformer, showing that LLMs can teach themselves in a self-supervised manner to call external APIs (calculators, search engines, translation tools) via text delimiters. Qin et al. (ICLR 2024) [23] released ToolLLM, scaling tool manipulation to over 16,000 real-world REST APIs.")
    add_p("Yao et al. (ICLR 2023) [24] published ReAct, formalizing the synergistic alternating loop of reasoning ('Thought') and action execution ('Action' -> 'Observation'), establishing the foundation for interactive agent workflows.")
    add_p("Park et al. (UIST 2023) [21] presented 'Generative Agents: Interactive Simulacra of Human Behavior', deploying 25 autonomous LLM agents in a sandbox RPG town. The authors introduced architectural memory retrieval based on Recency, Importance, and Relevance, alongside periodic reflection and planning modules.")
    add_p("Wang et al. (ACL 2024) [35] proposed Plan-and-Solve (PS) prompting, improving multi-step problem solving by first outlining a structured plan before executing sub-tasks.")

    add_sec("4.7", "Multi-Agent Collaboration, Persona Specialization, and Social Simulation")
    add_p("Li et al. (NeurIPS 2023) [27] introduced CAMEL (Communicative Agents for 'Mind' Exploration of Large Language Model Society), proposing role-playing communication between AI User and AI Assistant agents using inception prompting to prevent dialogue loops.")
    add_p("Wu et al. (COLM 2024) [25] released AutoGen, a multi-agent framework enabling customizable, conversable agents that integrate LLMs, human input, and tool execution across flexible multi-agent conversation patterns.")
    add_p("Hong et al. (ICLR 2024) [26] developed MetaGPT, encoding Standard Operating Procedures (SOPs) from software engineering into sequential multi-agent pipelines (Product Manager, Architect, Project Manager, Engineer, QA), showing that structured role handoffs reduce communication chatter.")
    add_p("Chen et al. (EMNLP 2024) [29] presented AgentVerse, exploring dynamic agent team assembly and automated role assignment for diverse collaborative tasks.")
    add_p("Qian et al. (ACL 2024) [30] introduced ChatDev, modeling the entire software development lifecycle as communicative agent dialogue phases, generating full executable code repositories through virtual team collaboration.")
    add_p("Du et al. (ICML 2024) [28] and Yin et al. (AAAI 2024) [38] established that multi-agent debate protocols significantly reduce individual model hallucination and improve factual consensus.")

    add_sec("4.8", "Agent Benchmarks and Evaluation Frameworks")
    add_p("As LLM agents transitioned into interactive environments, traditional static NLP benchmarks (MMLU, GSM8K) proved inadequate (Chang et al., ACM TIST 2024 [44]). A wave of interactive agent benchmarks emerged:")
    add_bullet("AgentBench (Liu et al., ICLR 2024 [39]): Evaluated single agents across eight digital environments (OS shells, databases, web browsing, house games).")
    add_bullet("SWE-bench (Jimenez et al., ICLR 2024 [40]): Benchmarked agents on resolving real-world Python GitHub pull requests and issues against unit test suites.")
    add_bullet("WebArena (Zhou et al., ICLR 2024 [41]): Evaluated end-to-end web navigation across e-commerce, forums, and CMS environments.")
    add_bullet("GAIA (Mialon et al., ICLR 2024 [42]): Benchmarked general AI assistant tasks requiring multimodal comprehension, web search, and tool execution.")
    add_bullet("OSWorld (Xie et al., NeurIPS 2024 [43]): Evaluated multimodal agents performing real-world operating system tasks on Ubuntu desktops.")

    add_sec("4.9", "The Milestone Benchmark: MultiAgentBench (Zhu et al., ACL 2025)")
    add_p("The foundational multi-agent benchmark directly preceding this seminar is MultiAgentBench, published by Kunlun Zhu, Hongyi Du, Zhaochen Hong et al. in the Proceedings of the Association for Computational Linguistics (ACL 2025) [6].")
    add_p("MultiAgentBench established the MARBLE coordination engine, introducing the first comprehensive evaluation framework for LLM multi-agent systems across both collaborative environments (academic research writing, software coding, database administration, and cooperative Minecraft building) and competitive environments (Werewolf social deduction, two-player resource bargaining).")
    add_p("The authors evaluated agents using milestone-based Key Performance Indicators (KPIs) and multi-agent behavioral profiling (MAST). Their empirical findings demonstrated that multi-agent collaboration consistently outperformed single agents in domain environments where tasks required heterogeneous tool sets or adversarial deception.")
    add_p("Relevance to MultiAgentTopologyEval: MultiAgentTopologyEval takes direct inspiration from MultiAgentBench but addresses complementary, unexamined operational dimensions. While MultiAgentBench evaluated systems inside complex, compute-heavy game simulators and tracked macro milestone flags, MultiAgentTopologyEval strictly isolates communication topology as the primary controlled variable, captures decoupled prompt/completion token consumption, measures step-level wall-clock latency, enforces strict deterministic constraint checking, and profiles systems-level runtime failures in a lightweight, 100% reproducible testbed.")

    add_sec("4.10", "Literature Synthesis and Thematic Evolution")
    add_p("The academic literature demonstrates a clear evolutionary trajectory: from the Transformer's self-attention mechanism [2] to emergent scaling laws [1], to single-agent deliberative prompting (CoT [10], ReAct [24], ToT [16]), to multi-agent collaborative frameworks (MetaGPT [26], AutoGen [25]), and finally to multi-agent benchmarking (MultiAgentBench [6]). However, this synthesis highlights a conspicuous gap: the lack of controlled empirical evaluations that isolate interaction topology under unified prompt and model constraints.")

print("Chapter 4 module written.")


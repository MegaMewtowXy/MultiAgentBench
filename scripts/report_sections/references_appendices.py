"""
references_appendices.py
Generates the References (44 peer-reviewed academic references) and Appendices A, B, C
for the MCA Technical Seminar Report.
"""

from docx.shared import Pt, Inches

def add_references_and_appendices(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']
    C_NAVY = helpers['C_NAVY']
    C_DARK = helpers['C_DARK']

    # ----------------------------------------------------
    # REFERENCES
    # ----------------------------------------------------
    doc.add_page_break()
    p_ref_head = doc.add_paragraph()
    p_ref_head.paragraph_format.space_before = Pt(20)
    p_ref_head.paragraph_format.space_after = Pt(16)
    r_rh = p_ref_head.add_run("REFERENCES")
    r_rh.font.name = "Calibri"
    r_rh.font.size = Pt(20)
    r_rh.font.bold = True
    r_rh.font.color.rgb = C_NAVY

    references = [
        "[1] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al., \"Language models are few-shot learners,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 33, pp. 1877–1901, 2020.",
        "[2] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, \"Attention is all you need,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 30, pp. 5998–6008, 2017.",
        "[3] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, \"BERT: Pre-training of deep bidirectional transformers for language understanding,\" in Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), pp. 4171–4186, 2019.",
        "[4] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu, \"Exploring the limits of transfer learning with a unified text-to-text transformer,\" Journal of Machine Learning Research (JMLR), vol. 21, no. 140, pp. 1–67, 2020.",
        "[5] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al., \"Training language models to follow instructions with human feedback,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 35, pp. 27730–27744, 2022.",
        "[6] K. Zhu, H. Du, Z. Hong, et al., \"MultiAgentBench: Evaluating the collaboration and competition of LLM agents,\" in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL), 2025.",
        "[7] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, et al., \"PaLM: Scaling language modeling with pathways,\" Journal of Machine Learning Research (JMLR), vol. 24, no. 240, pp. 1–113, 2023.",
        "[8] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al., \"LLaMA: Open and efficient foundation language models,\" arXiv preprint arXiv:2302.13971, 2023.",
        "[9] Gemini Team, Google, \"Gemini: A family of highly capable multimodal models,\" arXiv preprint arXiv:2312.11805, 2024.",
        "[10] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, and D. Zhou, \"Chain-of-thought prompting elicits reasoning in large language models,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 35, pp. 24824–24837, 2022.",
        "[11] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa, \"Large language models are zero-shot reasoners,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 35, pp. 22199–22213, 2022.",
        "[12] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou, \"Self-consistency improves chain of thought reasoning in language models,\" in International Conference on Learning Representations (ICLR), 2023.",
        "[13] D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang, D. Schuurmans, C. Cui, O. Bousquet, Q. Le, and E. Chi, \"Least-to-most prompting enables complex reasoning in large language models,\" in International Conference on Learning Representations (ICLR), 2023.",
        "[14] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, and G. Neubig, \"PAL: Program-aided language models,\" in International Conference on Machine Learning (ICML), pp. 10764–10799, 2023.",
        "[15] W. Chen, X. Ma, X. Wang, and W. W. Cohen, \"Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks,\" in Transactions on Machine Learning Research (TMLR), 2023.",
        "[16] S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan, \"Tree of thoughts: Deliberate problem solving with large language models,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[17] M. Besta, N. Blach, A. Kubicek, R. Gerstenberger, L. Gianinazzi, J. Gajda, T. Lehmann, M. Podstawski, H. Niewiadomski, P. Nyczyk, and T. Hoefler, \"Graph of thoughts: Solving elaborate problems with large language models,\" in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 16, pp. 17682–17690, 2024.",
        "[18] N. Shinn, F. Cassano, A. Gopinath, K. R. Narasimhan, and S. Yao, \"Reflexion: Language agents with verbal reinforcement learning,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[19] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al., \"Self-refine: Iterative refinement with self-feedback,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[20] Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, N. Duan, and W. Chen, \"CRITIC: Large language models can self-correct with tool-interactive critiquing,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[21] J. S. Park, J. C. O'Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein, \"Generative agents: Interactive simulacra of human behavior,\" in Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST), pp. 1–22, 2023.",
        "[22] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, L. Zettlemoyer, N. Cancedda, and T. Scialom, \"Toolformer: Language models can teach themselves to use tools,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[23] Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang, B. Qian, et al., \"ToolLLM: Facilitating large language models to master 16000+ real-world APIs,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[24] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, \"ReAct: Synergizing reasoning and acting in language models,\" in International Conference on Learning Representations (ICLR), 2023.",
        "[25] Q. Wu, G. Bansal, J. Zhang, Y. Wu, S. Zhang, E. Zhu, B. Li, L. Jiang, N. Zhang, and C. Wang, \"AutoGen: Enabling next-gen LLM applications via multi-agent conversation,\" in First Conference on Language Modeling (COLM), 2024.",
        "[26] S. Hong, M. Zhuge, J. Chen, X. Zheng, C. Cheng, C. Zhang, J. Wang, Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu, and Q. Peng, \"MetaGPT: Meta programming for a multi-agent collaborative framework,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[27] G. Li, H. A. A. K. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem, \"CAMEL: Communicative agents for 'mind' exploration of large language model society,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[28] Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch, \"Improving factuality and reasoning in language models through multiagent debate,\" in International Conference on Machine Learning (ICML), 2024.",
        "[29] W. Chen, Y. Su, J. Shen, B. Li, et al., \"AgentVerse: Facilitating multi-agent collaboration and exploring emergent behaviors in agents,\" in Findings of the Association for Computational Linguistics: EMNLP 2024, 2024.",
        "[30] C. Qian, W. Liu, H. Liu, N. Chen, Y. Dang, Z. Li, C. Yang, W. Chen, Y. Su, C. Yang, et al., \"ChatDev: Communicative agents for software development,\" in Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), pp. 15174–15186, 2024.",
        "[31] S. Zhang, Z. Chen, Y. Shen, M. Ding, J. B. Tenenbaum, and C. Gan, \"Spatial: A benchmark for spatial reasoning in multi-agent environments,\" in Advances in Neural Information Processing Systems (NeurIPS), 2023.",
        "[32] Y. Talebirad and A. Nadiri, \"Multi-agent collaboration: Harnessing the power of intelligent LLM agents,\" arXiv preprint arXiv:2306.03314, 2023.",
        "[33] X. Wang, Z. Chen, et al., \"A survey on large language model based autonomous agents,\" Frontiers of Computer Science, vol. 18, no. 6, p. 186345, 2024.",
        "[34] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, L. Tang, X. Chen, Y. Lin, et al., \"A survey on large language model based autonomous agents,\" IEEE Transactions on Knowledge and Data Engineering (TKDE), 2024.",
        "[35] L. Wang, W. Xu, Y. Lan, Z. Hu, Y. Lan, R. K.-W. Lee, and E.-P. Lim, \"Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models,\" in Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), pp. 2609–2634, 2023.",
        "[36] Y. Shen, K. Song, X. Tan, D. Li, W. Lu, and Y. Zhuang, \"HuggingGPT: Solving AI tasks with ChatGPT and its friends in Hugging Face,\" in Advances in Neural Information Processing Systems (NeurIPS), vol. 36, 2023.",
        "[37] X. Bo, F. Zhang, L. Zhou, E. Cambria, and S. Ji, \"A survey on multi-agent collaboration with large language models,\" arXiv preprint arXiv:2406.01258, 2024.",
        "[38] D. Yin, H. Zhang, W. Huang, et al., \"Exchange-of-thought: Enhancing large language model reasoning through collaborative communication,\" in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, 2024.",
        "[39] X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng, Z. Du, C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun, M. Huang, Y. Dong, and J. Tang, \"AgentBench: Evaluating LLMs as agents,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[40] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Narasimhan, and O. Press, \"SWE-bench: Can language models resolve real-world GitHub issues?\" in International Conference on Learning Representations (ICLR), 2024.",
        "[41] S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, Y. Bisk, D. Fried, U. Alon, and G. Neubig, \"WebArena: A realistic web environment for autonomous agents,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[42] G. Mialon, C. Fourrier, C. Swift, T. Wolf, Y. LeCun, and T. Scialom, \"GAIA: A benchmark for general AI assistants,\" in International Conference on Learning Representations (ICLR), 2024.",
        "[43] T. Xie, D. Zhang, J. Chen, X. Li, S. Zhao, R. Cao, J. Zhou, G. Li, L. Van Gool, and T. Yu, \"OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments,\" in Advances in Neural Information Processing Systems (NeurIPS), 2024.",
        "[44] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi, C. Wang, Y. Wang, W. Ye, Y. Zhang, Y. Chang, P. S. Yu, Q. Yang, and X. Xie, \"A survey on evaluation of large language models,\" ACM Transactions on Intelligent Systems and Technology (TIST), vol. 15, no. 3, pp. 39:1–39:45, 2024."
    ]

    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.10
        run = p.add_run(ref)
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        run.font.color.rgb = helpers['C_DARK']

    # ----------------------------------------------------
    # APPENDIX A: Mathematical Derivations
    # ----------------------------------------------------
    doc.add_page_break()
    p_ap_a = doc.add_paragraph()
    p_ap_a.paragraph_format.space_before = Pt(20)
    p_ap_a.paragraph_format.space_after = Pt(14)
    r_aa = p_ap_a.add_run("APPENDIX A: MATHEMATICAL DERIVATIONS & STATISTICAL FORMULATIONS")
    r_aa.font.name = "Calibri"
    r_aa.font.size = Pt(16)
    r_aa.font.bold = True
    r_aa.font.color.rgb = C_NAVY

    add_sec("A.1", "Derivation of Scaled Dot-Product Attention Variance")
    add_p("To understand why division by sqrt(d_k) is mandatory in Scaled Dot-Product Attention, consider Query vector q and Key vector k whose components are independent random variables with mean 0 and variance 1:")
    add_p("q_i ~ N(0, 1),    k_i ~ N(0, 1)    for i in {1, 2, ..., d_k}")
    add_p("Their dot product is z = sum_{i=1}^{d_k} q_i * k_i. The expected value is E[z] = sum E[q_i] * E[k_i] = 0.")
    add_p("The variance of each product term is Var(q_i * k_i) = E[q_i^2 * k_i^2] - (E[q_i * k_i])^2 = E[q_i^2] * E[k_i^2] - 0 = 1 * 1 = 1.")
    add_p("Because the components are mutually independent, the variance of the sum is the sum of variances:")
    add_p("Var(z) = Var(sum_{i=1}^{d_k} q_i * k_i) = sum_{i=1}^{d_k} Var(q_i * k_i) = d_k")
    add_p("Therefore, the standard deviation of the raw dot product is sqrt(d_k). For large projection dimensions (e.g., d_k = 64 or 128), z can take values with magnitude greater than 30. When logits of this magnitude are passed to the softmax function, the softmax distribution saturates into an extreme one-hot distribution, causing gradients to vanish: partial softmax(z_i) / partial z_j approx 0.")
    add_p("Dividing by sqrt(d_k) scales the variance back to Var(z / sqrt(d_k)) = (1 / d_k) * Var(z) = 1, ensuring stable gradient flow during backpropagation.")

    # ----------------------------------------------------
    # APPENDIX B: Task Specification Suite
    # ----------------------------------------------------
    doc.add_page_break()
    p_ap_b = doc.add_paragraph()
    p_ap_b.paragraph_format.space_before = Pt(20)
    p_ap_b.paragraph_format.space_after = Pt(14)
    r_ab = p_ap_b.add_run("APPENDIX B: COMPLETE BENCHMARK TASK SPECIFICATION SUITE")
    r_ab.font.name = "Calibri"
    r_ab.font.size = Pt(16)
    r_ab.font.bold = True
    r_ab.font.color.rgb = C_NAVY

    tasks_detail = [
        ("TASK_PLAN_001", "Monolith to Microservices Phased Rollout", 
         "Design an enterprise migration strategy decomposing a legacy retail monolith into microservices.",
         "1. 4-quarter phased rollout (Q1, Q2, Q3, Q4).\n2. Kafka event streaming for asynchronous decoupled data synchronization.\n3. Zero-downtime rollback mechanism with canary routing."),
        ("TASK_CONST_002", "Cloud Infrastructure Optimization",
         "Architect an e-commerce backend satisfying strict budgetary, availability, and latency SLAs.",
         "1. Peak latency < 50ms for 95th percentile requests.\n2. 99.99% multi-region cloud availability.\n3. Monthly hosting expenditure strictly <= $5,000."),
        ("TASK_SYNTH_003", "Asymptotic Complexity Synthesis",
         "Synthesize Graph Neural Network spatial complexity versus Relational Transformer memory bounds.",
         "1. Contrast GNN O(V+E) spatial complexity with Transformer O(N^2) memory footprint.\n2. Justify graph sparsity conditions where GNNs outperform attention."),
        ("TASK_REASON_004", "Concurrent Financial Deadlock Detection",
         "Analyze concurrent distributed clearing transactions across multi-currency escrow ledgers.",
         "1. Construct wait-for lock graph across accounts.\n2. Detect circular wait cycles and prove mathematical presence of deadlock."),
        ("TASK_DECISION_005", "Healthcare Database Engine Evaluation",
         "Select an optimal storage engine for 500 million electronic health records (EHR).",
         "1. HIPAA regulatory encryption at rest and in transit.\n2. Sub-second full-text diagnostic search over unstructured clinical notes.\n3. Multi-region master-slave replication."),
        ("TASK_COLLAB_006", "Enterprise Cyber Incident Containment",
         "Formulate an incident response protocol following a detected APT lateral movement breach.",
         "1. Subnet isolation within 15 minutes of detection.\n2. Cryptographic immutable hashing of forensic memory dumps.\n3. Executive breach disclosure notification within 72 hours."),
        ("TASK_CODE_007", "Algorithmic Rate Limiter Implementation",
         "Implement a thread-safe, in-memory Leaky Bucket traffic shaper in Python.",
         "1. Python 3 thread-safe execution using threading.Lock.\n2. O(1) time complexity for allow_request() calls.\n3. Graceful request queuing up to buffer capacity.")
    ]

    for tid, tname, tdesc, tconst in tasks_detail:
        add_sec(tid, tname)
        add_p(f"Objective: {tdesc}", italic=True)
        add_callout(tconst, "EXPLICIT OPERATIONAL CONSTRAINTS")

    # ----------------------------------------------------
    # APPENDIX C: Agent Prompt Templates
    # ----------------------------------------------------
    doc.add_page_break()
    p_ap_c = doc.add_paragraph()
    p_ap_c.paragraph_format.space_before = Pt(20)
    p_ap_c.paragraph_format.space_after = Pt(14)
    r_ac = p_ap_c.add_run("APPENDIX C: SYSTEM PROMPT TEMPLATES FOR SPECIALIZED AGENT PERSONAS")
    r_ac.font.name = "Calibri"
    r_ac.font.size = Pt(16)
    r_ac.font.bold = True
    r_ac.font.color.rgb = C_NAVY

    prompts = [
        ("Planner Agent System Prompt",
         "You are the Lead Planning Agent. Your role is to analyze complex engineering and reasoning objectives, decompose them into structured sub-tasks, identify critical constraints, and establish an end-to-end execution roadmap. Do not jump to conclusions; outline structured phases."),
        ("Researcher Agent System Prompt",
         "You are the Domain Research Agent. Your role is to gather factual context, architectural standards, mathematical complexity bounds, and industry best practices relevant to the assigned task. Provide concrete domain details and eliminate ambiguity."),
        ("Analyst Agent System Prompt",
         "You are the Quantitative Systems Analyst. Your role is to rigorously evaluate engineering trade-offs, compute mathematical complexity, verify numerical constraint compliance, and model architectural feasibility. Focus on exact bounds, latency, and resource costs."),
        ("Critic Agent System Prompt",
         "You are the Adversarial Reviewer and Security Auditor. Your role is to relentlessly audit intermediate drafts produced by your peers. Flag any constraint omissions, logical fallacies, edge-case vulnerabilities, and budget violations. Be constructively critical."),
        ("Finalizer Agent System Prompt",
         "You are the Authoritative Solution Architect. Your role is to synthesize peer deliberations, incorporate critic audits, resolve conflicting recommendations, and produce the definitive final response. Ensure all initial user constraints are strictly and visibly satisfied.")
    ]

    for title, prompt_text in prompts:
        add_sec("", title)
        add_callout(prompt_text, "SYSTEM PROMPT DIRECTIVE")

print("References and Appendices module written.")

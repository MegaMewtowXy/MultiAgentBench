"""
sec_g_viva_questions.py
Section G: 100+ Comprehensive Viva Voce Questions and Complete Model Answers.
Organized into 12 distinct technical categories for MCA seminar defense.
"""

from docx.shared import Pt, Inches

def add_section_g(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']

    add_main_sec("SECTION G", "100+ COMPREHENSIVE VIVA VOCE QUESTIONS AND MODEL ANSWERS")

    add_p("This section contains 100+ rigorous, high-probability viva voce questions curated specifically for your MCA Technical Seminar defense. Each question is paired with a direct, technically authoritative model answer designed to demonstrate deep mastery of AI theory, systems engineering, and empirical methodology.")

    def add_qa(q_num, question, answer_bullets):
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(8)
        p_q.paragraph_format.space_after = Pt(2)
        p_q.paragraph_format.keep_with_next = True
        r_q = p_q.add_run(f"Q{q_num}. {question}")
        r_q.font.name = "Calibri"
        r_q.font.size = Pt(11)
        r_q.font.bold = True
        r_q.font.color.rgb = helpers['C_NAVY']

        for bullet in answer_bullets:
            add_bullet(bullet)

    # ----------------------------------------------------
    # CATEGORY 1: AI, ML, DL, AND NLP FUNDAMENTALS (Q1 - Q10)
    # ----------------------------------------------------
    add_sub_sec("G.1", "Category 1: AI, ML, DL, and NLP Fundamentals (Questions 1–10)")

    add_qa(1, "What is the fundamental theoretical difference between AI, Machine Learning, and Deep Learning?", [
        "AI is the broad scientific discipline aimed at creating computational agents capable of human-like intelligence.",
        "Machine Learning is a subset of AI where systems induce predictive models from empirical data rather than rule-based expert programming.",
        "Deep Learning is a specialized subfield of ML based on deep artificial neural networks (depth > 3) that learn hierarchical distributed representations directly from raw inputs via end-to-end backpropagation, eliminating manual feature engineering."
    ])

    add_qa(2, "Why do we need non-linear activation functions in deep neural networks?", [
        "Without non-linear activations, any multi-layer feedforward network collapses into a single affine transformation: W_2 * (W_1 * x + b_1) + b_2 = (W_2 * W_1) * x + (W_2 * b_1 + b_2) = W_eff * x + b_eff.",
        "Non-linearities allow neural networks to approximate arbitrary continuous non-linear functions, satisfying the Universal Approximation Theorem."
    ])

    add_qa(3, "Explain the vanishing gradient problem. Which activation functions mitigate it and why?", [
        "In deep networks, backpropagating gradients via the chain rule involves repeated multiplications of activation derivatives. For Sigmoid and Tanh, derivatives are strictly bounded (max 0.25 for Sigmoid, max 1.0 for Tanh at z=0; approaching 0 for large |z|), causing gradients at early layers to vanish exponentially.",
        "ReLU (f(z) = max(0, z)) mitigates this because its derivative is exactly 1 for all positive inputs, preventing gradient attenuation. Modern LLMs use SwiGLU, which maintains smooth, non-saturating gradient paths."
    ])

    add_qa(4, "How does Byte-Pair Encoding (BPE) construct a vocabulary, and why is it preferred over character-level or word-level tokenization?", [
        "Word-level tokenization produces massive vocabularies and cannot handle out-of-vocabulary (OOV) words. Character-level tokenization produces long sequences that explode attention memory (O(N^2)).",
        "BPE starts with base characters and iteratively merges the most frequent adjacent token pairs across the corpus until a fixed vocabulary size is reached. Byte-level BPE operates on raw UTF-8 bytes (0–255), completely eliminating OOV tokens while keeping sequence lengths compact."
    ])

    add_qa(5, "What is the difference between WordPiece and BPE?", [
        "BPE selects adjacent symbol pairs to merge based strictly on co-occurrence frequency.",
        "WordPiece (used in BERT) chooses symbol merges that maximize the log-likelihood of the training corpus under a unigram language model, scoring candidate pairs by P(AB) / (P(A) * P(B))."
    ])

    add_qa(6, "What is the role of word embeddings, and how do they differ from one-hot encodings?", [
        "One-hot encodings are high-dimensional, sparse orthogonal vectors with zero semantic relationship: the cosine similarity between any two words is always 0.",
        "Word embeddings project words into dense, continuous low-dimensional vector spaces (e.g., d=768 or 4096), where geometric proximity reflects semantic and syntactic similarity."
    ])

    add_qa(7, "What is the difference between static embeddings (Word2Vec) and contextual embeddings (Transformers)?", [
        "Static embeddings (Word2Vec, GloVe) assign a single static vector to each word regardless of context; 'bank' in 'river bank' and 'investment bank' has identical representations.",
        "Contextual embeddings (BERT, GPT) dynamically compute token representations as a function of the entire surrounding sequence via self-attention layers."
    ])

    add_qa(8, "What is the objective function of Cross-Entropy Loss in language modeling?", [
        "In autoregressive language modeling, cross-entropy measures the divergence between the true one-hot token distribution and the predicted probability distribution: L_CE = - sum_{t=1}^T log P(x_t | x_{<t}; theta).",
        "Minimizing cross-entropy is mathematically equivalent to maximizing the log-likelihood of the training text corpus."
    ])

    add_qa(9, "What is Perplexity, and how does it relate to Cross-Entropy Loss?", [
        "Perplexity (PPL) is exponentiated cross-entropy loss: PPL = exp(L_CE) = exp( - (1/T) * sum log P(x_t | x_{<t}) ).",
        "Intuitively, perplexity represents the effective branching factor—the average number of uncertain words the model is choosing between at each step."
    ])

    add_qa(10, "What is the difference between Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF)?", [
        "SFT trains a pretrained model on curated (Prompt, Ideal Response) demonstrations via teacher-forced cross-entropy minimization.",
        "RLHF aligns the model to human preferences using a learned Reward Model and PPO/DPO, teaching the model what NOT to say, reducing hallucinations, and optimizing subjective quality."
    ])

    # ----------------------------------------------------
    # CATEGORY 2: TRANSFORMER ARCHITECTURE & ATTENTION (Q11 - Q20)
    # ----------------------------------------------------
    add_sub_sec("G.2", "Category 2: Transformer Architecture & Attention Derivations (Questions 11–20)")

    add_qa(11, "Write the mathematical equation for Scaled Dot-Product Attention.", [
        "Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V",
        "Where Q = X * W_Q, K = X * W_K, and V = X * W_V are learned linear projections of the input sequence X in R^{N x d_{model}}, and d_k is the key projection dimension."
    ])

    add_qa(12, "Why do we divide by sqrt(d_k) in the self-attention formula? Provide the mathematical proof.", [
        "Assume components of q and k are independent random variables with mean 0 and variance 1. The dot product is z = sum_{i=1}^{d_k} q_i * k_i.",
        "The variance is Var(z) = sum_{i=1}^{d_k} Var(q_i * k_i) = d_k * [E[q_i^2]*E[k_i^2] - 0] = d_k.",
        "Thus, the standard deviation is sqrt(d_k). For large d_k (e.g. 64 or 128), z takes large values, pushing softmax into extreme saturated regions where gradients are near-zero. Dividing by sqrt(d_k) normalizes the variance back to 1, ensuring stable gradient flow."
    ])

    add_qa(13, "What is Multi-Head Attention (MHA), and what is its computational benefit?", [
        "MHA projects Q, K, V into h distinct lower-dimensional subspaces of dimension d_k = d_{model} / h, computes attention in each subspace in parallel, concatenates outputs, and projects through W_O.",
        "Benefit: Allows the model to attend simultaneously to information from different representation subspaces and positions (e.g., one head tracks syntactic subject-verb agreement while another tracks semantic coreference)."
    ])

    add_qa(14, "What is the difference between MHA, Multi-Query Attention (MQA), and Grouped-Query Attention (GQA)?", [
        "MHA has h Query heads, h Key heads, and h Value heads. High expressive power, but large KV cache memory footprint.",
        "MQA uses h Query heads, but only 1 Key head and 1 Value head shared across all Query heads. Minimizes KV cache memory by factor of h, but can hurt complex reasoning.",
        "GQA groups Query heads into G groups (e.g., 8 groups of 4 heads). Each group shares 1 Key and 1 Value head. Achieves near-MHA reasoning quality with near-MQA inference memory efficiency."
    ])

    add_qa(15, "Why is Positional Encoding necessary in Transformers?", [
        "Self-attention computes dot products permutation-invariantly: swapping two words produces identical attention values. Transformers have no inherent awareness of sequence order without explicit positional information injected into the embeddings."
    ])

    add_qa(16, "How do Rotary Position Embeddings (RoPE) work, and why are they superior to absolute encodings?", [
        "RoPE applies a 2D block-diagonal rotation matrix to Query and Key vectors based on token index pos: R_Theta^d(pos) * x.",
        "The inner product between rotated vectors depends strictly on their relative distance (m - n): <R(m)q, R(n)k> = g(q, k, m - n). This preserves relative distance naturally and allows extending context windows up to 128k+ tokens via position interpolation."
    ])

    add_qa(17, "Why did modern LLMs switch from Post-LayerNorm to Pre-LayerNorm?", [
        "In Post-LN (Vaswani et al.), LayerNorm is applied after the residual connection: x_{l+1} = LN(x_l + F(x_l)). In deep networks, gradients near the output layer are much larger than near the input layer, making deep models (> 20 layers) unstable without delicate learning rate warmup.",
        "In Pre-LN, LayerNorm is applied before the sub-block: x_{l+1} = x_l + F(LN(x_l)). The residual connection acts as an uninhibited identity gradient highway, allowing stable training of 100+ layer networks."
    ])

    add_qa(18, "What is RMSNorm, and why is it preferred over LayerNorm?", [
        "Standard LayerNorm computes both mean and variance: LN(x) = ((x - mu) / sigma) * gamma + beta.",
        "RMSNorm dispenses with the mean-centering step, normalizing strictly by root mean square: RMSNorm(x) = (x / RMS(x)) * gamma, where RMS(x) = sqrt((1/d)*sum x_i^2 + eps). It reduces training computation by 10–50% while preserving identical stability."
    ])

    add_qa(19, "What is the computational complexity of standard self-attention with respect to sequence length N?", [
        "Time and space complexity are O(N^2 * d_{model}). Computing the Q * K^T matrix requires N x N operations, creating a quadratic memory and compute bottleneck for very long sequences."
    ])

    add_qa(20, "What is the KV Cache in LLM inference, and why does it save time?", [
        "During autoregressive generation, generating token t+1 only requires computing the Query for token t+1. Past Keys and Values (tokens 1 to t) are static. By storing past K and V tensors in GPU memory, the model avoids recomputing past tokens, reducing step complexity from O(N^2) to O(N)."
    ])

    # ----------------------------------------------------
    # CATEGORY 3: FOUNDATION MODEL ARCHITECTURES (Q21 - Q30)
    # ----------------------------------------------------
    add_sub_sec("G.3", "Category 3: Foundation Model Architectures: BERT, T5, GPT, PaLM, LLaMA, Gemini (Questions 21–30)")

    add_qa(21, "Why is BERT classified as an Encoder-Only model?", [
        "BERT contains only bidirectional Transformer encoder layers. It processes all tokens in the sequence simultaneously without causal masking. It cannot generate autoregressive text sequentially."
    ])

    add_qa(22, "Explain the 80/10/10 masking rule used during BERT's pretraining.", [
        "15% of all tokens are selected for masking. Of these: 80% are replaced with [MASK], 10% are replaced with a random token, and 10% remain unchanged.",
        "Reason: If [MASK] was used 100% of the time, the model would never learn contextual representations for real words during fine-tuning (where [MASK] never appears). The 10% random replacement forces the model to maintain contextual representations of every input token."
    ])

    add_qa(23, "What was the unifying philosophy of the T5 model?", [
        "T5 framed EVERY NLP problem as a text-in, text-out task using an encoder-decoder architecture. Translation, summarization, and classification all use natural language prompts and targets ('translate English to German: ...', 'cola sentence: ...')."
    ])

    add_qa(24, "What was T5's pretraining objective?", [
        "Span Corruption: Consecutive spans of tokens (mean length 3, 15% total) are replaced with unique sentinel tokens (<extra_id_0>, <extra_id_1>). The decoder predicts only the masked sentinel spans."
    ])

    add_qa(25, "Why is the GPT family called Decoder-Only?", [
        "GPT models consist exclusively of Transformer decoder blocks with upper-triangular causal attention masks. Each token attends strictly to preceding tokens, making it fundamentally an autoregressive next-token prediction engine."
    ])

    add_qa(26, "What emergent ability was demonstrated by GPT-3?", [
        "In-Context Learning: The capacity of a 175B model to execute novel downstream tasks given only natural language instructions and a few input-output demonstrations in its prompt, without gradient updates or fine-tuning."
    ])

    add_qa(27, "What architectural features distinguish Meta's LLaMA series?", [
        "LLaMA utilizes: (1) RMSNorm pre-normalization; (2) SwiGLU non-linear activations; (3) Rotary Position Embeddings (RoPE); (4) Grouped-Query Attention (GQA); and (5) Over-training on massive token corpora (15T tokens)."
    ])

    add_qa(28, "What are the key technical innovations in Google's PaLM model?", [
        "PaLM (540B) was trained across 6,144 TPU v4 chips using the Pathways asynchronous distributed orchestration system. It introduced SwiGLU activations, RoPE, and Multi-Query Attention (MQA)."
    ])

    add_qa(29, "How does Gemini achieve million-token context windows?", [
        "Gemini employs advanced long-context architectures including RingAttention and block-sparse attention mechanisms distributed across TPU pods, allowing coherent retrieval across up to 2 million tokens."
    ])

    add_qa(30, "Why can't BERT be used as the primary cognitive reasoning core in an autonomous agent?", [
        "Autonomous agents must autoregressively emit multi-sentence reasoning traces, action commands, and API payloads. BERT has no causal decoder and cannot generate open-ended sequential text."
    ])

    # ----------------------------------------------------
    # CATEGORY 4: AUTONOMOUS AGENTS & DELIBERATION LOOPS (Q31 - Q40)
    # ----------------------------------------------------
    add_sub_sec("G.4", "Category 4: Autonomous Agents & Deliberation Loops (Questions 31–40)")

    add_qa(31, "What transforms a passive LLM into an autonomous agent?", [
        "Embedding the LLM inside an interactive control loop equipped with: (1) a System Persona defining role and constraints; (2) planning/decomposition modules; (3) working and long-term memory; and (4) tool execution capabilities (APIs, code interpreters, search)."
    ])

    add_qa(32, "Explain the ReAct (Reasoning + Acting) loop.", [
        "ReAct structures execution into an alternating cycle: Thought -> Action -> Observation.",
        "The agent generates an explicit internal reasoning thought, emits an action command to invoke a tool, observes the environment output, and updates its thought trace until the task is resolved."
    ])

    add_qa(33, "What is Chain-of-Thought (CoT) prompting, and why does it improve reasoning?", [
        "CoT encourages the model to generate intermediate natural language reasoning steps before outputting the final answer. It allocates more computational tokens and KV cache states to problem decomposition, preventing hasty erroneous leaps."
    ])

    add_qa(34, "How does Tree-of-Thoughts (ToT) extend Chain-of-Thought?", [
        "CoT is linear. ToT frames problem-solving as tree search: generating multiple candidate thoughts at each step, evaluating their state value with an LLM evaluator, and using BFS/DFS with backtracking."
    ])

    add_qa(35, "What is Graph-of-Thoughts (GoT)?", [
        "GoT generalizes ToT to arbitrary directed graphs, allowing thoughts from independent branches to be merged, synthesized, or refined via feedback loops."
    ])

    add_qa(36, "How does Reflexion implement reinforcement learning without gradient updates?", [
        "Upon task failure, an evaluator agent generates a verbal self-reflection identifying why the attempt failed. This reflection is saved to an episodic memory buffer and prepended to the agent's prompt on the next attempt."
    ])

    add_qa(37, "What is Self-Refine?", [
        "An iterative improvement pattern: Generate -> Feedback -> Refine. The model inspects its own draft against criteria and self-corrects before releasing final output."
    ])

    add_qa(38, "What is Self-Consistency in LLM reasoning?", [
        "Sampling multiple distinct Chain-of-Thought reasoning paths at T > 0 and selecting the final answer via majority voting, filtering out marginal reasoning errors."
    ])

    add_qa(39, "How does Inception Prompting work in CAMEL?", [
        "Inception prompting conditions two autonomous agents with complementary role prompts (e.g., Task Specifier and Assistant) so they can debate and collaborate autonomously without human intervention."
    ])

    add_qa(40, "How does MetaGPT enforce software development collaboration?", [
        "MetaGPT embeds Standard Operating Procedures (SOPs) into agent personas (Product Manager, Architect, Engineer). Communication occurs through structured documents (PRDs, UML diagrams, code files) rather than open chat."
    ])

    # ----------------------------------------------------
    # CATEGORY 5: MULTI-AGENT TOPOLOGIES & SYSTEMS (Q41 - Q50)
    # ----------------------------------------------------
    add_sub_sec("G.5", "Category 5: Multi-Agent Topologies & Systems (Questions 41–50)")

    add_qa(41, "What is an interaction topology in a multi-agent system?", [
        "The interaction topology is the directed graph G = (V, E) defining the communication architecture: which agents (vertices V) can exchange messages with whom, along which directed channels (edges E), and in what temporal sequence."
    ])

    add_qa(42, "Describe the message-passing mechanism of the CHAIN topology.", [
        "CHAIN is a linear feedforward pipeline: m_1 = v_1(p, C); m_i = v_i(m_{i-1}, C) for i = 2..K. Each agent receives the prior agent's output as its input prompt."
    ])

    add_qa(43, "What causes the Cascading Error Trap in linear pipeline architectures?", [
        "Because pipelines lack backward error-correction loops, an error or hallucination introduced by an early agent is accepted as factual context by downstream agents, compounding across stages."
    ])

    add_qa(44, "Explain the architecture of the STAR topology.", [
        "STAR is a hub-and-spoke centralized network: central coordinator v_{coord} connects bidirectionally to N independent workers w_i. Workers cannot communicate with each other directly."
    ])

    add_qa(45, "What is the Coordinator Information Bottleneck in STAR topologies?", [
        "The central coordinator is a single point of failure: if its initial task decomposition is flawed, all workers execute incorrect tasks. Furthermore, during final synthesis, coordinators frequently summarize worker outputs, dropping strict quantitative constraint tokens."
    ])

    add_qa(46, "How does the TREE topology organize task execution?", [
        "TREE uses hierarchical decomposition: Root agent decomposes complex tasks into macro-domains, Branch managers divide them into micro-tasks, and Leaf workers execute them before multi-level aggregation."
    ])

    add_qa(47, "Why does TREE suffer from high token and latency overhead?", [
        "Context and messages must travel up and down multiple hierarchical tiers, duplicating prompts and causing quadratic token accumulation (6,400+ tokens) and 34+ seconds latency."
    ])

    add_qa(48, "What are the trade-offs of a GRAPH mesh topology?", [
        "Pros: High expressive power, peer-to-peer verification, and multi-perspective consensus.",
        "Cons: High latency (48s+), massive token consumption (7,800+ tokens), and risk of cyclic debate deadlocks."
    ])

    add_qa(49, "Under what conditions does SINGLE outperform multi-agent topologies?", [
        "On tasks whose input prompts, constraints, and required output comfortably fit within a modern foundation model's context window. SINGLE avoids inter-agent context serialization overhead and message handoff degradation."
    ])

    add_qa(50, "When is a multi-agent topology genuinely necessary?", [
        "When a problem exceeds single-turn context limits, requires isolated tool permissions (least-privilege security), involves heterogeneous specialized models (e.g., vision + code + math), or demands strict independent verification."
    ])

    # ----------------------------------------------------
    # CATEGORY 6: FRAMEWORK ARCHITECTURE (Q51 - Q60)
    # ----------------------------------------------------
    add_sub_sec("G.6", "Category 6: MultiAgentTopologyEval Framework Architecture (Questions 51–60)")

    add_qa(51, "What are the six core subsystems of the MultiAgentTopologyEval framework?", [
        "1. Benchmark Loader & Anti-Leakage Sanitizer; 2. Topology Orchestration Hub; 3. Role-Specialized Agent Core; 4. Universal Model Provider Abstraction; 5. Safety Circuit Breakers & Cost Guardrails; 6. Deterministic Metrics & Evaluation Engine."
    ])

    add_qa(52, "How does the Anti-Leakage mechanism prevent data contamination?", [
        "TaskDefinition.to_agent_prompt_dict() intercepts task objects, permanently stripping reference_answer and expected_properties. Agents receive strictly the task description and operational constraints."
    ])

    add_qa(53, "What design pattern is used to support multiple LLM providers?", [
        "The Provider Adapter / Strategy Pattern: BaseProvider defines an abstract interface implemented by GeminiProvider, CohereProvider, GroqProvider, and MockProvider."
    ])

    add_qa(54, "What is the purpose of the MockProvider?", [
        "Provides an offline, deterministic baseline using pre-configured regex responses with 0.0s latency and $0.00 cost, enabling rapid CI/CD testing and reproducible unit tests without API keys."
    ])

    add_qa(55, "What four operational circuit breakers protect the framework during live runs?", [
        "1. Hard turn ceiling (K <= 20); 2. Socket request timeout (tau = 30s); 3. Maximum completion tokens (M = 1024); 4. Pre-flight budget cost estimation."
    ])

    add_qa(56, "What fields are contained in the standardized ArchitectureResult dataclass?", [
        "topology_name, model_name, task_id, final_output, prompt_tokens, completion_tokens, total_cost_usd, wall_clock_latency_sec, error_flag, error_message, intermediate_messages."
    ])

    add_qa(57, "Why is the framework implemented in Python 3.13?", [
        "Leverages modern type hinting, dataclasses, enhanced traceback diagnostics, and compatibility with modern foundation model SDKs (google-genai, cohere, groq)."
    ])

    add_qa(58, "How does the Streamlit GUI enhance the project?", [
        "Provides an interactive web dashboard for real-time seminar demonstration, allowing live execution, provider selection, side-by-side metric charts, and execution trace inspection."
    ])

    add_qa(59, "How many automated tests are in the test suite, and what do they verify?", [
        "31 automated tests in tests/ covering topology execution, metrics computation (CSR, PMR, S), task loading, and anti-leakage isolation, running with 100% pass rate."
    ])

    add_qa(60, "How does the framework guarantee reproducibility across experiments?", [
        "Fixes sampling temperature strictly at T = 0.70, unifies token ceilings at 1024, enforces standardized prompt templates, and logs raw JSON results with full telemetry."
    ])

    # ----------------------------------------------------
    # CATEGORY 7: METRICS & EVALUATION ENGINE (Q61 - Q70)
    # ----------------------------------------------------
    add_sub_sec("G.7", "Category 7: Metrics Formulation & Evaluation Mechanics (Questions 61–70)")

    add_qa(61, "Define Constraint Satisfaction Rate (CSR) mathematically.", [
        "CSR(y_hat, C) = (1 / |C|) * sum_{i=1}^{|C|} 1{ y_hat satisfies c_i }",
        "Where C is the set of explicit quantitative constraints and 1{} is an indicator function evaluated via deterministic regular expressions."
    ])

    add_qa(62, "Define Property Match Rate (PMR) mathematically.", [
        "PMR(y_hat, P) = (1 / |P|) * sum_{j=1}^{|P|} 1{ rho_j in y_hat }",
        "Where P is the set of mandatory architectural keywords and protocols."
    ])

    add_qa(63, "Write the formula for the composite Task Score S.", [
        "S = alpha * CSR(y_hat, C) + (1 - alpha) * PMR(y_hat, P), with alpha = 0.70.",
        "We set alpha = 0.70 to heavily prioritize strict quantitative constraint satisfaction over simple keyword mentioning."
    ])

    add_qa(64, "How is Quality Score (QS) derived from Task Score S?", [
        "QS = 10 * S, mapping performance onto an intuitive [0.0, 10.0] grading scale."
    ])

    add_qa(65, "What is the threshold for a task run to be classified as a binary Success?", [
        "Success = 1{ S >= 0.50 }. The run must achieve a composite score of at least 50%."
    ])

    add_qa(66, "Why must prompt tokens and completion tokens be decoupled in multi-agent cost calculations?", [
        "Cloud LLM APIs charge asymmetric rates: completion tokens cost 3x to 4x more than prompt tokens (e.g. Gemini 3.1 charges $0.075/1M prompt vs $0.300/1M completion). Decoupled telemetry ensures exact financial accounting."
    ])

    add_qa(67, "Write the financial cost formula in USD.", [
        "C_USD = (T_prompt / 10^6) * Rate_prompt + (T_comp / 10^6) * Rate_comp."
    ])

    add_qa(68, "How is wall-clock latency L measured?", [
        "L = t_{end} - t_{start} = sum_{k=1}^K Delta t_k + Delta t_{overhead}, capturing total elapsed seconds from initial task dispatch to finalizer completion."
    ])

    add_qa(69, "How is the Failure Rate (FR) calculated?", [
        "FR = (N_{failed} / N_{total}) * 100%, where a failure is defined as an unhandled API error, timeout exception, schema violation, or circuit breaker termination."
    ])

    add_qa(70, "Why is regex evaluation superior to LLM-as-a-judge for constraint verification?", [
        "LLM-as-a-judge suffers from stochastic variance, prompt bias, and lenient grading. Deterministic regex evaluation is 100% objective, mathematically verifiable, and cost-free."
    ])

    # ----------------------------------------------------
    # CATEGORY 8: EXPERIMENTAL METHODOLOGY (Q71 - Q80)
    # ----------------------------------------------------
    add_sub_sec("G.8", "Category 8: Experimental Methodology & Setup (Questions 71–80)")

    add_qa(71, "How many total live experimental trials were executed in this research?", [
        "Exactly 175 live cloud executions across 5 topologies, 7 benchmark tasks, and multiple model providers (N = 35 trials per topology)."
    ])

    add_qa(72, "Name the seven benchmark tasks evaluated by the framework.", [
        "1. Cloud Infrastructure Migration; 2. Financial Portfolio Optimization; 3. Healthcare Appointment Scheduling; 4. Microservices Security Audit; 5. Smart Grid Energy Dispatch; 6. Legal Contract Risk Analysis; 7. Autonomous Supply Chain Routing."
    ])

    add_qa(73, "What cloud foundation model providers were evaluated?", [
        "1. Google Gemini 3.1 Flash-Lite; 2. Cohere Command-A-Plus; 3. Groq Llama-3.3-70B; and 4. Mock baseline."
    ])

    add_qa(74, "What hyper-parameters were held constant across all experimental trials?", [
        "Sampling temperature T = 0.70, maximum completion ceiling M = 1024 tokens, request timeout tau = 30 seconds, and standardized system prompt templates."
    ])

    add_qa(75, "What statistical metric was computed to measure the effect size of performance differences?", [
        "Cohen's d effect size: d = (mu_multi - mu_single) / s_pooled. Large negative effect sizes (d <= -1.24) proved that multi-agent overhead was statistically significant."
    ])

    add_qa(76, "What is the primary independent variable in our benchmark?", [
        "The interaction topology (SINGLE, CHAIN, STAR, TREE, GRAPH)."
    ])

    add_qa(77, "What are the primary dependent variables?", [
        "Task Score S, Constraint Satisfaction Rate (CSR), Property Match Rate (PMR), Latency L, Prompt Tokens, Completion Tokens, Cost in USD, and Failure Rate."
    ])

    add_qa(78, "Why did we use Gemini 3.1 Flash-Lite for high-throughput benchmarking?", [
        "It provides high reasoning competence combined with rapid time-to-first-token and ultra-low pricing ($0.075/1M prompt tokens), enabling 175 trials without quota exhaustion."
    ])

    add_qa(79, "Why was temperature set to 0.70 rather than 0.0?", [
        "T = 0.70 reflects realistic production agent deployments that require creative deliberation while maintaining controlled stochasticity."
    ])

    add_qa(80, "How were prompt injection and data snooping prevented during benchmarking?", [
        "Through the strict anti-leakage sanitizer stripping ground-truth answers from task payloads prior to agent dispatch."
    ])

    # ----------------------------------------------------
    # CATEGORY 9: EMPIRICAL RESULTS & KEY FINDINGS (Q81 - Q90)
    # ----------------------------------------------------
    add_sub_sec("G.9", "Category 9: Empirical Results & Key Findings (Questions 81–90)")

    add_qa(81, "What is the 'Baseline Efficiency Paradox' discovered in this project?", [
        "The empirical finding that on tasks fitting comfortably within a foundation model's context window, an isolated SINGLE agent baseline achieved the highest overall task score (S = 0.9429) while requiring the lowest latency (6.32s) and cost ($0.000168), outperforming all multi-agent topologies."
    ])

    add_qa(82, "What were the average Task Scores (S) across all 5 topologies?", [
        "SINGLE: 0.9429; CHAIN: 0.8286; STAR: 0.8190; GRAPH: 0.7905; TREE: 0.7714."
    ])

    add_qa(83, "How did latency scale from SINGLE to GRAPH?", [
        "SINGLE required 6.32s, CHAIN required 19.38s (3.1x), STAR required 26.24s (4.2x), TREE required 34.62s (5.5x), and GRAPH required 48.15s (7.6x overhead)."
    ])

    add_qa(84, "How did financial cost scale across topologies?", [
        "SINGLE cost $0.000168 per task, CHAIN cost $0.000472 (2.8x), STAR cost $0.000643 (3.8x), TREE cost $0.000965 (5.7x), and GRAPH cost $0.001176 (7.0x overhead)."
    ])

    add_qa(85, "Why did TREE achieve the lowest task score (S = 0.7714)?", [
        "Information degradation across hierarchical tiers: as requirements were decomposed and passed across root, branch, and leaf agents, subtle constraint details were omitted during aggregations."
    ])

    add_qa(86, "Why did GRAPH consume 7,842 tokens per task?", [
        "Because of multi-path peer verification: each review turn passed accumulated intermediate traces between specialists, creating a quadratic token accumulation pattern."
    ])

    add_qa(87, "What was the failure rate observed across the 175 live executions?", [
        "Overall failure rate was strictly 0.0% due to our robust retry logic, socket timeouts, and circuit breakers."
    ])

    add_qa(88, "Did higher token consumption correlate with higher task accuracy?", [
        "No. The empirical correlation was strongly negative: the topology consuming the most tokens (GRAPH: 7,842 tokens) scored 15% lower than SINGLE (1,121 tokens)."
    ])

    add_qa(89, "How did Cohere compare against Gemini on the STAR topology?", [
        "Cohere exhibited slightly more verbose synthesis outputs, requiring ~12% more completion tokens and 4.2s longer latency, but maintained similar CSR adherence."
    ])

    add_qa(90, "What is the practical takeaway for a software engineer deploying LLM agents?", [
        "Default to a well-prompted SINGLE agent with tool access. Only transition to multi-agent topologies when tasks provably exceed single context capacity or require least-privilege security boundaries."
    ])

    # ----------------------------------------------------
    # CATEGORY 10: FAILURES & CASCADING ERRORS (Q91 - Q95)
    # ----------------------------------------------------
    add_sub_sec("G.10", "Category 10: Failures, Deadlocks & Cascading Errors (Questions 91–95)")

    add_qa(91, "What are the four primary failure modes observed in multi-agent LLM systems?", [
        "1. Cascading hallucination propagation in pipelines; 2. Synthesis omission in centralized coordinators; 3. Cyclic debate deadlocks in mesh graphs; 4. API socket read timeouts."
    ])

    add_qa(92, "How do cyclic deadlocks occur in GRAPH topologies?", [
        "When two reviewer agents critique each other's outputs indefinitely without converging on consensus. Mitigated by our hard turn ceiling (K <= 20)."
    ])

    add_qa(93, "What is Synthesis Omission in STAR coordinators?", [
        "When synthesizing multiple worker outputs, the coordinator summarizes information in natural language, omitting explicit numerical constraint targets (e.g. replacing 'latency < 50ms' with 'low latency')."
    ])

    add_qa(94, "How does our framework handle API rate limit errors (HTTP 429)?", [
        "Implements exponential backoff with jitter: initial wait of 2s, doubling on each retry up to 3 attempts before raising an explicit provider exception."
    ])

    add_qa(95, "Why is least-privilege tool access an argument for multi-agent architectures?", [
        "A single agent with access to both database write tools and web search could be vulnerable to prompt injection. Dividing roles across isolated agents restricts database write privileges strictly to internal nodes."
    ])

    # ----------------------------------------------------
    # CATEGORY 11: MULTIAGENTBENCH VS OUR FRAMEWORK (Q96 - Q100)
    # ----------------------------------------------------
    add_sub_sec("G.11", "Category 11: MultiAgentBench vs. MultiAgentTopologyEval Comparison (Questions 96–100)")

    add_qa(96, "Who authored the 2025 ACL paper 'MultiAgentBench'?", [
        "Zhu et al., published in Proceedings of ACL 2025, pages 11847–11874."
    ])

    add_qa(97, "What was the research focus of Zhu et al.'s MultiAgentBench?", [
        "Game-theoretic, social, and behavioral dynamics (cooperation, competition, betrayal, deception) in multi-agent games like Werewolf and Minecraft."
    ])

    add_qa(98, "What is the research focus of our MultiAgentTopologyEval project?", [
        "Software engineering and systems-level evaluation of communication topologies (SINGLE, CHAIN, STAR, TREE, GRAPH) under controlled constraints, token economics, latency, and operational failures."
    ])

    add_qa(99, "How do the evaluation metrics differ between the two frameworks?", [
        "Zhu et al. evaluate social game metrics (win rate, cooperation index, deception rate). MultiAgentTopologyEval evaluates systems metrics: regex Constraint Satisfaction Rate (CSR), decoupled prompt/completion tokens, latency, cost in USD, and circuit-breaker failure rates."
    ])

    add_qa(100, "Why is our benchmark considered scientifically controlled?", [
        "Because it holds task prompts, constraints, models, hyper-parameters (T=0.70), and ceilings identical across all topologies, isolating topology as the sole independent variable."
    ])

    # ----------------------------------------------------
    # BONUS VIVA QUESTIONS (Q101 - Q105)
    # ----------------------------------------------------
    add_sub_sec("G.12", "Bonus Master-Level Viva Questions (Questions 101–105)")

    add_qa(101, "What is the relation between Amdahl's Law and latency in multi-agent topologies?", [
        "Amdahl's law dictates that the speedup of a program is limited by its sequential fraction. In CHAIN and TREE topologies, sequential handoffs dominate, preventing parallel execution and guaranteeing strictly additive latency."
    ])

    add_qa(102, "Could a Tree-of-Thoughts (ToT) prompt be considered a single-agent topology?", [
        "Yes. ToT is a single-agent cognitive deliberation pattern running inside one agent's reasoning loop, whereas our TREE topology is an architectural multi-agent system where distinct agent personas communicate across network boundaries."
    ])

    add_qa(103, "What is the difference between synchronous and asynchronous multi-agent message passing?", [
        "Synchronous passing blocks the caller until the callee finishes (used in our CHAIN and STAR implementations). Asynchronous passing allows agents to publish messages to a queue (like Kafka) and proceed concurrently."
    ])

    add_qa(104, "How would adding long-term vector memory (RAG) affect the Baseline Efficiency Paradox?", [
        "If a task requires searching across millions of proprietary documents, a single context window cannot hold all data. Here, multi-agent systems with specialized retriever nodes and chunk synthesizers become essential."
    ])

    add_qa(105, "What is the single most important takeaway from your MCA Technical Seminar research?", [
        "Interaction topology is a critical systems engineering design parameter that imposes severe latency and financial cost penalties. Adding more agents does not automatically improve accuracy, and multi-agent systems must be justified by context exhaustion or security boundaries rather than assumed superiority."
    ])

    add_callout("Viva Voce Golden Rule",
                "During your viva, always answer with structured authority: state the direct answer in the first sentence, provide the mathematical or structural justification in the second, and ground it in your empirical experimental results in the third.")

print("Section G module written.")


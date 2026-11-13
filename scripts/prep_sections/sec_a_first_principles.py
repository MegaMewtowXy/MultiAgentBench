"""
sec_a_first_principles.py
Section A: First-Principles Concepts in AI, ML, DL, NLP, and Foundation Models.
Exhaustive mathematical derivations, learning mechanics, tokenization, embeddings,
self-attention, normalization, and training paradigms for seminar defense.
"""

from docx.shared import Pt, Inches

def add_section_a(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']

    add_main_sec("SECTION A", "FIRST-PRINCIPLES ARTIFICIAL INTELLIGENCE, MACHINE LEARNING, AND FOUNDATION CONCEPTS")

    add_p("To successfully defend an advanced MCA technical seminar, one must demonstrate mastery of foundational computer science, machine learning, and deep learning principles. A candidate who cannot derive backpropagation, explain why softmax gradients saturate, or differentiate WordPiece from BPE will falter during external viva questioning. This section provides an exhaustive, mathematically rigorous foundation.")

    add_sub_sec("A.1", "Taxonomy: AI vs. Machine Learning vs. Deep Learning vs. LLMs vs. Autonomous Agents")
    add_p("Intelligent systems must be conceptualized as a strictly nested hierarchy of computational paradigms:")
    add_bullet("Artificial Intelligence (AI): The overarching scientific discipline dedicated to designing machines, algorithms, and computational artifacts capable of executing tasks that traditionally require biological human intelligence. Encompasses symbolic reasoning, expert rule systems, heuristic search (A*), constraint satisfaction, and connectionist architectures.")
    add_bullet("Machine Learning (ML): A functional subset of AI where computational programs are not explicitly hardcoded with rules, but instead induce predictive functions and patterns directly from empirical training data. Governed by statistical estimation theory, empirical risk minimization, and loss optimization.")
    add_bullet("Deep Learning (DL): A specialized branch of ML based on Artificial Neural Networks with multiple hierarchical hidden layers (typically depth > 3). DL eliminates the manual 'feature engineering' bottleneck of traditional ML by learning end-to-end distributed representations from raw data using backpropagation.")
    add_bullet("Large Language Models (LLMs): High-capacity foundation models based on the Transformer architecture (typically billions of parameters) trained via self-supervised objectives (next-token prediction) on massive multi-terabyte natural language corpora. They exhibit emergent capabilities such as in-context learning and zero-shot reasoning.")
    add_bullet("Autonomous LLM Agents: Encapsulated computational entities that position a foundation model as a centralized cognitive engine situated inside an interactive control loop. Agents perceive external environments, formulate explicit multi-step reasoning plans, invoke external tools (APIs, calculators, databases), store state across working memory, and execute actions to satisfy goals.")

    add_sub_sec("A.2", "Mathematical Mechanics of Artificial Neural Networks and Backpropagation")
    add_p("An Artificial Neural Network is a parameterized directed acyclic computational graph. Let us derive its forward and backward propagation mechanics from first principles.")
    add_p("Forward Propagation Mechanics:", bold=True)
    add_p("Consider an L-layer feedforward network. Let x in R^{d_0} be the input vector, and let a^[0] = x. For any layer l in {1, 2, ..., L}:")
    add_bullet("z^[l] = W^[l] * a^[l-1] + b^[l],   where W^[l] in R^{n_l x n_{l-1}} is the weight matrix, b^[l] in R^{n_l} is the bias vector, and z^[l] is the pre-activation logit vector.")
    add_bullet("a^[l] = sigma(z^[l]),   where sigma is an element-wise non-linear activation function, and a^[l] is the post-activation state.")
    add_p("At the final layer L, the output y_hat = a^[L] is evaluated against the ground-truth target y using a scalar loss function L(y_hat, y), such as Mean Squared Error (MSE) for regression or Categorical Cross-Entropy for classification:")
    add_p("L_{CE}(y, y_hat) = - sum_{k=1}^C y_k * log(y_hat_k)")

    add_p("Backpropagation Derivation (Vectorized Chain Rule):", bold=True)
    add_p("Training minimizes the expected loss J(W, b) = (1/N) * sum L(y_hat_i, y_i) via gradient descent. To compute partial derivatives with respect to weights and biases, we define the layer-wise error delta^[l] = partial L / partial z^[l]:")
    add_bullet("For the output layer L (assuming softmax activation and cross-entropy loss): delta^[L] = y_hat - y.")
    add_bullet("For intermediate hidden layers l = L-1, L-2, ..., 1: delta^[l] = ((W^[l+1])^T * delta^[l+1]) odot sigma'(z^[l]), where odot denotes the Hadamard (element-wise) product.")
    add_bullet("Gradient with respect to weights: partial L / partial W^[l] = delta^[l] * (a^[l-1])^T.")
    add_bullet("Gradient with respect to biases: partial L / partial b^[l] = delta^[l].")
    add_p("Weight updates proceed via stochastic gradient descent with learning rate eta: W^[l] := W^[l] - eta * (partial L / partial W^[l]).")

    add_sub_sec("A.3", "Activation Functions: Mathematical Profiles and Vanishing Gradients")
    add_p("Activation functions inject essential non-linearity into neural networks, enabling them to approximate arbitrary continuous functions (Universal Approximation Theorem). Without non-linearity, a composition of any number of linear layers collapses to a single affine transformation: W_2 * (W_1 * x) = (W_2 * W_1) * x = W_eff * x.")
    
    act_data = [
        ["Sigmoid", "sigma(z) = 1 / (1 + e^{-z})", "sigma'(z) = sigma(z)(1 - sigma(z))", "Max gradient = 0.25 at z=0. Severe vanishing gradients in deep networks; output not zero-centered."],
        ["Tanh", "tanh(z) = (e^z - e^{-z}) / (e^z + e^{-z})", "tanh'(z) = 1 - tanh^2(z)", "Max gradient = 1.0 at z=0. Zero-centered, but saturates for |z| > 3, causing vanishing gradients."],
        ["ReLU", "f(z) = max(0, z)", "f'(z) = 1 if z > 0 else 0", "Non-saturating for z > 0, fast O(1) computation. Vulnerable to 'Dying ReLU' if neurons get stuck with negative inputs."],
        ["LeakyReLU", "f(z) = max(alpha*z, z), alpha=0.01", "f'(z) = 1 if z > 0 else alpha", "Prevents dying ReLU by allowing a small, non-zero gradient alpha for negative inputs."],
        ["GELU", "GELU(z) = z * Phi(z) = z * P(X <= z)", "Smooth, probabilistic non-linearity", "Standard in BERT, GPT-2, GPT-3. Weighs inputs by their percentile value under Gaussian distribution."],
        ["SwiGLU", "SwiGLU(x) = Swish(x * W) odot (x * V)", "Gated Linear Unit with Swish", "Standard in modern frontier LLMs (LLaMA-3, PaLM, Gemini). Provides superior gradient flow and representation capacity."]
    ]
    act_tbl = doc.add_table(rows=1, cols=4)
    style_table(act_tbl, [Inches(1.1), Inches(1.8), Inches(1.8), Inches(1.8)], ["Function", "Formula", "Derivative", "Behavioral Properties"], act_data)

    add_sub_sec("A.4", "Tokenization Algorithms: BPE, WordPiece, and SentencePiece")
    add_p("Neural networks operate on numerical tensors, not raw character strings. Tokenization decomposes raw text into discrete tokens mapped to unique integer IDs in a fixed vocabulary V.")
    add_bullet("Byte-Pair Encoding (BPE; Sennrich et al., 2016): Begins with a base vocabulary of individual characters. Iteratively counts the most frequent adjacent pair of tokens across the training corpus and merges them into a new single token. Continues until target vocabulary size |V| is reached (e.g., 50,000 for GPT-2, 128,000 for LLaMA-3). Byte-level BPE maps raw UTF-8 bytes (0-255), completely eliminating out-of-vocabulary (OOV) tokens.")
    add_bullet("WordPiece (Schuster & Nakajima, 2012; used in BERT): Similar to BPE, but instead of merging based strictly on frequency, WordPiece chooses the merge that maximizes the likelihood of the training data according to a unigram language model. Prepends '##' to sub-word continuations (e.g., 'playing' -> ['play', '##ing']).")
    add_bullet("SentencePiece (Kudo & Richardson, 2018): Treats raw input as an uninterrupted stream of characters, including whitespace (represented by an underscore '_'). Language-agnostic, handling languages without explicit word spaces (e.g., Japanese, Chinese) without heuristic pre-tokenizers.")

    add_sub_sec("A.5", "Continuous Vector Representations and Positional Encodings")
    add_p("Tokens are projected into a continuous vector space R^{d_{model}} via an embedding matrix E in R^{|V| x d_{model}}. Unlike discrete one-hot vectors, distributed embeddings place semantically similar tokens close together in geometric space (cosine similarity).")
    add_p("Positional Encodings:", bold=True)
    add_p("Because self-attention computes dot products between all token pairs permutation-invariantly, the Transformer has no inherent sense of token order. Positional information must be explicitly injected:")
    add_bullet("Absolute Sinusoidal (Vaswani et al., 2017): PE_{(pos, 2i)} = sin(pos / 10000^{2i/d}), PE_{(pos, 2i+1)} = cos(pos / 10000^{2i/d}). Allows model to extrapolate to longer sequences via linear trigonometric relationships.")
    add_bullet("Learned Positional Embeddings (BERT, GPT-2): A parameter matrix P in R^{max\_seq\_len x d_{model}} trained via backpropagation. Cannot extrapolate beyond max_seq_len.")
    add_bullet("Rotary Position Embeddings (RoPE; Su et al., 2024): Modern gold standard (LLaMA, Gemini, Mistral). Multiplies Query and Key vectors by a 2D block-diagonal rotation matrix: R_Theta^d(pos) * x. Preserves relative position distance through the inner product: <R(m)q, R(n)k> = g(q, k, m - n). Allows context extension up to 128k+ tokens via NTK-aware interpolation.")

    add_sub_sec("A.6", "The Self-Attention Mechanism from First Principles")
    add_p("Given an input sequence X in R^{N x d_{model}}, the Scaled Dot-Product Attention transforms X into Queries (Q), Keys (K), and Values (V) via learned projection matrices W_Q, W_K, W_V in R^{d_{model} x d_k}:")
    add_bullet("Q = X * W_Q,    K = X * W_K,    V = X * W_V")
    add_bullet("Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V")
    add_p("Mathematical Proof: Why Divide by sqrt(d_k)?", bold=True)
    add_p("Let q and k be independent random vectors with zero mean and unit variance: E[q_i] = 0, Var(q_i) = 1, E[k_i] = 0, Var(k_i) = 1. The dot product is z = sum_{i=1}^{d_k} q_i * k_i. The variance is:")
    add_bullet("Var(z) = sum_{i=1}^{d_k} Var(q_i * k_i) = sum_{i=1}^{d_k} [E[q_i^2]*E[k_i^2] - (E[q_i]*E[k_i])^2] = sum_{i=1}^{d_k} [1 * 1 - 0] = d_k.")
    add_p("Thus, the standard deviation is sqrt(d_k). For large projection dimensions (e.g., d_k = 64 or 128), z can easily reach values of +/-30. When logits of this magnitude are passed to softmax, the softmax distribution becomes extremely sharp (approaching a one-hot distribution), pushing the gradients of softmax toward zero (vanishing gradient). Dividing by sqrt(d_k) normalizes the variance back to Var(z / sqrt(d_k)) = 1, ensuring stable gradient flow during backpropagation.")

    add_sub_sec("A.7", "Attention Variants: MHA, MQA, and GQA")
    add_bullet("Multi-Head Attention (MHA): Computes h independent attention heads in parallel with distinct Q, K, V projection matrices. Output heads are concatenated and multiplied by W_O. Problem: In autoregressive inference, caching Keys and Values (KV Cache) for every head across long contexts consumes massive GPU VRAM.")
    add_bullet("Multi-Query Attention (MQA; Shazeer, 2019): Uses multiple Query heads (e.g., 32), but all heads share a single Key head and a single Value head. Reduces KV cache memory by a factor of h, drastically accelerating inference throughput at a slight cost in model expressive capacity.")
    add_bullet("Grouped-Query Attention (GQA; Ainslie et al., 2023): An optimal compromise between MHA and MQA (used in LLaMA-3.3 and modern LLMs). Groups Query heads into G groups (e.g., 8 groups of 4 heads). Each group shares one Key and Value head. Delivers near-MHA reasoning quality with near-MQA inference memory efficiency.")

    add_sub_sec("A.8", "Normalization Strategies: Post-LN, Pre-LN, and RMSNorm")
    add_bullet("Post-LN (Original Transformer): LayerNorm is applied AFTER the residual addition: x_{l+1} = LayerNorm(x_l + Sublayer(x_l)). Cause of failure: Gradients at output layers are much larger than at input layers, requiring delicate warm-up schedules and making deep models (> 20 layers) unstable to train.")
    add_bullet("Pre-LN (GPT-2, GPT-3): LayerNorm is applied to the input of each sublayer BEFORE the residual connection: x_{l+1} = x_l + Sublayer(LayerNorm(x_l)). The residual stream serves as an unhindered identity gradient highway, allowing stable training of very deep networks (> 100 layers).")
    add_bullet("RMSNorm (Root Mean Square Normalization; Zhang & Sennrich, 2019): Replaces standard LayerNorm by dispensing with the mean-centering step: RMSNorm(x) = (x / RMS(x)) odot gamma, where RMS(x) = sqrt((1/d) * sum x_i^2 + epsilon). Reduces computational overhead by 10-50% while preserving identical training stability. Standard in LLaMA, PaLM, and Gemini.")

    add_sub_sec("A.9", "Training Paradigms: Pretraining, SFT, RLHF, and DPO")
    add_bullet("Self-Supervised Pretraining: Model trains on multi-terabyte web text via Causal Language Modeling (CLM; predicting x_t given x_{<t}) or Masked Language Modeling (MLM). Induces general linguistic syntax, factual knowledge, and reasoning patterns without human labels.")
    add_bullet("Supervised Fine-Tuning (SFT): Fine-tuning pretrained weights on curated high-quality instruction-response pairs {(Prompt, Demonstration)}. Teaches the model to format answers, obey system personas, and act as a conversational assistant.")
    add_bullet("Reinforcement Learning from Human Feedback (RLHF; Ouyang et al., 2022): Trains a scalar Reward Model r_psi(x, y) on pairwise human preference rankings (y_w > y_l). The policy LLM pi_theta is optimized via Proximal Policy Optimization (PPO) to maximize reward while penalizing divergence from the reference policy via a KL-divergence penalty: max E[r(x, y) - beta * D_KL(pi_theta || pi_ref)].")
    add_bullet("Direct Preference Optimization (DPO; Rafailov et al., 2023): Mathematically reparameterizes the RL objective, showing that the optimal policy can be extracted directly from preference data without training a separate reward model or running unstable online PPO reinforcement learning: L_DPO(theta) = - E_{(x, y_w, y_l)} [ log sigma( beta * log(pi_theta(y_w|x)/pi_ref(y_w|x)) - beta * log(pi_theta(y_l|x)/pi_ref(y_l|x)) ) ].")

    add_callout("Viva Takeaway: Section A Defense Strategy",
                "If an examiner asks: 'What is the mathematical justification for dividing by sqrt(d_k) in attention?' do NOT give an intuitive answer. Immediately write the variance derivation: Var(sum q_i k_i) = d_k, explaining that large logit variance pushes softmax into saturated regions with near-zero gradients. This demonstrates first-principles mastery.")

print("Section A module written.")


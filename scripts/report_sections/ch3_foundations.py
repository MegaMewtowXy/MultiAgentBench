"""
ch3_foundations.py
Generates Chapter 3: Technical Background and Theoretical Foundations for the MCA Technical Seminar Report.
Extremely detailed mathematical derivations, model breakdowns, agent architectures, and MAS fundamentals.
"""

from docx.shared import Inches, Pt

def add_chapter_3(doc, helpers):
    add_chapter_heading = helpers['add_chapter_heading']
    add_sec = helpers['add_sec']
    add_subsec = helpers['add_subsec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']
    C_NAVY = helpers['C_NAVY']

    add_chapter_heading(3, "TECHNICAL BACKGROUND AND THEORETICAL FOUNDATIONS")

    add_sec("3.1", "Artificial Neural Networks: Architecture, Propagation, and Training")
    add_p("To understand modern foundation models and autonomous multi-agent systems, one must first master the mathematical and structural principles of Artificial Neural Networks (ANNs). Inspired by biological neural networks, an ANN is a directed computational graph composed of interconnected artificial neurons organized into hierarchical layers.")

    add_subsec("3.1.1", "The Artificial Neuron and Multilayer Perceptrons (MLPs)")
    add_p("The fundamental unit of computation is the artificial neuron (perceptron). Given an input vector x = [x_1, x_2, ..., x_d]^T in R^d, a neuron computes a parameterized affine transformation followed by an element-wise non-linear activation function sigma:")
    add_callout(
        "Neuron Activation Equation:\n"
        "z = sum_{i=1}^d (w_i * x_i) + b = w^T * x + b\n"
        "a = sigma(z)\n\n"
        "Where:\n"
        "• x in R^d is the input feature vector.\n"
        "• w in R^d is the learnable weight vector governing synaptic connection strength.\n"
        "• b in R is the learnable scalar bias parameter allowing the activation threshold to shift.\n"
        "• z in R is the pre-activation logit.\n"
        "• sigma: R -> R is the non-linear activation function.\n"
        "• a in R is the final post-activation output scalar.",
        "MATHEMATICAL FORMULATION OF ARTIFICIAL NEURON"
    )
    add_p("A single perceptron can only separate linearly separable classes (as proved by Minsky and Papert, 1969). To learn non-linear decision boundaries, neurons are stacked into Multilayer Perceptrons (MLPs) comprising an Input Layer, one or more Hidden Layers, and an Output Layer. In a fully connected feed-forward layer l, the activation vector a^(l) is computed from the activations of the preceding layer a^(l-1):")
    add_p("z^(l) = W^(l) * a^(l-1) + b^(l),    a^(l) = sigma(z^(l))")
    add_p("By stacking multiple non-linear hidden layers, an MLP functions as a Universal Function Approximator (Hornik et al., 1989), capable of approximating any continuous mathematical mapping on compact subsets of R^d to arbitrary precision, given sufficient hidden neurons.")

    add_subsec("3.1.2", "Non-Linear Activation Functions")
    add_p("Activation functions introduce non-linearity into neural networks. Without non-linear activations, stacking multiple linear layers would collapse into a single trivial linear transformation (W_2 * W_1 * x = W_effective * x). Modern deep learning utilizes several canonical activation functions:")
    add_bullet("Sigmoid Function: sigma(z) = 1 / (1 + e^(-z)). Maps inputs to the range (0, 1). Historically used for binary probabilities, but suffers from severe vanishing gradient problems when |z| is large because sigma'(z) = sigma(z)(1 - sigma(z)) approaches 0.")
    add_bullet("Hyperbolic Tangent (Tanh): tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z)). Zero-centered output in (-1, 1). Superior to sigmoid for hidden units, but still saturates at extreme values.")
    add_bullet("Rectified Linear Unit (ReLU): ReLU(z) = max(0, z). The standard modern activation. Possesses constant derivative 1 for z > 0, completely avoiding vanishing gradients in the positive domain and accelerating gradient descent convergence. However, it suffers from the 'Dying ReLU' problem where neurons with z < 0 permanently deactivate.")
    add_bullet("Gaussian Error Linear Unit (GELU): GELU(z) = z * Phi(z) = z * P(X <= z), where X ~ N(0, 1). Employs probabilistic gating. Used universally in Transformer architectures including BERT, GPT-2, GPT-3, and ViT.")
    add_bullet("SwiGLU: SwiGLU(x, W, V, b, c) = Swish(xW + b) (xV + c), where Swish(z) = z * sigmoid(beta * z). A gated activation variant introduced by Shazeer (2020), adopted in frontier models like LLaMA and PaLM for superior gradient flow.")

    add_subsec("3.1.3", "Forward Propagation, Loss Functions, and Backpropagation")
    add_p("Neural network training is formalized as empirical risk minimization. In Forward Propagation, an input batch X is propagated layer-by-layer through the network parameters Theta = {W^(l), b^(l)} to produce a predictive output y_hat = f(X; Theta).")
    add_p("The discrepancy between the predicted output y_hat and the ground-truth target y is quantified by an objective Loss Function L(y_hat, y):")
    add_bullet("Mean Squared Error (MSE): L_MSE = (1 / 2N) * sum_{k=1}^N ||y_k - y_hat_k||^2. Standard for continuous regression.")
    add_bullet("Cross-Entropy Loss: L_CE = -sum_{c=1}^C y_c * log(y_hat_c). Standard for classification and autoregressive language modeling, measuring the Kullback-Leibler (KL) divergence between empirical target distributions and predicted softmax probabilities.")
    add_p("To optimize network parameters, the network employs Backpropagation—an application of the multivariable calculus Chain Rule that computes the partial derivative of the scalar loss L with respect to every weight matrix W^(l) and bias vector b^(l):")
    add_callout(
        "Backpropagation Error Term Derivation:\n"
        "Let delta^(l) = partial L / partial z^(l) denote the error vector at layer l.\n\n"
        "For the output layer L:\n"
        "delta^(L) = nabla_{a^(L)} L  sigma'(z^(L))\n\n"
        "For any hidden layer l in {L-1, L-2, ..., 1}:\n"
        "delta^(l) = ((W^(l+1))^T * delta^(l+1))  sigma'(z^(l))\n\n"
        "The parameter gradients are computed directly as:\n"
        "partial L / partial W^(l) = delta^(l) * (a^(l-1))^T\n"
        "partial L / partial b^(l) = delta^(l)",
        "MATHEMATICAL DERIVATION OF BACKPROPAGATION"
    )
    add_p("Once gradients are computed, parameter updates are executed via Gradient Descent: Theta <- Theta - eta * nabla_Theta L, where eta is the learning rate. Modern LLM pretraining predominantly utilizes adaptive optimizers—notably Adam (Kingma and Ba, 2014) and AdamW (Loshchilov and Hutter, 2019)—which maintain decoupled first-moment (momentum) and second-moment (uncentered variance) running averages with decoupled weight decay.")

    add_sec("3.2", "Deep Learning and Natural Language Processing: Embeddings, Tokenization, and Sequence Modeling")
    add_p("Natural language is inherently discrete, symbolic, and compositionally complex. Processing language with continuous neural networks requires transforming discrete character sequences into dense, semantically meaningful mathematical spaces.")

    add_subsec("3.2.1", "Word Embeddings: Distributed Vector Representations")
    add_p("Historically, NLP represented words using One-Hot Vectors in R^|V|, where |V| is the vocabulary size. Under one-hot representations, all word vectors are mutually orthogonal (w_i^T * w_j = 0 for all i != j), completely destroying semantic relationships (e.g., 'cat' and 'feline' were as mathematically distant as 'cat' and 'refrigerator').")
    add_p("The foundational breakthrough was the Distributed Hypothesis (Harris, 1954; Firth, 1957): 'Words that occur in similar contexts have similar meanings.' Word2Vec (Mikolov et al., 2013) formalized this via two neural architectures: Continuous Bag-of-Words (CBOW; predicting a target word from context tokens) and Skip-Gram (predicting context words from a target token). Skip-Gram optimizes the log-probability objective:")
    add_p("L_Word2Vec = sum_{t=1}^T sum_{-c <= j <= c, j != 0} log P(w_{t+j} | w_t)")
    add_p("By factoring co-occurrence statistics, Word2Vec and GloVe (Pennington et al., 2014) learned dense geometric spaces in R^d (typically d = 300) exhibiting linear semantic compositionality (e.g., vector('King') - vector('Man') + vector('Woman') approx vector('Queen')).")

    add_subsec("3.2.2", "Subword Tokenization: BPE, WordPiece, and SentencePiece")
    add_p("While word-level embeddings represented semantics well, they suffered from Out-Of-Vocabulary (OOV) tokens, morphological inflexibility, and vocabulary bloat. Character-level tokenization solved OOV issues but resulted in excessively long sequence lengths, inflating computational complexity.")
    add_p("Modern LLMs resolve this trade-off via Subword Tokenization algorithms:")
    add_bullet("Byte-Pair Encoding (BPE; Sennrich et al., 2016): Begins with a base vocabulary of individual characters or bytes. The algorithm iteratively counts the most frequent adjacent character pairs across a corpus and merges them into new subword units until a target vocabulary size |V| is reached (typically 32,000 to 128,000 tokens). Byte-level BPE (employed in GPT-2, GPT-3, GPT-4, and LLaMA) operates directly on UTF-8 raw bytes, guaranteeing zero out-of-vocabulary tokens for any language or binary string.")
    add_bullet("WordPiece (Schuster and Nakajima, 2012): Employed in BERT. Similar to BPE, but selects merge candidates based on maximizing the likelihood of the language model on the training data rather than pure raw frequency.")
    add_bullet("SentencePiece (Kudo and Richardson, 2018): Treats raw input text as a continuous stream of characters, including whitespace (represented as a special symbol '_'), avoiding language-dependent word-splitting pre-tokenizers.")

    add_subsec("3.2.3", "Sequence Modeling Evolution: RNNs, LSTMs, and the Attention Bottleneck")
    add_p("Prior to 2017, sequential language processing relied on Recurrent Neural Networks (RNNs). An RNN processes a sequence x_1, x_2, ..., x_T sequentially, updating an internal hidden state vector h_t at each time step:")
    add_p("h_t = tanh(W_hh * h_{t-1} + W_xh * x_t + b_h)")
    add_p("While recurrent networks possessed theoretical infinite memory, in practice they suffered from Vanishing and Exploding Gradients (Hochreiter, 1991; Bengio et al., 1994). Because backpropagation through time requires multiplying repeated weight matrices (W_hh)^k across k time steps, gradients exponentially decay toward zero or explode to infinity as k grows.")
    add_p("Long Short-Term Memory (LSTM; Hochreiter and Schmidhuber, 1997) networks introduced an internal constant error carousel governed by three multiplicative gates: an Input Gate i_t, a Forget Gate f_t, and an Output Gate o_t, alongside a Cell State c_t:")
    add_bullet("Forget Gate: f_t = sigma(W_f * [h_{t-1}, x_t] + b_f)  (Controls what to erase from memory).")
    add_bullet("Input Gate: i_t = sigma(W_i * [h_{t-1}, x_t] + b_i)  (Controls what new information to store).")
    add_bullet("Candidate State: c_tilde_t = tanh(W_c * [h_{t-1}, x_t] + b_c).")
    add_bullet("Cell State Update: c_t = f_t  c_{t-1} + i_t  c_tilde_t.")
    add_bullet("Output Gate: o_t = sigma(W_o * [h_{t-1}, x_t] + b_o),    h_t = o_t  tanh(c_t).")
    add_p("While LSTMs enabled training across sequences of several hundred tokens, they faced an insurmountable architectural constraint: sequential computation. Computing h_t strictly requires h_{t-1}. This prevented parallelization during training across GPUs. Furthermore, in sequence-to-sequence translation, compressing an entire source sentence into a single fixed-length context vector c created an informational bottleneck. Bahdanau et al. (2014) resolved this by introducing additive Attention—allowing the decoder to attend to all hidden states of the encoder—paving the direct conceptual path to the Transformer.")

    add_sec("3.3", "The Transformer Architecture: Mathematical Derivation and Mechanics")
    add_p("Published by Vaswani et al. (2017) [2], the Transformer completely eliminated recurrent and convolutional connections, relying solely on attention mechanisms to draw global dependencies between input and output tokens.")

    add_subsec("3.3.1", "Scaled Dot-Product Attention")
    add_p("The foundational mathematical engine of the Transformer is Scaled Dot-Product Attention. Given an input matrix H in R^{N x d_model} representing N token embeddings of dimension d_model, the network computes three distinct projection matrices: Queries (Q), Keys (K), and Values (V):")
    add_p("Q = H * W_Q,    K = H * W_K,    V = H * W_V")
    add_p("Where W_Q, W_K in R^{d_model x d_k} and W_V in R^{d_model x d_v} are learnable parameter projection matrices.")
    add_callout(
        "Scaled Dot-Product Attention Equation:\n"
        "Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V\n\n"
        "Mathematical Roles:\n"
        "• Q * K^T in R^{N x N} computes the pairwise dot-product similarity between every Query i and Key j.\n"
        "• Division by sqrt(d_k) is the scaling factor. For large dimensions d_k, dot products grow large in magnitude, pushing softmax functions into regions with extremely small gradients. Dividing by sqrt(d_k) preserves unit variance.\n"
        "• Softmax normalizes each row into a probability distribution: sum_{j=1}^N A_{ij} = 1.\n"
        "• Multiplication by V computes the final representation as a weighted linear combination of all Value vectors.",
        "THE FOUNDATIONAL ATTENTION DERIVATION"
    )

    add_subsec("3.3.2", "Multi-Head Attention (MHA)")
    add_p("Instead of performing a single attention function with dimension d_model, Multi-Head Attention projects Queries, Keys, and Values h times with different learnable projections to lower-dimensional spaces (d_k = d_v = d_model / h). This allows the model to simultaneously attend to information from different representation subspaces at different positions:")
    add_p("MultiHead(Q, K, V) = Concat(head_1, head_2, ..., head_h) * W_O")
    add_p("head_i = Attention(Q * W_i^Q,  K * W_i^K,  V * W_i^V)")
    add_p("Where W_i^Q in R^{d_model x d_k}, W_i^K in R^{d_model x d_k}, W_i^V in R^{d_model x d_v}, and W_O in R^{h*d_v x d_model}. For standard architectures, d_model = 512, h = 8, d_k = 64; in frontier models (e.g. GPT-3), d_model = 12288, h = 96, d_k = 128.")

    add_subsec("3.3.3", "Positional Encodings: Sinusoidal, Learned, and RoPE")
    add_p("Because self-attention contains no recurrence and no convolution, it is permutation-equivariant: shuffling the input sequence yields identical shuffled outputs. To infuse sequential order, Positional Encodings must be injected into input token embeddings:")
    add_bullet("Sinusoidal Positional Encoding (Vaswani et al., 2017): Uses fixed trigonometric functions of varying frequencies:\nPE_(pos, 2i) = sin(pos / 10000^(2i / d_model))\nPE_(pos, 2i+1) = cos(pos / 10000^(2i / d_model))\nAllows the model to easily attend by relative positions, since for any fixed offset k, PE_(pos+k) can be represented as a linear function of PE_(pos).")
    add_bullet("Learned Positional Embeddings (BERT, GPT-2): Learn a dedicated positional parameter vector for each position index up to a fixed maximum sequence length (e.g., 2048 tokens).")
    add_bullet("Rotary Position Embedding (RoPE; Su et al., 2021): The contemporary standard (used in LLaMA, PaLM, Gemini). Incorporates relative positional information by rotating Query and Key vectors in the complex plane by an angle proportional to their sequence position: R_Theta,m^d * q_m. RoPE guarantees that the dot product <R_m * q, R_n * k> depends solely on the relative distance (m - n), enabling superior length extrapolation.")

    add_subsec("3.3.4", "Position-Wise Feed-Forward Networks, Residual Connections, and LayerNorm")
    add_p("In addition to attention sub-layers, each Transformer block contains a Position-Wise Feed-Forward Network (FFN) applied to each token position identically and separately:")
    add_p("FFN(x) = max(0, x * W_1 + b_1) * W_2 + b_2")
    add_p("Typically, the inner dimension of the FFN is 4 times d_model (e.g., d_ff = 4 * 512 = 2048).")
    add_p("To facilitate gradient flow across dozens of layers, Residual Connections (He et al., 2016) surround every sub-layer, followed by Layer Normalization (Ba et al., 2016):")
    add_p("x_sub = LayerNorm(x + SubLayer(x))    (Post-LN Formulation)")
    add_p("Modern LLMs universally adopt Pre-LN (LayerNorm applied before the sub-layer: x + SubLayer(LayerNorm(x))) or RMSNorm (Zhang and Sennrich, 2019), which eliminates mean-centering, scaling solely by root-mean-square variance to stabilize pretraining.")

    add_sec("3.4", "Large Language Models: Comprehensive Taxonomy and Comparative Architectures")
    add_p("Large Language Models diverge primarily across three structural archetypes: Encoder-Only, Decoder-Only, and Encoder-Decoder architectures.")

    add_subsec("3.4.1", "Architectural Archetypes")
    add_bullet("Encoder-Only (Autoencoding) Models: Process text bidirectionally. Every token can attend to all preceding and subsequent tokens simultaneously. Exemplified by BERT [3] and RoBERTa. Trained via Masked Language Modeling (MLM). Ideal for extraction, classification, and sequence tagging, but inherently incapable of autoregressive free-form generative reasoning required for autonomous agents.")
    add_bullet("Decoder-Only (Autoregressive / Causal) Models: Process text causally from left to right. Employs a Causal Mask in the attention computation (setting upper-triangular logits to -infinity) to ensure token position i cannot attend to future tokens j > i. Exemplified by the GPT series [1], LLaMA [8], and PaLM [7]. Trained via Causal Language Modeling (CLM): P(W) = prod_{t=1}^T P(w_t | w_1, ..., w_{t-1}). This is the dominant architecture for autonomous reasoning agents.")
    add_bullet("Encoder-Decoder (Sequence-to-Sequence) Models: Maintain a bidirectional encoder paired with a causal autoregressive decoder. Exemplified by T5 [4] and BART. Ideal for mapping a distinct source sequence into an output sequence (e.g., translation, summarization).")

    add_subsec("3.4.2", "Detailed Model-by-Model Analysis")
    add_p("The seminar committee expects comprehensive technical mastery of the major foundational models cited in literature:")
    add_bullet("The GPT Family (OpenAI): GPT-1 (2018; 117M params) pioneered unsupervised generative pretraining followed by supervised fine-tuning. GPT-2 (2019; 1.5B params) demonstrated zero-shot multi-task capability on raw text without task fine-tuning. GPT-3 (2020; 175B params; Brown et al. [1]) established scaling laws and in-context few-shot learning across 96 attention layers and 12,288 hidden dimension. GPT-4 / GPT-4o (2023–2024) scaled this via Mixture-of-Experts (MoE) architectures, integrating multimodal native audio and vision perception.")
    add_bullet("BERT (Devlin et al., NAACL 2019 [3]): Bidirectional Encoder Representations from Transformers. Base: 12 layers, 768 hidden, 110M params; Large: 24 layers, 1024 hidden, 340M params. Pretrained on Masked Language Modeling (15% tokens masked: 80% [MASK], 10% random, 10% unchanged) and Next Sentence Prediction (NSP). Disadvantage for agents: Cannot perform open-ended generation.")
    add_bullet("T5 (Raffel et al., JMLR 2020 [4]): Text-to-Text Transfer Transformer. Scaled up to 11B parameters. Unified every NLP task into a text-to-text format ('translate English to German: ...', 'cola sentence: ...'). Trained via span-corruption (denoising consecutive spans with sentinel tokens <extra_id_0>).")
    add_bullet("PaLM (Chowdhery et al., 2023 [7]): Pathways Language Model. 540B dense decoder-only model trained across 6,144 TPU v4 chips using Google's Pathways system. Introduced SwiGLU activations, RoPE embeddings, and multi-query attention (MQA) where all attention heads share a single Key and Value projection, drastically accelerating autoregressive inference KV-caching. Evolved into Gemini 1.5 and 3.1 Flash-Lite architectures [9].")
    add_bullet("LLaMA (Touvron et al., Meta 2023 [8]): Demonstrated that smaller, open-weights models (7B, 13B, 65B, and later 70B in LLaMA-3.3) trained on massive token corpora (up to 15 trillion tokens) outperformed proprietary models like GPT-3 while running efficiently on local consumer GPU infrastructure. Key technical innovations: Pre-normalization using RMSNorm, SwiGLU activation functions, Rotary Position Embeddings (RoPE), and Grouped-Query Attention (GQA).")

    # Table 3.1
    p_t_intro = doc.add_paragraph()
    p_t_intro.paragraph_format.space_before = Pt(8)
    p_t_intro.paragraph_format.space_after = Pt(4)
    r_ti = p_t_intro.add_run("Table 3.1 provides a systematic comparative synthesis of these foundation model families:")
    r_ti.font.bold = True
    r_ti.font.color.rgb = C_NAVY

    tbl_m = doc.add_table(rows=1, cols=6)
    m_widths = [Inches(1.2), Inches(1.1), Inches(1.1), Inches(1.0), Inches(1.1), Inches(1.0)]
    m_headers = ["Model Family", "Architecture", "Attention Style", "Normalization", "Pretraining Task", "Agent Role"]
    m_data = [
        ["BERT", "Encoder-Only", "Full Bidirectional", "Post-LN", "Masked LM + NSP", "Extraction / Classifier"],
        ["T5", "Encoder-Decoder", "Cross-Attention", "Post-LN", "Span Corruption", "Translation / Rewrite"],
        ["GPT-3 / GPT-4", "Decoder-Only (MoE)", "Causal Masked", "Pre-LN", "Autoregressive CLM", "Primary Cognitive Core"],
        ["PaLM / Gemini", "Decoder-Only (MQA)", "Causal RoPE", "RMSNorm", "Autoregressive Multi-token", "High-Throughput Reasoning"],
        ["LLaMA-3.3-70B", "Decoder-Only (GQA)", "Causal RoPE GQA", "RMSNorm", "Autoregressive (15T tokens)", "Open-Weights Agent Brain"]
    ]
    style_table(tbl_m, m_widths, m_headers, m_data)

    add_sec("3.5", "LLM Agent Architecture: Cognitive Core, Planning, Memory, and Tools")
    add_p("An autonomous agent is an encapsulated computational entity that uses an LLM as its central decision-making engine. Structurally, an agent consists of five decoupled modules:")
    add_bullet("Cognitive Reasoning Core: The foundation model conditioned with a System Prompt defining its persona, operational role, behavioural rules, and output schema formatting.")
    add_bullet("Planning Subsystem: Responsible for macro-level goal decomposition and micro-level action scheduling.")
    add_bullet("Memory Subsystem: Divided into Short-Term Memory (in-context message history, tool observations, active scratchpads) and Long-Term Memory (vector databases storing external domain documents, retrieved via semantic embedding cosine similarity).")
    add_bullet("Tool Execution Subsystem: Intercepts structured JSON function calls emitted by the LLM, verifies argument schemas, executes target APIs or shell scripts in isolated runtimes, and formats output strings back into prompt context.")
    add_bullet("Perception & Action Interfacing: Manages environment interaction protocols, receiving user objectives and transmitting finalized responses.")

    add_sec("3.6", "Agent Deliberative Reasoning and Planning Paradigms")
    add_p("To solve complex tasks, agents rely on structured deliberative reasoning paradigms:")
    add_bullet("Chain-of-Thought (CoT; Wei et al., NeurIPS 2022 [10]): Prompts the LLM to emit a step-by-step reasoning trace before arriving at a final answer. Kojima et al. (2022) [11] showed that simply appending 'Let's think step by step' elicits zero-shot CoT, activating latent arithmetic and logic circuits.")
    add_bullet("ReAct (Reasoning + Acting; Yao et al., ICLR 2023 [24]): Synergizes reasoning traces with action execution in an alternating cycle: Thought -> Action -> Observation -> Thought.")
    add_bullet("Tree of Thoughts (ToT; Yao et al., NeurIPS 2023 [16]): Generalizes CoT from linear sequences to tree search. The agent generates multiple candidate thoughts at each step, evaluates their heuristic promise via self-assessment, and searches the tree using Breadth-First Search (BFS) or Depth-First Search (DFS) with backtracking.")
    add_bullet("Graph of Thoughts (GoT; Besta et al., AAAI 2024 [17]): Generalizes ToT to arbitrary directed graphs, enabling the combination of distinct thought branches and cyclic refinement.")
    add_bullet("Reflexion (Shinn et al., NeurIPS 2023 [18]) & Self-Refine (Madaan et al., NeurIPS 2023 [19]): Incorporates verbal reinforcement learning, prompting the agent to inspect its past failed execution trace, generate a natural language critique, and store it in memory to condition future attempts.")

    add_sec("3.7", "Multi-Agent Systems (MAS) Fundamentals and Message Passing")
    add_p("When scaling from a single agent to a multi-agent system, the primary engineering mechanism shifts to Inter-Agent Communication and Coordination Protocols:")
    add_bullet("Agent Personas & Functional Specialization: Each agent is initialized with a distinct system prompt confining its operational focus. In our framework, we instantiate five canonical roles: Planner (decomposition), Researcher (information gathering), Analyst (quantitative modeling), Critic (adversarial audit), and Finalizer (consolidation).")
    add_bullet("Message-Passing Paradigms: Agents communicate by serializing structured dataclasses (e.g., AgentMessage containing sender, receiver, role, timestamp, token counts, and textual payload). Communication can occur via Shared Blackboard (all agents read and write to a common memory log) or Point-to-Point Messaging (directed routing along graph edges).")
    add_bullet("Coordination Models: Can be Synchronous (blocking turn-taking where agent j awaits agent i) or Asynchronous (event-driven message queues). MultiAgentTopologyEval implements synchronous orchestration to maintain deterministic execution tracking and reproducible telemetry profiling.")

print("Chapter 3 module written.")

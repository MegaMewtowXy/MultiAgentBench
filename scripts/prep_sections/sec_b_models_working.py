"""
sec_b_models_working.py
Section B: Step-by-Step Architecture, Internal Working, and Mechanisms of All Key Foundation Models.
Exhaustive walkthroughs of BERT, T5, GPT Family, PaLM, LLaMA, and Gemini.
"""

from docx.shared import Pt, Inches

def add_section_b(doc, helpers):
    add_main_sec = helpers['add_main_sec']
    add_sub_sec = helpers['add_sub_sec']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_callout = helpers['add_callout']
    style_table = helpers['style_table']

    add_main_sec("SECTION B", "STEP-BY-STEP WORKING AND ARCHITECTURAL MECHANICS OF FOUNDATION MODELS")

    add_p("The seminar instructions state: 'You are expected to know all the models, their working and other details in the report.' During an MCA viva, the examiner can point to any model mentioned in your report or presentation—whether BERT, T5, GPT-4, LLaMA, PaLM, or Gemini—and ask: 'Explain its forward pass, its pretraining objective, its attention masking pattern, and why it is or is not suitable as an autonomous agent reasoning core.' This section equips you with comprehensive, step-by-step answers for every model.")

    add_sub_sec("B.1", "BERT: Bidirectional Encoder Representations from Transformers (Devlin et al., NAACL 2019)")
    add_p("Architecture & Structural Specifications:", bold=True)
    add_bullet("Encoder-Only Transformer: Composed exclusively of bidirectional Transformer encoder blocks. BERT-Base has L = 12 layers, hidden size d_{model} = 768, attention heads h = 12, total parameters = 110M. BERT-Large has L = 24 layers, d_{model} = 1024, h = 16, total parameters = 340M.")
    add_bullet("Input Representation: Every input token embedding is the element-wise sum of three embeddings: Token Embedding (WordPiece vocabulary of 30,522) + Segment Embedding (distinguishing Sentence A from Sentence B) + Position Embedding (learned absolute positional encodings up to sequence length 512).")
    add_bullet("Full Bidirectional Attention: Unlike causal decoders, BERT's attention mask is an all-ones matrix: every token attends to every other token (past, present, and future) in the sequence simultaneously: Attention_{ij} = softmax( (q_i k_j^T) / sqrt(d_k) ) v_j for all j in [1, N].")
    
    add_p("Pretraining Objectives (Two-Task Formulation):", bold=True)
    add_bullet("1. Masked Language Modeling (MLM): 15% of all input tokens are selected at random. Of these selected tokens: 80% are replaced with the special token [MASK], 10% are replaced with a random vocabulary token, and 10% are left unchanged. The model predicts the original identity of the masked tokens using cross-entropy loss over the final hidden states. Why 80/10/10? If the token was always [MASK], the model would never learn representations for ordinary words during fine-tuning. Replacing 10% with random tokens forces the model to maintain a contextual representation of every token.")
    add_bullet("2. Next Sentence Prediction (NSP): The model receives sentence pairs (Sentence A, Sentence B) separated by [SEP]. In 50% of pairs, B is the actual subsequent sentence in the corpus (IsNext); in 50%, B is a randomly selected sentence (NotNext). The hidden vector of the special classification token [CLS] is projected through a binary classification head to predict IsNext.")

    add_p("Role in Autonomous Agents & Fundamental Limitation:", bold=True)
    add_p("Why can't BERT be an autonomous agent cognitive core? Because BERT is an encoder-only model. It has no causal masking and cannot generate autoregressive tokens sequentially. If asked to 'propose a 3-step cloud migration plan', BERT cannot generate text token-by-token. In agent architectures, BERT is utilized exclusively as an auxiliary classifier, embedding retriever, or intent parser.")

    add_sub_sec("B.2", "T5: Text-to-Text Transfer Transformer (Raffel et al., JMLR 2020)")
    add_p("Architecture & Unifying Text-to-Text Philosophy:", bold=True)
    add_bullet("Encoder-Decoder Architecture: Standard Transformer encoder connected to an autoregressive causal decoder via cross-attention layers. Scaled from Small (60M) to 11 Billion parameters.")
    add_bullet("The Text-to-Text Paradigm: Raffel et al. revolutionized NLP by framing EVERY downstream task—whether translation, summarization, sentiment classification, or question answering—as a text-in, text-out task. Instead of appending classification heads, classification is emitted as literal words: input 'cola sentence: The course is jump' -> output 'unacceptable'; input 'translate English to German: That is good' -> output 'Das ist gut'.")
    add_bullet("Relative Position Embeddings: T5 discarded absolute position encodings. Instead, it adds a scalar bias b_{i,j} directly to the attention logits based on relative distance (i - j): Logits_{ij} = (q_i k_j^T) / sqrt(d_k) + b_{i,j}. These relative positions are binned logarithmically beyond distance 8.")

    add_p("Span Corruption Pretraining Objective:", bold=True)
    add_p("Instead of masking single tokens, T5 drops consecutive spans of tokens (mean span length = 3, masking 15% of tokens) and replaces each corrupted span with a unique sentinel token (<extra_id_0>, <extra_id_1>, etc.). The decoder is trained to autoregressively emit ONLY the missing sentinel tokens and their target text: Target: '<extra_id_0> for a few <extra_id_1> at the park <extra_id_2>'. This vastly accelerates training throughput by reducing target sequence length.")

    add_sub_sec("B.3", "The GPT Family: Generative Pre-trained Transformers (OpenAI, 2018–2024)")
    add_p("Structural Evolution from GPT-1 to GPT-4o:", bold=True)
    add_bullet("GPT-1 (Radford et al., 2018; 117M params, 12 layers): Established unsupervised autoregressive pretraining followed by supervised task-specific fine-tuning.")
    add_bullet("GPT-2 (Radford et al., 2019; 1.5B params, 48 layers): Introduced zero-shot task transfer. Moved LayerNorm to the input of each sub-block (Pre-LN architecture) and added an extra LayerNorm after the final self-attention layer.")
    add_bullet("GPT-3 (Brown et al., NeurIPS 2020; 175B params, 96 layers, 12,288 hidden dimension): Scaled decoder-only models to 175B parameters. Demonstrated that massive autoregressive pretraining induces 'in-context learning'—the ability to execute novel tasks from natural language prompts and few-shot examples without parameter updates.")
    add_bullet("GPT-4 / GPT-4o (2023–2024): Scaled via sparse Mixture-of-Experts (MoE) architectures, where a gating routing network activates only a subset of expert feedforward networks per token (e.g., 2 out of 16 experts), keeping inference FLOPs manageable while expanding effective model capacity to over 1 trillion parameters.")

    add_p("The Causal Decoder-Only Forward Pass & KV Caching:", bold=True)
    add_p("In a causal decoder, token t can attend strictly to past tokens tau <= t. This is enforced by adding an upper-triangular negative infinity mask M before the softmax operation:")
    add_bullet("M_{ij} = 0 if j <= i, else -infinity")
    add_bullet("Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) + M ) * V")
    add_p("KV Caching Optimization:", bold=True)
    add_p("During autoregressive generation, generating token t+1 only requires computing the Query for token t+1 (q_{t+1}). Past Keys K_{1:t} and Values V_{1:t} do not change. By caching past Key and Value tensors in GPU memory (the KV Cache), generation time drops from O(N^2) to O(N) per step.")

    add_sub_sec("B.4", "PaLM and Google Gemini (Chowdhery et al., 2023; Gemini Team, 2024)")
    add_p("Pathways Language Model (PaLM; 540B parameters):", bold=True)
    add_bullet("Trained across two 3,072-chip TPU v4 pods (6,144 TPU chips) using Google's Pathways asynchronous distributed orchestration system over data-center networks.")
    add_bullet("Key Innovations: Replaced ReLU with SwiGLU activation functions; replaced absolute positional encodings with Rotary Position Embeddings (RoPE); implemented Multi-Query Attention (MQA) where all attention heads share a single Key and Value head to minimize KV cache footprint.")

    add_p("Google Gemini (Gemini 1.5 & Gemini 3.1 Flash-Lite):", bold=True)
    add_bullet("Native Multimodality: Trained jointly from scratch across interleaved text, audio, images, and video sequences rather than patching together separate encoders.")
    add_bullet("Million-Token Context Window: Utilizes advanced RingAttention and block-sparse attention mechanisms, allowing the model to process up to 1,000,000 to 2,000,000 tokens in a single inference call with near-perfect needle-in-a-haystack retrieval.")
    add_bullet("Gemini 3.1 Flash-Lite in MultiAgentTopologyEval: Serves as the primary high-throughput evaluation model. With ultra-low token pricing ($0.075 / 1M prompt, $0.300 / 1M completion) and rapid time-to-first-token, Flash-Lite enables cost-effective, high-volume multi-agent benchmarking without hitting API quota exhaustion.")

    add_sub_sec("B.5", "LLaMA: Large Language Model Meta AI (Touvron et al., 2023–2024)")
    add_p("Meta's open-weights LLaMA series (LLaMA-1, LLaMA-2, LLaMA-3, LLaMA-3.3-70B) democratized frontier AI by demonstrating that open architectures trained on massive token corpora could match proprietary closed models.")
    add_bullet("Core Architectural Recipe: (1) Pre-normalization with RMSNorm for gradient stability; (2) SwiGLU activation functions with hidden dimension (8/3)*d_{model}; (3) Rotary Position Embeddings (RoPE) applied to Queries and Keys; (4) Grouped-Query Attention (GQA) with 8 Key-Value heads to balance throughput and expressive capacity.")
    add_bullet("Over-Training Beyond Chinchilla Optimality: Chinchilla scaling laws (Hoffmann et al., 2022) suggested training a 7B model on ~140B tokens. Meta deliberately 'over-trained' LLaMA-3 on over 15 trillion tokens. While computationally expensive during pretraining, over-training produces a compact model that is vastly cheaper to serve during inference.")
    add_bullet("Groq Llama-3.3-70B in Our Benchmark: Executed on Groq's custom Language Processing Units (LPUs) using Tensor Streaming Architecture, achieving inference speeds exceeding 250 tokens per second.")

    add_callout("Viva Takeaway: Section B Defense Strategy",
                "When asked to compare BERT, T5, and GPT: immediately classify them by architectural family: BERT is Encoder-Only (bidirectional, classification/extraction, cannot generate), GPT is Decoder-Only (causal masked, autoregressive generation, foundation for agents), and T5 is Encoder-Decoder (cross-attention, text-to-text transformation).")

print("Section B module written.")


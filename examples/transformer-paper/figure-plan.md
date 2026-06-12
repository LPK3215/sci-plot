# Figure Plan: Attention Is All You Need

**Total Figures**: 3  
**Style**: paper-figure (default)  
**Language**: English  
**Aspect Ratio**: 2:3 (portrait) for mechanisms, 16:9 (landscape) for overview  
**Purpose**: Technical blog / README illustration

---

## Figure 1: Transformer Architecture Overview
**Type**: method-overview  
**Aspect Ratio**: 2:3 (portrait)  
**Purpose**: Show the full encoder-decoder flow at a glance

**Content**:
- Left side: Encoder stack (6 layers)
  - Input embedding + positional encoding
  - Multi-head attention → Add & Norm → FFN → Add & Norm
- Right side: Decoder stack (6 layers)
  - Output embedding + positional encoding
  - Masked multi-head attention → cross-attention → FFN
- Arrows showing data flow: input → encoder → decoder → output
- Key dimension annotations (d_model=512, h=8 heads, d_ff=2048)

---

## Figure 2: Multi-Head Attention Mechanism
**Type**: mechanism-detail  
**Aspect Ratio**: 2:3 (portrait)  
**Purpose**: Break down how multi-head attention works internally

**Content**:
- Top: Input splits into Q, K, V (d_model=512)
- Middle: 8 parallel attention heads
  - Each head: Q×Kᵀ → softmax → ×V
  - Show scaled dot-product formula: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V
  - Dimension per head: dₖ=dᵥ=64
- Bottom: Concatenate 8 head outputs → Linear projection → Output (512-dim)
- Highlight: attention score heatmap visualization (small grid)

---

## Figure 3: Positional Encoding
**Type**: mechanism-detail  
**Aspect Ratio**: 2:3 (portrait)  
**Purpose**: Explain how position information is injected

**Content**:
- Top: Token embedding vector (512-dim)
- Middle: Positional encoding vector (512-dim)
  - Show sinusoidal wave curves (sine for even indices, cosine for odd)
  - Formula annotation: PE(pos,2i) = sin(pos/10000^(2i/d))
- Bottom: Element-wise addition → Final input representation
- Small example: pos=0,1,2,3 encoded as color-coded wave patterns

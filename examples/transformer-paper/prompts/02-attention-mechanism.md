# Page 2: Multi-Head Attention Mechanism

## Metadata
- **Type**: mechanism-detail
- **Style**: paper-figure
- **Language**: en
- **Aspect Ratio**: 2:3

## Composition Description
Portrait layout with three main horizontal zones: top (input split), middle (parallel attention heads), bottom (concatenation). Data flows top to bottom. Eight parallel heads arranged in a 2×4 grid. Small attention heatmap visualization in one head. Clear dimension annotations at each transformation step.

## Content Elements
- Top: Input vector (d_model=512) splits into Q, K, V
- Middle: 8 attention heads arranged in grid
  - Each head: scaled dot-product attention
  - Formula: Attention(Q,K,V) = softmax(QK^T/√d_k)V
  - Show d_k = d_v = 64 per head
  - One head includes small heatmap grid showing attention scores
- Bottom: Concatenate outputs → Linear projection → Output (512-dim)
- Arrows showing data flow
- Dimension labels at each stage

---

## ▶ English Prompt (Core — Copy Directly)

A technical diagram explaining multi-head attention mechanism in paper figure style. White background. Portrait 2:3 aspect ratio.

Top section (input split):
- Large box at top labeled "Input (d_model = 512)"
- Three arrows pointing down to three boxes: "Q (Query)", "K (Key)", "V (Value)"
- Each Q/K/V box is medium-sized with light gray fill

Middle section (parallel heads):
- Label: "8 Parallel Attention Heads"
- Eight small boxes arranged in 2 rows × 4 columns
- Each box represents one attention head
- Label on first head: "Head 1: d_k = d_v = 64"
- Inside one head (bottom-left), show a small 5×5 grid with gradient shading representing attention scores
- Formula displayed prominently: "Attention(Q,K,V) = softmax(QK^T / √d_k) V"
- Downward arrows from Q/K/V to all 8 heads

Bottom section (concatenation):
- Eight thin arrows converging from the 8 heads to a single box labeled "Concat"
- Arrow from Concat box to "Linear (W^O)" box
- Final arrow to "Output (512-dim)" box at bottom

Key visual elements:
- Use rounded rectangles for all boxes
- Attention heatmap: small 5×5 grid with blue-to-yellow gradient showing attention weights
- Dimension annotations in small gray text: "512", "64", "512"
- Formula in center, slightly larger font
- Dashed box around the 8 heads labeled "h = 8 heads"

Color scheme:
- Boxes: white fill with dark gray borders
- Q/K/V boxes: light blue tint (#EBF5FF)
- Attention heads: white with blue borders
- Heatmap: blue (#2563EB) to yellow (#F59E0B) gradient
- Text: black for labels, dark gray for annotations
- Arrows: medium gray, 2px width

Visual style: Clean, professional paper figure. No 3D effects. No decorative patterns. Vector-feel modules. Emphasis on the 8 parallel heads and the attention formula.

---

## Copy to Image Generation Tool
Copy the "English Prompt" section above in full to the input box of the following tools:
- **ChatGPT (DALL-E)**: Paste directly
- **Doubao**: Text-to-image entry
- **Qwen (Tongyi Wanxiang)**: Text-to-image entry
- **Midjourney**: Paste after `/imagine`

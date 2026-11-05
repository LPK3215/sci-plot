"""
generate_architecture.py — Generate sci-plot workflow architecture diagrams (EN & CN) as SVG.

Visual language: editorial / publication-grade, aligned with the project overview page.
Light paper surface, ink typography, one blue accent, hairline rules, no glow or gradients.

Usage:
    python docs/scripts/generate_architecture.py

Output:
    docs/architecture.svg
    docs/architecture_cn.svg
"""

import os

W, H = 1000, 680

# Design tokens (kept in sync with docs/project_overview/index.html)
PAPER = "#F7F8FA"
SURFACE = "#FFFFFF"
INK = "#0E1A2B"
BODY = "#435266"
MUTED = "#6B7A8D"
LINE = "#E1E7EE"
LINE_2 = "#CBD5E0"
BLUE = "#1E4FD8"
BLUE_SOFT = "#EDF2FF"
TEAL = "#0B8A78"
TEAL_SOFT = "#E8F5F2"
AMBER = "#B4690E"
AMBER_SOFT = "#FDF3E4"
ARROW = "#94A3B8"

SERIF = "Cambria, Georgia, 'Times New Roman', serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', Arial, sans-serif"
MONO = "Consolas, 'SFMono-Regular', Menlo, monospace"

COPY = {
    "en": {
        "title": "Sci-Plot Workflow Pipeline",
        "subtitle": "Any skill repository + business topic -> portable Markdown prompt assets",
        "meta": "v1.2.0   /   DETERMINISTIC 5-ROUND PIPELINE",
        "p1": "01   INPUT & SEMANTIC ANALYSIS",
        "p2": "02   RULES POOL & SCOPE ISOLATION",
        "p3": "03   DELIVERABLES & CONSUMPTION",
        "r0": ("ROUND 0", "Determine Target", "Auto-detect .tex / .md / code / text"),
        "r1": ("ROUND 1", "Deep Analysis", "Innovations / data flow / formulas / baselines"),
        "r2": ("ROUND 2", "Extract Visuals", "Must-illustrate vs skip filter"),
        "pool": "Dual-Track Rules Pool",
        "local_tag": "LOCAL",
        "cloud_tag": "CLOUD",
        "local": "Local  -  paper-figure, sketchnote, custom .md",
        "cloud": "Cloud  -  journal guides, live URLs, external skills",
        "r3": ("ROUND 3", "Match & Confirm", "Aspect ratio, count, rule source"),
        "iso": ("SCOPE ISOLATION", "Drop every unselected rule;", "keep exactly one locked spec"),
        "r4": ("ROUND 4", "Compile Prompts", "base-rules + one locked rule"),
        "r5": ("ROUND 5", "Output & Deliver", "Structured Markdown prompt files"),
        "out": "Deliverables   sci-plot-output/",
        "consume": "Universal Multi-Platform Consumption",
        "files": [("analysis.md", "Deep analysis"), ("figure-plan.md", "Figure plan"),
                  ("prompts/*.md", "Per-figure prompts"), ("README.md", "Usage guide")],
        "platforms": ["ChatGPT / DALL-E 3", "Midjourney v6.1", "Doubao / Qwen",
                      "Stable Diffusion / Flux", "SVG / HTML / Matlab / Origin"],
        "note": "Prompts are a persistent Intermediate Representation (IR) - auditable, editable, zero runtime dependencies.",
        "foot": "Sci-Plot  ·  Portable Prompt Compiler  ·  MIT License",
    },
    "cn": {
        "title": "Sci-Plot 架构流程",
        "subtitle": "任意 Skill 仓库 + 业务主题 → 可移植 Markdown 提示词资产",
        "meta": "v1.2.0   /   确定性五轮流水线",
        "p1": "01   输入与语义分析",
        "p2": "02   双轨规范池与上下文隔离",
        "p3": "03   交付物与全平台消费",
        "r0": ("ROUND 0", "锁定目标", "自动扫描 .tex / .md / 代码 / 文本"),
        "r1": ("ROUND 1", "语义深度分析", "创新点 / 数据流 / 公式 / 基准"),
        "r2": ("ROUND 2", "提取图解切片", "总览 / 机制放大 / 过滤纯文本"),
        "pool": "双轨规范池",
        "local_tag": "本地池",
        "cloud_tag": "云端池",
        "local": "本地池  -  paper-figure、sketchnote、自定义 .md",
        "cloud": "云端池  -  期刊指南、在线 URL、外部 Skill",
        "r3": ("ROUND 3", "沟通与规范匹配", "确认画幅、张数与规范来源"),
        "iso": ("烟消云散隔离", "清空全部未选规则，", "仅保留唯一锁定规范"),
        "r4": ("ROUND 4", "规范融合生成", "底座红线 + 唯一选定规范"),
        "r5": ("ROUND 5", "规范交付", "生成标准 Markdown 提示词包"),
        "out": "交付物   sci-plot-output/",
        "consume": "全平台自由消费与持久化",
        "files": [("analysis.md", "深度分析"), ("figure-plan.md", "图解总方案"),
                  ("prompts/*.md", "每页提示词"), ("README.md", "消费指引")],
        "platforms": ["ChatGPT / DALL-E 3", "Midjourney v6.1", "豆包 / 通义万相",
                      "Stable Diffusion / Flux", "SVG / HTML / Matlab / Origin"],
        "note": "提示词是可持久化的中间表示（IR）：可审计、可微调、零运行环境依赖。",
        "foot": "Sci-Plot  ·  可移植提示词编译器  ·  MIT License",
    },
}


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def text(x, y, value, size=10, fill=BODY, font=SANS, weight="400", anchor="start", spacing="0"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{esc(value)}</text>')


def rect(x, y, w, h, fill=SURFACE, stroke=LINE, r=8, sw=1, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def label(x, y, value, color=BLUE, bg=BLUE_SOFT, width=76):
    return rect(x, y, width, 17, bg, "none", 4) + text(x + 8, y + 12, value, 8.5, color, MONO, "600", spacing="0.4")


def arrow(x1, y1, x2, y2, color=ARROW):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="1.4" marker-end="url(#arrow)"/>')


def round_card(x, y, w, h, data, accent=BLUE, accent_soft=BLUE_SOFT, featured=False):
    tag, title_, desc = data
    fill = accent_soft if featured else SURFACE
    stroke = accent if featured else LINE
    sw = 1.4 if featured else 1
    out = [rect(x, y, w, h, fill, stroke, 8, sw)]
    out.append(rect(x, y, 3, h, accent, "none", 1.5))
    out.append(label(x + 16, y + 16, tag, accent, accent_soft if not featured else "#FFFFFF", 74))
    out.append(text(x + 16, y + 50, title_, 13.5, INK, SERIF, "600"))
    out.append(f'<line x1="{x+16}" y1="{y+60}" x2="{x+w-16}" y2="{y+60}" stroke="{LINE}" stroke-width="1"/>')
    out.append(text(x + 16, y + 78, desc, 9.5, MUTED))
    return "".join(out)


def build_svg(lang="en"):
    c = COPY[lang]
    o = []

    o.append('<?xml version="1.0" encoding="UTF-8"?>')
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">')
    o.append('<title>' + esc(c["title"]) + '</title>')
    o.append('<defs>'
             '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
             f'<path d="M0,1 L10,5 L0,9 Z" fill="{ARROW}"/></marker>'
             '<filter id="card-shadow" x="-5%" y="-8%" width="110%" height="120%">'
             '<feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="#0E1A2B" flood-opacity="0.05"/>'
             '</filter>'
             '</defs>')

    # Surface + brand header
    o.append(rect(0, 0, W, H, PAPER, LINE, 14, 1))
    o.append(rect(28, 24, 30, 30, BLUE, "none", 7))
    o.append(f'<path d="M35 45 L41 38 L45 41 L51 33" fill="none" stroke="#FFFFFF" stroke-width="2" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(text(70, 40, c["title"], 20, INK, SERIF, "600"))
    o.append(text(70, 58, c["subtitle"], 10.5, MUTED))
    o.append(text(970, 40, c["meta"], 9, MUTED, MONO, "500", "end", "0.6"))
    o.append(f'<line x1="28" y1="76" x2="972" y2="76" stroke="{LINE}" stroke-width="1"/>')

    # Phase 1
    o.append(text(30, 100, c["p1"], 9.5, BLUE, MONO, "600", spacing="1.2"))
    o.append(f'<line x1="30" y1="108" x2="972" y2="108" stroke="{LINE}" stroke-width="1"/>')
    for i, key in enumerate(("r0", "r1", "r2")):
        x = 30 + i * 320
        o.append(round_card(x, 120, 300, 92, c[key]))
        if i < 2:
            o.append(arrow(x + 302, 166, x + 316, 166))

    # Phase 2
    o.append(text(30, 242, c["p2"], 9.5, BLUE, MONO, "600", spacing="1.2"))
    o.append(f'<line x1="30" y1="250" x2="972" y2="250" stroke="{LINE}" stroke-width="1"/>')

    # Rules pool
    o.append(rect(30, 262, 232, 176, SURFACE, LINE, 8, 1, 'filter="url(#card-shadow)"'))
    o.append(text(46, 286, c["pool"], 12.5, INK, SERIF, "600"))
    o.append(f'<line x1="46" y1="295" x2="246" y2="295" stroke="{LINE}" stroke-width="1"/>')
    o.append(rect(44, 306, 204, 56, BLUE_SOFT, "#D9E3FF", 6))
    o.append(text(54, 326, c["local_tag"], 8.5, BLUE, MONO, "600", spacing="0.5"))
    o.append(text(54, 345, c["local"], 9, BODY))
    o.append(rect(44, 370, 204, 56, TEAL_SOFT, "#CBE9E1", 6))
    o.append(text(54, 390, c["cloud_tag"], 8.5, TEAL, MONO, "600", spacing="0.5"))
    o.append(text(54, 409, c["cloud"], 9, BODY))
    o.append(arrow(264, 350, 278, 350))

    # Round 3
    o.append(round_card(282, 262, 170, 176, c["r3"]))
    o.append(arrow(454, 350, 468, 350, AMBER))

    # Scope isolation highlight
    o.append(rect(472, 262, 156, 176, AMBER_SOFT, "#E8C79B", 8, 1.4))
    o.append(rect(472, 262, 3, 176, AMBER, "none", 1.5))
    o.append(text(488, 288, "ISOLATION", 8.5, AMBER, MONO, "600", spacing="0.6"))
    o.append(text(488, 318, c["iso"][0], 12.5, INK, SERIF, "600"))
    o.append(f'<line x1="488" y1="330" x2="612" y2="330" stroke="#E8C79B" stroke-width="1"/>')
    o.append(text(488, 352, c["iso"][1], 9, BODY))
    o.append(text(488, 368, c["iso"][2], 9, BODY))
    o.append(label(488, 392, "FOCUS GUARD", AMBER, "#FFFFFF", 108))
    o.append(arrow(630, 350, 644, 350))

    # Round 4 (featured)
    o.append(round_card(648, 262, 150, 176, c["r4"], BLUE, BLUE_SOFT, True))
    o.append(arrow(800, 350, 814, 350, TEAL))
    # Round 5
    o.append(round_card(818, 262, 152, 176, c["r5"], TEAL, TEAL_SOFT))

    # Phase 3
    o.append(text(30, 474, c["p3"], 9.5, BLUE, MONO, "600", spacing="1.2"))
    o.append(f'<line x1="30" y1="482" x2="972" y2="482" stroke="{LINE}" stroke-width="1"/>')

    # Deliverables
    o.append(rect(30, 494, 456, 150, SURFACE, LINE, 8, 1, 'filter="url(#card-shadow)"'))
    o.append(text(46, 518, c["out"], 12.5, INK, SERIF, "600"))
    for i, (fname, desc) in enumerate(c["files"]):
        x = 46 + i * 108
        o.append(rect(x, 532, 100, 50, PAPER, LINE, 5))
        o.append(text(x + 50, 552, fname, 9, BLUE, MONO, "600", "middle"))
        o.append(text(x + 50, 568, desc, 8.5, MUTED, SANS, "400", "middle"))
    o.append(text(46, 610, c["note"], 9, MUTED))

    # Consumption
    o.append(rect(506, 494, 464, 150, SURFACE, LINE, 8, 1, 'filter="url(#card-shadow)"'))
    o.append(text(522, 518, c["consume"], 12.5, INK, SERIF, "600"))
    for i, name in enumerate(c["platforms"][:4]):
        x = 522 + (i % 2) * 224
        y = 532 + (i // 2) * 30
        o.append(rect(x, y, 216, 25, PAPER, LINE, 12.5, 0.8))
        o.append(rect(x + 10, y + 9, 5, 5, BLUE if i < 2 else TEAL, "none", 2.5))
        o.append(text(x + 22, y + 16.5, name, 9, BODY))
    o.append(rect(522, 596, 440, 28, BLUE_SOFT, "#D9E3FF", 14, 1))
    o.append(text(742, 614, c["platforms"][4], 9.5, BLUE, MONO, "600", "middle"))

    # Footer
    o.append(f'<line x1="28" y1="656" x2="972" y2="656" stroke="{LINE}" stroke-width="1"/>')
    o.append(text(30, 670, c["foot"], 9, MUTED, MONO, "400", spacing="0.3"))
    o.append(text(970, 670, "docs/architecture.svg", 9, MUTED, MONO, "400", "end"))
    o.append('</svg>')

    return "\n".join(o) + "\n"


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for lang, name in (("en", "architecture.svg"), ("cn", "architecture_cn.svg")):
        path = os.path.join(base_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_svg(lang))
        print(f"Generated: {path}")


if __name__ == "__main__":
    main()

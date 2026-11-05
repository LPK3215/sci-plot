"""
generate_architecture.py — Generate sci-plot workflow architecture diagrams (EN & CN) as SVG.

Usage:
    python docs/scripts/generate_architecture.py

Output:
    docs/architecture.svg
    docs/architecture_cn.svg
"""

import os

SVG_WIDTH = 1000
SVG_HEIGHT = 680


def build_svg(lang="en"):
    is_cn = lang == "cn"

    title = "Sci-Plot 架构流程 (Workflow Pipeline v1.2.0)" if is_cn else "Sci-Plot Workflow Pipeline (v1.2.0)"
    subtitle = (
        "双轨规范池与【烟消云散】隔离机制：从学术论文到全平台提示词"
        if is_cn
        else "Dual-Track Rules Pool & Scope Isolation: From Academic Content to Cross-Platform Prompts"
    )

    phase1_title = "阶段一：输入与语义分析 (INPUT & ANALYSIS)" if is_cn else "PHASE 1: INPUT & SEMANTIC ANALYSIS"
    r0_name = "Round 0: 锁定目标" if is_cn else "Round 0: Target"
    r0_desc = "自动扫描 .tex / .md / 代码 / 文本" if is_cn else "Auto-detect .tex / .md / code / text"

    r1_name = "Round 1: 语义深度分析" if is_cn else "Round 1: Deep Analysis"
    r1_desc = "创新点 / 数据流 / 核心公式 / 基准" if is_cn else "Innovations / data flow / formulas / baselines"

    r2_name = "Round 2: 提取图解切片" if is_cn else "Round 2: Extract Visuals"
    r2_desc = "总览 / 机制放大 / 过滤纯文本" if is_cn else "Must-illustrate vs skip filter"

    phase2_title = "阶段二：双轨规范池与【烟消云散】隔离 (RULES POOL & SCOPE ISOLATION)" if is_cn else "PHASE 2: RULES POOL & SCOPE ISOLATION"
    
    pool_title = "双轨规范池 (Rules Pool)" if is_cn else "Dual-Track Rules Pool"
    local_pool = "📁 本地池: paper-figure, sketchnote, 自定义.md" if is_cn else "📁 Local Pool: paper-figure, sketchnote, custom .md"
    cloud_pool = "🌐 云端池: 期刊指南 (Nature/IEEE), 在线URL, Skills" if is_cn else "🌐 Cloud Pool: Journal guidelines, URLs, Skills"

    r3_name = "Round 3: 沟通与规范匹配" if is_cn else "Round 3: Match & Confirm"
    r3_desc = "确认画幅、张数与规范来源" if is_cn else "Confirm count, ratio & rule source"

    isolate_badge = "⚡ 烟消云散隔离" if is_cn else "⚡ Scope Isolation"
    isolate_desc = "其余候选规则全部清空，只保留唯一选定规范" if is_cn else "Unselect all candidates, keep ONLY locked rule"

    r4_name = "Round 4: 规范融合生成" if is_cn else "Round 4: Compile Prompts"
    r4_desc = "base-rules (物理红线) + 唯一选定规范" if is_cn else "base-rules + single locked rule"

    r5_name = "Round 5: 规范交付" if is_cn else "Round 5: Output & Deliver"
    r5_desc = "生成标准 Markdown 提示词包" if is_cn else "Structured Markdown prompt files"

    output_title = "交付物: sci-plot-output/" if is_cn else "Output Deliverables: sci-plot-output/"
    consume_title = "全平台自由消费与持久化 (Universal Consumption)" if is_cn else "Universal Multi-Platform Consumption"

    c1 = "ChatGPT / DALL-E (学术插图)" if is_cn else "ChatGPT / DALL-E (Academic Figures)"
    c2 = "Midjourney (高质感表现)" if is_cn else "Midjourney (Stylized Graphics)"
    c3 = "豆包 / 通义万相 (快速草图)" if is_cn else "Doubao / Qwen (Fast Drafts)"
    c4 = "Stable Diffusion / Flux" if is_cn else "Stable Diffusion / Flux (Local)"
    c5 = "SVG / HTML / Matlab / Origin" if is_cn else "SVG / HTML / Matlab / Origin"

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <defs>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="shadow" x="-4%" y="-4%" width="108%" height="112%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000" flood-opacity="0.3"/>
    </filter>
    <linearGradient id="bg-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="phase-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="rgba(30,41,59,0.7)"/>
      <stop offset="100%" stop-color="rgba(15,23,42,0.5)"/>
    </linearGradient>
    <linearGradient id="core-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="isolate-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <linearGradient id="output-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L10,5 L0,9 Z" fill="#64748b"/>
    </marker>
    <marker id="gold-arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L10,5 L0,9 Z" fill="#f59e0b"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="url(#bg-grad)" rx="14"/>

  <!-- Title Section -->
  <text x="{SVG_WIDTH/2}" y="36" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="800" fill="#f8fafc" letter-spacing="-0.5">{title}</text>
  <text x="{SVG_WIDTH/2}" y="56" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="11.5" fill="#94a3b8">{subtitle}</text>

  <!-- =================== PHASE 1: INPUT & ANALYSIS =================== -->
  <rect x="30" y="76" width="{SVG_WIDTH-60}" height="140" rx="10" fill="url(#phase-bg)" stroke="#1e293b" stroke-width="1"/>
  <rect x="44" y="84" width="260" height="20" rx="10" fill="rgba(30,41,59,0.8)" stroke="#334155" stroke-width="0.5"/>
  <text x="174" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="700" fill="#94a3b8" letter-spacing="1">{phase1_title}</text>

  <!-- Round 0 -->
  <rect x="50" y="114" width="265" height="86" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.2" filter="url(#shadow)"/>
  <text x="66" y="146" font-family="sans-serif" font-size="12" font-weight="700" fill="#818cf8">{r0_name}</text>
  <text x="66" y="172" font-family="sans-serif" font-size="10" fill="#94a3b8">{r0_desc}</text>

  <!-- Arrow 0->1 -->
  <line x1="315" y1="157" x2="355" y2="157" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Round 1 -->
  <rect x="365" y="114" width="265" height="86" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.2" filter="url(#shadow)"/>
  <text x="381" y="146" font-family="sans-serif" font-size="12" font-weight="700" fill="#818cf8">{r1_name}</text>
  <text x="381" y="172" font-family="sans-serif" font-size="10" fill="#94a3b8">{r1_desc}</text>

  <!-- Arrow 1->2 -->
  <line x1="630" y1="157" x2="670" y2="157" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Round 2 -->
  <rect x="680" y="114" width="265" height="86" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.2" filter="url(#shadow)"/>
  <text x="696" y="146" font-family="sans-serif" font-size="12" font-weight="700" fill="#818cf8">{r2_name}</text>
  <text x="696" y="172" font-family="sans-serif" font-size="10" fill="#94a3b8">{r2_desc}</text>

  <!-- =================== PHASE 2: RULES POOL & ISOLATION =================== -->
  <rect x="30" y="232" width="{SVG_WIDTH-60}" height="220" rx="10" fill="url(#phase-bg)" stroke="#1e293b" stroke-width="1"/>
  <rect x="44" y="240" width="360" height="20" rx="10" fill="rgba(30,41,59,0.8)" stroke="#334155" stroke-width="0.5"/>
  <text x="224" y="254" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="700" fill="#94a3b8" letter-spacing="1">{phase2_title}</text>

  <!-- Pool Box (Left) -->
  <rect x="50" y="270" width="250" height="166" rx="8" fill="#111827" stroke="#3b82f640" stroke-width="1.5"/>
  <text x="66" y="295" font-family="sans-serif" font-size="11" font-weight="700" fill="#60a5fa">{pool_title}</text>
  <rect x="60" y="310" width="230" height="50" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="70" y="332" font-family="sans-serif" font-size="9" fill="#e2e8f0">{local_pool}</text>
  <rect x="60" y="370" width="230" height="52" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="70" y="392" font-family="sans-serif" font-size="9" fill="#e2e8f0">{cloud_pool}</text>

  <!-- Arrow Pool -> Round 3 -->
  <line x1="300" y1="353" x2="335" y2="353" stroke="#3b82f6" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Round 3 (Communicate & Match) -->
  <rect x="340" y="270" width="180" height="166" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.2" filter="url(#shadow)"/>
  <text x="355" y="310" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#818cf8">{r3_name}</text>
  <text x="355" y="338" font-family="sans-serif" font-size="9.5" fill="#94a3b8">{r3_desc}</text>
  <text x="355" y="375" font-family="sans-serif" font-size="8.5" fill="#64748b">选定唯一样式 / 期刊</text>

  <!-- Scope Isolation Barrier / Pill -->
  <g transform="translate(530, 315)">
    <line x1="0" y1="38" x2="45" y2="38" stroke="#f59e0b" stroke-width="2" marker-end="url(#gold-arrow)"/>
    <rect x="2" y="10" width="130" height="56" rx="8" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="67" y="32" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="800" fill="#fbbf24">{isolate_badge}</text>
    <text x="67" y="50" text-anchor="middle" font-family="sans-serif" font-size="7.5" fill="#fde68a">{isolate_desc}</text>
  </g>

  <!-- Round 4 (Compile Prompts) -->
  <rect x="675" y="270" width="145" height="166" rx="8" fill="url(#core-grad)" stroke="#818cf880" stroke-width="1.8" filter="url(#glow)"/>
  <text x="688" y="310" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#c7d2fe">{r4_name}</text>
  <text x="688" y="340" font-family="sans-serif" font-size="9.5" fill="#a5b4fc">{r4_desc}</text>
  <text x="688" y="380" font-family="sans-serif" font-size="8" fill="#e0e7ff">单向编译，杜绝规则冲突</text>

  <!-- Arrow 4->5 -->
  <line x1="820" y1="353" x2="840" y2="353" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Round 5 (Output) -->
  <rect x="845" y="270" width="105" height="166" rx="8" fill="url(#output-grad)" stroke="#34d39960" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="858" y="310" font-family="sans-serif" font-size="11" font-weight="700" fill="#6ee7b7">{r5_name}</text>
  <text x="858" y="340" font-family="sans-serif" font-size="9" fill="#a7f3d0">{r5_desc}</text>

  <!-- =================== BOTTOM: OUTPUT & CONSUMPTION =================== -->
  <!-- Left: Deliverables -->
  <rect x="30" y="470" width="460" height="185" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="50" y="496" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc">{output_title}</text>

  <rect x="50" y="515" width="95" height="46" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="97" y="536" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="600" fill="#818cf8">analysis.md</text>
  <text x="97" y="550" text-anchor="middle" font-family="sans-serif" font-size="7.5" fill="#94a3b8">深度分析</text>

  <rect x="155" y="515" width="95" height="46" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="202" y="536" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="600" fill="#818cf8">figure-plan.md</text>
  <text x="202" y="550" text-anchor="middle" font-family="sans-serif" font-size="7.5" fill="#94a3b8">图解总方案</text>

  <rect x="260" y="515" width="105" height="46" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="312" y="536" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="600" fill="#818cf8">prompts/*.md</text>
  <text x="312" y="550" text-anchor="middle" font-family="sans-serif" font-size="7.5" fill="#94a3b8">每页独立提示词</text>

  <rect x="375" y="515" width="95" height="46" rx="6" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="422" y="536" text-anchor="middle" font-family="monospace" font-size="8.5" font-weight="600" fill="#818cf8">README.md</text>
  <text x="422" y="550" text-anchor="middle" font-family="sans-serif" font-size="7.5" fill="#94a3b8">使用指南</text>

  <text x="50" y="595" font-family="sans-serif" font-size="9.5" fill="#64748b">中间表示（IR）持久化保留，零运行环境依赖，随时重现与编辑</text>
  <text x="50" y="618" font-family="sans-serif" font-size="9" fill="#475569">✓ 版本可控  ✓ 免除生图环境崩溃  ✓ 支持二次微调</text>

  <!-- Right: Universal Multi-Platform Consumption -->
  <rect x="510" y="470" width="460" height="185" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <text x="530" y="496" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc">{consume_title}</text>

  <rect x="530" y="515" width="200" height="30" rx="15" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="630" y="534" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#38bdf8">{c1}</text>

  <rect x="745" y="515" width="205" height="30" rx="15" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="847" y="534" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#a78bfa">{c2}</text>

  <rect x="530" y="555" width="200" height="30" rx="15" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="630" y="574" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#34d399">{c3}</text>

  <rect x="745" y="555" width="205" height="30" rx="15" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="847" y="574" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#fbbf24">{c4}</text>

  <rect x="530" y="595" width="420" height="32" rx="16" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f180" stroke-width="1"/>
  <text x="740" y="615" text-anchor="middle" font-family="sans-serif" font-size="9.5" font-weight="600" fill="#818cf8">➔ {c5}</text>
</svg>'''
    return svg


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    en_path = os.path.join(base_dir, "architecture.svg")
    cn_path = os.path.join(base_dir, "architecture_cn.svg")

    with open(en_path, "w", encoding="utf-8") as f:
        f.write(build_svg("en"))
    print(f"Generated: {en_path}")

    with open(cn_path, "w", encoding="utf-8") as f:
        f.write(build_svg("cn"))
    print(f"Generated: {cn_path}")


if __name__ == "__main__":
    main()

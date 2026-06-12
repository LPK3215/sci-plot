# Sci-Plot — Scientific Figure Prompt Engine / 科研绘图 —— 从论文到插图的一站式引擎

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](CHANGELOG.md)
[![CodeBuddy Skill](https://img.shields.io/badge/CodeBuddy-skill-6366F1.svg)](SKILL.md)

Scientific illustration, from paper to figure — an all-in-one prompt engine. sci-plot does not generate images directly; it produces cross-platform prompts that you copy into any AI image generation tool.

科研绘图，从论文到插图的一站式引擎。不直接生图，只产出跨平台提示词。

## Workflow Architecture / 工作流架构

![Architecture](./docs/architecture.svg)

## Typical Use Cases / 典型使用场景

**Your paper is done — time for figures.** Your LaTeX paper (`.tex` file) is complete: methods, formulas, experiments are all written, but you lack a high-quality method architecture diagram or mechanism flowchart. Point sci-plot at your project directory or .tex file. It reads everything, proposes a figure plan, you confirm the parameters, and it outputs prompts for each figure. Copy the prompts to Doubao / Qwen / ChatGPT / Midjourney — images appear in seconds.

**论文写好了，该配图了。** 你的 LaTeX 论文（`.tex` 文件）已经完成，方法、公式、实验都写了，但缺少一张高质量的方法架构图或机制流程图。把项目目录或 .tex 文件交给 sci-plot，它读完全文后给出图解方案，你确认参数，它输出每张图的提示词。复制提示词到豆包 / Qwen / ChatGPT 等工具，几秒钟出图。

**Best results come from complete content.** The more complete and well-structured your input is, the more precise the extraction and the better the prompts will match your paper's academic context. Vague one-line ideas still work, but the output will be more generic.

**有现成文章的时候效果最好。** 内容越完整、结构越清晰，提取就越精准，生成的提示词也越贴合你的论文学术语境。如果只给一句模糊的想法，sci-plot 也能生成提示词，但会偏泛化、缺少论文特有的学术约束。

Also suitable for: project README illustrations, technical blog visuals, defense presentation slides, algorithm explanation diagrams.

也适用于：项目 README 配图、技术博客插图、答辩 PPT 配图、算法讲解图。

## Installation / 安装

```bash
git clone https://github.com/LPK3215/sci-plot.git
```

After cloning, open the sci-plot directory (or add it as a workspace/subproject). The AI will read SKILL.md and apply its rules.

克隆后，打开 sci-plot 目录（或把整个目录作为工作区/子项目打开），AI 就能读到 SKILL.md 中的规则。

## Usage / 使用方式

### Basic Usage / 基本用法

After cloning, open the sci-plot directory and send this prompt to the AI:

git clone 后打开 sci-plot 目录，直接发送给 AI 这段提示词：

```
Follow the /sci-plot/SKILL.md skill to generate scientific figure prompts.
Target: [optional — leave blank to auto-analyze current project]

按照 /sci-plot/SKILL.md 技能的要求输出科研绘图提示词。
目标：[可选，不填则自动分析当前项目]
```

**Target** supports any of the following formats:

**目标**支持以下任意一种写法：

- Leave blank → auto-analyze current project, prioritizing `.tex` files
- 留空 → 自动分析当前项目，优先找 `.tex` 文件
- Local path → `/path/to/your/paper/`
- 本地路径 → `/path/to/your/paper/`
- arxiv link → `https://arxiv.org/abs/2401.12345`
- arxiv 链接 → `https://arxiv.org/abs/2401.12345`
- Pasted content → paste abstract, method description, or algorithm steps directly
- 粘贴内容 → 直接粘贴论文摘要、方法描述或算法步骤
- arxiv ID → `1706.03762`

### Interaction Flow / 交互流程

1. AI analyzes your content and proposes a figure plan
2. You confirm: language (Chinese/English/Bilingual), style, number of figures, aspect ratio, purpose
3. AI generates prompt files into `sci-plot-output/prompts/` directory
4. You copy prompts into any AI image generation tool

1. AI 分析你的内容，给出图解方案建议
2. 你确认：语言（中文/English/双语）、风格、张数、比例、用途
3. AI 生成提示词文件到 `sci-plot-output/prompts/` 目录
4. 你复制提示词到生图工具中出图

### Available Styles / 可用风格

| Style / 风格 | Effect / 效果 | Best for / 适合 |
|------|------|------|
| **paper-figure** (default) | Paper figure style, white background, vector modules, restrained colors / 论文框架图风，白底、矢量模块、克制配色 | Journal figures, README hero images, technical displays / 论文配图、README、技术展示 |
| **sketchnote** | Warm research notes style, cream background, hand-drawn lines / 温暖科研笔记风，米白底、手绘线条 | Knowledge sharing, learning notes / 知识分享、学习笔记 |
| **journal-minimal** | Nature/IEEE style, extremely minimal academic / Nature/IEEE 风，极简学术 | Paper submission, defense / 论文投稿、答辩 |
| **warm-notes** | Bright handwritten style, approachable yet professional / 明亮手记风，亲和教学感 | Science communication, courses / 科普、课程 |
| **business-research** | Business research brief style, structured, data-driven / 商业简报风，结构化数据驱动 | Industry analysis, investor presentations / 行业分析、汇报 |

### Where to Paste Prompts / 提示词复制到哪些工具

| Tool / 工具 | Action / 操作 |
|------|------|
| **ChatGPT (recommended)** | Paste into DALL-E / 粘贴到 DALL-E |
| Doubao / 豆包 | Text-to-image → paste prompt / 文生图 → 直接粘贴提示词 |
| Qwen (Tongyi Wanxiang) / 通义万相 | Text-to-image → paste prompt (English works best) / 文生图 → 粘贴提示词（英文效果更好） |
| Midjourney | `/imagine` then paste prompt / `/imagine` 后粘贴提示词 |
| Stable Diffusion | txt2img paste / txt2img 粘贴 |
| Other image gen tools | Works equally well / 同样适用 |

### Output File Structure / 产出文件结构

```
sci-plot-output/
├── analysis.md          # Content analysis summary / 内容分析摘要
├── figure-plan.md       # Figure plan (what each page covers) / 图解方案（每页讲什么）
├── prompts/
│   ├── 01-overview.md   # Page 1 prompt / 第 1 页提示词
│   ├── 02-mechanism.md  # Page 2 prompt / 第 2 页提示词
│   └── ...
└── README.md            # This README / 本说明
```

## Project Structure / 项目结构

```
sci-plot/
├── SKILL.md                              # AI instruction: 6-round mandatory workflow / AI 指令：6 轮强制工作流
├── README.md                             # User-facing documentation / 用户说明文档
├── LICENSE                               # MIT License / MIT 许可证
├── CHANGELOG.md                          # Version history / 版本历史
├── CONTRIBUTING.md                       # Contribution guidelines / 贡献指南
├── .gitignore                            # Version control exclusions / 版本控制排除
├── .gitattributes                        # Line ending normalization / 行尾规范化
├── project_overview.html                 # Project overview dashboard entry / 项目全景观览页入口
├── project_overview/
│   ├── styles.css                        # Dark theme styles / 深色主题样式
│   └── main.js                           # Interactive logic / 交互逻辑
├── docs/
│   ├── architecture.svg                  # Workflow architecture diagram / 工作流架构图
│   └── scripts/
│       └── generate_architecture.py      # Architecture diagram generation script / 架构图生成脚本
└── references/
    ├── prompt-rules.md                   # Core prompt generation rules / 提示词生成核心规则
    ├── analysis-guide.md                 # Content analysis guide / 内容分析指南
    ├── layout-rules.md                   # Page composition & role definitions / 页面构图与角色定义
    └── styles/
        ├── paper-figure.md               # Paper figure style / 论文框架图风
        ├── sketchnote.md                 # Warm sketchnote style / 温暖科研笔记风
        ├── journal-minimal.md            # Nature/IEEE minimal style / Nature/IEEE 极简风
        ├── warm-notes.md                 # Bright handwritten style / 明亮手记风
        └── business-research.md          # Business research brief style / 商业简报风
```

## FAQ / 常见问题

**Q: Can sci-plot generate images directly? / sci-plot 能直接生成图片吗？**
A: No. sci-plot only produces prompts. You copy the prompts into ChatGPT/DALL-E, Doubao, Qwen, Midjourney, or other image generation tools. This approach makes prompts cross-platform compatible, not tied to any specific tool.
不能。sci-plot 只产出提示词，你需要把提示词复制到 ChatGPT/DALL-E、豆包、Qwen、Midjourney 等生图工具中出图。这样做的好处是提示词跨平台通用，不绑定任何特定工具。

**Q: Can I use it without a complete paper or project? / 没有完整的论文或项目能用吗？**
A: Yes, but results will be less precise. sci-plot works best with complete content — the more complete and well-structured your input, the more accurate the extraction. A vague one-liner still produces prompts, but they'll be more generic.
可以，但效果会打折。sci-plot 有现成文章时效果最好——内容越完整、结构越清晰，提取就越精准。如果只给一句模糊的想法，生成的提示词会偏泛化。

**Q: What input formats are supported? / 支持哪些输入格式？**
A: LaTeX papers (`.tex`, highest priority), Markdown documents, PDF, Python source code, arxiv links or IDs, and pasted text content.
支持 LaTeX 论文（`.tex`，优先级最高）、Markdown 文档、PDF、Python 源码、arxiv 链接或 ID，以及直接粘贴的文本内容。

**Q: Which part of the prompt file is the core output? / 提示词文件里哪个部分是核心？**
A: The `▶ English Prompt (core, copy directly)` section in each prompt file is the core output. Copy it directly into any image generation tool. The Chinese explanations, composition descriptions, and content elements are for human reference.
每个提示词文件的 `▶ English Prompt（核心，直接复制）` 部分是核心产出，直接复制到生图工具即可。中文说明、构图描述、内容元素是给人看的解释。

**Q: How do I add a new visual style? / 如何添加新的视觉风格？**
A: Create a new `.md` file under `references/styles/`, follow the format of existing style files, then register it in the style tables in both `SKILL.md` and `README.md`. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.
在 `references/styles/` 下创建新 `.md` 文件，参照现有风格文件的格式，然后在 `SKILL.md` 和 `README.md` 的风格表中注册。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**Q: What's the maximum number of figures? / 最多能生成几张图的提示词？**
A: Minimum 1, maximum 10. The exact number depends on content complexity: simple content 1-3, medium 4-6, complex 6-10.
最少 1 张，最多 10 张。具体张数取决于内容复杂度：简单内容 1-3 张，中等 4-6 张，复杂 6-10 张。

## Author / 作者

- **LPK3215** — [GitHub](https://github.com/LPK3215)

## License / 许可证

MIT — see [LICENSE](LICENSE) for details. / 详见 [LICENSE](LICENSE)

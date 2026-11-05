# HTML 独立可插拔渲染器 (Pluggable HTML Renderer)

本目录为 `sci-plot` 的**下游独立扩展模块**。它的唯一职责是：**在主线生图提示词全部落盘之后，单向将提示词结构转化为可交互、自包含的 HTML 网页图表**。

---

## 核心特性

1. **可插拔与完全独立**：
   - 核心提示词与规则保存在 [`prompt-profile.md`](prompt-profile.md)；
   - 你可以随时修改它、替换为新规范，甚至**单独将这个文件拷出去作为一个独立的 AI 提示词使用**；
   - 整体行为由 [`config.json`](config.json) 声明，未来可配置多个 profile（例如 `tailwind-profile.md`, `canvas-profile.md` 等）。

2. **绝对防干扰（Zero Context Bleed）**：
   - 在主线工作流（Round 0 ~ Round 5）执行期间，本目录处于**绝对休眠**状态，大模型严禁提前索引或读取本目录任何内容；
   - 只有在 Round 5 提示词完全落地、且用户明确下达转换指令时，才会被单独加载。

---

## 目录结构

```
references/renderers/html/
├── config.json             # 渲染器全局配置（指定激活的 profile 与输出路径）
├── prompt-profile.md       # 【核心配置插槽】：存放可插拔转换提示词
└── README.md               # 本使用说明
```

---

## 两种运行模式

### 模式 A：作为 sci-plot 的下游扩展运行（联动模式）
在 `sci-plot` 生成完提示词后，只需告诉 AI：
> *“把刚刚生成的 prompts/*.md 按照 html-renderer 规范转换为 HTML”*

AI 将读取 `prompt-profile.md` 中的规范，将每张图的结构单向编译并保存至 `sci-plot-output/html/` 目录下。

### 模式 B：完全脱离项目的单独使用（单机模式）
直接打开 `prompt-profile.md`，把里面的转换提示词复制到任何 AI 工具（ChatGPT / Claude / Cursor 等），然后把任意图表或文字描述贴给它，即可独立完成 HTML 代码生成。


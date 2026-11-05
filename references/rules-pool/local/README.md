# 本地规范池 (Local Rules Pool)

这里存放你最常用、长期维护的本地绘图规范与风格定义文档。

> **智能动态感知原则**：`sci-plot` 在执行本地规范检索时，**绝不依赖死板的硬编码列表**，而是实时动态扫描本目录下的所有 `.md` 文件（包括 5 款预置规范、用户自建规范、以及从云端或 GitHub 下载沉淀的 `downloaded-*.md` 文件）。

---

## 一、 5 款内置原生预置规范

1. [`paper-figure.md`](paper-figure.md)：顶会论文框架图风（默认推荐，白底、矢量线框、克制配色）。
2. [`journal-minimal.md`](journal-minimal.md)：Nature / IEEE 极简学术风。
3. [`sketchnote.md`](sketchnote.md)：手绘笔记风（适合知识分享与讲解）。
4. [`warm-notes.md`](warm-notes.md)：明亮手记风（适合科普与教学）。
5. [`business-research.md`](business-research.md)：商业简报风（结构化、数据驱动）。

---

## 二、 云端 / GitHub 下载沉淀规范 (`downloaded-*.md`)

当用户输入云端期刊指南、在线网页或 GitHub 开源 Skill 仓库地址后，AI 会自动提取核心规范并下载至本目录，例如：
- `downloaded-academic-research-skills.md`
- `downloaded-nature-skills.md`
- `downloaded-scientific-agent-skills.md`

一旦下载落盘，它们就立刻成为**一等公民本地规范**，支持断网离线使用，并在下次本地检索时被自动列出。

---

## 三、 如何添加你自己的新规范？

直接在这个目录下新建一个 `.md` 文件（例如 `my-lab-style.md` 或 `icml-poster.md`），包含以下几个核心要点即可：
- **画布背景**（如纯白 #FFFFFF）
- **限定配色**（主色 + 1~2 种强调色号）
- **线条与模块要求**（如直角线框、细线 1px、主箭头 3px）
- **核心 Prompt Snippet**（一段通用的风格英文描述词）

添加后，在对话中直接告诉 AI：*“请使用本地规范池里的 my-lab-style”*，AI 即可直接识别并应用！


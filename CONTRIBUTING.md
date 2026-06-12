# Contributing to Sci-Plot / 贡献指南

Thank you for your interest in contributing to sci-plot! This project is a CodeBuddy skill that generates scientific figure prompts.

感谢你对 sci-plot 的关注！本项目是一个生成科研绘图提示词的 CodeBuddy 技能。

## How to Contribute / 如何贡献

### Adding a New Style / 添加新风格

1. Create a new `.md` file under `references/styles/` / 在 `references/styles/` 下创建新 `.md` 文件
2. Follow the existing pattern in `paper-figure.md` or `sketchnote.md` / 参照 `paper-figure.md` 或 `sketchnote.md` 的现有模式
3. Include: style description, color palette, annotation rules, layout preferences, and an English prompt snippet / 包含：风格描述、配色方案、标注规则、布局偏好和英文提示词片段
4. Add the style to the table in `SKILL.md` (Five Visual Styles section) / 将风格添加到 `SKILL.md` 的风格表中（五种视觉风格章节）
5. Add the style to the table in `README.md` (Available Styles section) / 将风格添加到 `README.md` 的风格表中（可用风格章节）
6. Add the reference entry at the bottom of `SKILL.md` / 在 `SKILL.md` 底部添加引用条目

### Improving Existing Rules / 改进现有规则

1. Edit the relevant file in `references/` / 编辑 `references/` 中的相关文件
2. Keep rules concrete and actionable — avoid vague statements / 保持规则具体可操作——避免模糊表述
3. If adding constraints, also update `Forbidden` or `Must-Have` checklists in `prompt-rules.md` / 如果添加约束，同步更新 `prompt-rules.md` 中的禁止或必含清单
4. Test the changes by running sci-plot against a real paper / 用真实论文测试变更

### Updating the Workflow / 更新工作流

1. Edit `SKILL.md` — the workflow lives there / 编辑 `SKILL.md`——工作流在此定义
2. Each round must have `⛔` marker to indicate it's mandatory / 每轮必须有 `⛔` 标记表明其为强制步骤
3. All reference files must be listed at the bottom of `SKILL.md` / 所有参考文件必须在 `SKILL.md` 底部列出
4. Any new "Read first" instruction must have the corresponding reference file / 任何新的"先读取"指令必须有对应的参考文件

### Submitting Changes / 提交变更

1. Fork the repository / Fork 仓库
2. Create a feature branch: `git checkout -b feature/your-feature` / 创建功能分支
3. Make your changes / 进行修改
4. Commit with a descriptive message / 提交时使用描述性信息
5. Push to your fork / 推送到你的 fork
6. Open a pull request / 发起 Pull Request

## Project Structure / 项目结构

```
sci-plot/
├── SKILL.md                  # AI instruction: 6-round workflow / AI 指令：6 轮工作流
├── README.md                 # Human-facing documentation / 用户说明文档
├── LICENSE                   # MIT License / MIT 许可证
├── CHANGELOG.md              # Version history / 版本历史
├── CONTRIBUTING.md           # This file / 本文件
├── .gitignore                # Version control exclusions / 版本控制排除
├── .gitattributes            # Line ending normalization / 行尾规范化
└── references/
    ├── prompt-rules.md       # Core rules for prompt generation / 提示词生成核心规则
    ├── analysis-guide.md     # Content analysis checklists / 内容分析清单
    ├── layout-rules.md       # Page roles and composition / 页面角色与构图
    └── styles/
        ├── paper-figure.md
        ├── sketchnote.md
        ├── journal-minimal.md
        ├── warm-notes.md
        └── business-research.md
```

## Questions? / 有问题？

Open an issue on GitHub: https://github.com/LPK3215/sci-plot/issues

在 GitHub 上提交 Issue：https://github.com/LPK3215/sci-plot/issues

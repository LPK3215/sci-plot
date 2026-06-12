# Sci-Plot 贡献指南

感谢你对 sci-plot 的关注！本项目是一个生成科研绘图提示词的 CodeBuddy 技能。

[English Contribution Guide](CONTRIBUTING.md)

## 如何贡献

### 添加新风格

1. 在 `references/styles/` 下创建新 `.md` 文件
2. 参照 `paper-figure.md` 或 `sketchnote.md` 的现有模式
3. 包含：风格描述、配色方案、标注规则、布局偏好和英文提示词片段
4. 将风格添加到 `SKILL.md` 的风格表中（五种视觉风格章节）
5. 将风格添加到 `README.md` 的风格表中（可用风格章节）
6. 在 `SKILL.md` 底部添加引用条目

### 改进现有规则

1. 编辑 `references/` 中的相关文件
2. 保持规则具体可操作——避免模糊表述
3. 如果添加约束，同步更新 `prompt-rules.md` 中的禁止或必含清单
4. 用真实论文测试变更

### 更新工作流

1. 编辑 `SKILL.md`——工作流在此定义
2. 每轮必须有 `⛔` 标记表明其为强制步骤
3. 所有参考文件必须在 `SKILL.md` 底部列出
4. 任何新的"先读取"指令必须有对应的参考文件

### 提交变更

1. Fork 仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 进行修改
4. 提交时使用描述性信息
5. 推送到你的 fork
6. 发起 Pull Request

## 项目结构

```
sci-plot/
├── SKILL.md                  # AI 指令：6 轮工作流
├── README.md                 # 用户说明文档（英文）
├── README_CN.md              # 用户说明文档（中文）
├── LICENSE                   # MIT 许可证
├── CHANGELOG.md              # 版本历史（英文）
├── CHANGELOG_CN.md           # 版本历史（中文）
├── CONTRIBUTING.md           # 本文件（英文）
├── CONTRIBUTING_CN.md        # 本文件（中文）
├── .gitignore                # 版本控制排除
├── .gitattributes            # 行尾规范化
└── references/
    ├── prompt-rules.md       # 提示词生成核心规则
    ├── analysis-guide.md     # 内容分析清单
    ├── layout-rules.md       # 页面角色与构图
    └── styles/
        ├── paper-figure.md
        ├── sketchnote.md
        ├── journal-minimal.md
        ├── warm-notes.md
        └── business-research.md
```

## 有问题？

在 GitHub 上提交 Issue：https://github.com/LPK3215/sci-plot/issues

# Sci-Plot 贡献指南

感谢你对 sci-plot 的关注！本项目是一个生成科研绘图提示词的跨平台 AI 技能引擎。

[English Contribution Guide](CONTRIBUTING.md)

## 如何贡献

### 1. 向“本地规范池”添加新风格/规则

现在添加自定义规则非常简单，完全即插即用：
1. 在 `references/rules-pool/local/` 下创建新 `.md` 文件（如 `my-lab-style.md`）
2. 参照现有文件（如 `paper-figure.md`）包含：风格定位、画布与背景、限定配色（≤3色）、线框/箭头规范与核心英文提示词片段（Prompt Snippet）
3. 放入后，无需修改核心调度代码，直接在对话中指定该文件名即可被 AI 自动识别并加载

### 2. 向“云端/外部规范池”添加新渠道或 Skills 索引

1. 编辑 `references/rules-pool/cloud/cloud-channels.md`
2. 添加权威期刊图表指南链接，或开源生图 Skills 的提示词借取映射模式
3. 遵循“**只借其词（Prompt），绝不调其图（Image API）**”原则，剥离环境依赖

### 3. 改进底座物理红线与核心流程

1. 底座物理约束位于 `references/core/base-rules.md`（控制防乱码短字、色彩≤3种、无3D拟物）
2. 调度工作流位于 `SKILL.md`，任何流程修改需确保遵循【烟消云散】上下文隔离机制，防止大模型规则冲突
3. 用真实学术论文测试变更

### 4. 提交变更

1. Fork 仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 进行修改并通过自动化测试：运行 `python tests/run_all_tests.py`
4. 运行文档一致性校验：`python scripts/sync_documentation_metrics.py --check`
5. 提交时使用清晰的规范化提交信息
6. 推送到你的 fork 并发起 Pull Request

## 项目结构

```
sci-plot/
├── SKILL.md                              # AI 指令：5 轮标准化工作流与隔离调度
├── README.md                             # 用户说明文档（英文）
├── README.zh-CN.md                       # 用户说明文档（中文）
├── LICENSE                               # MIT 许可证
├── CHANGELOG.md                          # 版本历史（英文）
├── CHANGELOG.zh-CN.md                    # 版本历史（中文）
├── CONTRIBUTING.md                       # 本文件（英文）
├── CONTRIBUTING.zh-CN.md                 # 本文件（中文）
├── FAQ.md                                # 常见问题解答
├── AUTHORS                               # 作者与主要贡献者清单
├── pyproject.toml                        # 项目元数据与工具链配置
├── requirements.txt                      # Python 运行时与开发依赖说明
├── docs/                                 # GitHub Pages 部署根与架构图表资产
│   ├── index.html                        # Pages 部署重定向入口
│   ├── .nojekyll                         # 禁用 Jekyll 静态编译
│   ├── architecture.svg                  # 英文架构图
│   ├── architecture_cn.svg               # 中文架构图
│   ├── assets/
│   │   └── banner.svg                    # 品牌专属横幅 SVG
│   ├── archify/                          # Archify 可交互架构图集
│   └── project_overview/                 # 交互式全景观览页与精简名片
├── scripts/                              # 规范沉淀与雷达检索脚本
│   ├── universal_skill_harvester.py      # 自适应语义雷达扫描引擎
│   └── fetch_external_skills.py          # 外部开源技能规范拉取脚本
├── tests/                                # 自动化测试套件
│   ├── run_all_tests.py                  # 测试套件统一运行入口
│   └── test_*.py                         # 各项功能与规范测试用例
└── references/                           # 核心基座与规范池
    ├── core/                             # 核心基座
    │   └── base-rules.md                 # 底座物理红线（防乱码/限色彩/防3D）
    ├── analysis-guide.md                 # 内容分析清单
    ├── layout-rules.md                   # 页面角色与构图
    └── rules-pool/                       # 【双轨专业规范池】
        ├── local/                        # 本地规范池（预置风格与用户自定义.md）
        └── cloud/                        # 云端规范池（期刊在线指南、URL解析与Skills借取协议）
```

## 有问题？

在 GitHub 上提交 Issue：https://github.com/LPK3215/sci-plot/issues


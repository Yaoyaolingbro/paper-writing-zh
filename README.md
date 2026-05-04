# paper-writing-zh

中文优先的 AI/ML 会议论文写作 Codex skills 仓库。

这个仓库包含一个主论文写作 skill suite，以及用于生成会议风格 skill 的 prompt。它面向已经有研究工作和部分实验结果、但还需要梳理论文故事线、补充实验、大纲、LaTeX 注释草稿和学术英文表达的写作场景。

## 仓库结构

```text
.
├── README.md
├── install.sh
├── create-paper-style.md
├── ai-paper-writing-zh/
│   ├── SKILL.md
│   ├── abstract-writing/
│   │   └── SKILL.md
│   ├── outline-writing/
│   │   └── SKILL.md
│   ├── latex-comment-drafting/
│   │   └── SKILL.md
│   ├── chinese-expansion/
│   │   └── SKILL.md
│   ├── academic-translation/
│   │   └── SKILL.md
│   └── references/
│       ├── interview.md
│       ├── storyline.md
│       ├── fact-todo-policy.md
│       ├── conference-paper-structure.md
│       ├── latex-comment-style.md
│       └── revision-checklists.md
└── conference-style-*/
    ├── SKILL.md
    └── references/
```

`conference-style-*` 目录是后续扩展用的会议风格 skill，例如 `conference-style-emnlp2025-zh`。

## 安装

默认安装到 `~/.agents/skills`：

```bash
./install.sh
```

指定安装目录：

```bash
CODEX_SKILLS_DIR="$HOME/.codex/skills" ./install.sh
```

脚本会安装仓库根目录下所有包含 `SKILL.md` 的一级 skill 目录，例如：

- `ai-paper-writing-zh`
- `conference-style-*-zh`

## 主写作流程

主入口是 `ai-paper-writing-zh/SKILL.md`。它负责判断当前写作阶段，并引导 Codex 读取对应的阶段 skill 和共用 reference。

典型流程：

1. 访谈用户，明确研究问题、方法、实验和想讲的故事。
2. 生成初版中文摘要，作为临时故事线锚点。
3. 讨论缺失实验、薄弱证据和潜在审稿风险。
4. 用 Markdown 输出章节级和段落级大纲。
5. 修改 LaTeX 文件，插入中文 `%` 注释作为正文骨架。
6. 把中文注释扩写成更完整的中文写作笔记。
7. 在用户确认后，翻译为 AI/ML 会议论文风格的学术英文。

## 创建会议风格 skill

如果需要为某个会议、年份或领域创建专门的写作风格 skill，可以使用 [create-paper-style.md](create-paper-style.md) 中的 prompt。

推荐流程：

1. 让 Codex 收集某年某领域的代表性论文，保存到 `history_conference_papers/<CONFERENCE_YEAR>/papers`。
2. 通过 deep research 生成 `history_conference_papers/<CONFERENCE_YEAR>/deep-research-report.md`。
3. 让 Codex 读取 deep research 报告和 `create-paper-style.md`，自动创建新的 `conference-style-<conference-year>-zh` skill。
4. 在主写作流程中，根据目标会议调用对应 style skill，调整 abstract、introduction、related work、experiments 和 limitation 的写法。

`history_conference_papers/` 是本地研究资料目录，默认不纳入 git。

## 写作原则

- 不编造实验结果、数值、数据集、baseline、引用或 state-of-the-art 主张。
- 不确定内容必须写成 `[TODO: ...]`。
- 摘要只是临时故事线契约，后续可以随着论文结构和证据调整。
- LaTeX 写作优先使用中文注释，方便用户逐段修改。
- 如果实验不足，要明确指出并建议补充实验，不能把建议写成已完成事实。

## 扩展原则

新增会议风格 skill 时，应优先基于历史论文和 deep research 报告总结“写作偏好”和“审稿风险”，不要把历史论文中的具体技术结论迁移到当前论文中。

会议风格 skill 只负责调整写作风格和叙事偏好，不能覆盖 `ai-paper-writing-zh/references/fact-todo-policy.md` 中的事实约束。

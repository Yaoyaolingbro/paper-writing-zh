# paper-writing-zh

中文优先的 AI/ML 会议论文写作 Codex skills 仓库。

这个仓库包含一个主论文写作 skill suite，以及用于生成会议风格文件的 prompt。它面向已经有研究工作和部分实验结果、但还需要梳理论文故事线、补充实验、大纲、LaTeX 注释草稿和学术英文表达的写作场景。

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
│   ├── conference-styles/
│   │   └── <style-id>/
│   │       └── style.md
│   └── references/
│       ├── interview.md
│       ├── storyline.md
│       ├── fact-todo-policy.md
│       ├── conference-paper-structure.md
│       ├── latex-comment-style.md
│       └── revision-checklists.md
```

`conference-styles/<style-id>/style.md` 是后续扩展用的会议风格文件，例如 `conference-styles/emnlp2025/style.md`。

当前已包含的会议风格文件：

- `ai-paper-writing-zh/conference-styles/acl2025-agent/style.md`：基于 ACL2025 与 EMNLP2025 agent/evolve deep research 报告，总结 agent/evolve 方向写作偏好。

## 安装

默认安装到 `~/.agents/skills`：

```bash
./install.sh
```

指定安装目录：

```bash
CODEX_SKILLS_DIR="$HOME/.codex/skills" ./install.sh
```

脚本安装主 skill：

- `ai-paper-writing-zh`

会议风格文件会作为 `ai-paper-writing-zh` 的子目录一并安装。

## 主写作流程

主入口是 `ai-paper-writing-zh/SKILL.md`。它负责判断当前写作阶段，并引导 Codex 读取对应的阶段 skill 和共用 reference。

典型流程：

1. 先询问目标投稿会议，以及是否已有对应 `conference-styles/<style-id>/style.md`。
2. 访谈用户，明确研究问题、方法、实验和想讲的故事。
3. 生成初版中文摘要，作为临时故事线锚点。
4. 讨论缺失实验、薄弱证据和潜在审稿风险。
5. 用 Markdown 输出章节级和段落级大纲。
6. 修改 LaTeX 文件，插入中文 `%` 注释作为正文骨架。
7. 把中文注释扩写成更完整的中文写作笔记。
8. 在用户确认后，翻译为 AI/ML 会议论文风格的学术英文。

## 创建会议风格文件

如果需要为某个会议、年份或领域创建专门的写作风格文件，可以使用 [create-paper-style.md](create-paper-style.md) 中的 prompt。

推荐流程：

1. 让 Codex 收集某年某领域的代表性论文，保存到 `history_conference_papers/<CONFERENCE_YEAR>/papers`。
2. 通过 deep research 生成 `history_conference_papers/<CONFERENCE_YEAR>/deep-research-report.md`。
3. 让 Codex 读取 deep research 报告和 `create-paper-style.md`，自动创建新的 `ai-paper-writing-zh/conference-styles/<style-id>/style.md`。
4. 在主写作流程中，根据目标会议读取对应 style 文件，调整 abstract、introduction、related work、experiments 和 limitation 的写法。

`history_conference_papers/` 中的 Markdown 调研报告会纳入 git；PDF、zip 和 `.DS_Store` 等大文件或本地文件默认忽略。

## 写作原则

- 不编造实验结果、数值、数据集、baseline、引用或 state-of-the-art 主张。
- 不确定内容必须写成 `[TODO: ...]`。
- 摘要只是临时故事线契约，后续可以随着论文结构和证据调整。
- LaTeX 写作优先使用中文注释，方便用户逐段修改。
- 如果实验不足，要明确指出并建议补充实验，不能把建议写成已完成事实。

## 扩展原则

新增会议风格文件时，应优先基于历史论文和 deep research 报告总结“写作偏好”和“审稿风险”，不要把历史论文中的具体技术结论迁移到当前论文中。

会议风格文件只负责调整写作风格和叙事偏好，不能覆盖 `ai-paper-writing-zh/references/fact-todo-policy.md` 中的事实约束。

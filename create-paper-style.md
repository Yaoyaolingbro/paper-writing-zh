# Create Paper Style Prompt

下面这段 prompt 用于让 Codex 基于某一年、某个会议或领域的历史论文与 deep research 报告，自动创建一个新的 conference style 文件。

注意：会议风格不再创建为独立 skill，而是安装到 `ai-paper-writing-zh` skill 内部：

```text
ai-paper-writing-zh/conference-styles/<STYLE_ID>/style.md
```

你可以把下面的 prompt 直接发给 Codex，并根据目标会议替换占位符。

```md
我需要你为 `<CONFERENCE_YEAR>` 创建一个新的 AI/ML conference style 文件。

目标是：基于历史论文和 deep research 报告，总结该会议/领域在论文写作上的偏好，并生成一个可被 `ai-paper-writing-zh` 主流程读取的会议风格文件。这个 style 文件不负责编造论文内容，只负责指导写作风格、叙事结构、章节组织、审稿风险和表达偏好。

## 输出位置

请创建或更新：

`ai-paper-writing-zh/conference-styles/<STYLE_ID>/style.md`

其中 `<STYLE_ID>` 使用英文小写和短横线，例如：

- `emnlp2025`
- `iclr2026`
- `neurips2025-agents`
- `acl2025-rag`

不要创建独立的 `conference-style-*` skill 目录，也不要创建新的 `SKILL.md`。

## 输入位置

请使用以下目录和文件：

- 历史论文目录：`history_conference_papers/<CONFERENCE_YEAR>/papers`
- deep research 报告：`history_conference_papers/<CONFERENCE_YEAR>/deep-research-report.md`
- 创建指南：`create-paper-style.md`
- 主写作流程：`ai-paper-writing-zh/SKILL.md`
- 事实/TODO 规则：`ai-paper-writing-zh/references/fact-todo-policy.md`
- 论文结构参考：`ai-paper-writing-zh/references/conference-paper-structure.md`

如果 `history_conference_papers/<CONFERENCE_YEAR>/papers` 或 `deep-research-report.md` 不存在，请先告诉我缺少什么，并建议下一步如何收集论文或生成 deep research 报告。

## 任务

1. 先阅读 `deep-research-report.md`，提取该会议/领域的写作风格信号。
2. 必要时抽样阅读 `history_conference_papers/<CONFERENCE_YEAR>/papers` 中的论文，验证报告中的结论。
3. 创建 `ai-paper-writing-zh/conference-styles/<STYLE_ID>/style.md`。
4. 更新根目录 `README.md`，说明新增 style 文件的目标会议、适用范围和调用方式。
5. 如果新增了 style 文件，也要检查 `ai-paper-writing-zh/SKILL.md` 是否已经说明启动前需要询问目标会议和 style 文件。

## style.md 的职责

`style.md` 应该指导 Codex：

- 如何根据该会议/领域偏好调整论文故事线。
- abstract 和 introduction 通常如何组织。
- related work 更偏好按什么逻辑分类。
- method section 应该强调哪些设计解释。
- experiments section 应该如何呈现主结果、消融和分析。
- limitations 或 ethics/broader impact 是否常见，以及应如何写。
- 哪些 claim 容易被审稿人质疑。
- 哪些写法看起来不像该会议/领域的高质量论文。

## 必须遵守

- 不能编造历史论文中不存在的结论。
- 不能复制历史论文的原文句子作为模板。
- 只能总结结构、偏好、常见模式和审稿风险。
- 所有不确定结论必须标为 `[TODO: ...]` 或“需要用户确认”。
- `style.md` 必须继续服从 `ai-paper-writing-zh/references/fact-todo-policy.md`。
- 不要让风格规则覆盖事实约束。
- 不要把历史论文的技术结论迁移到当前用户论文中。

## style.md 推荐结构

请至少包含以下内容：

```md
# <CONFERENCE_YEAR> Paper Style

## 来源与适用范围

## 会议/领域总体写作偏好

## 常见论文类型

## Abstract 模式

## Introduction 叙事模式

## Related Work 组织方式

## Method 写作重点

## Experiments 写作重点

## Analysis / Ablation 偏好

## Limitations / Ethics / Broader Impact 偏好

## 高频审稿风险

## 不建议模仿的写法

## 与 ai-paper-writing-zh 主流程的配合方式

## 需要用户确认的问题
```

## 输出要求

完成后请报告：

- 新增或更新了哪个 `style.md` 文件。
- 这个 style 文件适合在哪些写作阶段读取。
- 哪些结论来自 deep research 报告，哪些是对论文样本的验证。
- 还有哪些不确定点需要用户确认。

在报告完成前，请检查：

- `ai-paper-writing-zh/conference-styles/<STYLE_ID>/style.md` 是否存在。
- 是否错误创建了独立 `conference-style-*` skill 目录。
- 是否存在把风格偏好写成事实主张的问题。
- 是否存在没有证据支撑的会议偏好判断。
```

## 推荐前置工作流

如果历史论文和 deep research 报告还没有准备好，可以先让 Codex 执行：

```md
请帮我收集 `<CONFERENCE_YEAR>` 中 `<FIELD_OR_TOPIC>` 方向的代表性论文，保存到：

`history_conference_papers/<CONFERENCE_YEAR>/papers`

然后基于这些论文做 deep research，生成：

`history_conference_papers/<CONFERENCE_YEAR>/deep-research-report.md`

报告重点不是总结每篇论文的技术内容，而是总结该会议/领域的论文写作风格、叙事结构、实验呈现方式、审稿风险和常见 section pattern。
```

## 使用建议

- `<CONFERENCE_YEAR>` 建议使用无空格格式，例如 `EMNLP2025`、`ICLR2026`、`NeurIPS2025`。
- `<STYLE_ID>` 建议统一小写，例如 `emnlp2025`、`iclr2026-agents`。
- 如果目标太大，先限定领域，例如 `emnlp2025-rag` 或 `iclr2026-agents`。
- deep research 报告应优先分析高质量接收论文、oral/spotlight 论文和与用户研究方向接近的论文。
- style 文件只提供写作偏好，不提供事实内容。具体论文的实验、方法和结论仍由用户当前项目决定。

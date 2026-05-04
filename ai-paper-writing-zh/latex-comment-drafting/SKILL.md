---
name: ai-paper-latex-comment-drafting-zh
description: "当需要修改 AI/ML 会议论文 LaTeX 文件，加入中文注释式章节和段落计划，但还不写最终英文正文时使用。"
---

# 中文 AI 论文 LaTeX 注释草稿

## 输入

读取当前大纲、摘要和相关 `.tex` 文件。读取：

- `../references/latex-comment-style.md`
- `../references/fact-todo-policy.md`

## 流程

1. 检查 LaTeX 项目结构，识别各 section 文件。
2. 除非用户要求替换，否则保留已有用户正文。
3. 在 section/subsection 后或目标段落前插入中文 `%` 注释。
4. 注释中写明段落目标、主张、证据、衔接和 TODO。
5. 如果有帮助，可以在写作笔记或顶层草稿上下文中保留最新摘要，但不要在每个文件里重复粘贴。

## LaTeX 修改规则

- 使用原生 LaTeX 注释，以 `%` 开头。
- 不要编造引用。用 `[TODO: 补充引用 ...]` 写在注释中。
- 不要编造结果。用 `[TODO: 补充结果/表格/图片 ...]` 标记。
- 注释要短，方便用户直接编辑。
- 避免破坏 LaTeX 命令、label、引用和会议模板宏。

## 校验

编辑后检查修改过的文件；如果可行，运行项目已有的 LaTeX 构建命令，或至少做面向语法的检查。如果没有可用构建命令，需要明确说明。

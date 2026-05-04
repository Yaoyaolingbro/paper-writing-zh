---
name: ai-paper-chinese-expansion-zh
description: "当需要在学术英文翻译之前，把 AI/ML 会议论文的中文 LaTeX 注释或段落计划扩写为更完整的中文写作笔记时使用。"
---

# 中文 AI 论文扩写

## 输入

读取最新摘要、大纲、LaTeX 注释和用户修改。读取：

- `../references/latex-comment-style.md`
- `../references/fact-todo-policy.md`
- `../references/revision-checklists.md`

## 流程

1. 把用户修改过的中文注释视为权威依据。
2. 根据用户需求，把注释扩写为更完整的中文写作笔记，可以写在 LaTeX 注释中，也可以写在单独 Markdown 笔记中。
3. 保留摘要和 TODO。
4. 不要把不确定性抹平，必须继续显式保留。
5. 在进入学术英文翻译前停下来让用户审阅。

## 扩写规则

- 每个扩写段落只保留一个主要主张。
- 在需要时补充连接逻辑、动机和局限。
- 实验性主张必须绑定到已确认的证据。
- 对缺失数值、引用、baseline、图表和消融使用 `[TODO: ...]`。
- 不要用润色掩盖结构问题；要直接标出。

## 输出形式

Markdown 笔记：

```md
## 摘要锚点

## 中文扩写草稿笔记

## 剩余 TODO

## 需要更多证据的主张
```

LaTeX：

```tex
% [段落目标] ...
% [中文扩写] ...
% [证据/TODO] ...
```

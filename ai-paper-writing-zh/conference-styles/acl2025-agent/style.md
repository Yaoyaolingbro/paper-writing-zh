# ACL2025 Agent Paper Style

## 来源与适用范围

本文件基于以下本地 deep research 报告总结：

- `history_conference_papers/ACL2025/deep-research-report.md`
- `history_conference_papers/EMNLP2025/deep-research-report.md`

主要适用于面向 ACL 2025 风格的 agent / agentic system / multi-agent / interactive learning / self-improvement / dynamic benchmark / evolving model-update 方向论文。它提供写作风格、叙事结构、章节组织和审稿风险建议，不提供当前用户论文的事实内容。

使用本文件时，仍必须遵守 `ai-paper-writing-zh/references/fact-todo-policy.md`：不能编造实验结果、数据集、baseline、数值、引用或 state-of-the-art 主张。

## 会议/领域总体写作偏好

ACL2025 agent/evolve 方向的高质量论文更偏好“大问题 + 清晰机制”，而不是“小指标 + 新模块”。好的故事通常会重新定义研究对象：例如把 opinion collection 写成 agentic social sensing，把 factuality evaluation 推向动态 benchmark，把 persona 从静态设定写成会影响行为的动态变量。

核心写作目标不是证明“LLM agent 能完成任务”，而是证明“LLM agent 能在真实或仿真的动态环境里，通过交互、反馈和状态更新形成可解释、可评估、可扩展的行为系统”。

EMNLP2025 agent 报告提供了可迁移补充：agent 论文常先承认 LLM agent 的能力红利，再指出真实环境中的长程、动态、高风险、异构或多目标复杂性，然后把方法写成可执行系统框架，并用 benchmark、消融、案例或真实应用证明它不是单点 trick。

## 常见论文类型

- **Agent as experimental infrastructure**：把 agent 放入可控社会、教育、新闻、故事、文化或专业场景中，用于模拟人类行为、意见、角色人格或互动过程。重点是 realism、diversity、controllability 和 human/expert validation。
- **Multi-agent interaction mechanism**：强调 interaction topology、debate protocol、persona role、消息传递或隐喻通信。重点不是“多个 agent 投票”，而是“结构产生能力”。
- **Tool/reflection-augmented system**：面向工具使用、临床、OS/GUI/browser、数学解释等任务。方法通常包含 planner、executor、reflector、tool selector、verifier 或 environment interface。
- **Evolution / self-improvement loop**：强调静态数据、静态 benchmark、静态模型或 one-shot fine-tuning 无法处理变化，因此需要生成、交互、反馈、筛选、更新和再评估的闭环。
- **Benchmark or evaluation-first paper**：先说明现有评估无法测到目标能力，再引入动态或过程性评测，最后用该评测支撑方法。

## Abstract 模式

ACL2025 agent 风格的摘要应尽早暴露“动态性”和“机制”。推荐结构：

1. 先说明真实或仿真场景中的动态问题：用户、环境、persona、工具、世界知识、模型版本、任务目标或评测分布在变化。
2. 指出现有 LLM、RAG、prompting、single-agent 或 static benchmark 的具体失败模式。
3. 引出本文的 agent framework、interaction protocol、reflection loop、dynamic benchmark 或 update mechanism。
4. 概括系统闭环：输入如何进入 agent，agent 如何行动，反馈如何返回，状态如何更新，下一轮如何被评估。
5. 概括证据类型：human/expert evaluation、cross-model/domain evaluation、interaction/memory/reflection/persona/feedback ablation、dynamic/temporal evaluation、qualitative case study。

避免只写“we propose a framework and improve performance”。摘要中应说明框架为什么存在，以及它捕捉了什么静态方法捕捉不到的过程。

## Introduction 叙事模式

推荐引言主线：

1. **定义动态性**：先明确任务里什么在变。可以是用户目标、世界事实、模型版本、agent persona、工具环境、任务分布、反馈信号或评测标准。
2. **定义旧方法失败模式**：说明 static dataset、fixed benchmark、single-shot reasoning、simple majority vote、prompt-only agent 或 outcome-only supervision 为什么不够。
3. **定义 agent 状态**：说明 agent 需要记住什么、更新什么、与谁互动、如何影响下一轮行为。
4. **定义机制而非模块清单**：不要只列角色或组件，要说明信息流和更新流。
5. **定义证据承诺**：提前告诉读者后文会用哪些过程证据证明系统有效。

ACL2025 oral 风格尤其重视“这个问题应该被这样重新建模”。如果论文只是在常规 benchmark 上提高若干分数，引言需要额外解释为什么这不是局部工程优化。

## Related Work 组织方式

Related Work 应按研究关系组织，而不是按论文罗列：

- **Static vs dynamic setting**：哪些工作假设数据、模型、用户或 benchmark 静态；本文处理哪种变化。
- **Single-agent vs structured interaction**：哪些工作依赖单 agent、投票或简单协作；本文的交互拓扑或协议多了什么。
- **Outcome supervision vs process/feedback loop**：哪些工作只看最终结果；本文如何使用中间状态、反思、环境反馈或过程监督。
- **Task tool use vs grounded execution**：哪些工具增强方法缺少可靠执行、反思或验证；本文如何让工具链闭环。
- **Benchmark gap**：已有评估测不到哪些行为过程，例如恢复、更新、角色变化、文化公平、动态 factuality 或长期互动。

Related Work 不应替代实验。若某类强 baseline 或 benchmark 缺失，必须写成 `[TODO: ...]`。

## Method 写作重点

方法部分应把系统写成闭环，而不是模块堆叠。至少说明：

- 输入是什么：任务、环境状态、用户反馈、历史经验、persona、工具状态或 benchmark item。
- agent 做什么：行动、提问、解释、访谈、辩论、模拟、工具调用、反思或数据生成。
- 反馈来自哪里：环境、用户、人类专家、评测器、verifier、reward model、tool result 或模型自检。
- 状态如何更新：memory、persona、data pool、benchmark、policy、prompt、参数或 tool policy。
- 下一轮如何被重新评估：用什么指标、案例、动态设置或人类评估证明闭环有效。

如果使用多 agent，必须解释角色分工、消息传递、交互拓扑和冲突解决机制。不要只说“多个 agent 协作”。需要说明为什么这种结构能带来公平性、稳健性、创造性、解释性或效率提升。

如果使用人类工作流或系统隐喻，隐喻必须服务于方法设计。例如专家流程、OS memory、clinical reflection、debate protocol、tool dependency graph 等都应对应具体模块和失败模式。

## Experiments 写作重点

实验部分要证明“过程有效”，不只是最终分数更高。优先组织成评估问题：

- 系统是否比 static / single-shot / single-agent 设置更能处理动态环境？
- interaction、memory、reflection、persona、feedback 或 tool interface 是否必要？
- 方法是否跨模型、跨领域、跨时间或跨任务设置有效？
- human/expert evaluation 是否支持模拟真实性、解释质量、安全性或领域可信度？
- qualitative case study 是否展示 agent 如何行动、失败、修正、协作或演化？

强实验组合通常包括：

- main result
- cross-model 或 cross-domain evaluation
- dynamic / temporal evaluation
- ablation of interaction / memory / reflection / persona / feedback
- process-level 或 trajectory-level analysis
- human/expert evaluation
- qualitative case study
- failure analysis

如果当前只有最终 accuracy，需要谨慎降低主张强度，并添加 `[TODO: 补充过程证据或动态评测]`。

## Analysis / Ablation 偏好

ACL2025 agent 风格偏好能解释机制必要性的分析：

- 去掉 interaction topology 后是否退化？
- 去掉 memory 或 state update 后是否无法处理长期变化？
- 去掉 reflection/verifier/tool feedback 后是否出现更多 hallucination、tool misuse 或 unsafe behavior？
- 不同 persona、角色、辩论轮数或反馈频率是否影响结果？
- 系统在哪些场景失败，失败是否暴露了动态性、grounding 或评估设计问题？

消融最好映射到引言中的失败模式。不要把消融写成“我们试了几个组件”；要写成“每个组件解决哪个过程性失败”。

## Limitations / Ethics / Broader Impact 偏好

Agent/evolve 论文经常涉及社会模拟、教育、临床、文化公平、新闻访谈、OS 操作或高风险交互，因此 limitation 和 ethics 不能只写泛泛风险。

应优先说明：

- agent simulation 是否能代表真实人类行为。
- human/expert validation 的范围和偏差。
- 动态 benchmark 是否可能过拟合到特定时间、平台或模型版本。
- 多 agent debate 是否可能放大偏见、群体极化或表面共识。
- 工具/OS/clinical agent 是否有安全、隐私、误用和责任边界。
- self-improvement 是否可能积累错误反馈或造成不可控漂移。

不要在 limitation 中引入新主张。所有限制必须与方法和实验范围一致。

## 高频审稿风险

- **“只是又一个 agent 框架”**：如果没有清楚动态性、失败模式和闭环机制，容易被认为是模块拼装。
- **“多 agent 只是增加复杂度”**：需要证明交互结构带来的不是表面多样性，而是公平、稳健、创造性或解释性收益。
- **“缺少真实过程证据”**：只给最终分数不足以支撑 agent/evolve 论文。
- **“评估不够动态”**：如果故事主张是变化和更新，实验却是静态 benchmark，会不一致。
- **“human/expert validation 不足”**：社会模拟、教育、临床、意见收集、文化 alignment 等主题尤其需要验证真实性。
- **“方法解释停留在隐喻”**：OS、专家流程、debate、reflection 等隐喻必须落到具体模块、状态和反馈。
- **“领域只是包装”**：如果法律、医疗、教育、文化公平等领域结构没有进入方法和评估，容易显得牵强。

## 不建议模仿的写法

- 不要开头只说 LLM agents are powerful，然后直接提出框架。
- 不要只列 planner/executor/critic/reflector，而不说明状态如何流动。
- 不要把多 agent 写成 majority vote 或简单 ensemble。
- 不要把 self-improvement 写成模糊口号；必须说明改进发生在数据、参数、prompt、memory、benchmark、persona 还是 tool policy。
- 不要用静态实验支撑动态主张。
- 不要把 case study 当作主要证据，除非它和系统性实验互相支撑。
- 不要复制历史论文的表达或标题结构；只能借鉴叙事功能。

## 与 ai-paper-writing-zh 主流程的配合方式

在 `ai-paper-writing-zh` 启动阶段，如果用户目标会议是 ACL、ACL2025 或 agent/evolve 方向，可读取本文件作为风格参考。

推荐使用方式：

- **访谈阶段**：优先询问“任务中什么在变化”“agent 维护什么状态”“反馈如何进入下一轮”。
- **摘要阶段**：检查摘要是否包含动态问题、旧方法失败、闭环机制和过程证据。
- **大纲阶段**：把 introduction、method、experiments 都围绕动态性和闭环组织。
- **LaTeX 注释阶段**：在每节注释中标出“动态性”“状态更新”“反馈来源”“过程证据”。
- **中文扩写阶段**：强化机制解释，避免把模块列表写成方法贡献。
- **英文翻译阶段**：保持克制，不把风格建议翻译成事实主张。

## 需要用户确认的问题

- 目标投稿是否确认为 ACL 2025 风格，还是只是参考 ACL agent/evolve oral 写法？
- 当前论文属于哪类故事：社会/专业场景模拟、多 agent 交互、工具/反思增强、self-improvement、dynamic benchmark，还是混合型？
- 论文中“动态性”具体是什么？
- agent 维护或更新的状态是什么？
- 反馈来自用户、环境、人类专家、评测器、verifier、reward model 还是模型自检？
- 是否已有 process-level、trajectory-level、human/expert、dynamic/temporal、cross-model 或 cross-domain 实验证据？
- 哪些主张目前还缺少证据，需要写成 `[TODO: ...]`？

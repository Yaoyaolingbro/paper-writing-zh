# ACL 2025 Oral Papers: Agent / Evolution 方向论文写作分析

生成日期：2026-05-04

## 1. 更正说明

上一版下载的论文并不是 oral。根据 ACL 2025 官方详细程序表的 `Type of Presentation` 字段，上一版的核心论文如 Gödel Agent、AgentGym、Agentic Reasoning、HiAgent、FACT-AUDIT、EvoPatient、AgentDropout、Interactive Evolution 等均为 `IP-Poster`；AgentCourt 为 `Not Pres.`，AnnaAgent 为 Findings poster。

因此，本版重新按以下口径筛选：

1. 必须是 ACL 2025 main conference paper，即官方程序表中 paper number 后缀为 `-MAIN`。
2. 必须是 oral，即 `Type of Presentation = IP-Oral`。
3. 主题与 agent、agentic system、multi-agent、interactive learning、self-improvement、dynamic benchmark、evolving model/update 等方向高相关。

上一版非 oral PDF 已移动到同级目录 `non_oral_previous/`。当前 `papers/` 目录只保留本版 oral 论文。

官方来源：

- ACL 2025 Program Overview: https://2025.aclweb.org/program/
- ACL 2025 Detailed Program / Paper Assignments: https://docs.google.com/spreadsheets/d/1O-n3HPvv8vY0L_kjyP5AtRTcWWjqLk2deCYtrMgCGw4/edit
- ACL Anthology ACL 2025 Long Papers: https://aclanthology.org/volumes/2025.acl-long/

## 2. 已下载 Oral 论文清单

| Anthology ID | 论文 | Oral session | 本地文件 |
|---|---|---|---|
| 2025.acl-long.221 | SurveyPilot: an Agentic Framework for Automated Human Opinion Collection from Social Media | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.221_SurveyPilot.pdf` |
| 2025.acl-long.260 | Dually Self-Improved Counterfactual Data Augmentation Using Large Language Model | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.260_Dually-Self-Improved-Counterfactual-DA.pdf` |
| 2025.acl-long.332 | TheoremExplainAgent: Towards Video-based Multimodal Explanations for LLM Theorem Understanding | Session 11: IP-Orals, Wed Jul 30 09:00-10:30 | `papers/2025.acl-long.332_TheoremExplainAgent.pdf` |
| 2025.acl-long.369 | OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use | Session 3: IP-Orals, Mon Jul 28 14:00-15:30 | `papers/2025.acl-long.369_OS-Agents-Survey.pdf` |
| 2025.acl-long.389 | CoMet: Metaphor-Driven Covert Communication for Multi-Agent Language Games | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.389_CoMet.pdf` |
| 2025.acl-long.409 | Growing Through Experience: Scaling Episodic Grounding in Language Models | Session 3: IP-Orals, Mon Jul 28 14:00-15:30 | `papers/2025.acl-long.409_Growing-Through-Experience.pdf` |
| 2025.acl-long.441 | INTERACT: Enabling Interactive, Question-Driven Learning in Large Language Models | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.441_INTERACT.pdf` |
| 2025.acl-long.481 | Investigating and Extending Homans’ Social Exchange Theory with Large Language Model based Agents | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.481_Homans-Social-Exchange-Agents.pdf` |
| 2025.acl-long.488 | Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.488_Embracing-Imperfection.pdf` |
| 2025.acl-long.663 | ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents | Session 11: IP-Orals, Wed Jul 30 09:00-10:30 | `papers/2025.acl-long.663_ReflecTool.pdf` |
| 2025.acl-long.719 | Adapt Once, Thrive with Updates: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models | Session 11: IP-Orals, Wed Jul 30 09:00-10:30 | `papers/2025.acl-long.719_Adapt-Once-Thrive-With-Updates.pdf` |
| 2025.acl-long.773 | BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.773_BOOKWORLD.pdf` |
| 2025.acl-long.1210 | Multiple LLM Agents Debate for Equitable Cultural Alignment | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.1210_Multiple-LLM-Agents-Debate.pdf` |
| 2025.acl-long.1515 | Persona Dynamics: Unveiling the Impact of Persona Traits on Agents in Text-Based Games | Session 3: IP-Orals, Mon Jul 28 14:00-15:30 | `papers/2025.acl-long.1515_Persona-Dynamics.pdf` |
| 2025.acl-long.1580 | NewsInterview: a Dataset and a Playground to Evaluate LLMs' Grounding Gap via Informational Interviews | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.1580_NewsInterview.pdf` |
| 2025.acl-long.1587 | FactBench: A Dynamic Benchmark for In-the-Wild Language Model Factuality Evaluation | Session 9: IP-Orals, Tue Jul 29 14:00-15:30 | `papers/2025.acl-long.1587_FactBench.pdf` |

## 3. 这些 Oral 论文的论文故事类型

### 3.1 Agent 作为“真实社会 / 专业场景模拟器”

代表论文：SurveyPilot、Homans Social Exchange Agents、Embracing Imperfection、BOOKWORLD、Persona Dynamics、NewsInterview。

这一类 oral 论文的共同叙事是：LLM agent 不只是完成任务的工具，而是可以被放进一个可控社会或专业场景中，用来模拟人类意见、学生认知、角色人格、访谈互动、故事社会或社会交换行为。

写作特点：

1. 引言通常从一个现实研究痛点切入，例如人工意见收集昂贵、学生模拟不够真实、社会理论难以大规模验证、新闻访谈需要长期策略。
2. 方法不是单个 prompt，而是一个带角色、记忆、行为规则、互动环境的 agent playground。
3. 论文会强调 realism、diversity、controllability 和 human/subject expert validation。
4. 实验不仅汇报自动指标，还会展示 case study 或与人类行为的一致性。

这种故事适合写成“agent as experimental infrastructure”：agent 的价值不在于单次回答正确，而在于提供一个可复现、可扩展、可干预的人类行为模拟环境。

### 3.2 Agent 作为“多智能体协作 / 辩论机制”

代表论文：CoMet、Multiple LLM Agents Debate、Tree-of-Debate 类近邻、BOOKWORLD。

这一类论文把 agent 的核心能力放在 interaction topology 或 debate protocol 上。论文通常不满足于“多个 agent 投票”，而是让不同 persona、不同角色或不同隐喻通信规则形成结构化互动。

写作特点：

1. 开头先指出单模型或简单 majority vote 无法处理价值冲突、文化公平、博弈、创造性推理等开放问题。
2. 方法部分强调角色分工、轮次结构、消息传递、辩论树或隐式通信机制。
3. 实验部分会证明多 agent 机制带来的不是表面多样性，而是更公平、更稳健或更有创造性的输出。
4. 好的论文会解释“为什么这种交互结构有效”，而不是只报告多 agent 超过 single agent。

这一类口头报告论文的叙事重心是“结构产生能力”：能力来自 agent 之间的组织方式，而不只是更强的 base LLM。

### 3.3 Agent 作为“工具增强 / 反思增强系统”

代表论文：TheoremExplainAgent、ReflecTool、OS Agents。

这类论文面向工具使用、临床任务、操作系统/GUI/浏览器等 agent 应用。它们的故事通常是：已有 LLM 有知识或视觉能力，但缺少可靠的工具链、反思机制、任务分解或环境接口，因此需要 agent framework。

写作特点：

1. 引言常从“LLM 能力强但落地不稳”开始，而不是从模型参数或训练算法开始。
2. 方法里会出现 planner、executor、reflector、tool selector、verifier、environment interface 等模块。
3. 叙述会特别强调 reliability、reflection、grounding、execution feedback。
4. 实验不仅看最终 accuracy，还会看解释质量、工具调用质量、临床安全性、环境覆盖面或失败恢复能力。

这一类论文适合学习如何把 agent 写成系统论文：每个模块都要对应一个实际失败模式，如 hallucination、tool misuse、缺少 reflection、无法跨应用泛化。

### 3.4 Evolution / Self-Improvement 作为“数据或模型更新闭环”

代表论文：Dually Self-Improved Counterfactual Data Augmentation、Growing Through Experience、INTERACT、Adapt Once Thrive with Updates、FactBench。

这一类 oral 论文不一定都在标题里写 agent，但和 “evolve” 方向强相关。它们共同讲的是：静态数据、静态模型、静态 benchmark 或静态 fine-tuning 无法应对持续变化的任务环境，因此系统需要从交互、经验、问题驱动学习、模型更新或动态评测中不断改进。

写作特点：

1. 引言会把传统方法的问题概括为 static、one-shot、fixed benchmark、fixed base model 或 fixed training data。
2. 方法会设计一个循环：生成 / 交互 / 反馈 / 筛选 / 更新 / 再评估。
3. 实验会强调随迭代增加的收益、跨时间或跨模型更新的迁移能力、对分布变化的鲁棒性。
4. 这类论文的标题通常有 self-improved、experience、interactive、updates、dynamic benchmark 等信号词。

这类论文的写作关键是把“变化”具体化：到底是数据在变、用户问题在变、base model 在变、世界事实在变，还是评测分布在变。

## 4. Oral 论文的共同叙事风格

### 4.1 口头报告论文更偏“大问题 + 清晰机制”

这批 oral 论文的引言一般都不只是修补一个小指标，而是试图重新定义一个研究对象：

- SurveyPilot：把 opinion collection 变成 agentic social sensing。
- OS Agents：把计算机、手机、浏览器使用统一成 MLLM-based OS agent 研究。
- FactBench：把 factuality evaluation 从静态 benchmark 推向 in-the-wild dynamic benchmark。
- INTERACT：把 LLM 学习从被动训练改成 question-driven interactive learning。
- Persona Dynamics：把 agent persona 从静态设定改成会影响行为和表现的动态变量。

也就是说，oral 论文更常见的故事不是“我们的方法比 baseline 高 2%”，而是“这个问题应该被这样重新建模”。

### 4.2 标题通常直接暴露贡献角度

这些标题的可学习点很明显：

- `SurveyPilot`：用系统名 + agentic framework，强调可用工具。
- `TheoremExplainAgent`：用任务名 + Agent，直接说明 agent 的应用边界。
- `OS Agents`：用领域对象复数化，暗示 survey / taxonomy。
- `Growing Through Experience`：用隐喻表达经验扩展。
- `INTERACT`：用强动词表达交互式学习。
- `Adapt Once, Thrive with Updates`：用对偶句表达 evolving base models 下的迁移。
- `FactBench`：用 benchmark 名 + dynamic factuality evaluation，强调评测资源。

好的标题基本做到三件事：对象明确、机制明确、研究野心明确。

### 4.3 方法叙事强调“闭环”而不是“模块堆叠”

agent/evolution 方向的 oral 论文普遍会避免只列 agent 角色。它们会说明状态如何流动：

1. agent 接收任务或环境输入。
2. agent 生成行动、问题、解释、访谈、辩论或模拟行为。
3. 环境、用户、模型或评测器给出反馈。
4. 系统更新经验、persona、数据、benchmark、参数或策略。
5. 下一轮表现被重新评估。

这就是 agent/evolve 论文最核心的故事骨架：系统不是一次性推理，而是持续行动和更新。

### 4.4 实验更重视“真实性”和“动态性”

相比普通模型论文，这些 oral 论文更常见以下实验证据：

- human evaluation 或 expert evaluation，用来证明模拟或解释是否真实。
- cross-model / cross-domain evaluation，用来证明框架不是只适配一个模型。
- ablation of interaction / memory / reflection / persona / feedback，用来证明闭环必要。
- dynamic or temporal evaluation，用来证明系统能处理变化。
- qualitative case study，用来展示 agent 行为过程。

对于 agent 论文，过程证据往往比单个最终分数更重要。高分写法会让读者看到 agent 是如何一步步行动、失败、修正、协作或演化的。

## 5. 对写作的直接启发

如果你要写 ACL oral 水平的 agent/evolve 论文，可以按这个模板组织故事：

1. **先定义动态性**：你的任务里什么东西在变？用户、世界知识、模型版本、agent persona、工具环境、任务目标，还是评测分布？
2. **再定义 agent 的状态**：agent 需要记住什么、更新什么、向谁反馈、如何影响下一轮？
3. **把方法写成闭环**：不要只画模块图，要画信息流和更新流。
4. **把实验写成过程证明**：展示随着交互、经验、更新或辩论，系统为什么变好。
5. **加一层真实场景约束**：临床、教育、社会意见、OS 操作、新闻访谈、文化公平等场景，都能让 agent 故事更有说服力。
6. **不要泛泛说 self-improvement**：要精确说明 self-improvement 发生在数据、参数、prompt、memory、benchmark、persona 还是 tool policy 上。

一句话总结：ACL 2025 的 oral agent/evolve 论文，核心不是“LLM agent 能完成任务”，而是“LLM agent 能在真实或仿真的动态环境里，通过交互、反馈和状态更新形成可解释、可评估、可扩展的行为系统”。

# EMNLP 2025 Agent / Evolve Oral Papers: 论文叙事风格与写作特点

## 范围与口径

本次下载与分析的范围是 EMNLP 2025 main conference 中，ACL Anthology 条目为 `2025.emnlp-main.*`、Underline 元数据标记为 `technical paper` 且 `poster_lecture=false`，并且标题包含 `Agent` / `Agentic` / `Multi-Agent` 或 `Evolve` / `Evolving` 的论文。这个口径对应“非 poster 的技术报告/口头展示候选”，来源交叉使用了 EMNLP 2025 官网日程页、ACL Anthology 和 Underline 的论文页面元数据。

需要注意：一些标题很相关但 Underline 明确标成 poster 的论文没有纳入下载与主体分析，例如 `EvolveSearch: An Iterative Self-Evolving Search Agent`、`DEBATE, TRAIN, EVOLVE: Self-Evolution of Language Model Reasoning`、`Co-Evolving LLMs and Embedding Models via Density-Guided Preference Optimization for Text Clustering`。

## 已下载论文

PDF 均已下载到 `papers/` 目录：

| ACL ID | 论文 | 主题叙事类型 |
|---|---|---|
| 53 | IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents | 安全防御：从威胁模型到结构性约束 |
| 212 | BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism | GUI agent 纠错：从单步准确到轨迹恢复 |
| 227 | COLA: Collaborative Multi-Agent Framework with Dynamic Task Scheduling for GUI Automation | 多智能体协作：从静态流程到动态调度 |
| 276 | Search-o1: Agentic Search-Enhanced Large Reasoning Models | 检索增强推理：从知识不足到主动搜索 |
| 325 | MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations | 社会仿真：从个体生成到群体传播机制 |
| 403 | PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements | 垂直领域应用：法律长文档拆解与协作 |
| 423 | Robust Native Language Identification through Agentic Decomposition | 任务拆解：从捷径特征到可解释代理流程 |
| 454 | WebEvolver: Enhancing Web Agent Self-Improvement with Co-evolving World Model | 自演化 agent：agent 与 world model 共同进化 |
| 506 | AgentPro: Enhancing LLM Agents with Automated Process Supervision | 过程监督：从结果反馈到轨迹级训练信号 |
| 594 | EmoAgent: Assessing and Safeguarding Human-AI Interaction for Mental Health Safety | 高风险交互安全：评估加防护 |
| 630 | CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space | 具身问答：从室内任务扩展到城市空间 |
| 652 | AI Chatbots as Professional Service Agents: Developing a Professional Identity | 专业服务 agent：从问答工具到职业身份 |
| 728 | PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides | 生成式工具：从文本到幻灯片工作流 |
| 808 | ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks | 自组织多智能体：从人工设计到奖励驱动 |
| 938 | OMS: On-the-fly, Multi-Objective, Self-Reflective Ad Keyword Generation via LLM Agent | 商业决策 agent：在线、多目标、自反思 |
| 1190 | ZERA: Zero-init Instruction Evolving Refinement Agent | prompt 演化：从零初始指令到结构化提示 |
| 1318 | Memory OS of AI Agent | 长期记忆：用操作系统隐喻组织 agent memory |
| 1330 | The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents | 演化仿真：从真新闻到假新闻的过程建模 |
| 1341 | FedMABench: Benchmarking Mobile GUI Agents on Decentralized Heterogeneous User Data | benchmark 叙事：从集中式数据到联邦异构评测 |
| 1487 | Can LLM Agents Maintain a Persona in Discourse? | 角色一致性评测：从单轮 persona 到语篇维持 |
| 1575 | AutoCT: Automating Interpretable Clinical Trial Prediction with LLM Agents | 医疗应用 agent：自动化、可解释、专家流程 |

## 总体论文故事模式

这些 oral/technical papers 的叙事有一个高度稳定的骨架：先承认 LLM agent 的能力红利，再指出“真实环境中的长程、动态、高风险、异构、多目标”使现有方法失效，最后把自己的方法写成一个可执行的系统框架，并用新 benchmark、消融、案例或真实应用来证明它不是单点 trick。

最常见的故事公式是：

> LLM agents are promising -> current systems fail in real-world long-horizon settings -> the missing capability is X -> we introduce a named framework with modules A/B/C -> experiments and ablations show each module matters -> this opens a more reliable/scalable/autonomous agent direction.

其中 `X` 往往不是纯模型能力，而是系统能力：memory management、process supervision、backtracking、dynamic scheduling、tool-dependency constraints、world-model co-evolution、professional identity、multi-objective monitoring、federated evaluation。

## 叙述风格特点

### 1. “真实世界复杂性”是最常用的开场钩子

大多数论文不是从模型架构开始，而是从应用场景的复杂性开场：GUI 自动化、法律合同、广告关键词、医疗问答、临床试验、城市空间、心理健康、长会话记忆。写法上强调“现有方法在实验室可行，但到了真实环境会暴露出长程规划、异构数据、动态反馈、安全风险、评估缺口”。

这类开场的好处是很快把论文价值从“又一个 agent 框架”提升到“一个真实部署瓶颈”。例如 IPIGuard 把故事压在 indirect prompt injection 的结构性风险上；BacktrackAgent 把 GUI agent 从“动作准确率”推进到“错误后能否恢复”；MemoryOS 把长上下文限制转写成“缺少操作系统式记忆管理”。

### 2. 论文喜欢把方法写成“系统工程产品”，而不是单一算法

这些论文的主角通常是一个有名字的系统：IPIGuard、COLA、WebEvolver、AgentPro、EmoAgent、PPTAgent、ReSo、ZERA、MemoryOS。叙述上常见三段式：

1. 给出系统名和核心隐喻。
2. 拆成 3-5 个模块。
3. 用流程图说明模块如何串起来。

这种写法让 contribution 看起来更完整，也更适合 agent 论文，因为 agent 的创新往往分布在 planning、execution、reflection、retrieval、memory、evaluation、supervision 多个环节，而不是一个孤立公式。

### 3. 很多论文用“人类工作流”作为叙事桥梁

Agent 论文特别喜欢从人类流程中借结构：

- PPTAgent 模仿人类做 slides 的“参考、规划、编辑”流程。
- PAKTON 把法律长协议 QA 写成多专家分工与证据整合。
- AutoCT 强调临床试验预测需要可解释的专家式判断链。
- MemoryOS 直接借用操作系统的分层存储、更新、检索、生成。
- AI Chatbots as Professional Service Agents 把 chatbot 从“回答问题”升级成“带职业身份完成专业目标”。

这种写法的核心不是类比本身，而是借类比说明为什么普通 prompting 不够：真实任务需要角色、过程、状态和反馈。

### 4. “从静态到动态”是 evolve 类论文的主线

Evolve 相关论文的故事重点不是“性能更高”，而是“对象会随时间变化”：

- WebEvolver：agent 自我改进时，如果世界模型不一起更新，就会产生训练环境与真实环境的错位，因此要 co-evolve。
- ZERA：prompt 不是一次性设计，而是在原则评价和元认知 refinement 中逐步演化。
- The Stepwise Deception：假新闻不是一开始就存在，而是从真实新闻逐步偏移、变形、传播出来。

这类论文的写作特点是把研究对象从一个静态 artifact 改写成一个过程：trajectory、iteration、evolution、feedback loop、stage-wise transformation。它们的 contribution 也常常不是单个模块，而是“如何刻画和控制演化过程”。

### 5. Benchmark / evaluation 往往和方法共同构成故事

不少论文不是只提出方法，还同时提出评测框架或数据集：FedMABench、CityEQA、FUSE-EVAL、PPTEval、EmoEval/EmoGuard、AgentPro 的过程监督评估、ReSo 的自动数据合成 benchmark。写法上，它们会先说“现有评估无法测到我们关心的能力”，再引出 benchmark，最后再让方法在该 benchmark 上成立。

这是一种很典型的 EMNLP agent 论文写法：先重定义问题，再给出工具，再用工具证明方法。它比“在旧 benchmark 上刷分”更容易讲出论文故事。

### 6. 安全类论文强调“模型内在能力不够，需要结构性约束”

IPIGuard、EmoAgent、BacktrackAgent、AgentPro 都有相近的叙事倾向：LLM 本身会犯错，单纯靠 prompt 或结果判断不够，必须在执行过程外面加结构性机制。

具体写法包括：

- 把失败定义成可定位的过程问题，而不是泛泛的 hallucination。
- 引入 guard、judger、reflector、process supervisor、tool dependency graph 等外部结构。
- 用消融说明外部结构确实贡献了稳定性。

这类论文的语气更“工程可靠性”，少谈模型智能，多谈约束、检测、恢复和可控执行。

### 7. 应用型 agent 论文常用“领域不可替代性”支撑价值

法律、医疗、广告、心理健康、临床试验这些论文会反复强调：领域任务不是普通 QA，因为它们有专业目标、政策约束、伦理风险、证据要求或业务指标。写作上会把“领域结构”转化为方法模块，例如：

- 法律合同 QA 需要多 agent 分工和长协议证据定位。
- 医疗问答需要职业身份、患者中心、伦理表达。
- 广告关键词需要在线指标、多目标优化和自反思。
- 临床试验预测需要可解释的中间判断。

这类论文的故事成功与否，取决于作者能否让读者相信：领域知识不是背景装饰，而是方法设计的必要条件。

## 单篇论文叙事点评

### IPIGuard

故事非常清晰：web/tool agents 面临 indirect prompt injection，现有防御依赖模型自觉，缺少行为层面的结构约束。它把贡献写成“从 prompt-level defense 到 task-execution paradigm 的转变”，这比单纯提出一个检测器更有说服力。写作特点是威胁模型明确、方法动机强、结构图重要。

### BacktrackAgent

论文把 GUI agent 的失败从“下一步点错”扩展为“错误会沿轨迹传播”。叙述重点是 error detection + backtracking，把 agent 写成一个能自我纠错的过程系统。它的故事适合学习：先指出主流指标忽略恢复能力，再引入恢复机制和对应数据构造。

### COLA

COLA 的叙事是多智能体 GUI 自动化中的“协作调度”问题。它不像单 agent 论文那样强调某个 reasoning trick，而是强调任务分解、角色协同和动态 scheduling。写作偏系统框架型，适合用“复杂任务需要组织结构”来讲故事。

### Search-o1

Search-o1 把 reasoning model 的长链推理与外部搜索结合起来，故事核心是“推理长了以后，知识不足会更致命”。它不是简单说 RAG 有用，而是强调 agentic search 能在推理过程中补知识。叙述风格是能力扩展型：从 closed-book reasoning 到 search-enhanced reasoning。

### MOSAIC

MOSAIC 走社会科学与 agent simulation 叙事路线。它的重点不是单个 agent 的最优决策，而是多 agent 社会网络里的内容传播和监管。写作上更像“建模框架 + 社会机制分析”，重视可解释变量、群体行为和仿真设定。

### PAKTON

PAKTON 的故事基于法律长协议的复杂性：长文档、多条款、证据分散、普通 QA 不够。它把 multi-agent 写成法律专家流程的自动化。写作特点是用领域困难自然引出 agent 分工，因此方法不显得是为了 agent 而 agent。

### Robust Native Language Identification through Agentic Decomposition

这篇的叙事重点是反捷径：NLI 模型容易利用表面线索，agentic decomposition 让判断过程拆解、透明、稳健。写作上把 agent 作为“分析流程组织器”，而不是自主执行环境中的 actor。

### WebEvolver

WebEvolver 是 evolve 主题里故事最完整的一篇：agent 自我训练依赖自采样轨迹，但环境模型如果静态，会造成改进信号失真。因此它提出 agent 和 world model co-evolve。写作关键词是 self-improvement、feedback loop、co-evolution，强烈突出“动态系统”而不是单轮训练。

### AgentPro

AgentPro 把 agent 训练从 outcome supervision 推到 process supervision。叙事上它抓住一个很有力的痛点：最终成功/失败信号太粗，无法告诉 agent 哪一步错了。写法偏 RL/process-feedback，适合强调“监督粒度”的重要性。

### EmoAgent

EmoAgent 以心理健康安全为高风险场景，故事由“AI characters 可能伤害脆弱用户”驱动。它不是只做评测，也提出 safeguard。写作特点是风险先行、评估与防护并列，伦理动机比性能动机更强。

### CityEQA

CityEQA 把 embodied QA 从室内扩展到城市空间。叙事重点是空间规模、环境层级和行动复杂性。它的 agent 不是聊天工具，而是分层导航和问答系统。写作偏 benchmark + hierarchical agent。

### AI Chatbots as Professional Service Agents

这篇的叙事亮点是“professional identity”。它把 chatbot 的问题从信息准确性扩展到职业目标、沟通伦理和患者中心表达。写作上理论感更强，借专业身份框架把方法合理化。

### PPTAgent

PPTAgent 的故事非常适合应用型生成任务：现有 text-to-slides 太像摘要，无法保证内容、设计和连贯性。它用人类 slide 制作流程讲方法，用 PPTEval 支撑评估完整性。叙述风格清楚、产品感强。

### ReSo

ReSo 的叙事是“多智能体系统不能再靠人工手工设计”。它提出 reward-driven self-organizing MAS，用 collaborative reward model 解决 agent selection 和协作优化。写作上更偏通用方法，目标是把 MAS 从 heuristic 推向可优化系统。

### OMS

OMS 是商业场景 agent 的典型写法：关键词生成不是离线文本生成，而是受 impressions、clicks、conversions 等多目标指标约束的在线决策。叙述特点是把 agentic reasoning 放入业务闭环，用真实 A/B 或人工偏好增强可信度。

### ZERA

ZERA 的故事是 prompt evolution。它从 APO 的三类问题切入：依赖初始 prompt、反馈不结构化、迭代成本高。然后用八个通用原则和 meta-cognitive refinement 讲“结构化演化”。写作风格很规整，适合作为方法论文的模板。

### MemoryOS

MemoryOS 用操作系统隐喻讲 agent memory，叙事上非常直观：短期、中期、长期记忆对应分层存储，更新、检索、生成对应 OS 式管理。它的写作强项是隐喻稳定，读者很容易理解模块为什么存在。

### The Stepwise Deception

这篇把 misinformation 从静态分类对象改写成动态演化过程。它的故事不是“检测假新闻”，而是“解释真新闻如何一步步变成假新闻”。写作上过程感很强，agent roles、social network、FUSE-EVAL 共同支撑“演化模拟”。

### FedMABench

FedMABench 是 benchmark-first 论文。它的主线是 mobile GUI agent 训练依赖集中式数据，但真实用户数据分散、异构且有隐私问题。写作上先定义评测缺口，再用大规模 benchmark 覆盖算法、模型、app 类别和数据异构性。

### Can LLM Agents Maintain a Persona in Discourse?

这篇从 persona consistency 切入，关注 agent 在语篇推进中是否维持角色。叙事比系统构建更偏评测诊断，适合展示 agent 在多轮 discourse 中的隐性退化。

### AutoCT

AutoCT 把 clinical trial prediction 写成 AI agent 可以承担的专家辅助流程。它强调解释性和自动化，叙事上用医疗研发的高成本、高风险、长周期来支撑任务价值。写作特点是应用价值强，但需要评估设计足够可信。

## 可借鉴的写作策略

1. 不要只说“我们提出一个 agent 框架”，要先定义一个旧系统无法处理的过程性失败：长程错误传播、动态环境错位、记忆遗忘、反馈过粗、专业身份缺失、评估盲区。
2. 方法最好有一个稳定隐喻或组织原则，例如 OS memory、human slide editing、professional identity、tool dependency graph、co-evolving world model。
3. Agent 论文的 contribution 应该分层写：任务重新定义、系统模块、评估框架、实证发现。只写模块通常不够有故事。
4. Evolve 类论文要突出时间轴：初始状态是什么、每轮如何变化、反馈如何进入、最终演化出什么能力或风险。
5. 引言里要尽早回答“为什么现有 LLM/RAG/ReAct/prompting 不够”。这些论文普遍在前两页就把 failure mode 画出来或列出来。
6. 实验叙事不要只报主结果。强论文通常会配套消融、案例、错误分析、真实应用或人类评价，用来证明系统各模块不是装饰。
7. 标题和摘要偏好强动词：Enhancing、Safeguarding、Automating、Simulating、Benchmarking、Generating、Evolving、Self-organizing。这些动词直接告诉读者论文解决的是一个动态过程。

## 参考来源

- EMNLP 2025 program overview: https://2025.emnlp.org/program/
- EMNLP 2025 accepted main conference papers: https://2025.emnlp.org/program/main_papers/
- ACL Anthology EMNLP 2025 proceedings: https://aclanthology.org/events/emnlp-2025/
- Underline EMNLP 2025 lecture metadata, e.g. SwarmAgentic page: https://underline.io/lecture/129845-swarmagentic-towards-fully-automated-agentic-system-generation-via-swarm-intelligence

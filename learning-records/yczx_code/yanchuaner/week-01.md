# 第 1 周学习记录

> GitHub 用户名：yanchuaner
>
> 日期：2026年7月19日

## 本周学习内容

- AI 应用开发的环境配置
- hello-agents：前言、第一章《初识智能体》。
- learn-claude-code：中文 README、s01_agent_loop

## 我用自己的话理解了什么

1. 核心架构定义

    Agent 在本质上并非单一模型，而是「基座大模型（LLM）」与「编排控制层（Harness / Orchestration Layer）」的复合体（Composite）。
    其中，LLM 充当认知核心（Cognitive Core），负责意图理解与策略生成；Harness 则充当执行骨架（Execution Skeleton），负责工具调度、状态维护与外部环境交互。

2. 工程落地的本质

    仿照 Claude Code 从零构建轻量级编码 Agent（例如 yczx code），其根本任务就是 Harness 工程的系统化实现。
    这不仅仅是接口调用，更涉及文件系统操作、Shell 命令执行、长文本截断（Truncation）以及上下文窗口溢出防护（Context Overflow Protection）等底层工程约束的处理。

3. 核心控制流（ReAct 范式）

    Harness 运转的引擎严格遵循 ReAct（Reasoning -> Acting -> Observing）范式。
    这是一个精密的闭环迭代，而非宽泛的“思考-执行”：

    - 推理（Reasoning）：LLM 分析当前状态并规划下一步。
    - 行动（Acting）：调用外部工具或生成代码变更。
    - 观察（Observation）：接收环境返回的执行结果或报错信息。

    与此同时，Harness 还充当状态机（State Machine），负责管理循环的终止条件（如达到最大迭代步数、LLM 输出终止信号或陷入无效循环）。

4. LLM 的底层生成机理

    LLM 在该框架中的核心机制是自回归式（Autoregressive）概率预测。
    它基于当前输入的完整上下文（Prompt + 历史信息），逐次计算词表中每一个 Token 的生成概率分布，并通过采样策略（Sampling Strategy）决定最终的输出内容。
    它本身不具备主动行动意识，其输出完全由上下文所锚定。

5. 动态交互与演化

    正是得益于 Harness 层面对多轮对话历史、系统级提示词（System Prompt）、工具调用返回值等上下文信息的持续性动态构建、压缩与注入，LLM 的通用推理能力才得以被锚定在具体的编码场景中。
    这种“构建上下文 → 模型推理 → 解析结果 → 更新上下文”的紧密耦合，最终催生了具备复杂工程协作能力的 Agent 产品（如 Claude Code）。

## 我运行或修改了什么

- 示例代码：1.3.py

## 验证命令与结果

- `git --version`
- `git version 2.54.0.windows.1`

- `py -3.12 --version`
- `Python 3.12.10`

## 仍然困惑的问题（学习缺口自检清单）

### 1. ReAct 循环的“状态机”实现（代码逻辑）

- [ ] **解析鲁棒性**：如果LLM输出的不是标准JSON/XML，而是夹杂了自然语言，Harness是如何做“容错提取（Strict Parsing vs. Fuzzy Parsing）”的？
- [ ] **异步与非阻塞**：在执行Shell命令或文件读写时，Harness是同步等待（Blocking）还是异步回调（Async/Await）？如果命令卡死怎么办？

### 2. 上下文窗口的“内存管理”（工程难点）

- [ ] **截断策略**：当对话历史 + 读取的代码文件超过LLM上下文窗口（如128K）时，Harness是丢弃最早的对话，还是对代码文件做摘要压缩（Map-Reduce）？
- [ ] **文件过滤**：Harness在读取项目文件时，是如何自动忽略 `.git`、`node_modules` 等无关目录的？（是否内置了 `.gitignore` 解析？）

### 3. 工具调用的“边界与安全”（架构设计）

- [ ] **权限校验**：如果Agent执行 `rm -rf /` 或修改系统关键文件，Harness是否有拦截层或用户确认机制（User Confirmation）？
- [ ] **环境隔离**：yczx code 的每次运行是独立的临时虚拟环境，还是直接作用于当前宿主机？

### 4. 底层原理的“黑盒迷雾”（概念理解）

- [ ] **Function Calling 的本质**：LLM是如何“知道”它该调用哪个工具的？是模型微调时强化的能力，还是全靠Harness在System Prompt里塞入了海量的工具描述（Tool Descriptor）？
- [ ] **推理链（CoT）的可控性**：我们能否强制要求LLM先输出推理过程再输出行动，还是说这是模型自发涌现的？

## 下周准备尝试什么

- 自己动手改写示例代码 1.3.py

## AI 工具使用说明

- AI 辅助概念与代码理解

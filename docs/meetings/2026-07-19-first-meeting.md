# 第一次组会：会议概述与摘要

> 时间：2026 年 7 月 19 日（周日）15:00—17:00
>
> 平台：腾讯会议
>
> 主题：从开发环境到 Agent Loop，认识 YCZX Code 的学习与开发路径
>
> 状态：会前概述；会议结束后补充实际结论

## 会议目标

这次会议希望帮助所有成员建立一张共同的知识地图：

1. 理解开发环境、Git 和可重复运行之间的关系。
2. 区分 LLM、普通聊天、Workflow、Agent 和 Agent Harness。
3. 看懂最小 Agent Loop 如何连接模型、工具与环境。
4. 了解 YCZX Code 当前状态、暑期边界和推荐开发顺序。
5. 确认参与方式，并公布下一周学习与实践任务。

本次会议不会讲完所有 Agent 技术，也不会要求新成员立即参与正式产品代码。第一阶段先统一概念、环境和协作方法。

## 会议安排

| 时间 | 环节 | 内容 |
| --- | --- | --- |
| 15:00—15:08 | 开场 | 说明会议目标和暑期主线 |
| 15:08—15:35 | 成员分享 | 本周学习、主要问题、可投入时间和参与意向 |
| 15:35—15:50 | 开发与环境 | Git、Python、uv、VS Code 各自解决什么问题 |
| 15:50—16:15 | Agent 整体概念 | LLM、Workflow、Agent、Harness、Tool、Environment |
| 16:15—16:35 | Agent Loop 演示 | 模型决策、Harness 执行、工具结果回传 |
| 16:35—16:48 | YCZX Code | 当前状态、模块边界和开发顺序 |
| 16:48—16:56 | 协作方式 | 学习仓库、分支、PR 和参与方式 |
| 16:56—17:00 | 下周安排 | 公布学习范围和成果要求 |

## 会前准备

- 完成或尝试完成 [`Windows 环境配置`](../setup/windows.md)。
- 阅读 YCZX Code 第 1 周任务：[`week-01.md`](../../projects/yczx_code/tasks/week-01.md)。
- 记录一个最希望在会议中解决的问题。
- 不需要配置真实 API Key，也不需要启动 Docker 和 AI 底座。

## 核心概念摘要

### 开发不只是写代码

一个最小开发闭环包括：明确目标和限制、编写代码、在确定环境运行、验证结果、记录变化，并确保其他人能够复现。

### LLM、Agent 与 Harness

- LLM：根据上下文生成文本或结构化工具请求，但不会自动看到或操作本机文件。
- Agent：围绕目标持续观察、决策、行动，并根据环境反馈继续推进。
- Harness：开发者围绕模型构建的运行与控制系统，包括 CLI、工具、上下文、权限、日志和循环。
- Tool：Harness 提供的受控动作，例如读取文件、搜索、应用补丁和运行测试。
- Environment：Agent 工作并产生影响的外部环境，例如代码仓库、文件系统和终端。

模型负责提出下一步决策，Harness 负责校验和执行。真正读取文件或运行命令的是应用代码，不是模型本身。

### 最小 Agent Loop

```text
用户任务
  -> 把消息和工具定义交给模型
  -> 模型返回最终答案：结束
  -> 模型请求工具：Harness 检查并执行
  -> 工具结果作为新观察返回模型
  -> 重复，直到完成或达到系统限制
```

真实 Agent Loop 还必须有最大轮数、超时、路径限制、权限确认、错误处理和日志，不能只是无限循环。

## 公共演示

演示使用个人 API Key 完成真实模型调用和工具循环。先按 [`真实案例教程`](../../projects/yczx_code/tutorials/README.md) 设置当前终端环境变量，再运行：

```powershell
git clone https://github.com/yanchuaner/yczx_code_lab.git
Set-Location yczx_code_lab
uv sync
uv run python examples/yczx_code/01_first_chat.py
uv run python examples/yczx_code/03_agent_loop.py
```

第一个案例展示一次模型请求；第二个案例展示模型请求真实本地工具、Harness 执行、工具结果回传和模型最终回答。演示会产生少量 API 费用，不得共享或展示真实 Key。

## YCZX Code 当前状态

截至 2026 年 7 月 18 日：

- 产品定位、学习路线、技术栈和开发路线已经形成文档。
- 正式仓库尚未形成完整可运行 Agent。
- CLI、Model Provider、工具系统、权限、上下文、日志和评测仍需逐步实现。
- AI 底座已有 PoC，但第一阶段案例直接使用个人 DeepSeek API Key，不依赖 AI 底座启动。

推荐顺序是：工程基线、模型适配、只读工具、Agent Loop、上下文、安全修改、Shell 测试闭环、会话与评测。每一步都要有可运行结果、测试或验证和文档。

## 参与方式

- 核心开发：愿意稳定完成学习和代码任务，通过分支与 PR 参与主线。
- 学习参与：跟随资料和会议学习，可以提交记录、文档、测试和问题。
- 暂时旁听：先了解项目，不承担固定任务，之后可以调整。

三种方式不是能力等级。持续投入、按时反馈和可靠交付，比起点高低更重要。

所有成员都通过个人分支和 Pull Request 协作，不直接推送 `main`。学习记录和个人练习分别放在：

```text
learning-records/yczx_code/<github-id>/week-XX.md
exercises/yczx_code/<github-id>/week-XX/
```

## 第二周入口

第二周任务以 [`projects/yczx_code/tasks/week-02.md`](../../projects/yczx_code/tasks/week-02.md) 为准，重点是：

- 学习 LLM 交互、模型幻觉、ReAct 和 Tool Use。
- 复习 `s01_agent_loop`，阅读 `s02_tool_use`。
- 完成 [`五个真实案例教程`](../../projects/yczx_code/tutorials/README.md) 中的 01–03。
- 观察并解释 `tool_use`、本地执行和 `tool_result`。
- 核心开发候选继续完成只读代码库 ReAct 案例。
- 周六提交原创学习记录、练习代码和验证结果。

## 会后摘要

以下内容在会议结束后由维护者补充：

### 参会情况

待补充。

### 已确认共识

待补充。

### 参与与维护安排

待补充。

### 未解决问题

| 问题 | 负责人 | 预计回复时间 |
| --- | --- | --- |
| 待补充 |  |  |

### 下次会议

计划为 2026 年 7 月 26 日（周日）15:00—17:00，最终以群内通知为准。

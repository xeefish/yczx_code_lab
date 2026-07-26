# YCZX Code 第 2 周：LLM 交互、ReAct 与 Tool Use

> 周期：2026 年 7 月 20 日至 26 日

## 学习范围

### hello-agents

- 第三章 3.2《与大语言模型交互》。
- 第三章 3.3.2《模型幻觉》。
- 第四章 4.2.1《ReAct 的工作流程》。
- 时间充足时阅读第四章 4.2.2 至 4.2.4，不要求配置真实 API Key。

### learn-claude-code

- 复习 `s01_agent_loop`，逐段解释循环。
- 阅读 `s02_tool_use`，重点理解工具注册和分发。

### Python

- 函数、参数、返回值。
- `list`、`dict`、`for`、`while`。
- `pathlib`、类型标注和基础异常处理。

## 实践任务

所有成员：

1. 运行案例 01：完成一次真实模型对话。
2. 运行案例 02：观察真实模型产生的结构化工具请求。
3. 运行案例 03：完成工具结果回传模型的 Agent Loop。
4. 在个人练习目录修改案例 01 和案例 03，并记录实际输出。
5. 写下 Agent Loop 的执行顺序，并说明单次模型调用为什么还不是 Agent。

核心开发候选额外完成：

1. 运行案例 04：完成只读代码库 ReAct Agent。
2. 修改任务，让 Agent 阅读 `AGENTS.md` 和当前周任务。
3. 解释路径边界、敏感文件拦截和最大步数分别解决什么风险。

进度较快的成员选做案例 05，理解 Provider、ToolRegistry 和 Agent 的模块边界。案例入口见 [`examples/yczx_code/`](../../../examples/yczx_code/README.md)。

## 提交

周六提交 `learning-records/yczx_code/<github-id>/week-02.md`、`exercises/yczx_code/<github-id>/week-02/` 下的练习代码，以及运行命令和输出说明。真实模型结果可以只摘录不含隐私的短文本，禁止提交 API Key。

## 验收

- 能解释模型决策与 Harness 执行的区别。
- 能通过环境变量完成一次本地真实模型调用。
- 能观察并解释真实 `tool_use` 和 `tool_result`。
- 能运行和修改完整 Agent Loop。
- 核心开发候选完成只读 ReAct 案例，或提交可复现的阻塞。

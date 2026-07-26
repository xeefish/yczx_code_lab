# YCZX Code 核心开发路线第 3 周：CLI Agent 骨架

> 周期：2026 年 7 月 27 日至 8 月 2 日

## 本周结果

确定 CLI 交互式 Agent 的最小架构，并跑通“用户输入 -> 模型 -> 工具 -> 工具结果 -> 模型”的闭环。

## 学习材料

- `hello-agents`：第三章和第四章 ReAct 实现。
- `learn-claude-code`：`s01_agent_loop`、`s02_tool_use`。
- 本仓库案例：[`01_first_chat.py`](../../../../examples/yczx_code/01_first_chat.py)、[`02_first_tool_call.py`](../../../../examples/yczx_code/02_first_tool_call.py)、[`03_agent_loop.py`](../../../../examples/yczx_code/03_agent_loop.py)。

## 开发任务

1. 确定 Python 包入口和启动命令，例如 `uv run python -m yczx_code`。
2. 定义 Provider、Agent、Tool 和会话消息的最小接口。
3. 实现命令行输入循环和 `/help`、`/reset`、`/context`、`/quit` 命令。
4. 实现单工具闭环，再扩展为多个工具。
5. 让工具调用过程对用户可见。

## 验收

- 能连续完成至少两轮对话。
- 能观察到工具请求、工具执行和工具结果。
- Provider 不负责工具执行，Agent 不直接操作文件系统。
- 至少有消息构造和停止条件测试。

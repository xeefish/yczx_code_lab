# YCZX Code 学习路线第 3 周：从模型调用到 Agent Loop

> 周期：2026 年 7 月 27 日至 8 月 2 日

## 学习目标

- 理解模型输出、Harness 执行和 Tool Result 回传之间的边界。
- 能用自己的话解释 ReAct 的思考、行动、观察循环。
- 运行并修改一个最小 Agent Loop。

## 学习材料

- `hello-agents`：第二章重点阅读，第三章 3.1 至 3.3。
- `hello-agents`：第四章 4.2，重点是 ReAct。
- `learn-claude-code`：`s01_agent_loop`、`s02_tool_use`，复习并逐段解释代码。
- 本仓库案例：[`01_first_chat.py`](../../../../examples/yczx_code/01_first_chat.py)、[`02_first_tool_call.py`](../../../../examples/yczx_code/02_first_tool_call.py)、[`03_agent_loop.py`](../../../../examples/yczx_code/03_agent_loop.py)。

## 必做实践

1. 运行一个真实模型对话或使用项目提供的无 Key 替代输入。
2. 画出一次 Tool Use 的消息顺序：用户、模型、工具、结果、模型。
3. 修改案例 03 的一个工具或提示词，并记录行为变化。
4. 完成个人学习记录，说明单次模型调用为什么还不是 Agent。

## 验收

- 能口头解释 Agent Loop 的停止条件。
- 能指出 Tool Schema、Tool Handler 和 Tool Result 各自的职责。
- 提交实际运行命令；没有 API Key 时提交可复现的阻塞说明。

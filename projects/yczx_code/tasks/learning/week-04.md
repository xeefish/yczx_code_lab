# YCZX Code 学习路线第 4 周：经典范式与框架边界

> 周期：2026 年 8 月 3 日至 9 日

## 学习目标

- 理解 ReAct、Plan-and-Solve、Reflection 的适用场景和代价。
- 区分使用 Agent 框架与理解 Agent 框架。
- 初步理解工具注册、Provider 和 Agent 的模块边界。

## 学习材料

- `hello-agents`：第四章完整阅读，第五章和第六章选读。
- `learn-claude-code`：`s03_permission`、`s04_hooks`、`s05_todowrite`。
- 本仓库案例：[`04_readonly_react_agent.py`](../../../../examples/yczx_code/04_readonly_react_agent.py)，了解只读边界和最大步数。

## 必做实践

1. 为同一个代码库问题分别写一个直接回答提示词和一个 ReAct 提示词。
2. 比较两次结果的步骤、工具调用和失败方式。
3. 写一页笔记，说明 Provider、Tool Registry、Agent Loop 为什么应该分开。

## 验收

- 能解释至少两种经典范式的差异。
- 能说明权限检查应位于工具执行前，而不是只写在提示词中。
- 学习记录包含一个失败案例及其原因分析。

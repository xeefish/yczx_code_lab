# YCZX Code 学习入口

本目录维护 YCZX Code 的阶段性学习任务和配套教程，目标是让成员从 Agent 基础概念逐步走到 Coding Agent Harness 的工程实践。

## 学习顺序

1. 环境、Git、LLM、Agent 和 Harness 基础。
2. 真实模型对话与 Tool Use。
3. Tool Result、Agent Loop 与 ReAct。
4. 路径安全、最大步数和只读工具。
5. Model Provider、Tool Registry 与模块化。
6. 上下文、权限、Diff、安全写入、测试和评测。

## 本目录内容

- [`tasks/week-01.md`](./tasks/week-01.md)：第一周启动与基础认知任务。
- [`tasks/week-02.md`](./tasks/week-02.md)：第二周 Agent Loop 与 Tool Use 任务。
- [`tutorials/README.md`](./tutorials/README.md)：五个真实案例的学习顺序与公共准备。

## 当前边界

本阶段不安排复杂 GUI、多 Agent 并行、插件市场、API 转卖或无限制命令执行。学习重点是先理解一个安全、可观察、可以逐步扩展的最小 Coding Agent 循环。

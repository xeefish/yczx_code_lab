# YCZX Code 学习入口

本目录维护 YCZX Code 的阶段性学习任务和配套教程，目标是让成员从 Agent 基础概念逐步走到 Coding Agent Harness 的工程实践。

## 学习顺序

1. 环境、Git、LLM、Agent 和 Harness 基础。
2. 真实模型对话与 Tool Use。
3. Tool Result、Agent Loop 与 ReAct。
4. 路径安全、最大步数和只读工具。
5. Model Provider、Tool Registry 与模块化。
6. 上下文、权限、测试和评测；安全写入和 Diff 留到预览版之后评估。

## 暑期双路线

第二周结束后，任务分为两条路线。两条路线共享前两周的基础，但目标和提交要求不同。

### 学习路线

面向所有希望系统学习 Agent 的成员。主教材是 [`hello-agents`](https://github.com/datawhalechina/hello-agents)，辅以 [`learn-claude-code`](https://github.com/shareAI-lab/learn-claude-code)。重点是读懂概念、运行示例、完成小练习并用自己的话复盘，不要求参与 YCZX Code 开发。

### 核心开发路线

面向参与 YCZX Code 预览版开发的成员。以两个学习项目为材料，逐步实现一个轻量级命令行交互式 Agent。预览版只做安全、可观察的代码库只读分析，不追求复刻 Claude Code 的全部功能。

核心开发任务和学习说明保留在本仓库；预览版的正式设计、代码、测试和发布进入 [YCZX Code 正式仓库](https://github.com/yanchuaner/yczx_code)，按正式仓库的 Issue、分支和 PR 规则执行。个人原型仍可放在本仓库自己的 `exercises/` 目录，但不会自动迁移为正式功能。

暑期阶段目标为 9 月 1 日左右完成预览版验收。实际进度较快时可以提前合并后续任务，但不能跳过安全边界、测试和文档。

## 本目录内容

- [`tasks/week-01.md`](./tasks/week-01.md)：第一周启动与基础认知任务。
- [`tasks/week-02.md`](./tasks/week-02.md)：第二周 Agent Loop 与 Tool Use 任务。
- [`tasks/learning/`](./tasks/learning/)：学习路线第三周至第七周任务。
- [`tasks/core/`](./tasks/core/)：核心开发路线第三周至第七周任务。
- [`tasks/README.md`](./tasks/README.md)：路线、提交归属和完成等级。
- [`../../examples/yczx_code/`](../../examples/yczx_code/README.md)：五个可运行案例及公共准备。

## 暑期验收

- 学习路线：能解释模型、Harness、工具、权限和上下文的关系，运行并修改至少一个 Agent Loop 示例，提交本人独立完成的学习记录和失败分析。
- 核心开发路线：在正式仓库完成可启动的 CLI Agent，具备多轮对话、只读工具、项目规则加载、路径安全、最大步数、测试、固定评测和复现文档。

## 当前边界

预览版的目标交互方式是本地命令行 REPL，例如 `uv run python -m yczx_code`。首版应支持多轮对话、目录和文本只读、项目规则加载、工具调用展示、最大步数和安全路径检查。

本阶段不安排文件写入、无限制 Shell、多 Agent 并行、插件市场、复杂 GUI 或完整 MCP 运行时。预览版必须在 README 中说明能力、限制、测试命令和已知问题。

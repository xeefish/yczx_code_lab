# YCZX Code 示例

本目录的案例统一使用 Python 3.12、uv、Anthropic SDK 和 DeepSeek Anthropic 兼容接口，按一个概念一步递进。

| 文件 | 新增概念 | 工具行为 |
| --- | --- | --- |
| [`01_first_chat.py`](./01_first_chat.py) | 一次真实模型请求 | 不执行工具 |
| [`02_first_tool_call.py`](./02_first_tool_call.py) | Tool Schema 与模型工具请求 | 本地执行一次，不回传模型 |
| [`03_agent_loop.py`](./03_agent_loop.py) | Tool Result 与完整 Agent Loop | 执行计算工具 |
| [`04_readonly_react_agent.py`](./04_readonly_react_agent.py) | 代码库 Action-Observation 与安全边界 | 只读指定路径 |
| [`05_mini_agent/`](./05_mini_agent/README.md) | Provider、ToolRegistry、Agent 模块边界 | 只读指定路径 |
| [`SOURCES.md`](./SOURCES.md) | 概念来源与许可证边界 | 不适用 |

真实模型案例只从环境变量读取 API Key，且所有请求都可能产生费用。运行前确认模型、任务和最大步数，不要把 Key 写入本目录的任何文件。

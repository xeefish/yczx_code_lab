# 案例 05：模块化 Mini Agent

本目录把单文件 Agent 拆成职责明确的模块：

| 文件 | 职责 |
| --- | --- |
| `main.py` | 组装应用并定义用户任务 |
| `config.py` | 从环境变量读取配置 |
| `provider.py` | 封装模型接口 |
| `tools.py` | 定义工具和 `ToolRegistry` |
| `agent.py` | 维护 Agent Loop |
| `__init__.py` | 标记 Python 包 |

在本目录中运行：

```powershell
uv run python .\main.py
```

这里仍然只提供读取目录和文本文件的工具，不写文件、不运行 Shell。这个结构用于理解模块边界，不代表最终产品架构。

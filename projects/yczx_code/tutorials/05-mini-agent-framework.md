# 案例 05：模块化 Mini Agent

代码目录：[`05_mini_agent`](../../../examples/yczx_code/05_mini_agent/README.md)

## 运行

```powershell
uv run python examples/yczx_code/05_mini_agent/main.py
```

## 模块职责

| 文件 | 职责 |
| --- | --- |
| `config.py` | 环境变量和运行限制 |
| `provider.py` | Anthropic 兼容模型接口 |
| `tools.py` | Tool、ToolRegistry 和只读工具 |
| `agent.py` | Agent Loop 和工具结果回传 |
| `main.py` | 组装依赖并定义任务 |

这一步对应上游第七章“构建自己的 Agent 框架”的核心思想：稳定模型、工具和 Agent 的职责边界。它仍然是教学案例，不应直接复制成 YCZX Code 的正式架构。

## 练习

- 在 `ToolRegistry` 注册一个新只读工具。
- 给 Provider 增加超时配置。
- 给 Agent 增加总工具调用次数限制。
- 画出五个模块的调用关系，并说明未来哪些接口可能变化。

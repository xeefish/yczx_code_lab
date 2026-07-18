# 案例 02：第一次真实工具请求

代码：[`02_first_tool_call.py`](../../../examples/yczx_code/02_first_tool_call.py)

## 运行

```powershell
uv run python examples/yczx_code/02_first_tool_call.py
```

## 观察重点

程序把计算器的名称、描述和 JSON Schema 一起发给模型。模型返回结构化 `tool_use`，其中包含工具名和参数；Python 再用安全 AST 计算器执行表达式。

案例故意在本地执行后停止，没有把计算结果交还模型。因此它展示了 Tool Calling，但还没有形成完整闭环。

## 为什么不用 `eval`

`eval` 可以执行任意 Python 表达式，不适合处理模型生成的输入。案例只允许数字、括号和加减乘除节点，其他语法会被拒绝。

## 练习

- 修改算术问题并观察模型参数。
- 增加幂运算前，先思考数值范围和滥用风险。
- 用自己的话解释 Tool Schema 为什么同时服务模型和 Harness。

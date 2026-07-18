# 案例 03：完整 Agent Loop

代码：[`03_agent_loop.py`](../../../examples/yczx_code/03_agent_loop.py)

## 运行

```powershell
uv run python examples/yczx_code/03_agent_loop.py
```

## 执行过程

```text
用户任务
  -> 模型请求 calculate 或 get_current_time
  -> Python 校验并执行工具
  -> tool_result 作为 Observation 交还模型
  -> 模型继续请求工具或生成最终回答
  -> 没有工具请求时结束
```

案例能够处理模型在同一轮请求多个工具，并设置最大 5 步，避免无限循环。工具失败时通过 `is_error` 把错误交还模型，而不是伪装成成功结果。

## 练习

- 修改任务，让模型只使用一个工具。
- 增加一个返回固定学习计划的只读工具。
- 解释为什么每个 `tool_use_id` 都必须对应一个 `tool_result`。
- 思考 API 超时、用户中止和总成本限制应该加在哪里。

# 案例 04：只读代码库 ReAct

代码：[`04_readonly_react_agent.py`](../../../examples/yczx_code/04_readonly_react_agent.py)

## 运行

```powershell
uv run python examples/yczx_code/04_readonly_react_agent.py
```

## ReAct 在这里怎样体现

程序不打印模型隐藏推理，只展示可验证的 Action 和 Observation：模型选择列目录或读文件，Harness 执行并返回真实结果，模型据此决定下一步。

案例加入了 Coding Agent 必需的第一批边界：

- 只允许工作区相对路径。
- 拒绝路径越界。
- 忽略 `.git`、`.venv` 和缓存。
- 拒绝 `.env`、证书和私钥文件。
- 限制目录结果和文件内容长度。
- 限制最大执行步数。

## 练习

- 尝试要求 Agent 读取 `../outside.txt`，观察拦截结果。
- 修改任务，让 Agent 阅读 `AGENTS.md` 和项目任务。
- 增加一个只读 `search_text` 工具，并为结果数量设置上限。

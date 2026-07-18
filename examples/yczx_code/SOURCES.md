# 概念来源与许可证说明

本目录原创代码采用仓库根目录的 MIT License。外部项目的名称、链接和概念说明不改变其各自许可证；若以后直接复制或改编第三方实现，必须在对应文件中单独标注并遵守上游许可证。

## hello-agents

- 上游仓库：<https://github.com/datawhalechina/hello-agents>
- 本次参考提交：`6c616938c521c89bc4b2bf001bf237d259f1726b`
- 上游许可证：[CC BY-NC-SA 4.0](https://github.com/datawhalechina/hello-agents/blob/main/LICENSE.txt)

重点参考：

- `code/chapter1/FirstAgentTest.py`：Thought、Action、Observation 教学循环。
- `code/chapter4/llm_client.py`：模型客户端边界。
- `code/chapter4/tools.py`：工具执行器和注册思想。
- `code/chapter4/ReAct.py`：ReAct 最大步数与观察历史。
- `code/chapter7/my_simple_agent.py`：多轮工具调用。
- `code/chapter7/my_react_agent.py`：自定义 ReAct Agent。
- `code/chapter7/my_calculator_tool.py`：AST 计算器工具。

本目录的案例是针对 YCZX Code Lab 的原创重写：改用 Anthropic 原生 Tool Use、DeepSeek 兼容接口、uv、环境变量、路径限制和中文错误提示，没有直接复制上述源码。

若未来直接复制或改编上游具体实现，必须在对应文件中保留来源、标明修改，并遵守 CC BY-NC-SA 4.0 的署名、非商业和相同方式共享要求；这类内容不能仅凭仓库根目录的 MIT License 重新授权。

## Anthropic SDK 与 DeepSeek

- Anthropic Python SDK：<https://github.com/anthropics/anthropic-sdk-python>
- DeepSeek Anthropic API：<https://api-docs.deepseek.com/guides/anthropic_api>

代码使用 Anthropic SDK 的结构化 `tool_use` 和 `tool_result`，避免依赖脆弱的自然语言正则解析。

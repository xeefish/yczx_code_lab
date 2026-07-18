# 案例 01：第一次真实模型对话

代码：[`01_first_chat.py`](../../../examples/yczx_code/01_first_chat.py)

## 运行

先完成 [`公共准备`](./README.md)，然后运行：

```powershell
uv run python examples/yczx_code/01_first_chat.py
```

正常情况下会显示实际模型名，并返回一段关于 AI Agent 的中文说明。

## 观察重点

代码从环境变量读取 Base URL、模型名和 API Key，创建 Anthropic 客户端，再通过 `messages.create()` 发送 system 和 user 消息。

这只是一次远程模型请求，不是 Agent：程序没有提供工具，也没有根据环境反馈继续循环。

## 练习

复制到个人目录并修改用户问题：

```powershell
$githubId = "your-github-id"
$exerciseDir = "exercises/yczx_code/$githubId/week-02"
New-Item -ItemType Directory -Force -Path $exerciseDir
Copy-Item "examples/yczx_code/01_first_chat.py" "$exerciseDir/01_first_chat.py"
code "$exerciseDir/01_first_chat.py"
uv run python "$exerciseDir/01_first_chat.py"
```

在学习记录中解释：本地 Python、Anthropic SDK、DeepSeek API 和模型分别承担什么职责。

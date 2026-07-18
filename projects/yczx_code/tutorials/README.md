# YCZX Code 真实案例教程

## 公共准备

先在仓库根目录同步依赖：

```powershell
uv sync
```

在当前 PowerShell 中安全设置 DeepSeek 环境变量：

```powershell
$env:ANTHROPIC_BASE_URL = "https://api.deepseek.com/anthropic"
$env:DEEPSEEK_MODEL = "deepseek-v4-pro"
$secureKey = Read-Host "请输入 DeepSeek API Key" -AsSecureString
$env:ANTHROPIC_API_KEY = [System.Net.NetworkCredential]::new("", $secureKey).Password
```

检查变量是否存在，但不要打印 Key：

```powershell
if ($env:ANTHROPIC_API_KEY) { "API Key 已设置" } else { "API Key 未设置" }
$env:ANTHROPIC_BASE_URL
$env:DEEPSEEK_MODEL
```

这些变量只在当前 PowerShell 窗口有效。所有真实请求都可能产生费用，不要改成无限循环。

## 学习顺序

1. [`01-first-chat.md`](./01-first-chat.md)：第一次真实模型对话。
2. [`02-first-tool-call.md`](./02-first-tool-call.md)：模型怎样请求工具。
3. [`03-agent-loop.md`](./03-agent-loop.md)：怎样把工具结果交还模型。
4. [`04-readonly-react-agent.md`](./04-readonly-react-agent.md)：安全读取真实代码库。
5. [`05-mini-agent-framework.md`](./05-mini-agent-framework.md)：从单文件走向模块化 Harness。

前三个案例适合作为第二周共同任务；第四、第五个案例适合核心开发候选继续学习。

## 完成后清除 Key

```powershell
Remove-Item Env:ANTHROPIC_API_KEY
Remove-Variable secureKey -ErrorAction SilentlyContinue
```

不要把真实 Key 写入 Python、Markdown、`.env`、截图、学习记录或 Git 历史。

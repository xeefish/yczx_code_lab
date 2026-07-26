# YCZX Code 核心开发路线第 4 周：只读工具与安全边界

> 周期：2026 年 8 月 3 日至 9 日

## 本周结果

让 Agent 能安全地阅读一个真实代码库，并在越界或敏感访问时拒绝执行。

## 学习材料

- `hello-agents`：第四章经典范式，第七章框架开发相关内容。
- `learn-claude-code`：`s03_permission`、`s04_hooks`、`s05_todowrite`。
- 本仓库案例：[`04_readonly_react_agent.py`](../../../../examples/yczx_code/04_readonly_react_agent.py) 和 [`05_mini_agent/`](../../../../examples/yczx_code/05_mini_agent/README.md)。

## 开发任务

1. 实现 `list_dir`、`read_file`、`search_files` 和 `get_project_rules`。
2. 为每个工具提供清晰的 Schema、参数校验和统一结果格式。
3. 将工作目录解析为绝对路径，拒绝路径穿越和工作区外访问。
4. 拦截 `.env`、密钥文件、数据库、日志和明显的私密配置。
5. 增加最大步数和工具错误返回。

## 验收

- Agent 能回答一个真实 Python 项目的目录和入口问题。
- 越界路径、敏感文件和不存在文件都有可读错误信息。
- 安全检查由代码强制执行，不依赖模型自觉。
- 为路径边界和敏感文件至少各写 3 个测试。

# 贡献入口

## 开始前

1. 阅读根目录 [`README.md`](../README.md) 和 [`AGENTS.md`](../AGENTS.md)。
2. 完成 [`Windows 环境配置`](./setup/windows.md)。
3. 阅读 [`Git 核心概念`](./git/concepts.md) 和 [`完整上手流程`](./git/quickstart.md)。
4. 查看当前项目任务，确认自己的提交路径。

## 仓库规则

- 不直接推送 `main`，每项任务使用独立分支和 PR。
- 学习记录必须本人独立完成。
- 代码可以使用 AI 辅助，但作者必须理解并验证全部修改。
- 不提交 `.env`、API Key、数据库、日志、个人资料和本地配置。
- 个人内容只放在自己的 GitHub 用户名目录。
- 公共教程和示例先认领再修改。

## 提交路径

```text
learning-records/<project-id>/<github-id>/week-XX.md
exercises/<project-id>/<github-id>/week-XX/
```

## 验证

```powershell
uv sync
uv run ruff check .
uv run python scripts/check_naming.py
```

没有自动测试时，在 PR 中写明实际运行命令、输出和未验证部分。

## 需要帮助

Git 错误先查看 [`troubleshooting.md`](./git/troubleshooting.md)。求助时提供完整命令、错误信息、当前分支和 `git status --short --branch`，不要只说“运行不了”。

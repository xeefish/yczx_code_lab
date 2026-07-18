# YCZX Code Lab 协作说明

## 仓库定位

本仓库是燕中生态的长期学习、练习和实验平台，不是任何项目的正式生产仓库。允许提交不成熟但可解释的练习；正式功能必须进入对应正式仓库并单独评审。

## 修改前

- 先阅读根目录 `README.md`、本文件、通用工作流文档和当前项目任务。
- 先查看 Git 状态：`git status --short --branch`。
- 不覆盖其他成员未提交的修改。
- 不把真实 API Key、`.env`、数据库、日志、上传文件、个人资料或私有配置放入仓库。

## 项目扩展规则

- 新项目先在 `projects/<project-id>/README.md` 中说明定位、正式仓库、负责人、学习入口和边界。
- 项目专属任务放在 `projects/<project-id>/tasks/`。
- 学习记录放在 `learning-records/<project-id>/<github-id>/week-XX.md`。
- 个人练习放在 `exercises/<project-id>/<github-id>/week-XX/`。
- 可复用示例放在 `examples/<project-id>/`，并配套说明和可复现的验证方式；只有存在明确可验证行为时才新增测试。
- 通用环境、Git、PR 和安全规则放在 `docs/`，不要为每个项目复制一份。

## 提交规则

- 使用分支和 Pull Request，不直接推送 `main`。
- 分支建议命名为 `week-XX/<github-id>/<short-topic>`。
- 一个 Pull Request 只完成一个主题，描述中写明目的、修改内容和验证命令。
- 学习记录必须本人独立完成，不能由 AI 代写或拼接。
- 代码可以使用 AI 辅助，但提交者必须理解全部修改并说明验证方法。
- 新增文档和代码注释使用中文；代码标识符遵循项目原有风格。
- 不进行无关重构、格式化或目录移动。

## 验证要求

根据改动范围运行最小必要检查：

```powershell
uv run ruff check .
uv run python scripts/check_naming.py
```

练习若没有自动测试，至少在 PR 中写明实际运行命令和输出。无法验证时要明确说明原因。

## 从实验到正式项目

练习仓库的代码不自动进入任何正式仓库。如果某个练习值得进入正式主线，需要先说明正式问题，在正式仓库中重新设计模块边界、补充测试和安全规则，再按正式项目的 Issue 和 PR 流程提交。

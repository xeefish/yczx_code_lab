# YCZX Code Lab 协作说明

## 仓库定位

本仓库是燕中生态的长期学习、练习和实验平台，不是任何项目的正式生产仓库。允许提交不成熟但可解释的练习；正式功能必须进入对应正式仓库并单独评审。

本仓库当前的主要学习项目是 YCZX Code。它以 `hello-agents` 为主线教材、以 `learn-claude-code` 为 Harness 工程补充材料。YCZX Code 从第三周起分为两条路线：`projects/yczx_code/tasks/learning/` 面向全体学习者，`projects/yczx_code/tasks/core/` 面向核心开发者。核心路线的暑期目标是轻量级命令行交互式 Agent 预览版，不是完整 Claude Code。

YCZX Code 的任务计划和个人原型可以留在本仓库；预览版的正式设计、产品代码、测试和发布必须进入 `https://github.com/yanchuaner/yczx_code`，遵循该仓库自己的 `AGENTS.md`、Issue 和 PR 规则。

其他项目必须在自己的 `projects/<project-id>/README.md` 中重新说明定位、路线、阶段目标和边界；不要把 YCZX Code 的产品假设复制到其他项目。

## 修改前

- 先阅读根目录 `README.md`、本文件、通用工作流文档和当前项目任务。
- 先查看 Git 状态：`git status --short --branch`。
- 不覆盖其他成员未提交的修改。
- 不把真实 API Key、`.env`、数据库、日志、上传文件、个人资料或私有配置放入仓库。
- 使用本地 Agent 时，先读取目标项目的 `README.md`、`tasks/README.md`（如有）和当前路线任务，再决定修改范围。
- 不因为 Agent 的建议自动扩大范围；不修改其他成员目录、公共教程或公共示例，除非任务明确授权。
- 工作区存在未提交修改时，不执行会覆盖、清理或强制重置的 Git 操作；同步远端前先说明影响并保留现有修改。

## 项目扩展规则

- 新项目先在 `projects/<project-id>/README.md` 中说明定位、正式仓库、负责人、学习入口和边界。
- 项目专属任务放在 `projects/<project-id>/tasks/`。
- 学习记录放在 `learning-records/<project-id>/<github-id>/week-XX.md`。
- 个人练习放在 `exercises/<project-id>/<github-id>/week-XX/`。
- 可复用示例放在 `examples/<project-id>/`，并配套说明和可复现的验证方式；只有存在明确可验证行为时才新增测试。
- 通用环境、Git、PR 和安全规则放在 `docs/`，不要为每个项目复制一份。
- 项目任务按路线放在 `tasks/learning/` 或 `tasks/core/`；跨路线的共同基础可以保留在 `tasks/week-XX.md`，但新增任务应使用路线目录。
- 阶段性目标、明确不做的内容和重要取舍统一写在项目 README，避免维护重复文件。

## 提交规则

- 使用分支和 Pull Request，不直接推送 `main`。
- 分支建议命名为 `week-XX/<github-id>/<short-topic>`。
- 一个 Pull Request 只完成一个主题，描述中写明目的、修改内容和验证命令。
- 学习记录必须本人独立完成，不能由 AI 代写或拼接。
- 本地 Agent 可以解释材料、定位错误、检查代码和提出修改建议，但不能代替成员组织学习记录、伪造运行结果或生成未经理解的个人感悟。
- 代码可以使用 AI 辅助，但提交者必须理解全部修改并说明验证方法。
- 新增文档和代码注释使用中文；代码标识符遵循项目原有风格。
- 不进行无关重构、格式化或目录移动。
- 未经成员明确确认，不代表成员创建、合并或推送 Pull Request；操作前由成员确认 diff、提交信息和验证结果。

## 验证要求

根据改动范围运行最小必要检查：

```powershell
uv run ruff check .
uv run python scripts/check_naming.py
```

练习若没有自动测试，至少在 PR 中写明实际运行命令和输出。无法验证时要明确说明原因。

## 本地 Agent 行为边界

- 默认只读检查：读取文件、搜索内容、查看 Git 状态和运行非破坏性检查。
- 写文件前先向成员说明将修改哪些路径；只在当前任务范围内编辑。
- 不读取与任务无关的 `.env`、数据库、日志、上传文件和个人资料；禁止打印或提交任何 API Key、令牌或其他敏感内容。
- YCZX Code 预览版当前只设计只读代码库工具；不要擅自加入文件写入、任意 Shell、多 Agent、插件市场或完整 MCP 运行时。
- 任何无法验证的结论都要明确标记为未验证，并给出成员可执行的验证命令。

## PR 前自检

```powershell
git branch --show-current
git status --short --branch
git diff --check
uv run ruff check .
uv run python scripts/check_naming.py
```

检查 diff 只包含当前主题、没有敏感文件、学习记录由本人独立组织，并在 PR 描述中写明目的、改动、验证命令和未完成项。

## 从实验到正式项目

练习仓库的代码不自动进入任何正式仓库。如果某个练习值得进入正式主线，需要先说明正式问题，在正式仓库中重新设计模块边界、补充测试和安全规则，再按正式项目的 Issue 和 PR 流程提交。

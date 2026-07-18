# Git 完整上手流程

> 适用环境：Windows PowerShell
>
> 示例任务：从模板创建 YCZX Code 第 2 周学习记录，并通过个人分支提交 PR

开始前先阅读 [`concepts.md`](./concepts.md)，确保理解 `origin`、`main`、分支、push 和 PR。

## 第 0 步：准备 GitHub 账号和权限

1. 注册并登录自己的 GitHub 账号。
2. 把 GitHub 用户名发给仓库管理员。
3. 接受 `yczx_code_lab` 的协作者邀请。
4. 建议在 GitHub 的 Settings → Emails 中启用邮箱隐私，并使用 GitHub 提供的 noreply 邮箱配置 Git。

不要共享 GitHub 密码、访问令牌或登录验证码。

## 第 1 步：检查 Git

```powershell
git --version
```

能够显示 `git version 2.x.x` 才继续。命令找不到时先完成 [`Windows 环境配置`](../setup/windows.md)。

## 第 2 步：配置提交身份

把下面两项替换为自己的信息。`user.name` 建议使用 GitHub 用户名；邮箱使用 GitHub noreply 邮箱或与 GitHub 账号绑定的邮箱。

```powershell
git config --global user.name "your-github-id"
git config --global user.email "your-github-noreply-email"
git config --global init.defaultBranch main
```

确认配置：

```powershell
git config --global --get user.name
git config --global --get user.email
git config --show-origin --get user.name
git config --show-origin --get user.email
```

前两条应显示刚才填写的值；后两条会同时显示配置来自哪个文件。

## 第 3 步：克隆仓库

选择统一的学习目录：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\Documents\yczx-study"
Set-Location "$HOME\Documents\yczx-study"
git clone https://github.com/yanchuaner/yczx_code_lab.git
Set-Location yczx_code_lab
```

重要：`git clone` 已经初始化了 Git 并自动配置 `origin`。不要在克隆后的目录再次执行 `git init`。

## 第 4 步：确认仓库和远程连接

```powershell
git rev-parse --is-inside-work-tree
git branch --show-current
git status --short --branch
git remote -v
git remote get-url origin
git ls-remote --heads origin
```

正常结果：

- `rev-parse` 返回 `true`。
- 当前分支是 `main`。
- `origin` 指向 `https://github.com/yanchuaner/yczx_code_lab.git`。
- `ls-remote` 能列出远程分支。

这只能确认读取连接。真正的写权限要在第 10 步推送个人分支时验证。

## 第 5 步：同步最新 main

每次开始新任务前都运行：

```powershell
git switch main
git pull --ff-only
```

如果 `pull` 失败，不要跳过并继续修改，把完整错误发到群里。

## 第 6 步：创建任务分支

先设置自己的 GitHub 用户名，再创建分支：

```powershell
$githubId = "your-github-id"
$branch = "week-02/$githubId/learning-record"
git switch -c $branch
git branch --show-current
```

必须把 `your-github-id` 换成真实 GitHub 用户名。最后一条应显示刚创建的分支，而不是 `main`。

为什么需要分支：个人修改先留在独立工作线上，经过 PR 评审后再进入公共 `main`，不会直接影响其他成员。

## 第 7 步：从模板创建正确文件

学习记录最终路径应为：

```text
learning-records/yczx_code/<github-id>/week-02.md
```

在 PowerShell 中运行：

```powershell
$githubId = "your-github-id"
$recordDir = "learning-records/yczx_code/$githubId"
New-Item -ItemType Directory -Force -Path $recordDir
Copy-Item "docs/templates/learning-record.md" "$recordDir/week-02.md"
code "$recordDir/week-02.md"
```

`Copy-Item` 可以简写为 `cp`。下面两条含义相同，选择一条执行，不要重复执行：

```powershell
Copy-Item "docs/templates/learning-record.md" "$recordDir/week-02.md"
cp "docs/templates/learning-record.md" "$recordDir/week-02.md"
```

`cp` 在 PowerShell 中是 `Copy-Item` 的别名；在 Linux 或 Git Bash 中，`cp` 是独立命令。团队教程优先写完整的 `Copy-Item`，减少不同终端造成的误解。

创建练习目录的方式类似：

```powershell
$exerciseDir = "exercises/yczx_code/$githubId/week-02"
New-Item -ItemType Directory -Force -Path $exerciseDir
Copy-Item "examples/yczx_code/03_agent_loop.py" "$exerciseDir/03_agent_loop.py"
code "$exerciseDir/03_agent_loop.py"
```

只修改自己的 GitHub 用户名目录，不覆盖其他成员文件和公共模板。

## 第 8 步：查看修改并运行检查

```powershell
git status --short --branch
git diff
uv sync
uv run ruff check .
```

新复制的文件在 `git diff` 中可能暂时不显示，因为它还未被 Git 跟踪，但 `git status` 会以 `??` 标出。

检查文件路径、内容和运行结果，确认没有 `.env`、API Key、数据库、私人文件或无关修改。

## 第 9 步：暂存并提交

只添加本任务文件，不要习惯性使用 `git add .`：

```powershell
$githubId = "your-github-id"
$record = "learning-records/yczx_code/$githubId/week-02.md"
git add $record
git status --short
git diff --cached
git diff --cached --check
git commit -m "docs: add week 02 learning record"
```

说明：

- `git add` 把选定变化放入本次提交候选区。
- `git diff --cached` 显示即将提交的内容。
- `git commit` 在本地创建版本记录，还没有上传 GitHub。

确认本地 commit：

```powershell
git log --oneline --decorate -3
git status --short --branch
```

## 第 10 步：推送个人分支

```powershell
$branch = git branch --show-current
git push -u origin $branch
```

首次推送可能打开浏览器要求登录 GitHub。使用自己的账号完成认证，不输入或发送账号密码、Token 和验证码。

成功时会看到类似：

```text
[new branch] week-02/your-github-id/learning-record
branch '...' set up to track 'origin/...'
```

如果出现 403 或权限错误，检查是否接受协作者邀请、是否登录正确账号，以及推送的是不是个人分支。不要改成向 `main` 强推。

## 第 11 步：创建 Pull Request

1. 打开 <https://github.com/yanchuaner/yczx_code_lab>。
2. GitHub 通常会显示 `Compare & pull request`，点击它。
3. 确认目标分支 `base` 是 `main`，来源分支 `compare` 是自己的任务分支。
4. 标题写清类型和结果，例如 `docs: add week 02 learning record`。
5. 按 PR 模板填写修改内容、验证命令、结果和未完成项。
6. 创建 PR，等待评审，不要自行直接合并。

PR 是“请求把个人分支合并进 main”，不是单纯上传文件。维护者可以逐行评论、要求修改，并在确认后合并。

## 第 12 步：处理评审意见

不需要新建 PR。在原分支继续修改、提交和推送：

```powershell
git branch --show-current
git status --short
git add "需要修改的文件路径"
git commit -m "docs: address review feedback"
git push
```

原 PR 会自动包含新的 commit。修改完成后在 PR 中回复评审者。

## 第 13 步：合并后同步

PR 由维护者合并后：

```powershell
$oldBranch = git branch --show-current
git switch main
git pull --ff-only
git branch -d $oldBranch
git status --short --branch
```

下一项任务重新从最新 `main` 创建新分支，不要长期复用旧分支。

## 附录：维护者如何从本地空目录初始化新仓库

普通成员不执行本节。只有创建全新仓库、且 GitHub 远程仓库为空时才需要：

```powershell
New-Item -ItemType Directory -Path "new-project"
Set-Location "new-project"
git init -b main
git remote add origin https://github.com/OWNER/REPOSITORY.git
git remote -v
"# New Project" | Set-Content README.md -Encoding utf8
git add README.md
git commit -m "chore: initialize repository"
git push -u origin main
```

如果远程仓库已经有 README、许可证或其他 commit，应直接 `git clone`，不要另建本地历史后强行推送。

遇到错误请阅读 [`troubleshooting.md`](./troubleshooting.md)，并提供完整命令、完整错误、当前分支和 `git status --short --branch` 输出。

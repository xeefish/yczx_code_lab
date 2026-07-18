# Git 与 GitHub 核心概念

## 先认识这些名词

| 名词 | 含义 |
| --- | --- |
| Git | 在本地记录文件版本、分支和合并历史的工具 |
| GitHub | 托管远程 Git 仓库并提供 Issue、PR 和权限管理的平台 |
| repository / repo | 一个由 Git 管理的项目目录，也称仓库 |
| working tree | 当前电脑中实际看到和修改的文件 |
| commit | 一次有说明、可追踪的版本记录 |
| branch | 从某个版本分出的独立工作线 |
| `main` | 仓库的默认稳定分支 |
| remote | 本地仓库记录的远程仓库地址 |
| `origin` | `git clone` 默认给远程仓库起的本地简称 |
| push | 把本地 commit 上传到远程仓库 |
| pull | 获取远程变化并整合到当前分支 |
| Pull Request / PR | 请求将一个分支的变化评审并合并到另一个分支 |

## `origin` 到底是什么

`origin` 不是 GitHub 账号，也不是固定网站。它只是本地仓库中一个远程地址的名字。

运行：

```powershell
git remote -v
git remote get-url origin
```

可能看到：

```text
origin  https://github.com/yanchuaner/yczx_code_lab.git (fetch)
origin  https://github.com/yanchuaner/yczx_code_lab.git (push)
```

因此 `git push origin my-branch` 的意思是：把本地 `my-branch` 推送到名为 `origin` 的远程仓库。

## `clone` 和 `init` 不要混用

加入现有项目时使用：

```powershell
git clone https://github.com/yanchuaner/yczx_code_lab.git
```

`git clone` 已经完成三件事：下载文件、初始化本地 Git 仓库、配置 `origin`。进入克隆目录后不要再次运行 `git init`。

只有从一个普通本地目录创建全新仓库时才使用 `git init`。这通常由仓库维护者完成，普通成员不需要重复初始化。

## 为什么要切换分支

`main` 用于保存已经评审和合并的公共版本。每个任务创建个人分支，可以：

- 不影响其他人正在使用的 `main`。
- 让 GitHub 精确比较本次改动。
- 通过 PR 讨论和评审。
- 任务取消时直接放弃分支，不污染稳定历史。

推荐流程：

```text
最新 main -> 创建任务分支 -> 修改和 commit -> push
-> 创建 PR -> 评审和修改 -> 合并到 main -> 本地同步 main
```

## PR 不等于 push

`git push` 只是把个人分支上传到 GitHub。PR 是在 GitHub 上发起的合并请求，它告诉维护者：

- 我改了什么。
- 为什么这样改。
- 怎样验证。
- 希望把哪个分支合并到 `main`。

PR 创建后继续向同一个分支 push，新 commit 会自动出现在原 PR 中，不需要重新创建 PR。

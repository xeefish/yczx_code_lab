# Git 检查与常见问题

## 一次性自检

在仓库目录中运行：

```powershell
git --version
git config --global --get user.name
git config --global --get user.email
git rev-parse --is-inside-work-tree
git branch --show-current
git remote -v
git status --short --branch
git ls-remote --heads origin
```

判断标准：

- `git --version` 能显示版本。
- 用户名和邮箱不是空值。
- `rev-parse` 返回 `true`。
- 当前分支名称符合预期。
- `origin` 指向正确仓库。
- `ls-remote` 能列出远程分支，说明读取连接正常。

`git ls-remote` 成功只证明可以读取远程。是否拥有写权限，要通过推送自己的任务分支验证。

## 推送时要求登录

GitHub 不接受账号密码作为 Git HTTPS 密码。Windows 上通常由 Git Credential Manager 打开浏览器完成登录。请使用自己的 GitHub 账号，并先接受仓库协作者邀请。

如果已经安装 GitHub CLI，可以检查：

```powershell
gh auth status
```

GitHub CLI 不是本仓库必备工具，未安装时不影响通过浏览器登录 Git。

## `Permission denied` 或 403

依次确认：

1. 浏览器登录的是不是正确 GitHub 账号。
2. 是否已经接受仓库邀请。
3. `git remote -v` 是否指向 `yanchuaner/yczx_code_lab`。
4. 推送的是不是个人分支，而不是受保护的 `main`。
5. 将完整命令和错误发给管理员，不要发送 Token。

## `remote origin already exists`

说明仓库已经有名为 `origin` 的远程。先查看：

```powershell
git remote -v
```

地址正确就不需要再次添加。地址错误时，在确认后使用：

```powershell
git remote set-url origin https://github.com/yanchuaner/yczx_code_lab.git
```

## `not a git repository`

说明当前目录不是仓库。运行 `Get-Location` 和 `Get-ChildItem -Force`，确认已经进入克隆后的 `yczx_code_lab` 目录。不要在任意目录直接运行 `git init` 来掩盖路径错误。

## `non-fast-forward` 或分支落后

先保留错误信息，不使用强制推送。运行：

```powershell
git fetch origin
git status --short --branch
git log --oneline --decorate --graph -10
```

初学者把输出发到群里，由维护者判断应该同步、合并还是重新建立任务分支。

## 出现冲突

运行 `git status` 查看冲突文件。不要删除冲突标记后随便选择一边，也不要覆盖其他成员内容。公共文件冲突应由涉及的成员共同确认。

## 不要自行使用

初学阶段不要在不理解后果时运行：

```text
git reset --hard
git clean -fd
git push --force
git checkout -- <file>
```

这些命令可能删除本地修改或覆盖远程历史。需要使用时先说明当前状态并让维护者确认。

# Windows 环境配置

适用 Windows 10/11 64 位。目标是让新成员可以阅读教程、编写 Python、运行练习并提交 PR。

## 先安装什么

必装：Git、Python 3.12、VS Code、uv。

暂时不装：Docker、PostgreSQL、Anaconda、PyCharm。AI 底座真正开始集成时，再按对应项目文档安装 Docker。

## 推荐安装：winget

打开 PowerShell，逐条执行：

```powershell
winget install -e --id Git.Git
winget install -e --id Python.Python.3.12
winget install -e --id Microsoft.VisualStudioCode
winget install -e --id astral-sh.uv
```

安装完成后关闭并重新打开 PowerShell。

## 图形安装入口

- Git：<https://git-scm.com/downloads/win>
- Python 3.12：<https://www.python.org/downloads/release/python-31210/>，选择 Windows installer (64-bit)，安装时勾选 `Add python.exe to PATH`。
- VS Code：<https://code.visualstudio.com/Download>
- uv：<https://docs.astral.sh/uv/getting-started/installation/>

## 检查结果

```powershell
git --version
py -3.12 --version
py -3.12 -m pip --version
uv --version
code --version
```

Python 必须显示 `3.12.x`，pip 必须明确对应 Python 3.12。Windows 上不要依赖裸 `python`，项目中优先使用 `uv run python`。

## 配置 VS Code

```powershell
code --install-extension ms-python.python
```

打开项目后按 Ctrl + Shift + P，运行 `Python: Select Interpreter`，选择当前项目 `.venv` 中的 Python。

## 创建第一个练习项目

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\Documents\yczx-study"
Set-Location "$HOME\Documents\yczx-study"
uv init --python 3.12 python-practice
Set-Location python-practice
uv run python --version
code .
```

编辑 `main.py` 后运行：

```powershell
uv run python main.py
```

添加第三方库使用：

```powershell
uv add rich
uv run python main.py
```

团队项目统一使用 `uv add`，不要把依赖只装在自己的全局 Python 中。

## 下载资料

```powershell
Set-Location "$HOME\Documents\yczx-study"
git clone https://github.com/datawhalechina/hello-agents.git
git clone https://github.com/shareAI-lab/learn-claude-code.git
git clone https://github.com/yanchuaner/yczx_code.git
git clone https://github.com/yanchuaner/yczx_code_lab.git
```

## 常见问题

### 命令找不到

关闭并重新打开 PowerShell。仍然失败时，发送完整命令、完整错误和版本检查结果，不要直接删除系统目录或反复安装多个 Python。

### `python` 打开 Microsoft Store 或版本错误

使用 `py -3.12` 或 `uv run python`。

### pip 不可用

使用 `py -3.12 -m pip --version`。项目依赖仍然优先使用 `uv add`。

### GitHub 下载失败

先用浏览器确认仓库网页是否能打开，再提供完整错误、网络环境和已尝试方法。不要直接照抄别人的代理端口。

### 求助时必须提供

系统版本、执行命令、完整错误、已尝试方法、`git --version`、`py -3.12 --version`、`uv --version`，以及浏览器能否打开 GitHub。

不要发送 API Key、访问令牌、`.env`、私人文件或含隐私的截图。

## 下一步

环境检查通过后，按 [`YCZX Code 真实案例教程`](../../projects/yczx_code/tutorials/README.md) 从第一次模型调用开始，再逐步进入 Tool Use 和 Agent Loop。

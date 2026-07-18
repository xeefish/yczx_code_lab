"""案例 04：使用真实模型和只读文件工具完成代码库 ReAct 循环。"""

import os
from pathlib import Path
from typing import Any

import anthropic


DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"
DEFAULT_MODEL = "deepseek-v4-pro"
MAX_STEPS = 6
MAX_FILE_CHARS = 12_000
MAX_LISTED_FILES = 80

WORKSPACE = Path(__file__).resolve().parents[2]
IGNORED_PARTS = {".git", ".venv", "__pycache__", ".ruff_cache"}
SENSITIVE_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}

TOOLS = [
    {
        "name": "list_files",
        "description": "列出工作区指定目录中的文件，默认最多递归两层。",
        "input_schema": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "相对工作区的目录，例如 . 或 docs。",
                }
            },
            "required": ["directory"],
            "additionalProperties": False,
        },
    },
    {
        "name": "read_text_file",
        "description": "读取工作区中的一个非敏感 UTF-8 文本文件。",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "相对工作区的文件路径，例如 README.md。",
                }
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
]


def is_sensitive(path: Path) -> bool:
    """判断路径是否属于默认禁止读取的敏感文件。"""
    name = path.name.lower()
    hidden_env = name.startswith(".env") and name != ".env.example"
    return hidden_env or path.suffix.lower() in SENSITIVE_SUFFIXES


def resolve_workspace_path(relative_path: str) -> Path:
    """解析工作区路径，并拒绝绝对路径、越界和敏感路径。"""
    requested = Path(relative_path)
    if requested.is_absolute():
        raise ValueError("只允许使用相对工作区的路径")

    resolved = (WORKSPACE / requested).resolve()
    if not resolved.is_relative_to(WORKSPACE):
        raise ValueError("拒绝访问工作区之外的路径")
    if any(part in IGNORED_PARTS for part in resolved.parts):
        raise ValueError("拒绝访问 Git、虚拟环境或缓存目录")
    if is_sensitive(resolved):
        raise ValueError("拒绝读取敏感文件")
    return resolved


def list_files(directory: str) -> str:
    """列出目录下最多两层的文件。"""
    base = resolve_workspace_path(directory)
    if not base.is_dir():
        raise ValueError(f"目录不存在：{directory}")

    base_depth = len(base.parts)
    entries: list[str] = []
    for path in sorted(base.rglob("*")):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        if len(path.parts) - base_depth > 2:
            continue
        if path.is_file() and not is_sensitive(path):
            entries.append(path.relative_to(WORKSPACE).as_posix())
        if len(entries) >= MAX_LISTED_FILES:
            entries.append(f"...结果已截断，最多显示 {MAX_LISTED_FILES} 个文件")
            break

    return "\n".join(entries) if entries else "目录中没有可显示的文件"


def read_text_file(path: str) -> str:
    """读取有限长度的 UTF-8 文本，避免一次塞入过多上下文。"""
    target = resolve_workspace_path(path)
    if not target.is_file():
        raise ValueError(f"文件不存在：{path}")
    if target.stat().st_size > MAX_FILE_CHARS * 4:
        raise ValueError("文件过大，不适合作为入门案例上下文")

    try:
        content = target.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("只允许读取 UTF-8 文本文件") from error

    if len(content) > MAX_FILE_CHARS:
        return content[:MAX_FILE_CHARS] + "\n...文件内容已截断"
    return content


def execute_tool(name: str, arguments: dict[str, Any]) -> str:
    """校验参数并分发只读工具。"""
    if name == "list_files":
        directory = arguments.get("directory")
        if not isinstance(directory, str):
            raise ValueError("list_files.directory 必须是字符串")
        return list_files(directory)
    if name == "read_text_file":
        path = arguments.get("path")
        if not isinstance(path, str):
            raise ValueError("read_text_file.path 必须是字符串")
        return read_text_file(path)
    raise ValueError(f"未知工具：{name}")


def create_client() -> anthropic.Anthropic:
    """从环境变量创建模型客户端。"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("没有找到 ANTHROPIC_API_KEY，请先按照教程完成配置。")
    return anthropic.Anthropic(
        api_key=api_key,
        base_url=os.getenv("ANTHROPIC_BASE_URL", DEFAULT_BASE_URL),
    )


def run_agent(task: str) -> None:
    """运行只读 Action-Observation 循环。"""
    client = create_client()
    messages: list[dict[str, Any]] = [{"role": "user", "content": task}]

    for step in range(1, MAX_STEPS + 1):
        print(f"\n=== 第 {step} 步 ===")
        try:
            response = client.messages.create(
                model=os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL),
                max_tokens=1800,
                system=(
                    "你是一个只读代码库助手。必须根据真实工具结果回答，不得猜测文件内容。"
                    "先观察目录，再读取完成任务所需的最少文件。"
                    "不能要求写文件或运行命令。"
                ),
                messages=messages,
                tools=TOOLS,
            )
        except anthropic.APIConnectionError as error:
            raise SystemExit(f"连接模型接口失败：{error}") from error
        except anthropic.APIStatusError as error:
            raise SystemExit(
                f"接口返回错误，状态码：{error.status_code}。请检查 Key、余额和模型名。"
            ) from error
        messages.append({"role": "assistant", "content": response.content})

        tool_calls = [block for block in response.content if block.type == "tool_use"]
        if not tool_calls:
            for block in response.content:
                if block.type == "text":
                    print(f"Final：{block.text}")
            return

        tool_results = []
        for call in tool_calls:
            print(f"Action：{call.name}({call.input})")
            try:
                result = execute_tool(call.name, dict(call.input))
                is_error = False
            except (OSError, TypeError, ValueError) as error:
                result = str(error)
                is_error = True

            preview = result if len(result) <= 500 else result[:500] + "..."
            print(f"Observation：{preview}")
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": call.id,
                    "content": result,
                    "is_error": is_error,
                }
            )

        messages.append({"role": "user", "content": tool_results})

    raise SystemExit(f"达到最大步数 {MAX_STEPS}，只读 Agent 已停止。")


if __name__ == "__main__":
    run_agent("先查看仓库根目录，再阅读 README.md，说明这个仓库的作用和新成员入口。")

"""只读工具及工具注册表。"""

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ToolHandler = Callable[[dict[str, Any]], str]
IGNORED_PARTS = {".git", ".venv", "__pycache__", ".ruff_cache"}
SENSITIVE_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}


def is_sensitive(path: Path) -> bool:
    """判断路径是否属于默认禁止读取的敏感文件。"""
    name = path.name.lower()
    hidden_env = name.startswith(".env") and name != ".env.example"
    return hidden_env or path.suffix.lower() in SENSITIVE_SUFFIXES


@dataclass(frozen=True)
class Tool:
    """一个可注册工具的描述和执行函数。"""

    name: str
    description: str
    input_schema: dict[str, Any]
    handler: ToolHandler

    def definition(self) -> dict[str, Any]:
        """返回可以发送给模型的工具定义。"""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.input_schema,
        }


class ToolRegistry:
    """集中注册、导出和执行工具。"""

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        """注册工具，并拒绝重名覆盖。"""
        if tool.name in self._tools:
            raise ValueError(f"工具已经存在：{tool.name}")
        self._tools[tool.name] = tool

    def definitions(self) -> list[dict[str, Any]]:
        """返回所有模型可见的工具定义。"""
        return [tool.definition() for tool in self._tools.values()]

    def execute(self, name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
        """执行工具，并把异常转换成可回传模型的结果。"""
        tool = self._tools.get(name)
        if tool is None:
            return f"未知工具：{name}", True
        try:
            return tool.handler(arguments), False
        except (OSError, TypeError, ValueError) as error:
            return str(error), True


def build_readonly_registry(workspace: Path) -> ToolRegistry:
    """创建仅能读取指定工作区的工具注册表。"""
    root = workspace.resolve()

    def resolve_path(relative_path: str) -> Path:
        requested = Path(relative_path)
        if requested.is_absolute():
            raise ValueError("只允许相对工作区路径")
        target = (root / requested).resolve()
        if not target.is_relative_to(root):
            raise ValueError("拒绝访问工作区之外的路径")
        if any(part in IGNORED_PARTS for part in target.parts):
            raise ValueError("拒绝访问 Git、虚拟环境或缓存目录")
        if is_sensitive(target):
            raise ValueError("拒绝读取敏感文件")
        return target

    def list_files(arguments: dict[str, Any]) -> str:
        directory = arguments.get("directory", ".")
        if not isinstance(directory, str):
            raise ValueError("directory 必须是字符串")
        base = resolve_path(directory)
        if not base.is_dir():
            raise ValueError(f"目录不存在：{directory}")

        files = []
        for path in sorted(base.iterdir(), key=lambda item: item.name.lower()):
            if path.name in IGNORED_PARTS or is_sensitive(path):
                continue
            suffix = "/" if path.is_dir() else ""
            files.append(path.relative_to(root).as_posix() + suffix)
        return "\n".join(files) if files else "目录为空"

    def read_file(arguments: dict[str, Any]) -> str:
        path = arguments.get("path")
        if not isinstance(path, str) or not path.strip():
            raise ValueError("path 必须是非空字符串")
        target = resolve_path(path)
        if not target.is_file():
            raise ValueError(f"文件不存在：{path}")
        if target.stat().st_size > 48_000:
            raise ValueError("文件过大，本案例拒绝读取")
        try:
            return target.read_text(encoding="utf-8")[:12_000]
        except UnicodeDecodeError as error:
            raise ValueError("只允许读取 UTF-8 文本文件") from error

    registry = ToolRegistry()
    registry.register(
        Tool(
            name="list_files",
            description="列出工作区指定目录的直接子项。",
            input_schema={
                "type": "object",
                "properties": {"directory": {"type": "string"}},
                "required": ["directory"],
                "additionalProperties": False,
            },
            handler=list_files,
        )
    )
    registry.register(
        Tool(
            name="read_file",
            description="读取工作区中的一个非敏感 UTF-8 文本文件。",
            input_schema={
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
                "additionalProperties": False,
            },
            handler=read_file,
        )
    )
    return registry

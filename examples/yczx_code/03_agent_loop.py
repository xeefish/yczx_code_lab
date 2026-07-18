"""案例 03：真实模型、多个本地工具和完整 Agent Loop。"""

import ast
import operator
import os
from collections.abc import Callable
from datetime import datetime
from typing import Any

import anthropic


DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"
DEFAULT_MODEL = "deepseek-v4-pro"
MAX_STEPS = 5

OPERATORS: dict[type[ast.operator], Callable[[float, float], float]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

TOOLS = [
    {
        "name": "calculate",
        "description": "安全计算只包含数字、括号和加减乘除的算术表达式。",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
            "additionalProperties": False,
        },
    },
    {
        "name": "get_current_time",
        "description": "读取运行程序这台电脑的当前本地时间。",
        "input_schema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
]


def evaluate_node(node: ast.expr) -> float:
    """递归计算白名单内的算术节点。"""
    if isinstance(node, ast.Constant) and type(node.value) in {int, float}:
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        operation = OPERATORS[type(node.op)]
        return operation(evaluate_node(node.left), evaluate_node(node.right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = evaluate_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    raise ValueError("表达式包含不允许的内容")


def calculate(expression: str) -> str:
    """执行安全算术计算。"""
    try:
        result = evaluate_node(ast.parse(expression, mode="eval").body)
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as error:
        raise ValueError(f"计算失败：{error}") from error
    return str(int(result)) if result.is_integer() else str(result)


def execute_tool(name: str, arguments: dict[str, Any]) -> str:
    """根据名称分发工具，并校验关键参数。"""
    if name == "calculate":
        expression = arguments.get("expression")
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError("calculate.expression 必须是非空字符串")
        return calculate(expression)
    if name == "get_current_time":
        return datetime.now().astimezone().isoformat(timespec="seconds")
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


def print_text_blocks(content: list[Any]) -> None:
    """打印响应中的自然语言文本。"""
    for block in content:
        if block.type == "text" and block.text.strip():
            print(block.text)


def run_agent(task: str) -> None:
    """运行有步数限制的 Agent Loop。"""
    client = create_client()
    model = os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL)
    messages: list[dict[str, Any]] = [{"role": "user", "content": task}]

    for step in range(1, MAX_STEPS + 1):
        print(f"\n=== 第 {step} 轮：请求模型 ===")
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1500,
                system=(
                    "你是一个会使用工具的助手。需要计算或读取当前时间时必须调用工具。"
                    "获得工具结果后，用简洁中文回答用户。"
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
        print_text_blocks(response.content)

        tool_calls = [block for block in response.content if block.type == "tool_use"]
        if not tool_calls:
            print("\nAgent 没有继续请求工具，循环结束。")
            return

        tool_results = []
        for call in tool_calls:
            print(f"Action：{call.name}({call.input})")
            try:
                result = execute_tool(call.name, dict(call.input))
                is_error = False
            except (TypeError, ValueError) as error:
                result = str(error)
                is_error = True
            print(f"Observation：{result}")
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": call.id,
                    "content": result,
                    "is_error": is_error,
                }
            )

        messages.append({"role": "user", "content": tool_results})

    raise SystemExit(f"达到最大步数 {MAX_STEPS}，Agent 已停止。")


if __name__ == "__main__":
    run_agent("请计算 (23 + 19) * 7，并告诉我当前本地时间。")

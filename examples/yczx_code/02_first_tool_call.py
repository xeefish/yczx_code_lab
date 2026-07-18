"""案例 02：让真实模型请求一次计算器工具，并在本地执行。"""

import ast
import operator
import os
from collections.abc import Callable

import anthropic


DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"
DEFAULT_MODEL = "deepseek-v4-pro"

OPERATORS: dict[type[ast.operator], Callable[[float, float], float]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

CALCULATOR_TOOL = {
    "name": "calculate",
    "description": "安全计算只包含数字、括号和加减乘除的算术表达式。",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "需要计算的表达式，例如 (23 + 19) * 7。",
            }
        },
        "required": ["expression"],
        "additionalProperties": False,
    },
}


def evaluate_node(node: ast.expr) -> float:
    """递归计算经过白名单限制的抽象语法树节点。"""
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
    """安全计算表达式，不使用 eval。"""
    try:
        parsed = ast.parse(expression, mode="eval")
        result = evaluate_node(parsed.body)
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as error:
        return f"计算失败：{error}"
    return str(int(result)) if result.is_integer() else str(result)


def create_client() -> anthropic.Anthropic:
    """从环境变量创建模型客户端。"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("没有找到 ANTHROPIC_API_KEY，请先按照教程完成配置。")
    return anthropic.Anthropic(
        api_key=api_key,
        base_url=os.getenv("ANTHROPIC_BASE_URL", DEFAULT_BASE_URL),
    )


def main() -> None:
    """请求模型选择计算器，并显示本地执行结果。"""
    try:
        response = create_client().messages.create(
            model=os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL),
            max_tokens=1000,
            system="遇到算术问题时必须使用 calculate 工具，不要自行心算。",
            messages=[{"role": "user", "content": "请计算 (23 + 19) * 7。"}],
            tools=[CALCULATOR_TOOL],
            tool_choice={"type": "any"},
        )
    except anthropic.APIConnectionError as error:
        raise SystemExit(f"连接模型接口失败：{error}") from error
    except anthropic.APIStatusError as error:
        raise SystemExit(
            f"接口返回错误，状态码：{error.status_code}。请检查 Key、余额和模型名。"
        ) from error

    tool_used = False
    for block in response.content:
        if block.type != "tool_use":
            continue

        tool_used = True
        print(f"模型请求工具：{block.name}")
        print(f"工具参数：{block.input}")
        if block.name == "calculate":
            expression = str(block.input.get("expression", ""))
            print(f"本地执行结果：{calculate(expression)}")

    if not tool_used:
        raise SystemExit("模型没有请求工具，请检查模型兼容性和 tool_choice 配置。")

    print("\n本案例到此停止：工具结果还没有返回模型，因此还不是完整 Agent Loop。")


if __name__ == "__main__":
    main()

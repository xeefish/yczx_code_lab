"""模块化 Agent Loop。"""

from typing import Any

from provider import AnthropicProvider
from tools import ToolRegistry


class Agent:
    """组合 Provider 和工具注册表的最小只读 Agent。"""

    def __init__(
        self,
        provider: AnthropicProvider,
        tools: ToolRegistry,
        *,
        system_prompt: str,
        max_steps: int,
    ) -> None:
        self.provider = provider
        self.tools = tools
        self.system_prompt = system_prompt
        self.max_steps = max_steps

    def run(self, task: str) -> str:
        """循环请求模型、执行工具并回传观察结果。"""
        messages: list[dict[str, Any]] = [{"role": "user", "content": task}]

        for step in range(1, self.max_steps + 1):
            print(f"\n=== Agent 第 {step} 步 ===")
            response = self.provider.create_message(
                system=self.system_prompt,
                messages=messages,
                tools=self.tools.definitions(),
            )
            messages.append({"role": "assistant", "content": response.content})

            tool_calls = [
                block for block in response.content if block.type == "tool_use"
            ]
            if not tool_calls:
                final_text = "\n".join(
                    block.text for block in response.content if block.type == "text"
                )
                return final_text or "模型没有返回文本结果"

            tool_results = []
            for call in tool_calls:
                print(f"Action：{call.name}({call.input})")
                result, is_error = self.tools.execute(call.name, dict(call.input))
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

        raise RuntimeError(f"达到最大步数 {self.max_steps}，Agent 已停止")

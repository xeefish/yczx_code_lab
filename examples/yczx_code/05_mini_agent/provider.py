"""模型 Provider 边界。"""

from typing import Any

import anthropic

from config import Settings


class AnthropicProvider:
    """封装 Anthropic 兼容 Messages API。"""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = anthropic.Anthropic(
            api_key=settings.api_key,
            base_url=settings.base_url,
        )

    def create_message(
        self,
        *,
        system: str,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]],
    ) -> Any:
        """发送一次模型请求。"""
        try:
            return self.client.messages.create(
                model=self.settings.model,
                max_tokens=1800,
                system=system,
                messages=messages,
                tools=tools,
            )
        except anthropic.APIConnectionError as error:
            raise RuntimeError(f"连接模型接口失败：{error}") from error
        except anthropic.APIStatusError as error:
            raise RuntimeError(
                f"接口返回错误，状态码：{error.status_code}。请检查 Key、余额和模型名。"
            ) from error

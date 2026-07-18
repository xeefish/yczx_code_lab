"""案例 01：通过 Anthropic SDK 完成一次真实模型对话。"""

import os

import anthropic


DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"
DEFAULT_MODEL = "deepseek-v4-pro"


def get_required_api_key() -> str:
    """读取 API Key，并在未配置时给出明确提示。"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "没有找到 ANTHROPIC_API_KEY。请先按照教程在当前终端设置环境变量。"
        )
    return api_key


def main() -> None:
    """发送一条消息，并打印模型返回的文本。"""
    client = anthropic.Anthropic(
        api_key=get_required_api_key(),
        base_url=os.getenv("ANTHROPIC_BASE_URL", DEFAULT_BASE_URL),
    )

    try:
        message = client.messages.create(
            model=os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL),
            max_tokens=1000,
            system="You are a helpful assistant.",
            messages=[
                {
                    "role": "user",
                    "content": "你好！请用两句话介绍什么是 AI Agent。",
                }
            ],
        )
    except anthropic.APIConnectionError as error:
        raise SystemExit(f"连接模型接口失败：{error}") from error
    except anthropic.APIStatusError as error:
        raise SystemExit(
            f"接口返回错误，状态码：{error.status_code}。请检查 Key、余额和模型名。"
        ) from error

    print(f"模型：{message.model}")
    print("回答：")
    for block in message.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()

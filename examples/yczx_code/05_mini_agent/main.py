"""组装并运行模块化 Mini Agent。"""

from pathlib import Path

from agent import Agent
from config import Settings
from provider import AnthropicProvider
from tools import build_readonly_registry


def main() -> None:
    """创建各模块并执行一次真实代码库任务。"""
    workspace = Path(__file__).resolve().parents[3]
    settings = Settings.from_env()
    agent = Agent(
        provider=AnthropicProvider(settings),
        tools=build_readonly_registry(workspace),
        system_prompt=(
            "你是一个只读代码库助手。先使用工具获取真实信息，再用简洁中文回答。"
            "不得猜测文件内容，也不得要求写文件或执行 Shell。"
        ),
        max_steps=settings.max_steps,
    )

    try:
        answer = agent.run(
            "查看仓库根目录并阅读 README.md，总结新成员从环境配置到第一次 PR 的路径。"
        )
    except RuntimeError as error:
        raise SystemExit(str(error)) from error
    print(f"\nFinal：{answer}")


if __name__ == "__main__":
    main()

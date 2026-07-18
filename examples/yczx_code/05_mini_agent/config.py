"""模型和 Agent 运行配置。"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """从环境变量加载的不可变配置。"""

    api_key: str
    base_url: str
    model: str
    max_steps: int = 6

    @classmethod
    def from_env(cls) -> "Settings":
        """读取配置，并在缺少 Key 时立即停止。"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise SystemExit("没有找到 ANTHROPIC_API_KEY，请先按照教程完成配置。")

        return cls(
            api_key=api_key,
            base_url=os.getenv(
                "ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic"
            ),
            model=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro"),
        )

"""
タグ生成プロンプト
"""

from __future__ import annotations

from ai.prompts.base_prompt import BasePrompt
from ai.tasks import AITask


class TagPrompt(BasePrompt):
    """タグ生成プロンプト"""

    TASK = AITask.TAG

    def build(self, text: str) -> str:
        raise NotImplementedError(
            "Tag analysis is not implemented."
        )

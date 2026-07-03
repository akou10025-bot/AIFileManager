"""
キーワード抽出プロンプト
"""

from __future__ import annotations

from ai.prompts.base_prompt import BasePrompt
from ai.tasks import AITask


class KeywordPrompt(BasePrompt):
    """キーワード抽出プロンプト"""

    TASK = AITask.KEYWORD

    def build(self, text: str) -> str:
        raise NotImplementedError(
            "Keyword analysis is not implemented."
        )

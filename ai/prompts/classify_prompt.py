"""
分類プロンプト
"""

from __future__ import annotations

from ai.prompts.base_prompt import BasePrompt
from ai.tasks import AITask


class ClassifyPrompt(BasePrompt):
    """分類プロンプト"""

    TASK = AITask.CLASSIFY

    def build(self, text: str) -> str:
        raise NotImplementedError(
            "Classification is not implemented."
        )

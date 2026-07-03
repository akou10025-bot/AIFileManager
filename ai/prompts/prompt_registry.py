"""
Prompt Registry
"""

from __future__ import annotations

from ai.tasks import AITask
from ai.prompts.base_prompt import BasePrompt


class PromptRegistry:

    _registry = {}

    @classmethod
    def register(
        cls,
        prompt: BasePrompt,
    ):

        cls._registry[prompt.TASK] = prompt

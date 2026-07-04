from ai.prompts.base_prompt import BasePrompt
from ai.tasks import AITask


class PromptRegistry:

    _prompts = {}

    @classmethod
    def register(cls, task, prompt):
        cls._prompts[task] = prompt

    @classmethod
    def get(cls, task):
        return cls._prompts[task]

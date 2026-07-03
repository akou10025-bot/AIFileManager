import ai.prompts
from ai.prompts.prompt_registry import PromptRegistry

from ai.tasks import AITask


class PromptBuilder:

    @staticmethod
    def build(
        task: AITask,
        text: str,
    ) -> str:

        prompt = PromptRegistry.get(task)

        return prompt.build(text)

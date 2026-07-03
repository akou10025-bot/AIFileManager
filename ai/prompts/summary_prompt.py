from ai.prompts.base_prompt import BasePrompt
from ai.tasks import AITask

class SummaryPrompt(BasePrompt):

    TASK = AITask.SUMMARY

    def build(
        self,
        text: str,
    ) -> str:

        return f"""
以下の文章を要約してください。

{text}
"""
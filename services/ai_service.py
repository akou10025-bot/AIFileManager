"""
AIサービス

責務:
    - AIとの対話
    - 文書要約
"""

from ai.client import OllamaClient
from ai.prompt_builder import PromptBuilder
from utils.logger import get_logger
from ai.tasks import AITask

logger = get_logger(__name__)


class AIService:
    """AIサービス。"""

    def __init__(self) -> None:
        self._client = OllamaClient()
        self._prompt_builder = PromptBuilder()

    def ask(self, question: str) -> str:
        """
        AIへ質問する。

        Args:
            question: 質問

        Returns:
            AIの回答
        """
        logger.info("Ask AI")

        return self._client.generate(question)
    
    def analyze(
        self,
        document: str,
        task: AITask,
    ) -> str:
        """
        文書をAI解析する。

        Args:
            document:
                文書内容
            task:
                AI解析タスク

        Returns:
            AI解析結果
        """

        prompt = PromptBuilder.build(
            task=task,
            text=document,
        )

        return self._client.generate(prompt)

    def summarize(
        self,
        document: str,
    ) -> str:
        """
        文書要約（Ver1互換API）
        """

        return self.analyze(
            document=document,
            task=AITask.SUMMARY,
        )

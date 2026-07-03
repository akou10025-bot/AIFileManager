"""
AIサービス

責務:
    - AIとの対話
    - 文書要約
"""

from ai.client import OllamaClient
from ai.prompt_builder import PromptBuilder
from utils.logger import get_logger

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

    def summarize(self, document: str) -> str:
        """
        文書を要約する。

        Args:
            document:
                要約対象文書

        Returns:
            AIの要約結果
        """
        logger.info("Summarize document")

        prompt = self._prompt_builder.build_summary_prompt(document)

        return self._client.generate(prompt)

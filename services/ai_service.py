"""
AIサービス
"""

from ai.client import OllamaClient
from ai.prompts import CHAT_PROMPT
from ai.prompts import SYSTEM_PROMPT

from utils.logger import get_logger

logger = get_logger(__name__)


class AIService:

    def __init__(self):

        self.client = OllamaClient()

    def ask(self, question: str) -> str:

        prompt = SYSTEM_PROMPT + "\n\n"

        prompt += CHAT_PROMPT.format(
            question=question
        )

        logger.info("Send Prompt")

        answer = self.client.generate(prompt)

        logger.info("Receive Answer")

        return answer

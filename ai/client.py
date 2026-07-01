"""
Ollamaとの通信クラス
"""

from __future__ import annotations

import requests

from config import MODEL_NAME
from config import OLLAMA_URL


class OllamaClient:
    """
    Ollama API Client
    """

    def __init__(self) -> None:

        self.url = OLLAMA_URL
        self.model = MODEL_NAME

    def generate(self, prompt: str) -> str:

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        response = requests.post(
            self.url,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        body = response.json()

        return body["response"]

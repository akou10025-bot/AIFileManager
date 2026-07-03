from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from ai.tasks import AITask


class BasePrompt(ABC):
    """Promptプラグイン基底クラス"""

    TASK: AITask

    @abstractmethod
    def build(
        self,
        text: str,
    ) -> str:
        ...
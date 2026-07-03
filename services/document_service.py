"""
文書管理サービス

責務:
    - 文書の読込
"""

from __future__ import annotations

from pathlib import Path

from document.reader import DocumentReader
from utils.logger import get_logger

logger = get_logger(__name__)


class DocumentService:
    """文書管理サービス。"""

    def __init__(self) -> None:
        """DocumentReaderを初期化する。"""
        self._reader = DocumentReader()

    def read(self, path: Path) -> str:
        """
        文書を読み込む。

        Args:
            path:
                読み込むファイル

        Returns:
            文書内容

        Raises:
            FileNotFoundError:
                ファイルが存在しない場合

            ValueError:
                未対応ファイルの場合
        """
        logger.info("Read request: %s", path)

        text = self._reader.read(path)

        logger.info("Read completed: %s", path)

        return text

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
    """文書読込サービス。"""

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
        if not path.exists():
            raise FileNotFoundError(path)

        logger.info("Read request: %s", path)

        text = self._reader.read(path)

        logger.info(
            "Read completed: %s (%d characters)",
            path.name,
            len(text),
        )

        return text

    def read_many(self, paths: list[Path]) -> dict[str, str]:
        """
        複数文書を読み込む。

        Args:
            paths:
                読み込むファイル一覧

        Returns:
            {ファイル名: 文書内容}
        """
        documents: dict[str, str] = {}

        for path in paths:
            documents[path.name] = self.read(path)

        return documents

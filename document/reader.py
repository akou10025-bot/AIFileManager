"""
文書読込クラス

責務:
    - 文書ファイルを読み込む
    - ファイル内容を文字列として返却する
"""

from __future__ import annotations

from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)


class DocumentReader:
    """文書読込クラス。"""

    _SUPPORTED_SUFFIXES = {
        ".txt",
        ".md",
    }

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
                未対応の拡張子の場合
        """
        if not path.exists():
            logger.error("File not found: %s", path)
            raise FileNotFoundError(path)

        if not path.is_file():
            logger.error("Not a file: %s", path)
            raise ValueError(f"Not a file: {path}")

        suffix = path.suffix.lower()

        print(path)
        print(path.suffix)

        # if suffix not in self._SUPPORTED_SUFFIXES:
        #     logger.error("Unsupported file type: %s", suffix)
        #     raise ValueError(f"Unsupported file type: {suffix}")

        logger.info("Read document: %s", path)

        return path.read_text(encoding="utf-8")

"""
ファイル管理サービス

責務:
    - アップロードファイルの保存
    - 保存済みファイル一覧の取得
"""

from __future__ import annotations

from pathlib import Path

from config import UPLOAD_DIR
from utils.logger import get_logger

logger = get_logger(__name__)


class FileService:
    """アップロードファイルを管理するサービス。"""

    def __init__(self) -> None:
        """保存先ディレクトリを初期化する。"""
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    def save(
        self,
        filename: str,
        data: bytes,
    ) -> Path:
        """
        ファイルを保存する。

        Args:
            filename: ファイル名
            data: ファイル内容

        Returns:
            保存したPath
        """
        destination = self._create_unique_path(filename)

        try:
            destination.write_bytes(data)

            logger.info("File saved: %s", destination)

            return destination

        except Exception:
            logger.exception("Failed to save file: %s", filename)
            raise

    def list_files(self) -> list[Path]:
        """
        保存済みファイル一覧を取得する。

        Returns:
            Pathオブジェクトのリスト
        """
        files = [path for path in UPLOAD_DIR.iterdir() if path.is_file()]

        return sorted(files, key=lambda p: p.name.lower())

    def get(self, filename: str) -> Path:
        """
        ファイル名から保存済みファイルを取得する。

        Args:
            filename:
                ファイル名

        Returns:
            Path

        Raises:
            FileNotFoundError
        """
        path = UPLOAD_DIR / filename

        if not path.exists():
            raise FileNotFoundError(path)

        return path

    @staticmethod
    def _create_unique_path(filename: str) -> Path:
        """
        重複しない保存先Pathを生成する。

        同名ファイルが存在する場合は

            sample.pdf
            sample(1).pdf
            sample(2).pdf

        のようにリネームする。

        Args:
            filename: 元ファイル名

        Returns:
            保存先Path
        """
        path = UPLOAD_DIR / filename

        if not path.exists():
            return path

        stem = path.stem
        suffix = path.suffix

        index = 1

        while True:
            candidate = UPLOAD_DIR / f"{stem}({index}){suffix}"

            if not candidate.exists():
                return candidate

            index += 1

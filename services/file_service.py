"""
ファイル管理サービス

責務:
    - アップロードファイルの保存
    - 保存済みファイル一覧の取得
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from config import UPLOAD_DIR
from utils.logger import get_logger

logger = get_logger(__name__)


class FileService:
    """アップロードファイルを管理するサービス。"""

    def __init__(self) -> None:
        """保存先ディレクトリを初期化する。"""
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    def save(self, uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> Path:
        """
        アップロードファイルを保存する。

        Args:
            uploaded_file: Streamlitのアップロードファイル

        Returns:
            保存したファイルのPath

        Raises:
            ValueError:
                uploaded_file が None の場合
            OSError:
                ファイル保存に失敗した場合
        """
        if uploaded_file is None:
            raise ValueError("uploaded_file is None.")

        destination = self._create_unique_path(uploaded_file.name)

        try:
            destination.write_bytes(uploaded_file.getbuffer())

            logger.info("File saved: %s", destination)

            return destination

        except Exception:
            logger.exception("Failed to save file: %s", uploaded_file.name)
            raise

    def list_files(self) -> list[Path]:
        """
        保存済みファイル一覧を取得する。

        Returns:
            Pathオブジェクトのリスト
        """
        files = [path for path in UPLOAD_DIR.iterdir() if path.is_file()]

        return sorted(files, key=lambda p: p.name.lower())

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

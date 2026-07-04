"""
文書リポジトリ

責務:
    - 文書の保存
    - 文書一覧取得
    - 文書検索
    - 文書読込
    - 全文読込
    - 文書削除
    - 文書情報取得
"""

from __future__ import annotations

from pathlib import Path

from models.document_info import DocumentInfo
from services.document_service import DocumentService
from services.file_service import FileService


class DocumentRepository:
    """文書管理リポジトリ"""

    def __init__(self) -> None:
        self._file_service = FileService()
        self._document_service = DocumentService()

    def save(
        self,
        filename: str,
        data: bytes,
    ) -> Path:
        """文書を保存する。"""
        return self._file_service.save(filename, data)

    def list_documents(self) -> list[DocumentInfo]:
        """保存済み文書一覧を取得する。"""
        infos: list[DocumentInfo] = []

        for path in self._file_service.list_files():
            infos.append(
                self._file_service.get_file_info(path)
            )

        return infos

    def search(
        self,
        keyword: str,
    ) -> list[DocumentInfo]:
        """
        ファイル名・本文から文書を検索する。

        Args:
            keyword:
                検索文字列

        Returns:
            条件に一致した文書一覧
        """
        keyword = keyword.strip().lower()

        if not keyword:
            return self.list_documents()

        results: list[DocumentInfo] = []

        for path in self._file_service.list_files():

            info = self._file_service.get_file_info(path)

            #
            # ファイル名検索
            #
            if keyword in info.name.lower():
                results.append(info)
                continue

            #
            # 本文検索
            #
            try:
                document = self._document_service.read(path)

                if keyword in document.lower():
                    results.append(info)

            except Exception:
                #
                # 読めないファイルは無視
                #
                continue

        return results

    def read(
        self,
        filename: str,
    ) -> str:
        """文書を読み込む。"""
        path = self._file_service.get(filename)
        return self._document_service.read(path)

    def read_all(self) -> str:
        """
        保存済み文書をすべて読み込む。

        Returns:
            AIへ渡せる1つの文字列
        """
        documents: list[str] = []

        for path in self._file_service.list_files():
            text = self._document_service.read(path)

            documents.append(
                f"### {path.name}\n\n{text}"
            )

        return "\n\n".join(documents)

    def delete(
        self,
        filename: str,
    ) -> None:
        """文書を削除する。"""
        self._file_service.delete(filename)

    def get_info(
        self,
        filename: str,
    ) -> DocumentInfo:
        """文書情報を取得する。"""
        path = self._file_service.get(filename)
        return self._file_service.get_file_info(path)

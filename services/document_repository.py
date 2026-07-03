"""
文書リポジトリ

責務:
    - 文書の保存
    - 文書一覧取得
    - 文書読込
    - 文書削除
    - 文書情報取得
"""

from pathlib import Path

from models.document_info import DocumentInfo
from services.document_service import DocumentService
from services.file_service import FileService


class DocumentRepository:
    """文書管理リポジトリ"""

    def __init__(self) -> None:
        self._file_service = FileService()
        self._document_service = DocumentService()

    def save(self, filename: str, data: bytes) -> Path:
        return self._file_service.save(filename, data)

    def list_documents(self) -> list[Path]:
        return self._file_service.list_files()

    def read(self, filename: str) -> str:
        path = self._file_service.get(filename)
        return self._document_service.read(path)

    def delete(self, filename: str) -> None:
        self._file_service.delete(filename)

    def get_info(self, filename: str) -> DocumentInfo:
        path = self._file_service.get(filename)
        return self._file_service.get_file_info(path)

    def get_path(self, filename: str) -> Path:
        return self._file_service.get(filename)

"""
Repository全体に対するAI分析サービス
"""

from analysis.analysis_plan import AnalysisPlan
from services.document_repository import DocumentRepository
from services.ai_service import AIService


class RepositoryAnalysisService:
    """Repository全体を分析するサービス"""

    def __init__(self) -> None:
        self._ai_service = AIService()

    def execute(
        self,
        repository: DocumentRepository,
        plan: AnalysisPlan,
    ) -> str:
        """
        Repository全体を分析する。
        """

        document = repository.read_all()

        return self._ai_service.ask(
            f"{plan.instruction}\n\n{document}"
        )

from analysis.analysis_plan import AnalysisPlan
from analysis.analysis_type import AnalysisType


class AnalysisPlanner:

    def create_plan(
        self,
        instruction: str,
    ) -> AnalysisPlan:

        text = instruction.lower()

        if "合計" in text:
            analysis_type = AnalysisType.AGGREGATE

        elif "抽出" in text:
            analysis_type = AnalysisType.EXTRACT

        elif "比較" in text:
            analysis_type = AnalysisType.COMPARE

        elif "検索" in text:
            analysis_type = AnalysisType.SEARCH

        elif "要約" in text:
            analysis_type = AnalysisType.SUMMARY

        else:
            analysis_type = AnalysisType.QUESTION

        return AnalysisPlan(
            analysis_type=analysis_type,
            instruction=instruction,
        )

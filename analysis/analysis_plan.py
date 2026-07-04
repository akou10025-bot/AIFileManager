from dataclasses import dataclass

from analysis.analysis_type import AnalysisType


@dataclass(slots=True)
class AnalysisPlan:

    analysis_type: AnalysisType

    instruction: str

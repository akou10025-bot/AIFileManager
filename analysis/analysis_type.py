from enum import Enum


class AnalysisType(str, Enum):

    SUMMARY = "summary"

    EXTRACT = "extract"

    AGGREGATE = "aggregate"

    SEARCH = "search"

    COMPARE = "compare"

    QUESTION = "question"

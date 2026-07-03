"""
AI解析タスク定義
"""

from __future__ import annotations

from enum import StrEnum


class AITask(StrEnum):
    """AI解析タスク"""

    SUMMARY = "summary"
    KEYWORD = "keyword"
    TAG = "tag"
    CLASSIFY = "classify"

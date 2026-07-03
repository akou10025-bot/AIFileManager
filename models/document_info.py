"""
Document Repository内の文書情報
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class DocumentInfo:
    """Repository内の文書情報"""

    path: Path
    name: str
    size: int
    updated_at: datetime
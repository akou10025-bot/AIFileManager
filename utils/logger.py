"""
共通ロガー
"""

import logging

from config import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("AIFileManager")

logger.setLevel(logging.INFO)

handler = logging.FileHandler(
    LOG_DIR / "application.log",
    encoding="utf-8",
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

"""
共通ロガー
"""

from __future__ import annotations

import logging

from config import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """
    Loggerを取得する。

    Args:
        name: Logger名（通常は __name__）

    Returns:
        Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(
        LOG_DIR / "application.log",
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

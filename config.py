"""
AI Document Manager
共通設定
"""

from pathlib import Path

# ----------------------------------------------------------------------
# Application
# ----------------------------------------------------------------------

APP_NAME = "AI Document Manager"

APP_VERSION = "0.2.0"

# ----------------------------------------------------------------------
# Ollama
# ----------------------------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "gemma3:4b"

# ----------------------------------------------------------------------
# Directory
# ----------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

UPLOAD_DIR = BASE_DIR / "uploads"

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

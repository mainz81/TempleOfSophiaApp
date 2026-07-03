import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")

TEMPLE_DB = Path(os.getenv("TEMPLE_DB", "data/temple.db"))
TEMPLE_VAULT = Path(os.getenv("TEMPLE_VAULT", "data/vault"))
TEMPLE_ARCHIVE = Path(os.getenv("TEMPLE_ARCHIVE", "data/archive"))
TEMPLE_EXPORTS = Path(os.getenv("TEMPLE_EXPORTS", "data/exports"))

SYSTEM_PROMPT_PATH = BASE_DIR / "sophia_core" / "system_prompt.txt"
WRITING_MODES_PATH = BASE_DIR / "sophia_core" / "writing_modes.json"

def ensure_directories():
    TEMPLE_DB.parent.mkdir(parents=True, exist_ok=True)
    TEMPLE_VAULT.mkdir(parents=True, exist_ok=True)
    TEMPLE_ARCHIVE.mkdir(parents=True, exist_ok=True)
    TEMPLE_EXPORTS.mkdir(parents=True, exist_ok=True)

def load_system_prompt() -> str:
    if SYSTEM_PROMPT_PATH.exists():
        return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    return "You are Sophia, a private writing assistant."

def get_model() -> str:
    return OPENAI_MODEL

def has_api_key() -> bool:
    return bool(OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here")
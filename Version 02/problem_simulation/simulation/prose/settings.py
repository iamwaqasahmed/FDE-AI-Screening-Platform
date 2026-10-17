"""LLM endpoint settings. Environment first, then a .env file (problem_simulation, Version 02, Version 01). Keys are never logged."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_FILES = (ROOT / ".env", ROOT.parent / ".env", ROOT.parent.parent / "Version 01" / ".env")


@dataclass(frozen=True)
class Settings:
    url: str
    key: str
    model: str


def _env_file() -> dict[str, str]:
    path = Path(os.environ["HARTLAND_ENV_FILE"]) if os.environ.get("HARTLAND_ENV_FILE") else None
    for candidate in ([path] if path else []) + list(ENV_FILES):
        if candidate and candidate.exists():
            pairs = {}
            for line in candidate.read_text(encoding="utf-8-sig").splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    name, value = line.split("=", 1)
                    pairs[name.strip()] = value.strip().strip('"').strip("'")
            return pairs
    return {}


def _first(names: tuple[str, ...], fallback: dict[str, str], default: str = "") -> str:
    for name in names:
        if os.environ.get(name):
            return os.environ[name]
    for name in names:
        if fallback.get(name):
            return fallback[name]
    return default


def settings() -> Settings:
    file = _env_file()
    return Settings(
        url=_first(("HARTLAND_LLM_URL", "OPENAI_BASE_URL"), file, "https://api.openai.com/v1").rstrip("/"),
        key=_first(("HARTLAND_LLM_KEY", "OPENAI_API_KEY"), file),
        model=_first(("HARTLAND_LLM_MODEL", "OPENAI_MODEL"), file, "gpt-4o-mini"),
    )

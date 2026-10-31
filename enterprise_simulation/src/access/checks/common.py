"""Shared artifact loading. Miss text from the checkers stays out of this module."""

from __future__ import annotations

import json
from pathlib import Path


def require_prediction(path: Path) -> list[str]:
    """Refuse to grade until a non-empty prediction sits beside the artifact."""
    prediction = path.parent / "prediction.txt"
    if not prediction.is_file() or not prediction.read_text(encoding="utf-8").strip():
        return ["a prediction file is missing"]
    return []


def load_object(path: Path) -> tuple[dict | None, list[str]]:
    if not path.is_file():
        return None, ["the artifact file is missing"]
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None, ["the artifact file is not JSON"]
    if not isinstance(raw, dict):
        return None, ["the artifact file is not an object"]
    return raw, []


def contains_key(value: object, key: str) -> bool:
    if isinstance(value, dict):
        if key in value:
            return True
        return any(contains_key(item, key) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False

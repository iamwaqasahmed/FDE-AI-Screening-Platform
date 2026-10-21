"""The team's findings file. A missing file is an empty answer, not an error."""

from __future__ import annotations

import json
from pathlib import Path


def load(work: Path) -> dict:
    path = work / "findings.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    items = payload.get("items", payload)
    return items if isinstance(items, dict) else {}

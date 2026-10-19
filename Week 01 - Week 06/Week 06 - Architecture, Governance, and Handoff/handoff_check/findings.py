"""Load one team's findings.json. A missing file scores as no items."""

from __future__ import annotations

import json
from pathlib import Path


def load(work: Path) -> dict:
    path = work / "findings.json"
    if not path.exists():
        return {}
    loaded = json.loads(path.read_text(encoding="utf-8"))
    items = loaded.get("items", loaded) if isinstance(loaded, dict) else {}
    return items if isinstance(items, dict) else {}

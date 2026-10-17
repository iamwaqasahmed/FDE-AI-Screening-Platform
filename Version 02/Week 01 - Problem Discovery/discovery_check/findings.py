"""Read findings.json. A missing file is an empty set of answers, not a crash."""

from __future__ import annotations

import json
from pathlib import Path


def load(work: Path) -> dict:
    path = work / "findings.json"
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    items = raw.get("items", raw) if isinstance(raw, dict) else {}
    return items if isinstance(items, dict) else {}

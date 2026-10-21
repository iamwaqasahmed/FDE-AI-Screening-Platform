"""Load the seed's Week 6 gold. The folder is closed to participants."""

from __future__ import annotations

import json
from pathlib import Path


def load(data: Path) -> dict:
    return json.loads((data / "truth" / "gold" / "handoff.json").read_text(encoding="utf-8"))

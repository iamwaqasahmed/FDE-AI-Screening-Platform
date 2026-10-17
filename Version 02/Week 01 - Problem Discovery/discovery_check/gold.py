"""Load the closed Week 1 gold for one built data folder."""

from __future__ import annotations

import json
from pathlib import Path


def load(data: Path) -> dict:
    path = data / "truth" / "gold" / "discovery.json"
    if not path.exists():
        raise SystemExit(f"No discovery gold at {path}. Rebuild that profile from problem_simulation.")
    return json.loads(path.read_text(encoding="utf-8"))


def personas(data: Path) -> dict:
    path = data / "truth" / "stakeholders" / "personas.json"
    if not path.exists():
        raise SystemExit(f"No persona truth at {path}.")
    return json.loads(path.read_text(encoding="utf-8"))["personas"]

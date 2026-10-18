"""Puts Version 02 module code and the simulation on the import path."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIRS = ("Week 01 - Problem Discovery", "Week 02 - Enterprise Data", "Week 03 - Retrieval and ML Evidence")
SIMULATION = "problem_simulation"


def install() -> None:
    entries = [str(ROOT / SIMULATION), *(str(ROOT / name) for name in MODULE_DIRS)]
    for entry in reversed(entries):
        if entry not in sys.path:
            sys.path.insert(0, entry)

"""Puts the week folders and the simulation on the import path."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _entry in (_ROOT, _ROOT / "problem_simulation", _ROOT / "Week 02 - Enterprise Data", _ROOT / "Week 03 - Retrieval and ML Evidence"):
    if str(_entry) not in sys.path:
        sys.path.insert(0, str(_entry))

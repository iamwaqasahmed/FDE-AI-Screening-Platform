"""Make the week package importable when pytest is run from Version 02."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEEK = Path(__file__).resolve().parents[1]
for entry in (ROOT, ROOT / "problem_simulation", WEEK):
    if str(entry) not in sys.path:
        sys.path.insert(0, str(entry))

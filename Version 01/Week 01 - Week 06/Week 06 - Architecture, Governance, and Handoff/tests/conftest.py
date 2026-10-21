"""Make the week package importable when pytest is run from Week 01 - Week 06."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEEK = Path(__file__).resolve().parents[1]
WEEKS = (
    ROOT / "Week 02 - Enterprise Data",
    ROOT / "Week 03 - Retrieval and ML Evidence",
    ROOT / "Week 04 - Graph Retrieval and Integration",
    ROOT / "Week 05 - The Agent and the Re-plan",
    WEEK,
)
for entry in (ROOT, ROOT / "problem_simulation", *WEEKS):
    if str(entry) not in sys.path:
        sys.path.insert(0, str(entry))

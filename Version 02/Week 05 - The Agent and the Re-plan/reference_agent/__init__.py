"""The maintainer solution for Week 5. It reads the drop, not the hidden model."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEEKS = (
    "Week 02 - Enterprise Data",
    "Week 03 - Retrieval and ML Evidence",
    "Week 04 - Graph Retrieval and Integration",
    "Week 05 - The Agent and the Re-plan",
)
for entry in (ROOT, ROOT / "problem_simulation", *(ROOT / name for name in WEEKS)):
    if str(entry) not in sys.path:
        sys.path.insert(0, entry)

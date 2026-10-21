"""Score a Week 5 agent and re-plan folder. It prints pass or fail, not a gold value."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _entry in (_ROOT, _ROOT / "problem_simulation"):
    if str(_entry) not in sys.path:
        sys.path.insert(0, str(_entry))

"""Week 1 keeps its import path. The comparisons live in course.checks."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from course.checks.rules import as_int, close, integers, normalise, present, same_set

__all__ = ["as_int", "close", "integers", "normalise", "present", "same_set"]

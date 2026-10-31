"""INV-09 handoff. The permit binding is graded with the clock checker."""

from __future__ import annotations

import json
from pathlib import Path

from access.checks.common import load_object


def grade_handoff(path: Path) -> list[str]:
    raw, problems = load_object(path)
    if raw is None:
        return problems
    for field in ("intent", "tried", "unresolved", "next_step"):
        value = raw.get(field)
        if not isinstance(value, str) or not value.strip():
            problems.append(f"the handoff is missing {field}")
    blob = json.dumps(raw)
    if "dec-clinical" in blob or "dec-accept" in blob:
        problems.append("the handoff invents a clinical decision from the previous desk")
    return problems

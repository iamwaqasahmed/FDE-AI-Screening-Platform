"""chk-w2-ux. A miss does not name a clause's wording or the delay."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.notes_w2d3 import written_problems
from alwaha.check.tables import contains_canary


def ux_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    if any(path.name == "model.json" for path in work.rglob("*") if path.is_file()):
        return [WATERMARK]
    return written_problems(work, gold)

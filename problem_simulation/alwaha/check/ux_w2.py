"""chk-w2-ux. A miss does not name a clause's wording or the delay.

This check grades the usability notes for the journey day. A planted token or a copied model file stops the check and returns only the watermark miss, so a failure message cannot quote a clause or a delay. When neither is present, the written-note grader supplies the rest of the misses.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.notes_w2d3 import written_problems
from alwaha.check.tables import contains_canary


def ux_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the usability misses for this work directory.

    A planted token is enough on its own. A file named as the model is treated the same way, even when the token string is absent, because that copy would let a later message name a clause. Only files are considered, so a directory cannot trip the check. Otherwise the written notes are graded and their misses are returned as-is.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    # A copied model file is treated as a planted sample, so the check stops before it can quote a clause or a delay.
    if any(path.name == "model.json" for path in work.rglob("*") if path.is_file()):
        return [WATERMARK]
    return written_problems(work, gold)

"""chk-individual-w4. A miss does not print the attack text."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary

BOOKED = "the guardrail lets the attack book"
MISSING = "the personal lab is missing"
RUN = "the personal lab did not run"
_MODULES = ("personal",)


def individual_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    folder = work / "app"
    if not (folder / "personal.py").is_file():
        return [MISSING]
    row = json.loads((pack / "personal" / "attack.json").read_text(encoding="utf-8"))
    try:
        with modules(folder, _MODULES) as loaded:
            got = loaded["personal"].stop(row)
    except Exception:
        return [RUN]
    if not isinstance(got, dict) or not got.get("blocked") or got.get("booked"):
        return [BOOKED]
    return []

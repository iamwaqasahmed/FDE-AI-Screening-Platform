"""chk-individual-m04-l05. A miss does not print the attack text.

This personal-lab check grades the guard on the attack row in the pack. Gold is accepted and unused. A planted token, a missing module, or a crash stops the check. The only behavioral miss is that the attack was allowed to book. The attack text itself is never printed.
"""

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
    """Return the personal-lab misses for the attack row.

    Gold is discarded because the row is read from the pack. A missing module is its own miss, before any call. The stop result must be a record that is blocked and did not book. A non-record, a false blocked flag, or a booking are the same miss. An exception is the run miss.
    """
    # Gold is unused. The attack row comes from the pack. The caller still loads the release so a missing pack fails first.
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
    # The guard must return a record that is blocked and did not book. A non-record, a miss on blocked, or a booking are the same miss.
    if not isinstance(got, dict) or not got.get("blocked") or got.get("booked"):
        return [BOOKED]
    return []

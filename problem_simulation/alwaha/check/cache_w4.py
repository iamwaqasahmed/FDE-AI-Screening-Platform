"""slice-cache. A miss does not print the cached sentence."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary

OLD = "old clinic hours are still served"
RUN = "the harness did not run"
_MODULES = ("cache",)


def cache_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    event = json.loads((pack / "events" / "document-changed.json").read_text(encoding="utf-8"))
    store = {"hours": gold["old_hours"]}
    try:
        with modules(work / "app", _MODULES) as loaded:
            got = str(loaded["cache"].answer(store, event))
    except Exception:
        return [RUN]
    if got != event["body"] or gold["old_hours"] in got:
        return [OLD]
    return []

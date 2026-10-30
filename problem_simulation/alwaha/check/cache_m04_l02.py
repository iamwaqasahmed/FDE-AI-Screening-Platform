"""slice-cache. A miss does not print the cached sentence.

This slice grades the document cache after a change event. The store is seeded with the previous hours, and the participant answer must come back as the new body. A planted token stops the check. A crash is the harness miss. The stale-hours sentence is the only other miss, and it does not include the cached text.
"""

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
    """Return the cache misses for this work directory.

    The change event and the previous hours come from the pack and from gold. The answer is read inside the participant cache module. It must equal the event body, and the previous hours must not still appear inside it. Either failure is the stale-cache miss. An exception while loading or answering is the harness miss.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    event = json.loads((pack / "events" / "document-changed.json").read_text(encoding="utf-8"))
    store = {"hours": gold["old_hours"]}
    try:
        with modules(work / "app", _MODULES) as loaded:
            got = str(loaded["cache"].answer(store, event))
    except Exception:
        return [RUN]
    # The reply must be the new body, and the previous hours must not still be inside it. Either failure is the stale-cache miss.
    if got != event["body"] or gold["old_hours"] in got:
        return [OLD]
    return []

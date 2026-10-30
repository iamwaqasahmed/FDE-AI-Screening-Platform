"""slice-surge. No batching, no router, or no public cache fails.

This slice grades batching, routing, and the public cache under a mixed load. Gold is accepted and unused because the sheet, the public store, and the mixed rows come from the pack. A planted token stops the check. No batching, a protected row sent to the external model, or a public answer that misses the cache each have their own miss.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary
from alwaha.engagement.m04_l03_rules import answer, target

EXTERNAL = "the batch is on ext-large"
GPU = "public answers still hit the GPU"
RUN = "the harness did not run"
UNBATCHED = "the batch is unbatched"
_MODULES = ("batch", "route", "public")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    The three probes are independent, and a repeated sentence should appear once.
    """
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _rate(module, sheet: dict) -> list[str]:
    """Return the unbatched miss, or the harness miss if the rate call crashes.

    The rate must be the batched throughput on the sheet. Any other value means the batch was not batched.
    """
    try:
        got = module.rate(sheet)
    except Exception:
        return [RUN]
    if got != int(sheet["local_batched_tps"]):
        return [UNBATCHED]
    return []


def _route(module, rows: list[dict]) -> list[str]:
    """Return the external-model miss, or the harness miss if a call crashes.

    Only a row that carries protected fields is checked. The first row whose target disagrees with the reference fails the probe. A clean row is not a route case.
    """
    try:
        for row in rows:
            # Only a row that carries protected fields is checked. A wrong target on that row means the work went to the external model.
            if row.get("phi") and module.target(row) != target(row):
                return [EXTERNAL]
    except Exception:
        return [RUN]
    return []


def _public(module, store: dict, rows: list[dict]) -> list[str]:
    """Return the GPU miss, or the harness miss if a call crashes.

    Only a public row is checked. The first public answer that disagrees with the reference means the cache was missed.
    """
    try:
        for row in rows:
            # Only a public question is checked. A mismatch means the answer missed the public cache.
            if row.get("kind") == "public" and module.answer(store, row) != answer(store, row):
                return [GPU]
    except Exception:
        return [RUN]
    return []


def surge_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the surge misses.

    Gold is discarded because the inputs are pack files. A planted token returns only the watermark. The three probes run under one import, and a crash of that import is the harness miss.
    """
    # Gold is unused. The sheet, the store, and the rows come from the pack. The caller still loads the release so a missing pack fails first.
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    sheet = json.loads((pack / "serving" / "throughput.json").read_text(encoding="utf-8"))
    store = json.loads((pack / "serving" / "public.json").read_text(encoding="utf-8"))
    rows = _rows(pack / "load" / "mixed.jsonl")
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _rate(loaded["batch"], sheet):
                _once(problems, item)
            for item in _route(loaded["route"], rows):
                _once(problems, item)
            for item in _public(loaded["public"], store, rows):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems

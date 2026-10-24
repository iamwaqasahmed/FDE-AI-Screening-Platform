"""slice-surge. No batching, no router, or no public cache fails."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d3_rules import answer, target

EXTERNAL = "the batch is on ext-large"
GPU = "public answers still hit the GPU"
RUN = "the harness did not run"
UNBATCHED = "the batch is unbatched"
_MODULES = ("batch", "route", "public")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _rate(module, sheet: dict) -> list[str]:
    try:
        got = module.rate(sheet)
    except Exception:
        return [RUN]
    if got != int(sheet["local_batched_tps"]):
        return [UNBATCHED]
    return []


def _route(module, rows: list[dict]) -> list[str]:
    try:
        for row in rows:
            if row.get("phi") and module.target(row) != target(row):
                return [EXTERNAL]
    except Exception:
        return [RUN]
    return []


def _public(module, store: dict, rows: list[dict]) -> list[str]:
    try:
        for row in rows:
            if row.get("kind") == "public" and module.answer(store, row) != answer(store, row):
                return [GPU]
    except Exception:
        return [RUN]
    return []


def surge_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
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

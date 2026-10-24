"""chk-w3-eval for the second run. A miss does not print a price, a count, or a doc id."""

from __future__ import annotations

import math
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w3d5 import note_problems
from alwaha.check.tables import contains_canary

COST = "the improvement cost misses the price sheet"
MISS = "the second run misses the held-out slice"
REPAIR = "the repair leaves the unauthorized citation"
RUN = "the harness did not run"
STUCK = "the second run does not move the retrieval failure"
_MODULES = ("repair", "remeasure", "cost")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _rows(gold: dict) -> list[dict]:
    return [{"label": dict(row["label"]), "pred": dict(row["pred"])} for row in gold["before"]]


def _number(got) -> bool:
    return not isinstance(got, bool) and isinstance(got, (int, float))


def _close(got, expect: float) -> bool:
    return _number(got) and math.isclose(float(got), float(expect), abs_tol=1e-9)


def repair_problems(module, gold: dict) -> list[str]:
    try:
        for row in _rows(gold):
            got = module.repair(dict(row["pred"]))
            if got.get("doc_id") != row["label"]["doc_id"] or got.get("span") != row["label"]["span"]:
                return [REPAIR]
    except Exception:
        return [RUN]
    return []


def remeasure_problems(module, gold: dict) -> list[str]:
    try:
        got = module.remeasure(_rows(gold))
        before, after = got["before"], got["after"]
    except Exception:
        return [RUN]
    if not _number(before) or not _number(after) or float(after) <= float(before) + 1e-9:
        return [STUCK]
    if not _close(before, gold["metrics"]["before"]) or not _close(after, gold["metrics"]["after"]):
        return [MISS]
    return []


def cost_problems(module, gold: dict) -> list[str]:
    spec = gold["cost"]
    try:
        got = module.spend(spec["count"], spec["price"], spec["budget_sar"])
    except Exception:
        return [RUN]
    expect = spec["spend"]
    if expect is None:
        return [] if got is None else [COST]
    if not _close(got, expect):
        return [COST]
    return []


def eval_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = note_problems(work)
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in repair_problems(loaded["repair"], gold):
                _once(problems, item)
            for item in remeasure_problems(loaded["remeasure"], gold):
                _once(problems, item)
            for item in cost_problems(loaded["cost"], gold):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems

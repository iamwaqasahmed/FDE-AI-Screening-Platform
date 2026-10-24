"""chk-w4-fair. A miss does not print a rate or the bound."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d1_rules import gap, stamp_rate

HIDES = "the disparity table hides a district or an insurance class"
OUTSIDE = "the disparity is outside the published bound"
STAMP = "the rubber-stamp rate is missing"
RUN = "the harness did not run"
_MODULES = ("fair",)


def _rows(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _close(got, expect: float) -> bool:
    return isinstance(got, (int, float)) and not isinstance(got, bool) and abs(float(got) - expect) <= 1e-9


def _fair(module, rows: list[dict], approvals: list[dict], bound: float) -> list[str]:
    problems = []
    try:
        got = module.gap(rows)
    except Exception:
        return [RUN]
    if not _close(got, gap(rows)):
        problems.append(OUTSIDE if isinstance(got, (int, float)) and not isinstance(got, bool) and float(got) > bound + 1e-9 else HIDES)
    try:
        stamped = module.stamp_rate(approvals)
    except Exception:
        problems.append(RUN)
        return problems
    if not _close(stamped, stamp_rate(approvals)):
        problems.append(STAMP)
    return problems


def fair_problems(work: Path, pack: Path, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    rows = _rows(pack / "fairness" / "outcomes.jsonl")
    approvals = _rows(pack / "fairness" / "approvals.jsonl")
    bound = float(json.loads((pack / "fairness" / "bound.json").read_text(encoding="utf-8"))["bound"])
    try:
        with modules(work / "app", _MODULES) as loaded:
            problems = _fair(loaded["fair"], rows, approvals, bound)
    except Exception:
        problems = [RUN]
    return problems

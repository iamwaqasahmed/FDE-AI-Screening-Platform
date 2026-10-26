"""chk-w4-fair. A miss does not print a rate or the bound.

This check grades the disparity gap and the rubber-stamp rate. Both are compared with the reference helpers. A planted token stops the check. A number above the published bound is outside it. Any other gap disagreement means a district or an insurance class was hidden. Rates and the bound are not printed.
"""

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
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _close(got, expect: float) -> bool:
    """Return true when the value is a real number and matches the expected value within the tight tolerance.

    A boolean is an integer in Python, so it is rejected before the comparison. Anything that is not a number is false.
    """
    # A boolean is an integer in Python, so it is rejected before the numeric comparison.
    return isinstance(got, (int, float)) and not isinstance(got, bool) and abs(float(got) - expect) <= 1e-9


def _fair(module, rows: list[dict], approvals: list[dict], bound: float) -> list[str]:
    """Return the gap and stamp misses.

    A crash in the gap call is the harness miss and the stamp is not called. A real number above the bound is the outside miss. Any other disagreement is the hidden-class miss. A crash in the stamp call keeps the gap miss and adds the harness miss. A stamp that is not the reference rate is the missing-rate miss.
    """
    problems = []
    try:
        got = module.gap(rows)
    except Exception:
        return [RUN]
    if not _close(got, gap(rows)):
        # A real number above the bound is outside it. Any other disagreement, including a non-number, means a class was hidden.
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
    """Return the fairness misses.

    A planted token returns only the watermark. Outcomes, approvals, and the bound are read from the pack. A crash while loading the module is the harness miss.
    """
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

"""chk-w3-eval for the second run. A miss does not print a price, a count, or a doc id.

Second-run evaluation check. Repair must put the citation back on the labeled document and span. The remeasure must move, and it must land on the gold before and after values. The cost must match the sheet, including a sheet whose expected spend is nothing. Notes are graded even when the harness crashes. A price, a count, or a document id is not printed.
"""

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
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _rows(gold: dict) -> list[dict]:
    """Return the before-rows as label and prediction pairs.

    Each side is copied so a repair cannot change the gold record the next row still needs.
    """
    return [{"label": dict(row["label"]), "pred": dict(row["pred"])} for row in gold["before"]]


def _number(got) -> bool:
    """Return true when the value is an int or a float and is not a boolean.

    A boolean is an integer in Python, so it is not a score.
    """
    return not isinstance(got, bool) and isinstance(got, (int, float))


def _close(got, expect: float) -> bool:
    """Return true when the value is a real number and is close to the expected value."""
    return _number(got) and math.isclose(float(got), float(expect), abs_tol=1e-9)


def repair_problems(module, gold: dict) -> list[str]:
    """Return the repair miss, or the run miss if a call crashes.

    The first prediction whose document or span still disagrees with the label is enough.
    """
    try:
        for row in _rows(gold):
            got = module.repair(dict(row["pred"]))
            if got.get("doc_id") != row["label"]["doc_id"] or got.get("span") != row["label"]["span"]:
                return [REPAIR]
    except Exception:
        return [RUN]
    return []


def remeasure_problems(module, gold: dict) -> list[str]:
    """Return the stuck miss or the held-out miss.

    A crash is the run miss. The after value must be a real number above the before value, or the run did not move. When it did move, both numbers must match gold, or the run missed the held-out slice.
    """
    try:
        got = module.remeasure(_rows(gold))
        before, after = got["before"], got["after"]
    except Exception:
        return [RUN]
    # The second run has to move. A non-number, or an after value that does not rise, is stuck.
    if not _number(before) or not _number(after) or float(after) <= float(before) + 1e-9:
        return [STUCK]
    if not _close(before, gold["metrics"]["before"]) or not _close(after, gold["metrics"]["after"]):
        return [MISS]
    return []


def cost_problems(module, gold: dict) -> list[str]:
    """Return the cost miss.

    A crash is the run miss. When gold has no spend, the module must return nothing. Any other return is the cost miss. When gold has a spend, the number must match.
    """
    spec = gold["cost"]
    try:
        got = module.spend(spec["count"], spec["price"], spec["budget_sar"])
    except Exception:
        return [RUN]
    expect = spec["spend"]
    # A sheet with no spend must come back as nothing. Any number is the cost miss.
    if expect is None:
        return [] if got is None else [COST]
    if not _close(got, expect):
        return [COST]
    return []


def eval_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the second-run misses.

    A planted token returns only the watermark. Notes are graded first. Repair, remeasure, and cost then add their misses. A crash of the import adds the harness miss and keeps the note misses.
    """
    # A planted token returns only the watermark, so the notes are not graded after it.
    if contains_canary(work, canary):
        return [WATERMARK]
    # Notes are graded first so a later crash still keeps them.
    problems = note_problems(work)
    try:
        with modules(work / "app", _MODULES) as loaded:
            # Repair, remeasure, and cost each add their misses once.
            for item in repair_problems(loaded["repair"], gold):
                _once(problems, item)
            for item in remeasure_problems(loaded["remeasure"], gold):
                _once(problems, item)
            for item in cost_problems(loaded["cost"], gold):
                _once(problems, item)
    except Exception:
        # A crash of the import adds the harness miss and keeps the note misses.
        _once(problems, RUN)
    return problems

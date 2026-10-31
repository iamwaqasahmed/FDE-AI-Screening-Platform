"""INV-06. score() must refuse a labeled file and refuse a winner."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_callable
from access.sealed_holdouts import SCORE_HOLDOUT
from access.sealed_release import SCORE_DECISION
from access.symptoms import CALIBRATION


def grade_score(path: Path) -> list[str]:
    fn, problems = load_callable(path, "score")
    if fn is None:
        return problems
    labeled = [dict(row) for row in CALIBRATION]
    unlabeled = [{key: value for key, value in row.items() if key != "pass"} for row in CALIBRATION]
    problems.extend(_labeled(fn, labeled))
    problems.extend(_unlabeled(fn, unlabeled))
    problems.extend(_unlabeled(fn, SCORE_HOLDOUT))
    return problems


def _labeled(fn, rows: list[dict]) -> list[str]:
    try:
        got = fn(rows)
    except Exception:
        return ["the scorer raised instead of refusing the label"]
    if not isinstance(got, dict) or got.get("accepted") is not False:
        return ["the scorer can still see the label"]
    if got.get("decision") not in (None, SCORE_DECISION) and got.get("decision") != "no-call":
        return ["the scorer can still see the label"]
    return []


def _unlabeled(fn, rows: list[dict]) -> list[str]:
    try:
        got = fn(rows)
    except Exception:
        return ["the scorer raised on an unlabeled file"]
    problems: list[str] = []
    if not isinstance(got, dict) or got.get("decision") != SCORE_DECISION:
        problems.append("the fixture does not support a winner")
    planted = {row["id"] for row in rows if row["n"] < 30 or row["score_a"] == row["score_b"]}
    cited = got.get("failure_ids") if isinstance(got, dict) else None
    if not isinstance(cited, list) or set(cited) != planted:
        problems.append("the cited rows are not the planted failures")
    return problems

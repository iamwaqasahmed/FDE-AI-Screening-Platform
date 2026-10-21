"""Coded calls are exact. The estimate and the baseline may move a little."""

from __future__ import annotations

from course.checks.rules import close
from simulation.eval.graph.bars import CALL_BASELINE_TOLERANCE, CALL_ESTIMATE_TOLERANCE, CODED_SHARE_TOLERANCE


def call_signal(answer: dict, gold: dict) -> bool:
    row = gold["items"]["call_signal"]
    given = {item.get("ref"): item for item in answer.get("windows", []) if isinstance(item, dict)}
    if set(given) != {item["ref"] for item in row["windows"]}:
        return False
    if not close(answer.get("coded_share"), row["coded_share"], CODED_SHARE_TOLERANCE, relative=False):
        return False
    return all(_window(given[item["ref"]], item) for item in row["windows"])


def _window(answer: dict, row: dict) -> bool:
    dates = answer.get("start") == row["start"] and answer.get("end") == row["end"]
    coded = answer.get("coded") == row["coded"]
    estimate = close(answer.get("estimate"), row["estimate"], CALL_ESTIMATE_TOLERANCE)
    baseline = close(answer.get("baseline_per_day"), row["baseline_per_day"], CALL_BASELINE_TOLERANCE)
    return dates and coded and estimate and baseline

"""Cohort size, grader noise, and the gap between the two references."""

from __future__ import annotations

from course.checks.rules import as_int, close, same_set
from simulation.eval.evidence.bars import RATE_TOLERANCE


def vendor_scope(answer: dict, gold: dict) -> bool:
    row = gold["items"]["vendor_scope"]
    numbers = ("captures", "rejected", "adjudicated")
    if any(as_int(answer.get(key)) != row[key] for key in numbers):
        return False
    return same_set(answer.get("removed_sites", []), row["removed_sites"])


def reference_gap(answer: dict, gold: dict) -> bool:
    row = gold["items"]["reference_gap"]
    if as_int(answer.get("rejected")) != row["rejected"] or float(answer.get("cut", -1)) != row["cut"]:
        return False
    return all(_rate(answer.get(key), row[key]) for key in ("routine", "adjudicated", "gap"))


def label_noise(answer: dict, gold: dict) -> bool:
    row = gold["items"]["label_noise"]
    if not _rate(answer.get("routine_missing_share"), row["routine_missing_share"]):
        return False
    if answer.get("most_over_call") != row["most_over_call"] or answer.get("most_miss") != row["most_miss"]:
        return False
    given = {item.get("grader"): item for item in answer.get("graders", []) if isinstance(item, dict)}
    for item in row["graders"]:
        other = given.get(item["grader"])
        if other is None or as_int(other.get("n")) != item["n"]:
            return False
        if any(not _rate(other.get(key), item[key]) for key in ("disagree", "over_call", "miss")):
            return False
    return True


def _rate(given, expected) -> bool:
    return close(given, expected, RATE_TOLERANCE, relative=False)

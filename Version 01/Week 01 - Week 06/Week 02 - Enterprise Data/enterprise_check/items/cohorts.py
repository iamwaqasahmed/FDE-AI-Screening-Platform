"""Cohort items: the overdue upper bound, the vendor cohort, and the leak from a random split."""

from __future__ import annotations

from course.checks.rules import as_int, close


def overdue(answer: dict, gold: dict) -> bool:
    row = gold["cohorts"]["overdue"]
    if as_int(answer.get("rows")) != row["rows"] or as_int(answer.get("blank_rows")) != row["blank_rows"]:
        return False
    if answer.get("is_upper_bound") is not True:
        return False
    span = row["upper_tolerance"]
    return close(answer.get("latest_blank"), row["latest_blank"], span) and close(answer.get("upper_bound"), row["upper_bound"], span)


def vendor_cohort(answer: dict, gold: dict) -> bool:
    row = gold["cohorts"]["vendor"]
    exact = ("captures", "linked_by_file", "unlinked")
    if any(as_int(answer.get(key)) != row[key] for key in exact):
        return False
    return close(answer.get("linked_people"), row["linked_people"], 0.02)


def split_leak(answer: dict, gold: dict) -> bool:
    row = gold["cohorts"]["vendor"]
    return as_int(answer.get("seed")) == row["leak_seed"] and close(answer.get("leak_share"), row["leak_share"], row["leak_tolerance"], relative=False)

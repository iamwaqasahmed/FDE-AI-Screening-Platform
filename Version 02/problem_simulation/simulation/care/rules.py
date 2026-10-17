"""Stamp the clause that bound each encounter. The lookup is cached by site and date."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.policy.apply import applicable_clause

TOPICS = ("grade_turnaround", "letter_turnaround", "specialist_review", "eligibility")


def stamp_rules(events: pd.DataFrame) -> None:
    cache: dict[tuple[str, str], tuple] = {}
    found_rows = []
    for site, photo in zip(events["site"], events["photo_date"]):
        found = cache.get((site, photo))
        if found is None:
            found = _lookup(site, date.fromisoformat(photo))
            cache[(site, photo)] = found
        found_rows.append(found)
    columns = list(zip(*found_rows)) if found_rows else [[]] * 7
    events["grade_clause"] = list(columns[0])
    events["grade_limit"] = list(columns[1])
    events["letter_clause"] = list(columns[2])
    events["letter_limit"] = list(columns[3])
    events["specialist_clause"] = list(columns[4])
    events["specialist_days"] = list(columns[5])
    events["eligibility_clause"] = list(columns[6])


def _lookup(site: str, on_date: date) -> tuple:
    grade, letter, specialist, eligibility = (applicable_clause(site, on_date, topic) for topic in TOPICS)
    return (
        grade.clause_id,
        int(grade.days or 0),
        letter.clause_id,
        int(letter.days or 0),
        specialist.clause_id,
        "" if specialist.days is None else str(specialist.days),
        eligibility.clause_id,
    )

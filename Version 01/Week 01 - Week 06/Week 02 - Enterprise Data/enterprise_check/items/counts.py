"""Count items: eligible people, the district split, and coverage against the warehouse."""

from __future__ import annotations

from course.checks.rules import as_int, close


def eligible_people(answer: dict, gold: dict) -> bool:
    row = gold["counts"]
    count = as_int(answer.get("count"))
    if count is None or count in (row["warehouse_eligible"], row["rows"]):
        return False
    return close(count, row["eligible"], row["eligible_tolerance"])


def eligible_by_district(answer: dict, gold: dict) -> bool:
    row = gold["counts"]["by_district"]
    given = answer.get("counts")
    if not isinstance(given, dict) or set(given) != set(row):
        return False
    return all(close(given[name], count, gold["counts"]["eligible_tolerance"]) for name, count in row.items())


def coverage(answer: dict, gold: dict) -> bool:
    row = gold["counts"]
    people = as_int(answer.get("people"))
    if people is None or people == row["warehouse_covered"]:
        return False
    return (
        close(people, row["coverage"], row["coverage_tolerance"])
        and as_int(answer.get("days")) == row["coverage_days"]
        and as_int(answer.get("warehouse_months")) == row["warehouse_months"]
    )

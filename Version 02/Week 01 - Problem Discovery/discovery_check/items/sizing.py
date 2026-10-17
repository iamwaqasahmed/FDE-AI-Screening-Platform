"""Sizing items: people, the warehouse, reminders, spend, the fee, the backlog, the vendor, urgency."""

from __future__ import annotations

from discovery_check.rules import as_int, close


def eligible_people(answer: dict, gold: dict) -> bool:
    row = gold["eligible"]
    count = as_int(answer.get("count"))
    if count is None or count in (row["registry_rows"], row["warehouse"]):
        return False
    return close(count, row["count"], row["tolerance"])


def warehouse_defect(answer: dict, gold: dict) -> bool:
    row = gold["warehouse"]
    return answer.get("counts_deceased") is row["counts_deceased"] and answer.get("coverage_months") == row["coverage_months"]


def reminder(answer: dict, gold: dict) -> bool:
    row = gold["reminder"]
    if answer.get("change_date") != row["change_date"]:
        return False
    districts = answer.get("districts")
    if not isinstance(districts, dict) or set(districts) != set(row["naive"]):
        return False
    for district, naive in row["naive"].items():
        given = districts[district]
        if not isinstance(given, dict):
            return False
        estimate = given.get("true_uplift")
        if not close(given.get("naive"), naive, row["naive_tolerance"], relative=False):
            return False
        if not isinstance(estimate, (int, float)) or isinstance(estimate, bool):
            return False
        if not 0 < float(estimate) < float(given["naive"]):
            return False
    return True


def agency_spend(answer: dict, gold: dict) -> bool:
    row = gold["agency"]
    return answer.get("year") == row["year"] and answer.get("centre") == row["centre"] and close(
        answer.get("gbp"), row["gbp"], row["tolerance"]
    )


def board_fee(answer: dict, gold: dict) -> bool:
    return as_int(answer.get("gbp")) == gold["board_fee"]["gbp"]


def backlog(answer: dict, gold: dict) -> bool:
    row = gold["backlog"]
    true = as_int(answer.get("true"))
    return (
        answer.get("from") == row["from"]
        and as_int(answer.get("lead")) == row["lead"]
        and as_int(answer.get("board")) == row["board"]
        and true is not None
        and 0 < true < row["lead"]
        and true != row["board"]
    )


def urgent_notes(answer: dict, gold: dict) -> bool:
    row = gold["urgent"]
    return answer.get("field") == row["field"] and answer.get("text") == row["text"] and as_int(answer.get("count")) == row["count"]


def vendor_claims(answer: dict, gold: dict) -> bool:
    row = gold["vendor"]
    return (
        answer.get("from") == row["from"]
        and answer.get("hospitals") is row["hospitals"]
        and answer.get("under_75") == row["under_75"]
        and answer.get("aged_75_plus") == row["aged_75_plus"]
        and answer.get("holds") is False
    )


def letter_peak(answer: dict, gold: dict) -> bool:
    row = gold["calls"]
    return answer.get("month") == row["letter_peak_month"] and answer.get("ref") == row["letter_ref"]


def hospital_calls(answer: dict, gold: dict) -> bool:
    return answer.get("ref") == gold["calls"]["hospital_ref"]


def letter_cause(answer: dict, gold: dict) -> bool:
    row = gold["letters"]
    return answer.get("ref") == row["ref"] and answer.get("start") == row["start"] and answer.get("end") == row["end"]


def rota(answer: dict, gold: dict) -> bool:
    return answer.get("ref") == gold["rota"]["ref"] and answer.get("date") == gold["rota"]["date"]

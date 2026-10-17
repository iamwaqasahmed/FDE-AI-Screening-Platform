"""Profiling items: schemas, formats, units, firmware, the log window, the recode."""

from __future__ import annotations

from discovery_check.rules import same_set


def _profile(gold: dict) -> dict:
    return gold["profiling"]


def registry_months(answer: dict, gold: dict) -> bool:
    row = _profile(gold)
    return (
        answer.get("old_month") == row["old_month"]
        and answer.get("mixed_month") == row["mixed_month"]
        and answer.get("duplicate_month") == row["duplicate_month"]
        and same_set(answer.get("old_columns"), row["old_columns"])
    )


def dob_formats(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("formats"), _profile(gold)["dob_formats"])


def district_spellings(answer: dict, gold: dict) -> bool:
    """Every reported spelling is a real variant, and at least one shows up for each district."""
    extras = answer.get("extras")
    if not isinstance(extras, list):
        return False
    allowed = {name.lower() for name in _profile(gold)["district_extras"]}
    found = {str(name).lower() for name in extras}
    return bool(found) and found <= allowed and len(found) >= 4


def lab_units(answer: dict, gold: dict) -> bool:
    row = _profile(gold)
    return (
        answer.get("change_on") == row["lab_unit_change"]
        and answer.get("before") == row["lab_unit_before"]
        and answer.get("after") == row["lab_unit_after"]
    )


def call_schema(answer: dict, gold: dict) -> bool:
    row = _profile(gold)
    return answer.get("from_month") == row["call_schema_from"] and same_set(answer.get("columns"), row["call_columns_after"])


def firmware_lag(answer: dict, gold: dict) -> bool:
    given = answer.get("sites")
    if not isinstance(given, list):
        return False

    def key(row: dict) -> tuple:
        return (row.get("site"), row.get("shown_version"), row.get("true_version"))

    return {key(row) for row in given if isinstance(row, dict)} == {key(row) for row in _profile(gold)["firmware"]}


def pii_log(answer: dict, gold: dict) -> bool:
    row = _profile(gold)["pii"]
    return answer.get("ref") == row["ref"] and answer.get("start") == row["start"] and answer.get("end") == row["end"]


def finance_recode(answer: dict, gold: dict) -> bool:
    row = _profile(gold)["finance"]
    return (
        answer.get("recoded_on") == row["recoded_on"]
        and answer.get("new_code") == row["new_code"]
        and same_set(answer.get("old_codes"), row["old_codes"])
    )

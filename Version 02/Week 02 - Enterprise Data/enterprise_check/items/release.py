"""Release items: the freeze, the windows, the blocked tickets, and the RACI row."""

from __future__ import annotations

from course.checks.rules import same_set


def release_plan(answer: dict, gold: dict) -> bool:
    row = gold["release"]
    keys = ("freeze_ref", "freeze_start", "freeze_end", "registry_release", "warehouse_release", "v2_stops")
    return all(answer.get(key) == row[key] for key in keys)


def freeze_blocked(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("tickets", []), gold["release"]["blocked_tickets"])


def rerun_contracts(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("contracts", []), gold["read"]["rerun_contracts"])


def raci_v3(answer: dict, gold: dict) -> bool:
    row = gold["read"]["raci"]
    return all(answer.get(key) == value for key, value in row.items())

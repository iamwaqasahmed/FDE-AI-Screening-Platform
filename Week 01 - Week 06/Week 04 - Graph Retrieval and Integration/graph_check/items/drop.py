"""The window, the keys, and what this drop changes."""

from __future__ import annotations

from course.checks.rules import same_set

TEXTS = ("requests", "dispatch_rows", "unique_dispatched", "duplicate_rows", "lost")
KEYS = ("transport_key", "business_key", "transport_rows_removed", "business_rows_removed")


def drop_incident(answer: dict, gold: dict) -> bool:
    row = gold["items"]["drop_incident"]
    if any(answer.get(key) != row[key] for key in TEXTS):
        return False
    if answer.get("notice_claims_hold") is not False:
        return False
    return same_set(answer.get("window", []), row["window"]) and same_set(answer.get("loop_days", []), row["loop_days"])


def outputs_changed(answer: dict, gold: dict) -> bool:
    row = gold["items"]["outputs_changed"]
    return (
        same_set(answer.get("contracts", []), row["contracts"])
        and answer.get("week2_rule") == row["week2_rule"]
        and same_set(answer.get("unchanged", []), row["unchanged"])
    )


def dedupe_keys(answer: dict, gold: dict) -> bool:
    row = gold["items"]["dedupe_keys"]
    return all(answer.get(key) == row[key] for key in KEYS)

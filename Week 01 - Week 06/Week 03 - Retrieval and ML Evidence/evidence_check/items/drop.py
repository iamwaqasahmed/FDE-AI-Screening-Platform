"""The memo, and the outputs it tells the team to rerun."""

from __future__ import annotations

from course.checks.rules import same_set


def drop_restriction(answer: dict, gold: dict) -> bool:
    row = gold["items"]["drop_restriction"]
    texts = ("effective", "banned_field", "replacement_field")
    if any(answer.get(key) != row[key] for key in texts):
        return False
    lists = ("allowed_sites", "removed_sites", "banned_in")
    return all(same_set(answer.get(key, []), row[key]) for key in lists)


def outputs_changed(answer: dict, gold: dict) -> bool:
    row = gold["items"]["outputs_changed"]
    return (
        same_set(answer.get("contracts", []), row["contracts"])
        and same_set(answer.get("week2_items", []), row["week2_items"])
        and answer.get("clusters_unchanged") is True
    )

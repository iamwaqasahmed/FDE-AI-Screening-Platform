"""Identity items: the defect counts, the keys that cannot be linked, and the confidence rule."""

from __future__ import annotations

from course.checks.rules import as_int, close, same_set


def identity_defects(answer: dict, gold: dict) -> bool:
    row = gold["identity"]
    counts = as_int(answer.get("aliases")) == row["aliases"] and as_int(answer.get("decoys")) == row["decoys"]
    window = answer.get("reversed_from") == row["reversed_from"] and answer.get("reversed_to") == row["reversed_to"]
    return counts and window and answer.get("reuse_month") == row["reuse_month"]


def unlinked_keys(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("keys", []), gold["read"]["unlinked_keys"])


def confidence_rule(answer: dict, gold: dict) -> bool:
    row = gold["read"]["confidence"]
    return all(close(answer.get(key), value, 0.0, relative=False) for key, value in row.items())

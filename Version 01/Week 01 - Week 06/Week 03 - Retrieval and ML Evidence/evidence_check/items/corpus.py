"""Counts and header facts from the corpus."""

from __future__ import annotations

from course.checks.rules import as_int, same_set


def policy_graph(answer: dict, gold: dict) -> bool:
    row = gold["items"]["policy_graph"]
    if not same_set(answer.get("drafts", []), row["drafts"]):
        return False
    if not same_set(answer.get("stale_register", []), row["stale_register"]):
        return False
    return _rows(answer.get("withdrawn"), row["withdrawn"]) and _rows(answer.get("overlays"), row["overlays"])


def originals(answer: dict, gold: dict) -> bool:
    row = gold["items"]["originals"]
    return all(as_int(answer.get(key)) == row[key] for key in ("pdf", "docx", "xlsx", "scan"))


def table_only(answer: dict, gold: dict) -> bool:
    row = gold["items"]["table_only"]
    return as_int(answer.get("boards")) == row["boards"] and as_int(answer.get("audits")) == row["audits"]


def scan_damage(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("pairs", []), gold["items"]["scan_damage"]["pairs"])


def near_duplicates(answer: dict, gold: dict) -> bool:
    row = gold["items"]["near_duplicates"]
    return as_int(answer.get("count")) == row["count"] and answer.get("suffix") == row["suffix"]


def _rows(given, expected) -> bool:
    if not isinstance(given, list) or len(given) != len(expected):
        return False
    key = lambda row: row.get("document_id", "")
    return all(dict(left) == dict(right) for left, right in zip(sorted(given, key=key), expected))

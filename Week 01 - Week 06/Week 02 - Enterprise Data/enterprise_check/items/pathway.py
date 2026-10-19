"""Pathway items: the site rules the warehouse missed, and the register that still says draft."""

from __future__ import annotations

from course.checks.rules import as_int, same_set


def site_rules(answer: dict, gold: dict) -> bool:
    row = gold["pathway"]["site_rules"]
    numbers = (
        "hill_recall_days", "national_ungradable_days", "ncec_specialist_days", "harbour_specialist_days",
    )
    if any(as_int(answer.get(key)) != row[key] for key in numbers):
        return False
    texts = (
        "hill_document", "hill_from", "ncec_from", "harbour_from", "oakridge_memo", "oakridge_from", "oakridge_sunset",
    )
    return all(answer.get(key) == row[key] for key in texts)


def stale_register(answer: dict, gold: dict) -> bool:
    row = gold["read"]["stale_register"]
    return same_set(answer.get("documents", []), row["documents"]) and answer.get("register_says") == row["register_says"]

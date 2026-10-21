"""Key-fact coverage for a note or a model. A banned sentence fails it outright."""

from __future__ import annotations

from course.checks.rules import close, integers, normalise, present

BAR = 0.8


def score_text(text: str, facts: list[dict], forbidden: list[str]) -> dict:
    hits = [_fact(text, fact) for fact in facts]
    banned = [claim for claim in forbidden if normalise(claim) in normalise(text)]
    return {"coverage": sum(hits) / len(hits) if hits else 0.0, "forbidden": banned}


def passed(row: dict, bar: float = BAR) -> bool:
    return row["coverage"] >= bar and not row["forbidden"]


def _fact(text: str, fact: dict) -> bool:
    if "number" in fact:
        return any(close(number, fact["number"], fact.get("tolerance", 0.0)) for number in integers(text))
    return all(present(text, token) for token in fact.get("tokens", []))

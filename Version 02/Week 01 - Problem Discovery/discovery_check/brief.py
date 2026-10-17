"""The brief passes on key-fact coverage. A banned sentence fails it outright."""

from __future__ import annotations

from pathlib import Path

from discovery_check.rules import close, integers, normalise, present

BAR = 0.8


def score_file(path: Path, gold: dict) -> dict:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return score_text(text, gold)


def score_text(text: str, gold: dict) -> dict:
    facts = gold["brief"]["facts"]
    hits = [_fact(text, fact) for fact in facts]
    forbidden = [claim for claim in gold["brief"]["forbidden"] if normalise(claim) in normalise(text)]
    return {"coverage": sum(hits) / len(hits) if hits else 0.0, "forbidden": forbidden}


def passed(row: dict) -> bool:
    return row["coverage"] >= BAR and not row["forbidden"]


def _fact(text: str, fact: dict) -> bool:
    if "number" in fact:
        return any(close(number, fact["number"], fact["tolerance"]) for number in integers(text))
    return all(present(text, token) for token in fact["tokens"])

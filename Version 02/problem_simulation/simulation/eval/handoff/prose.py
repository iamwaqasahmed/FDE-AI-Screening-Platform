"""Key-fact coverage for a handoff page. A banned sentence fails it outright."""

from __future__ import annotations

import re

INTEGER = re.compile(r"(?<![\d.,-])(\d{1,3}(?:,\d{3})+|\d+)(?![\d-])")
FLOAT = re.compile(r"\d+\.\d+")


def score_text(text: str, facts: list[dict], forbidden: list[str]) -> dict:
    hits = [_fact(text, fact) for fact in facts]
    banned = [claim for claim in forbidden if _norm(claim) in _norm(text)]
    return {"coverage": sum(hits) / len(hits) if hits else 0.0, "forbidden": banned}


def passed(row: dict, bar: float) -> bool:
    return row["coverage"] >= bar and not row["forbidden"]


def has_rate(text: str, target: float, tolerance: float) -> bool:
    for number in _floats(text):
        if abs(number - target) <= tolerance:
            return True
        if number > 1 and abs(number / 100 - target) <= tolerance:
            return True
    return False


def has_count(text: str, target: int) -> bool:
    return target in [int(match.group(1).replace(",", "")) for match in INTEGER.finditer(text)]


def _fact(text: str, fact: dict) -> bool:
    if "number" in fact:
        return has_count(text, int(fact["number"])) or has_rate(text, float(fact["number"]), fact.get("tolerance", 0.0))
    return all(token.lower() in _norm(text) for token in fact.get("tokens", []))


def _floats(text: str) -> list[float]:
    return [float(match) for match in FLOAT.findall(text)]


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", str(value)).strip().lower().rstrip(".")

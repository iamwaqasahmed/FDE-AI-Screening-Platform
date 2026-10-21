"""Score the written pages. Both handoff pages name the same sites and the same date."""

from __future__ import annotations

from simulation.eval.handoff.bars import FACT_BAR
from simulation.eval.handoff.prose import passed, score_text


def score_document(text: str, spec: dict) -> dict:
    row = score_text(text, spec["facts"], spec["forbidden"])
    row["ok"] = passed(row, FACT_BAR)
    return row


def pages_agree(executive: str, clinical: str, spec: dict) -> bool:
    if not executive.strip() or not clinical.strip():
        return False
    sites = all(site.lower() in executive.lower() and site.lower() in clinical.lower() for site in spec["sites"])
    return sites and spec["date"] in executive and spec["date"] in clinical

"""Apply a team's pathway table to the gold probes. A probe passes on the document and the days."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.eval.enterprise.bars import PROBE_BAR


def load(path: Path) -> pd.DataFrame:
    columns = ["site", "topic", "grade", "clause_id", "document_id", "days", "effective", "sunset"]
    if not path.exists():
        return pd.DataFrame(columns=columns)
    frame = pd.read_csv(path, dtype=str).fillna("")
    for column in columns:
        if column not in frame.columns:
            frame[column] = ""
    return frame


def score(rules: pd.DataFrame, probes: list[dict]) -> dict:
    if not probes:
        return {"coverage": 0.0, "ok": False}
    hits = sum(_hit(rules, probe) for probe in probes)
    coverage = hits / len(probes)
    return {"coverage": coverage, "ok": coverage >= PROBE_BAR}


def _hit(rules: pd.DataFrame, probe: dict) -> bool:
    if rules.empty:
        return False
    days = "" if probe["days"] is None else str(probe["days"])
    grade = probe["grade"] or ""
    matched = rules[
        rules["topic"].eq(probe["topic"])
        & rules["grade"].eq(grade)
        & rules["document_id"].eq(probe["document_id"])
        & rules["days"].eq(days)
        & rules["effective"].le(probe["on"])
        & (rules["sunset"].eq("") | rules["sunset"].gt(probe["on"]))
    ]
    if matched.empty:
        return False
    site = matched["site"].eq(probe["site"])
    return bool(site.any() or matched["site"].eq("").any())

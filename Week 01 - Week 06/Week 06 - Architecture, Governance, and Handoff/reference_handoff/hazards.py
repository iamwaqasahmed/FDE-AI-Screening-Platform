"""A hazard log that cites the files and is not signed."""

from __future__ import annotations

import pandas as pd

from simulation.eval.handoff.bars import HAZARD_COLUMNS

GROUPS = (
    ("subgroup", "R-01", "age"),
    ("firmware", "R-12", ""),
    ("scope", "CSO-2", ""),
    ("signoff", "CSO-3", ""),
    ("letters", "CSO-4", "people"),
    ("outage", "INC-0274", ""),
    ("merge", "I-03", ""),
)


def frame(evidence: dict, people: int, owner: str) -> pd.DataFrame:
    rows = []
    for hazard_id, anchor, kind in GROUPS:
        detail = _detail(kind, evidence, people)
        rows.append({
            "hazard_id": hazard_id, "cause": hazard_id, "effect": "harm if the pilot ignores it", "anchor": anchor,
            "evidence": detail, "control": "held until the owner signs", "control_owner": owner, "signed_by": "",
        })
    return pd.DataFrame(rows, columns=list(HAZARD_COLUMNS))


def _detail(kind: str, evidence: dict, people: int) -> str:
    if kind == "age":
        return f"sensitivity at age 75 and over is {evidence['age_75_plus']}"
    if kind == "people":
        return f"{people} people, an upper bound"
    return kind or "see the anchor"

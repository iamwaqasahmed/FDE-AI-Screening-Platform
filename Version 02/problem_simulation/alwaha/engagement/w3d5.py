"""rel-w3d5 gold. Labels, the label spend, and the gate map stay here."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w3d5_pages import CASE_DATE
from alwaha.engagement.w3d5_rows import before_labeled, personal_public
from alwaha.engagement.w3d5_rules import GATE, NON_GOALS, REQUIREMENT, cost_for, moved, remeasure

_SEATS = ("cdo", "access-mgr", "phc-lead", "dpo")


def _mentions(count: int) -> list[dict]:
    seats = [{"id": seat, "text": seat} for seat in _SEATS]
    return [
        {"id": "triage", "section": "Non-goals", "text": "p-triage"},
        {"id": "vendor", "section": "Non-goals", "text": "vendor-bot"},
        {"all": ["not the value model"], "id": "value", "kind": "all", "section": "Priorities"},
        *seats,
        {"id": "dms", "section": "Systems", "text": "dms"},
        {"id": "gate", "section": "Gates", "text": "g1"},
        {"all": ["risk"], "id": "risk", "kind": "all", "section": "Gates"},
        {"all": ["clinician", "urgency"], "id": "urgency", "kind": "all", "section": "Non-goals"},
        {"all": ["ext-large"], "id": "residency", "kind": "all"},
        {"id": "count", "kind": "count", "section": "Evidence", "value": count},
        {"any": list(_SEATS), "id": "persona", "kind": "any", "section": "Evidence"},
    ]


def _readout() -> dict:
    return {
        "asks": "Asks",
        "sections": [
            {"all": ["retrieval", "second"], "heading": "Remeasure", "id": "remeasure"},
            {"all": ["p-triage"], "any": ["non-goal", "out of scope"], "heading": "Spec", "id": "spec"},
            {"all": ["dms"], "heading": "Systems", "id": "systems"},
            {"all": ["p-triage"], "heading": "Backlog", "id": "backlog"},
            {"all": ["cost.label", "label"], "heading": "Cost", "id": "cost"},
        ],
    }


def _personal() -> dict:
    citations = []
    metrics = []
    for row in personal_public():
        if row["kind"] == "citation":
            citations.append({**row, "keep": row["audience"] != "staff"})
        else:
            metrics.append({"floor": row["floor"], "meets": row["value"] >= row["floor"], "value": row["value"]})
    return {"citations": citations, "metrics": metrics}


def gold(profile: Profile) -> dict:
    rows = before_labeled()
    scored = remeasure(rows)
    count = moved(rows)
    return {
        "before": rows,
        "case_date": CASE_DATE,
        "cost": cost_for(profile),
        "gate": GATE,
        "measured_count": count,
        "metrics": scored,
        "non_goals": list(NON_GOALS),
        "personal": _personal(),
        "readout": _readout(),
        "requirement_id": REQUIREMENT,
        "requirements": {"mentions": _mentions(count), "share": 0.8},
    }

"""rel-w3d5 gold.
Labels, the label spend, and the gate map stay here.

gold repairs nothing itself. It asks the reference scorer for the before-and-after metrics, the count of rows that moved, and what that count costs against the budget. The requirements block is told that count so the mention check uses the measured value rather than a fixed one.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w3d5_pages import CASE_DATE
from alwaha.engagement.w3d5_rows import before_labeled, personal_public
from alwaha.engagement.w3d5_rules import GATE, NON_GOALS, REQUIREMENT, cost_for, moved, remeasure

_SEATS = ("cdo", "access-mgr", "phc-lead", "dpo")


def _mentions(count: int) -> list[dict]:
    """Return the mention checks for the requirements page.

    The count is passed in from the measured rows, so this list does not store its own copy of how many rows moved.
    """
    # One mention per seat, built from the seat list rather than written out.
    seats = [{"id": seat, "text": seat} for seat in _SEATS]
    return [
        # Non-goals, the priority line, and the seats.
        {"id": "triage", "section": "Non-goals", "text": "p-triage"},
        {"id": "vendor", "section": "Non-goals", "text": "vendor-bot"},
        {"all": ["not the value model"], "id": "value", "kind": "all", "section": "Priorities"},
        *seats,
        # Systems, the gate, and the measured count that was passed in.
        {"id": "dms", "section": "Systems", "text": "dms"},
        {"id": "gate", "section": "Gates", "text": "g1"},
        {"all": ["risk"], "id": "risk", "kind": "all", "section": "Gates"},
        {"all": ["clinician", "urgency"], "id": "urgency", "kind": "all", "section": "Non-goals"},
        {"all": ["ext-large"], "id": "residency", "kind": "all"},
        {"id": "count", "kind": "count", "section": "Evidence", "value": count},
        {"any": list(_SEATS), "id": "persona", "kind": "any", "section": "Evidence"},
    ]


def _readout() -> dict:
    """Return the readout sections the closing page is checked against.

    The steps name the asks heading and list each section together with the words that section is checked for.
    """
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
    """Return which personal citations may be kept, and whether each metric meets its floor.

    A citation whose audience is staff is not kept. Metric rows record the value, the floor, and whether the value clears it.
    """
    citations = []
    metrics = []
    for row in personal_public():
        if row["kind"] == "citation":
            # A staff-only document is not kept on this public readout.
            citations.append({**row, "keep": row["audience"] != "staff"})
        else:
            metrics.append({"floor": row["floor"], "meets": row["value"] >= row["floor"], "value": row["value"]})
    return {"citations": citations, "metrics": metrics}


def gold(profile: Profile) -> dict:
    """Return the before rows, the remeasured scores, the label cost, and the requirement checks.

    The measured count is how many predictions still name a different document from the label. That same count is handed to the mention list.
    """
    rows = before_labeled()
    # Score the rows again, and count how many still name a different document from the label.
    scored = remeasure(rows)
    count = moved(rows)
    return {
        # Before rows, the case date, and the label cost for this profile.
        "before": rows,
        "case_date": CASE_DATE,
        "cost": cost_for(profile),
        "gate": GATE,
        # The measured count is the same value the mention list is given.
        "measured_count": count,
        "metrics": scored,
        "non_goals": list(NON_GOALS),
        "personal": _personal(),
        # Readout sections and the requirement checks.
        "readout": _readout(),
        "requirement_id": REQUIREMENT,
        "requirements": {"mentions": _mentions(count), "share": 0.8},
    }

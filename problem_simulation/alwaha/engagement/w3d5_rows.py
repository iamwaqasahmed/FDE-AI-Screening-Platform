"""Public rows for rel-w3d5.
Labels stay out of the pack.

before_public is the citation predictions a participant can see. before_labeled pairs each of those predictions with the in-force label for the checker. personal_public mixes citations and metric rows. stories names the work items, including the ones the proof will not build.
"""

from __future__ import annotations

IN_FORCE = "circ-ramadan"
SPAN = "hours-c1"
UNAUTH = "circ-ramadan-unauth"


def before_public() -> list[dict]:
    """Return the citation predictions: several that already match, then one that cites the unauthorized document."""
    right = {"doc_id": IN_FORCE, "span": SPAN}
    wrong = {"doc_id": UNAUTH, "span": SPAN}
    return [right, right, right, right, wrong]


def before_labeled() -> list[dict]:
    """Return each public prediction beside the in-force label it should have matched."""
    label = {"doc_id": IN_FORCE, "span": SPAN}
    return [{"label": label, "pred": dict(row)} for row in before_public()]


def personal_public() -> list[dict]:
    """Return the personal citations and the metric rows, including one staff citation and one metric under its floor.

    The steps append the citation rows and the metric rows, keeping the audience on each citation and the floor beside each value.
    """
    return [
        {"asker": "patient", "audience": "patient", "doc_id": IN_FORCE, "kind": "citation", "version": "v4"},
        {"asker": "patient", "audience": "staff", "doc_id": "prep-staff", "kind": "citation", "version": "v2"},
        {"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.9},
        {"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.5},
    ]


def stories() -> list[dict]:
    """Return the work items, including the ones the proof will not build and the citation requirement it will.

    The steps return the urgency story, the vendor story, and the citation story.
    """
    return [
        {"story_id": "p-triage", "title": "Set clinical urgency"},
        {"story_id": "vendor-bot", "title": "Replace the contact center with the vendor bot"},
        {"story_id": "req-cite", "title": "Cite the in-force document"},
    ]

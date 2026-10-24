"""Public rows for rel-w3d5. Labels stay out of the pack."""

from __future__ import annotations

IN_FORCE = "circ-ramadan"
SPAN = "hours-c1"
UNAUTH = "circ-ramadan-unauth"


def before_public() -> list[dict]:
    right = {"doc_id": IN_FORCE, "span": SPAN}
    wrong = {"doc_id": UNAUTH, "span": SPAN}
    return [right, right, right, right, wrong]


def before_labeled() -> list[dict]:
    label = {"doc_id": IN_FORCE, "span": SPAN}
    return [{"label": label, "pred": dict(row)} for row in before_public()]


def personal_public() -> list[dict]:
    return [
        {"asker": "patient", "audience": "patient", "doc_id": IN_FORCE, "kind": "citation", "version": "v4"},
        {"asker": "patient", "audience": "staff", "doc_id": "prep-staff", "kind": "citation", "version": "v2"},
        {"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.9},
        {"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.5},
    ]


def stories() -> list[dict]:
    return [
        {"story_id": "p-triage", "title": "Set clinical urgency"},
        {"story_id": "vendor-bot", "title": "Replace the contact center with the vendor bot"},
        {"story_id": "req-cite", "title": "Cite the in-force document"},
    ]

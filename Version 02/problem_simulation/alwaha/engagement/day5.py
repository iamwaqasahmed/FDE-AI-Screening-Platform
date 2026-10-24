"""Steering questions and the Day 5 document gold. Answers stay in the interviews."""

from __future__ import annotations

QUESTIONS = (
    "What, if anything, goes live before Ramadan?",
    "Where does patient data sit for this proof?",
    "Which failure did the scenario set expose, and what did the agent do?",
    "Which stage gate is still open?",
    "What will this proof not build?",
)

DOC_IDS = (
    "pol-stage-gate",
    "pol-assistant-use",
    "pol-approval",
    "pol-clinical-safety",
    "pol-sla",
    "crit-endo-v3",
    "crit-endo-v4",
    "doc-postmortem-2023",
    "doc-minutes-2023-11",
)


def steer_page() -> str:
    numbered = "\n".join(f"{index}. {text}" for index, text in enumerate(QUESTIONS, start=1))
    return f"# steer-w1\n\nThe steering committee asks these questions.\n\n{numbered}\n"


def document_gold() -> dict:
    return {
        "design": {
            "share": 0.8,
            "doc_ids": list(DOC_IDS),
            "mentions": [
                {"id": "intake", "text": "wf-intake"},
                {"id": "service", "text": "wf-self-service"},
                {"id": "zone-hospital", "text": "zone-hospital"},
                {"id": "zone-private", "text": "zone-private"},
                {"id": "zone-public", "text": "zone-public"},
                {"id": "status", "text": "referral.status"},
                {"id": "residency", "topic": "residency", "any": ["ext-large"]},
                {"id": "identity", "topic": "identity", "any": ["p-waitlist", "split", "duplicate"]},
                {"id": "criteria", "topic": "criteria", "any": ["v4", "draft"]},
                {"id": "hospital", "topic": "hospital", "any": ["h-ain"]},
                {"id": "citation", "kind": "citation"},
            ],
        },
        "readout": {
            "deadline": {"heading": "Deadline", "all": ["16", "week"], "cite": "cdo"},
            "data": {"heading": "Data", "all": ["ext-large", "private"], "cite": "dpo"},
            "failure": {"heading": "Failure", "any": ["timeout", "race-slot"]},
            "gate": {"heading": "Gate", "cite": "pol-stage-gate"},
        },
        "individual": {
            "tool": "safety.redirect",
            "document": "pol-clinical-safety",
            "refused": True,
        },
    }

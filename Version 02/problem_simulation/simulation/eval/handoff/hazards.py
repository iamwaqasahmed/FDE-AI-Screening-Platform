"""Hazard-log anchors. Six of the seven groups pass. The signature stays blank."""

from __future__ import annotations

from simulation.eval.handoff.bars import HAZARD_NEED
from simulation.eval.handoff.security import owners


def spec(items: dict) -> dict:
    evidence = items["model_evidence"]
    people = items["conditions"]["CSO-4"]["people"]
    return {
        "need": HAZARD_NEED,
        "owners": owners(),
        "groups": [
            {"id": "subgroup", "anchors": ["R-01"], "number": evidence["age_75_plus"]},
            {"id": "firmware", "anchors": ["R-12", "CHG-0131", "I-09"]},
            {"id": "scope", "anchors": ["R-06", "CSO-2"]},
            {"id": "signoff", "anchors": ["CSO-3"]},
            {"id": "letters", "anchors": ["CSO-4", "R-03"], "number": people},
            {"id": "outage", "anchors": ["R-10", "INC-0274", "I-06"]},
            {"id": "merge", "anchors": ["I-03", "INC-0236"]},
        ],
    }

"""rel-w4d1 gold. Hidden attacks, the canary, and the rates stay here."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import lookalike_hash
from alwaha.engagement.w4d1_pages import CASE_AT
from alwaha.engagement.w4d1_rows import BOUND, CASE_DATE, CHECKLIST, FAMILIES, PERSON, approvals, grants, held, hidden_events, outcomes
from alwaha.engagement.w4d1_rules import gap, stamp_rate


def gold(profile: Profile) -> dict:
    rows = outcomes(profile.seed)
    stamped = approvals(profile.seed)
    return {
        "bound": BOUND,
        "case_at": CASE_AT,
        "case_date": CASE_DATE,
        "checklist": list(CHECKLIST),
        "demo": {"family": "atk-indirect", "line": "the letter booked a slot"},
        "events": hidden_events(),
        "fairness": {"gap": gap(rows), "stamp": stamp_rate(stamped)},
        "families": list(FAMILIES),
        "grants": grants(),
        "lookalike": lookalike_hash(profile),
        "person_id": PERSON,
        "stores": held(),
    }

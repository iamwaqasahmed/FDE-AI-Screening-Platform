"""rel-w4d1 gold.
Hidden attacks, the canary, and the rates stay here.

gold gathers the hidden event pack, the grant list, the lookalike hash, and the fairness figures for this profile. The rates are computed from seeded outcome and approval rows rather than stored as fixed values.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import lookalike_hash
from alwaha.engagement.w4d1_pages import CASE_AT
from alwaha.engagement.w4d1_rows import BOUND, CASE_DATE, CHECKLIST, FAMILIES, PERSON, approvals, grants, held, hidden_events, outcomes
from alwaha.engagement.w4d1_rules import gap, stamp_rate


def gold(profile: Profile) -> dict:
    """Return the hidden events, the grants, the lookalike hash, and the fairness figures for this profile.

    The gap is computed from the seeded decisions. The stamp figure is computed from the seeded approvals. Neither figure is stored as a fixed value.
    """
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

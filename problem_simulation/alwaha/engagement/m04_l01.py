"""rel-m04-l01 gold.
Hidden attacks, the canary, and the rates stay here.

gold gathers the hidden event pack, the grant list, the lookalike hash, and the fairness figures for this profile. The rates are computed from seeded outcome and approval rows rather than stored as fixed values.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.m02_l04 import lookalike_hash
from alwaha.engagement.m04_l01_pages import CASE_AT
from alwaha.engagement.m04_l01_rows import BOUND, CASE_DATE, CHECKLIST, FAMILIES, PERSON, approvals, grants, held, hidden_events, outcomes
from alwaha.engagement.m04_l01_rules import gap, stamp_rate


def gold(profile: Profile) -> dict:
    """Return the hidden events, the grants, the lookalike hash, and the fairness figures for this profile.

    The gap is computed from the seeded decisions. The stamp figure is computed from the seeded approvals. Neither figure is stored as a fixed value.
    """
    # Seeded decisions and seeded approvals. The figures below are computed from these, not stored.
    rows = outcomes(profile.seed)
    stamped = approvals(profile.seed)
    return {
        # Case window and the checklist.
        "bound": BOUND,
        "case_at": CASE_AT,
        "case_date": CASE_DATE,
        "checklist": list(CHECKLIST),
        "demo": {"family": "atk-indirect", "line": "the letter booked a slot"},
        # Hidden events, and the fairness figures from the seeded rows.
        "events": hidden_events(),
        "fairness": {"gap": gap(rows), "stamp": stamp_rate(stamped)},
        "families": list(FAMILIES),
        # Grants, the lookalike, the person, and the held stores.
        "grants": grants(),
        "lookalike": lookalike_hash(profile),
        "person_id": PERSON,
        "stores": held(),
    }

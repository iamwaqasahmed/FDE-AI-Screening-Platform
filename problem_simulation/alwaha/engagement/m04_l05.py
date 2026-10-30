"""rel-m04-l05 gold.
The leave lag and the survey count stay here.

Both figures are derived from the profile seed. The rest of the object names the blocked work, the clock field, the cancel event, the owner, and the readout sections the closing page is checked against.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.m04_l05_rows import leave_lag, survey_phone


def gold(profile: Profile) -> dict:
    """Return the closing expectations for this profile.

    The leave lag and the phone-only count move with the seed. The readout sections name what the closing page must mention. The blocked list names the work that stays out.
    """
    return {
        # Work that stays out, the clock field, the demo question, and the cancel event.
        "blocked": ["p-triage"],
        "clock": "referred_at",
        "demo": {"question": "Which benefit is counted twice?"},
        "event": "session.cancelled",
        # The leave lag and the phone-only count. Both come from this profile's seed.
        "leave_lag": leave_lag(profile.seed),
        "owner": "med-dir",
        "phone_only": survey_phone(profile.seed),
        # Readout sections the closing page is checked against.
        "readout": {
            "asks": "Asks",
            "sections": [
                {"all": ["p-clock", "identity"], "heading": "Ranking", "id": "ranking"},
                {"all": ["summary"], "heading": "Handoff", "id": "handoff"},
                {"all": ["session.cancelled"], "heading": "Leave", "id": "leave"},
                {"all": ["same", "call"], "heading": "Benefit", "id": "benefit"},
                {"all": ["phone-only", "phc-rim"], "heading": "Channel", "id": "channel"},
            ],
        },
    }

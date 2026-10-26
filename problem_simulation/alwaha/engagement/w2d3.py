"""rel-w2d3 fixtures.
The old receipt delay stays in the gold.

The receipt clock, the working-day cases, the Hijri samples, and the channel scripts live here. gold turns each case start into a due date on working days and keeps the old delay beside the new interval so a submission that still uses the old delay can be seen.
"""

from __future__ import annotations

from datetime import date

from alwaha.config.profile import Profile
from alwaha.world.calendar import add_working_days, holiday_dates

OLD_DELAY_SECONDS = 30
INTERVAL_MINUTES = 5
SWITCH = "receipt-late"
CLAUSES = (
    "plain-language",
    "caregiver-complete",
    "named-control",
    "one-action",
)
CASES = (
    {"id": "thursday", "start": "2027-01-21", "count": 2},
    {"id": "eid", "start": "2027-03-09", "count": 3},
)


def receipt_clock() -> dict:
    """Return the interval and the switch name the new receipt path uses."""
    return {"minutes": INTERVAL_MINUTES, "switch": SWITCH}


def cases() -> list[dict]:
    """Return a copy of each working-day case so a caller cannot change the constant."""
    return [dict(row) for row in CASES]


def hijri_rows() -> list[dict]:
    """Return the month-end and month-start samples the calendar conversion is checked with."""
    return [
        {"id": "month-end", "value": "1448-07-29"},
        {"id": "month-start", "value": "1448-08-01"},
    ]


def scripts() -> list[dict]:
    """Return the channel scripts: a short status ask, a caregiver ask, and the same ask with no app."""
    return [
        {
            "actor": "patient",
            "id": "status-short",
            "layer": "foundation",
            "task": "Ask where the referral is. Use a short message.",
        },
        {
            "actor": "caregiver",
            "id": "caregiver",
            "layer": "foundation",
            "task": "A caregiver asks about her mother's referral.",
        },
        {
            "actor": "pop-literacy",
            "id": "phone-only",
            "layer": "advanced",
            "task": "Ask the same question by phone, with no app.",
        },
    ]


def model_fixture(profile: Profile) -> dict:
    """Return a booked-visit reply that includes this profile's canary."""
    return {"intent": "status", "text": f"The visit is booked. {profile.canary()}"}


def gold(profile: Profile) -> dict:
    """Return the due dates, the required clauses, the old delay, and the script outcomes.

    Each due date walks the case start forward by that case's working-day count and skips holidays. The profile is unused because none of these expectations move with the seed.
    """
    # Nothing here depends on the profile. The name is kept so every gold function has the same signature.
    del profile
    holidays = set(holiday_dates())
    rows = []
    for case in CASES:
        start = date.fromisoformat(case["start"])
        due = add_working_days(start, case["count"], holidays).isoformat()
        rows.append({"count": case["count"], "due": due, "id": case["id"], "start": case["start"]})
    return {
        "cases": rows,
        "clauses": list(CLAUSES),
        "interval_minutes": INTERVAL_MINUTES,
        "old_delay_seconds": OLD_DELAY_SECONDS,
        "scripts": [
            {"booked": False, "id": "status-short", "layer": "foundation", "outcome": "status"},
            {"booked": False, "id": "caregiver", "layer": "foundation", "outcome": "delegate"},
            {"booked": False, "id": "phone-only", "layer": "advanced", "outcome": "callback"},
        ],
        "switch": SWITCH,
    }

"""rel-w2d3 fixtures. The old receipt delay stays in the gold."""

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
    return {"minutes": INTERVAL_MINUTES, "switch": SWITCH}


def cases() -> list[dict]:
    return [dict(row) for row in CASES]


def hijri_rows() -> list[dict]:
    return [
        {"id": "month-end", "value": "1448-07-29"},
        {"id": "month-start", "value": "1448-08-01"},
    ]


def scripts() -> list[dict]:
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
    return {"intent": "status", "text": f"The visit is booked. {profile.canary()}"}


def gold(profile: Profile) -> dict:
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

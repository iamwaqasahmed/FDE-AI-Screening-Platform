"""Ain nightly files, and travel minutes. Rim is the long trip."""

from __future__ import annotations

from alwaha.people.dates import shift_date

RIM_MINUTES = 180
NEAR_MINUTES = 25


def nightly(profile) -> list[dict]:
    nights = ("2027-01-10", "2027-01-11", "2027-01-12")
    rows = []
    for index, night in enumerate(nights):
        arrived = index != 1
        rows.append(
            {
                "facility": "h-ain",
                "night": shift_date(night, profile.date_shift_days),
                "arrived": arrived,
                "slots": 4 if arrived else 0,
                "last_file_wins": True,
            }
        )
    return rows


def travel(profile) -> list[dict]:
    return [
        {"origin": "phc-rim", "destination": "h-wadi", "minutes": RIM_MINUTES},
        {"origin": "phc-nakhl-01", "destination": "h-nakhl", "minutes": NEAR_MINUTES},
        {"origin": "phc-safra-03", "destination": "h-safra", "minutes": NEAR_MINUTES},
        {"origin": "phc-wadi-02", "destination": "h-wadi", "minutes": NEAR_MINUTES + (profile.seed % 5)},
    ]

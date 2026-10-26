"""Ain nightly files, and travel minutes. Rim is the long trip.

Three nights are written. The middle night is the one that does not arrive, so that night has no slots. The other nights arrive and keep their slots. Each row says the last file wins. The travel table pairs an origin with a destination. The Wadi leg from the nearby primary center adds a small seed offset. Rim uses the long minute value.
"""

from __future__ import annotations

from alwaha.people.dates import shift_date

RIM_MINUTES = 180
NEAR_MINUTES = 25


def nightly(profile) -> list[dict]:
    """Return the Ain nightly rows, with dates shifted when the profile moves the calendar."""
    nights = ("2027-01-10", "2027-01-11", "2027-01-12")
    rows = []
    for index, night in enumerate(nights):
        # The middle night is the missed arrival. The nights on either side arrive.
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
    """Return origin, destination, and minutes. One nearby leg moves with the seed.

    The steps list the long Rim leg and the short legs, and they add a seed offset on the nearby Wadi leg.
    """
    return [
        {"origin": "phc-rim", "destination": "h-wadi", "minutes": RIM_MINUTES},
        {"origin": "phc-nakhl-01", "destination": "h-nakhl", "minutes": NEAR_MINUTES},
        {"origin": "phc-safra-03", "destination": "h-safra", "minutes": NEAR_MINUTES},
        {"origin": "phc-wadi-02", "destination": "h-wadi", "minutes": NEAR_MINUTES + (profile.seed % 5)},
    ]

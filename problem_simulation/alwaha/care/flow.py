"""Referrals, bookings, DNA labels, and SLA-clock breaches from the people and the need.

Each person keeps the first need only, so a later need does not open a second referral. Odd referral numbers are left unbooked. Booked rows take the long trip when the person is in Rim and the short trip otherwise. A reminder alternates. Insurance lapses on the stride and is active otherwise. prior_dna stays false on every row this builder writes. The attendance draw is compared with the probability: a draw above it is a miss. Breach rows cover only the opening slice of referrals, and each of those rows says Friday is not a working day.
"""

from __future__ import annotations

import hashlib

from alwaha.behavior.attendance import probability
from alwaha.capacity.travel import RIM_MINUTES

def referrals(needs: list[dict]) -> list[dict]:
    """Return one referral per person, using the first need seen for that person."""
    seen: dict[str, dict] = {}
    for need in needs:
        # A later need for the same person does not replace the first.
        seen.setdefault(need["person_id"], need)
    rows = []
    for person_id in sorted(seen):
        need = seen[person_id]
        rows.append(
            {
                "referral_id": f"r-{len(rows):06d}",
                "person_id": person_id,
                "specialty": need["specialty"],
                "submitted_on": need["onset"],
                "duplicate": False,
            }
        )
    return rows


def bookings(profile, people: list[dict], referral_rows: list[dict]) -> list[dict]:
    """Return bookings for the even referral numbers, with a drawn did-not-attend label."""
    by_id = {row["person_id"]: row for row in people}
    rows = []
    for referral in referral_rows:
        if int(referral["referral_id"].split("-")[1]) % 2:
            # Odd referral numbers stay unbooked so the world contains both states.
            continue
        person = by_id[referral["person_id"]]
        # Rim takes the long trip. Every other district takes the short trip.
        travel = RIM_MINUTES if person["district"] == "d-rim" else 25
        row = {
            "booking_id": f"b-{len(rows):06d}",
            "referral_id": referral["referral_id"],
            "person_id": referral["person_id"],
            "district": person["district"],
            "lead_days": 10,
            "travel_minutes": travel,
            "prior_dna": False,
            # Even booking counts are reminded. The lapse stride marks insurance inactive.
            "reminded": len(rows) % 2 == 0,
            "insurance": "lapsed" if len(rows) % 17 == 0 else "active",
        }
        row["p_attend"] = round(probability(row), 4)
        # A draw above the attendance probability is a miss.
        row["did_not_attend"] = _draw(profile.seed, row["booking_id"]) > row["p_attend"]
        rows.append(row)
    return rows


def breaches(referral_rows: list[dict]) -> list[dict]:
    """Return breach rows for the opening slice of referrals.

    The steps take the opening referrals and record each submission day as the clock start, with Friday excluded from the working week and the breach marked.
    """
    rows = []
    for referral in referral_rows[:2]:
        rows.append(
            {
                "referral_id": referral["referral_id"],
                "clock_starts": referral["submitted_on"],
                "friday_is_working": False,
                "breach": True,
            }
        )
    return rows


def _draw(seed: int, booking_id: str) -> float:
    """Return a unit-interval draw that is stable for this seed and booking id."""
    digest = hashlib.sha256(f"{seed}:{booking_id}".encode()).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF

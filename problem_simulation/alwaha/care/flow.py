"""Referrals, bookings, DNA labels, and SLA-clock breaches from the people and the need."""

from __future__ import annotations

import hashlib

from alwaha.behavior.attendance import probability
from alwaha.capacity.travel import RIM_MINUTES

def referrals(needs: list[dict]) -> list[dict]:
    seen: dict[str, dict] = {}
    for need in needs:
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
    by_id = {row["person_id"]: row for row in people}
    rows = []
    for referral in referral_rows:
        if int(referral["referral_id"].split("-")[1]) % 2:
            continue
        person = by_id[referral["person_id"]]
        travel = RIM_MINUTES if person["district"] == "d-rim" else 25
        row = {
            "booking_id": f"b-{len(rows):06d}",
            "referral_id": referral["referral_id"],
            "person_id": referral["person_id"],
            "district": person["district"],
            "lead_days": 10,
            "travel_minutes": travel,
            "prior_dna": False,
            "reminded": len(rows) % 2 == 0,
            "insurance": "lapsed" if len(rows) % 17 == 0 else "active",
        }
        row["p_attend"] = round(probability(row), 4)
        row["did_not_attend"] = _draw(profile.seed, row["booking_id"]) > row["p_attend"]
        rows.append(row)
    return rows


def breaches(referral_rows: list[dict]) -> list[dict]:
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
    digest = hashlib.sha256(f"{seed}:{booking_id}".encode()).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF

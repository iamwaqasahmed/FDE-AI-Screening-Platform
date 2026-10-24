"""rel-w4d4 gold. The SAR split and the arrival dates stay here."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w4d4_rows import (
    APPROVALS,
    budget_seconds,
    hospitals,
    lead_time,
    rent_days,
    replicas,
    timeout_seconds,
)
from alwaha.engagement.w4d4_rules import arrival, choice, split


def gold(profile: Profile) -> dict:
    note = lead_time(profile.seed)
    sites = replicas(profile)
    sheet = hospitals(profile.seed)
    price = int(sheet["local_per_1k"])
    costs = split(sheet, price)
    lookalike = sites["sites"][1]["models"][-1]
    return {
        "budget_seconds": budget_seconds(profile.seed),
        "buy_arrives": arrival(note, "buy"),
        "deadline": str(note["deadline"]),
        "demo": {"down": "site-a", "serving": "site-b"},
        "hospital_sar": costs,
        "local_sar": sum(costs.values()),
        "lookalike_hash": str(lookalike["hash"]),
        "lookalike_id": str(lookalike["id"]),
        "pending": list(APPROVALS),
        "rent_arrives": arrival(note, "rent"),
        "rent_days": rent_days(profile.seed),
        "route": choice(note),
        "timeout_seconds": timeout_seconds(profile.seed),
    }

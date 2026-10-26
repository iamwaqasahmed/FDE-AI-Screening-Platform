"""rel-w4d4 gold.
The SAR split and the arrival dates stay here.

gold asks the reference rules which route meets the deadline, when each route would arrive, and how the local cost splits across hospitals. The lookalike is the last model on the backup site, which is the unregistered candidate added beside the approved models.
"""

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
    """Return the route, both arrival dates, the hospital split, and the lookalike for this profile.

    The lookalike is the last model on the backup site. That site's list is the approved models plus the unregistered candidate.
    """
    note = lead_time(profile.seed)
    sites = replicas(profile)
    sheet = hospitals(profile.seed)
    price = int(sheet["local_per_1k"])
    costs = split(sheet, price)
    # The backup site's model list ends with the unregistered candidate.
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

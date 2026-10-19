"""What the duplicate prints cost, and what a careful re-send costs."""

from __future__ import annotations

from simulation.economics.costs import cost


def facts(items: dict, resend: list[dict]) -> dict:
    duplicates = int(items["drop_incident"]["duplicate_rows"])
    reprints = sum(row["action"] == "resend" for row in resend)
    duplicate_gbp = round(duplicates * cost("letter"), 2)
    reprint_gbp = round(reprints * cost("letter_reprint"), 2)
    return {"incident_cost": {
        "duplicates_gbp": duplicate_gbp,
        "resends_gbp": reprint_gbp,
        "total_gbp": round(duplicate_gbp + reprint_gbp, 2),
    }}

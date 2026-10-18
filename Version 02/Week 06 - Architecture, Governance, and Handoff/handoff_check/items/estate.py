"""The current estate, the flow rules, and the load figure."""

from __future__ import annotations

from handoff_check.items.match import near, same

ORDERED = ("callback_path", "callback_zones")
SETS = ("zones", "fhir", "no_backup")
LEVELS = ("peak_band", "peak_rpm", "peak_month", "design_rpm", "event_lag_minutes", "grader_tier", "vendor_tier", "grader_waits")
RATES = ("season_max", "vendor_availability", "vendor_downtime_hours")


def current_state(answer: dict, gold: dict) -> bool:
    row = gold["items"]["current_state"]
    ordered = all(answer.get(key) == row[key] for key in ORDERED)
    sets = all(same(answer.get(key), row[key]) for key in SETS)
    return ordered and sets and same(answer.get("tiers"), row["tiers"]) and answer.get("vendor_hosting") == row["vendor_hosting"]


def flow_rules(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["flow_rules"])


def service_levels(answer: dict, gold: dict) -> bool:
    row = gold["items"]["service_levels"]
    rates = all(near(answer.get(key), row[key], 0.05) for key in RATES)
    return rates and same({key: answer.get(key) for key in LEVELS}, {key: row[key] for key in LEVELS})

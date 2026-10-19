"""Tier 3 and the Week 3 numbers the model card has to carry."""

from __future__ import annotations

from handoff_check.items.match import near, same
from simulation.eval.handoff.bars import RATE_TOLERANCE

RATES = ("cut", "sensitivity", "age_75_plus", "age_under_75", "claimed", "drift_before", "drift_after")
TEXT = ("sites", "claim_holds_overall", "claim_population", "drift_site", "inventory_lags")


def tier_three(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["tier_three"])


def model_evidence(answer: dict, gold: dict) -> bool:
    row = gold["items"]["model_evidence"]
    rates = all(near(answer.get(key), row[key], RATE_TOLERANCE) for key in RATES)
    return rates and same({key: answer.get(key) for key in TEXT}, {key: row[key] for key in TEXT})

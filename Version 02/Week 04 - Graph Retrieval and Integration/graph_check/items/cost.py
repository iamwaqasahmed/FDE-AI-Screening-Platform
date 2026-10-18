"""Pounds, within a pound."""

from __future__ import annotations

from course.checks.rules import close
from simulation.eval.graph.bars import COST_TOLERANCE

AMOUNTS = ("duplicates_gbp", "resends_gbp", "total_gbp")


def incident_cost(answer: dict, gold: dict) -> bool:
    row = gold["items"]["incident_cost"]
    return all(close(answer.get(key), row[key], COST_TOLERANCE, relative=False) for key in AMOUNTS)

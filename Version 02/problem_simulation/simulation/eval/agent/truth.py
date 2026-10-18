"""Hidden values the debrief may quote and the invariants check."""

from __future__ import annotations

from simulation.eval.agent.bars import VETO_TASKS, WILSON_Z
from simulation.eval.graph.cohort import hidden_overdue


def facts(world: dict, items: dict) -> dict:
    integration = world["gold"].get("integration", {})
    return {
        "hidden_lost": integration.get("overdue_chase_letters_lost"),
        "hidden_overdue": hidden_overdue(world),
        "pilot_people": integration.get("overdue_people_primary_care"),
        "wilson_lower": wilson(items["veto_evidence"]["stop_tasks"], items["veto_evidence"]["stop_tasks"]),
        "veto_tasks": VETO_TASKS,
    }


def wilson(successes: int, trials: int, z: float = WILSON_Z) -> float:
    if trials <= 0:
        return 0.0
    proportion = successes / trials
    denom = 1 + z * z / trials
    centre = proportion + z * z / (2 * trials)
    margin = z * (proportion * (1 - proportion) / trials + z * z / (4 * trials * trials)) ** 0.5
    return round((centre - margin) / denom, 4)

"""The two numbers the conditions need: the earliest go-live, and the lost chase letters."""

from __future__ import annotations


def earliest(world: dict) -> str:
    dated = world["gold"].get("pilot_date", {}).get("earliest_pilot")
    if dated:
        return str(dated)
    from datetime import date

    from simulation.eval.agent.backlog import facts
    from simulation.eval.agent.paths import earliest as path

    items, _frame = facts(world)
    return path(date.fromisoformat(items["pace"]["build_done"]))["go_live"]


def lost(world: dict) -> tuple[int, bool]:
    row = world["gold"].get("graph", {}).get("items", {}).get("chase_lost_people")
    if row:
        return int(row["local_ids"]), bool(row["is_upper_bound"])
    from simulation.eval.graph import cohort, links, reconcile

    linked = links.prepare(world, reconcile.frame(world))
    items, _resend = cohort.facts(world, linked)
    found = items["chase_lost_people"]
    return int(found["local_ids"]), bool(found["is_upper_bound"])

"""One pure entry point: volumes, calls, value models, and problem costs computed from the world."""

from __future__ import annotations

from simulation.economics.calls import annual_calls_by_reason, expected_calls
from simulation.economics.dependencies import prerequisites, unlocks
from simulation.economics.problems import costliest, most_voiced, problem_costs
from simulation.economics.value import value_models
from simulation.economics.volumes import VALUE_FROM, YEARS, phones_by_district, volumes
from simulation.world.clock import SNAPSHOT


def calls_frame(world: dict):
    last = f"{SNAPSHOT.year}-{SNAPSHOT.month - 1:02d}" if SNAPSHOT.month > 1 else f"{SNAPSHOT.year - 1}-12"
    return expected_calls(world["events"], world["invitations"], last)


def economic_summary(world: dict) -> dict:
    v = volumes(world)
    v["phones_by_district"] = phones_by_district(world)
    v["calls"] = annual_calls_by_reason(calls_frame(world), VALUE_FROM.isoformat()[:7], SNAPSHOT.isoformat()[:7], YEARS)
    models = value_models(world, v)
    net = {row["key"]: row["net_annual_gbp"] for row in models}
    for row in models:
        row["depends_on"] = prerequisites(row["key"])
        row["unlocks"] = unlocks(row["key"])
        row["unlocked_net_gbp"] = round(sum(max(net[key], 0.0) for key in row["unlocks"]), 0)
    costs = problem_costs(v)
    return {
        "volumes": v,
        "opportunities": models,
        "net_rank": sorted(net, key=lambda key: (-net[key], key)),
        "problem_costs": costs,
        "costliest_problem": costliest(costs),
        "most_voiced_problem": most_voiced(costs),
    }

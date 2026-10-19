"""The account, the models, the log, the sweep, and the veto sample."""

from __future__ import annotations

from agent_check.items.match import near, same
from simulation.eval.agent.bars import CLOCK_DAY_TOLERANCE, COST_TOLERANCE, WILSON_TOLERANCE


def service_account(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["service_account"])


def model_routing(answer: dict, gold: dict) -> bool:
    row = gold["items"]["model_routing"]
    keys = ("personal", "official_only", "public_only", "cheapest_generator", "multi_hop_budget")
    costs = answer.get("multi_hop_cost") if isinstance(answer.get("multi_hop_cost"), dict) else {}
    priced = all(near(costs.get(model), cost, COST_TOLERANCE) for model, cost in row["multi_hop_cost"].items())
    return priced and same({key: answer.get(key) for key in keys}, {key: row[key] for key in keys})


def audit_and_logs(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["audit_and_logs"])


def sweep_summary(answer: dict, gold: dict) -> bool:
    row = gold["items"]["sweep_summary"]
    keys = ("rows", "blank_hospital", "with_local_clock", "clause_ids")
    return same({key: answer.get(key) for key in keys}, {key: row[key] for key in keys}) and near(
        answer.get("median_days_over"), row["median_days_over"], CLOCK_DAY_TOLERANCE)


def veto_evidence(answer: dict, gold: dict) -> bool:
    row = gold["items"]["veto_evidence"]
    return answer.get("stop_tasks") == row["stop_tasks"] and answer.get("families") == row["families"] and near(
        answer.get("wilson_lower"), row["wilson_lower"], WILSON_TOLERANCE)

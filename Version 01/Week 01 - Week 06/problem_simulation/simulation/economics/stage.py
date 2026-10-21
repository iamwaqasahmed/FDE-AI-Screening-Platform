"""Economics stage: public unit costs, budgets, and monthly attendance; truth value models, dependencies, and reminder gold."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.economics.budgets import budgets_frame, cost_centre_map
from simulation.economics.costs import harm_weights_frame, unit_costs_frame
from simulation.economics.dependencies import dependencies_frame
from simulation.economics.reminder import attendance_by_month, reminder_gold
from simulation.economics.summary import economic_summary

PUBLIC = "engagement/economics"
TRUTH = "truth/economics"


def build(world: dict, rng: np.random.Generator) -> None:
    summary = economic_summary(world)
    files = world["files"]
    files[f"{PUBLIC}/unit_costs.csv"] = unit_costs_frame()
    files[f"{PUBLIC}/budgets.csv"] = budgets_frame(world)
    files[f"{PUBLIC}/attendance_by_month.csv"] = attendance_by_month(world["invitations"])
    files[f"{TRUTH}/opportunities.json"] = {
        "window": summary["volumes"]["window"],
        "net_rank": summary["net_rank"],
        "opportunities": summary["opportunities"],
        "volumes": {key: value for key, value in summary["volumes"].items() if key != "window"},
        "problem_costs": summary["problem_costs"],
    }
    files[f"{TRUTH}/dependencies.csv"] = dependencies_frame()
    files[f"{TRUTH}/harm_weights.csv"] = harm_weights_frame()
    files[f"{TRUTH}/cost_centre_map.csv"] = cost_centre_map()
    gold = world.setdefault("gold", {})
    gold["reminder_uplift"] = reminder_gold(world["invitations"])
    gold["opportunity_values"] = [
        {key: row[key] for key in ("key", "net_annual_gbp", "value_range_gbp", "depends_on", "blockers", "must_cite")}
        for row in summary["opportunities"]
    ]
    world.setdefault("tables", {})["opportunity_net"] = _net_table(summary)


def _net_table(summary: dict) -> pd.DataFrame:
    rows = [{"key": row["key"], "net_annual_gbp": row["net_annual_gbp"]} for row in summary["opportunities"]]
    return pd.DataFrame(rows)

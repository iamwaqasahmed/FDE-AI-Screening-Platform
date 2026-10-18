"""Eligible people and coverage, both as the version-3 extract lets a team compute them."""

from __future__ import annotations

from datetime import timedelta

import pandas as pd

from simulation.eval.enterprise.drop import v3_frame
from simulation.systems.warehouse import _snapshot
from simulation.world.clock import SNAPSHOT, iso


def counts(world: dict) -> dict:
    frame = v3_frame(world)
    eligible = frame["FLAG"].eq("") & ~frame["LOCAL_PID"].str.startswith("LX")
    by_district = frame.loc[eligible].groupby("DISTRICT").size()
    warehouse = _warehouse(world)
    return {
        "eligible": int(eligible.sum()),
        "eligible_tolerance": 0.005,
        "by_district": {str(name): int(count) for name, count in sorted(by_district.items())},
        "coverage": _coverage(world, frame, eligible),
        "coverage_days": 730,
        "coverage_tolerance": 0.01,
        "warehouse_eligible": warehouse["eligible"],
        "warehouse_covered": warehouse["covered"],
        "warehouse_months": 12,
        "rows": int(len(frame)),
    }


def _coverage(world: dict, frame: pd.DataFrame, eligible: pd.Series) -> int:
    snapshot = _snapshot(world["people"], world["events"], world["identifiers"])
    reissue = world["files"]["truth/drops/week-2/reissue.csv"]
    renamed = dict(zip(reissue["OLD_REGISTRY_NO"], reissue["NEW_REGISTRY_NO"]))
    number = snapshot["registry_no"].map(lambda old: renamed.get(old, old))
    living = set(frame.loc[eligible, "REGISTRY_NO"])
    cutoff = iso(SNAPSHOT - timedelta(days=730))
    dated = snapshot["last_screen_date"].ne("") & snapshot["last_screen_date"].ge(cutoff)
    return int((number.isin(living) & dated).sum())


def _warehouse(world: dict) -> dict:
    snapshot = _snapshot(world["people"], world["events"], world["identifiers"])
    eligible = snapshot["flag"].isin(["", "DECEASED"])
    cutoff = (pd.Timestamp(SNAPSHOT) - pd.DateOffset(months=12)).strftime("%Y-%m-%d")
    dated = snapshot["last_screen_date"].ne("") & snapshot["last_screen_date"].ge(cutoff)
    return {"eligible": int(eligible.sum()), "covered": int((eligible & dated).sum())}

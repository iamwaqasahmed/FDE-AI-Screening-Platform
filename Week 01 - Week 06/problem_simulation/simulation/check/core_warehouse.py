"""The warehouse must disagree with truth for the planted reasons, and only those."""

from __future__ import annotations

import sqlite3
from datetime import timedelta

import pandas as pd

from simulation.paths import HANDOVER
from simulation.world.clock import SNAPSHOT, iso


def check(world: dict, errors: list[str]) -> None:
    connection = sqlite3.connect(HANDOVER / "warehouse" / "hartland.sqlite")
    try:
        mart = pd.read_sql("SELECT eligible, covered FROM person_mart", connection)
    finally:
        connection.close()
    people = world["people"]
    warehouse_eligible = int(mart["eligible"].sum())
    truth_eligible = int(((people["alias_of"] == "") & (people["flag"] == "")).sum())
    if warehouse_eligible == truth_eligible:
        errors.append("Warehouse eligibility matches the truth count.")
    snapshot = pd.read_csv(HANDOVER / "warehouse" / "registry_snapshot.csv", dtype=str).fillna("")
    expected = int(snapshot["flag"].isin(["", "DECEASED"]).sum())
    if warehouse_eligible != expected:
        errors.append(f"Warehouse eligible {warehouse_eligible} != snapshot rule {expected}")
    if int(mart["covered"].sum()) == truth_covered(world):
        errors.append("Warehouse coverage window matches the two-year rule.")


def truth_covered(world: dict) -> int:
    events = world["events"]
    people = world["people"]
    screened = events[(events["cohort"] == "completed") & (events["grade"] != "")]
    last = screened.groupby("person_uid")["photo_date"].max()
    eligible = people[(people["alias_of"] == "") & (people["flag"] == "")]
    dates = eligible["person_uid"].map(last).fillna("")
    cutoff = iso(SNAPSHOT - timedelta(days=730))
    return int(((dates != "") & (dates >= cutoff)).sum())

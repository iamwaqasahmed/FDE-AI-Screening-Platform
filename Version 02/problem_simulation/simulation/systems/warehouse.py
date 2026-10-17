"""The mart is built by SQL that still counts deceased people and uses a one-year window."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso

BUILD_SQL = """
-- Loaded from registry_snapshot.csv into table registry before this script runs.
-- Eligible here still includes a deceased flag. The register rule does not.
-- Covered here uses twelve months. The register rule in force uses two years.
DROP TABLE IF EXISTS person_mart;
CREATE TABLE person_mart AS
SELECT
  registry_no,
  district,
  flag,
  CASE
    WHEN flag IS NULL OR flag = '' OR upper(flag) = 'DECEASED' THEN 1
    ELSE 0
  END AS eligible,
  CASE
    WHEN last_screen_date IS NOT NULL
     AND last_screen_date != ''
     AND last_screen_date >= date('2026-10-01', '-12 months')
    THEN 1
    ELSE 0
  END AS covered
FROM registry;
"""


def write_warehouse(people: pd.DataFrame, events: pd.DataFrame, identifiers: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    snapshot = _snapshot(people, events, identifiers)
    snapshot.to_csv(folder / "registry_snapshot.csv", index=False)
    (folder / "build.sql").write_text(BUILD_SQL, encoding="utf-8")
    database = folder / "hartland.sqlite"
    if database.exists():
        database.unlink()
    connection = sqlite3.connect(database)
    try:
        snapshot.to_sql("registry", connection, index=False)
        connection.executescript(BUILD_SQL)
        connection.commit()
    finally:
        connection.close()


def _snapshot(people: pd.DataFrame, events: pd.DataFrame, identifiers: pd.DataFrame) -> pd.DataFrame:
    on = iso(SNAPSHOT)
    numbers = ids_on(identifiers, "registry_no", on)
    screened = events[(events["cohort"] == "completed") & (events["grade"] != "")]
    last = screened.groupby("person_uid")["photo_date"].max()
    recorded = (people["flag_recorded_on"] != "") & (people["flag_recorded_on"] <= on)
    frame = pd.DataFrame(
        {
            "registry_no": people["person_uid"].map(numbers).fillna(""),
            "surname": people["surname"].to_numpy(),
            "flag": [flag if shown else "" for flag, shown in zip(people["flag"], recorded)],
            "district": people["district"].to_numpy(),
            "last_screen_date": people["person_uid"].map(last).fillna(""),
        }
    )
    return frame[frame["registry_no"] != ""].reset_index(drop=True)

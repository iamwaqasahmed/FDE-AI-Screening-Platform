"""Week 2: the registry publishes schema v3, renames a field, adds columns, and reissues a batch of numbers."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.drops.common import add_drop
from simulation.drops.rules import NEW_FIELDS, RENAMED_FIELDS, REISSUED
from simulation.systems.resolve import ids_on
from simulation.world.engagement import REGISTRY_SCHEMA_V3
from simulation.world.sites import POSTCODE

ON = REGISTRY_SCHEMA_V3.isoformat()


def build(world: dict, rng: np.random.Generator) -> None:
    people, identifiers = world["people"], world["identifiers"]
    frame = _v3(people, identifiers)
    frame, reissue = _reissue(frame, rng)
    world["files"]["truth/drops/week-2/reissue.csv"] = reissue
    public = reissue.drop(columns=["person_uid"])
    files = {"registry/current_v3.csv": frame.drop(columns=["person_uid"]), "registry/reissue_batch.csv": public,
             "registry/schema_v3.md": _changelog()}
    brief = [
        "The ministry moved the registry extract to schema version 3 today and reissued a batch of registry numbers.",
        f"`{next(iter(RENAMED_FIELDS))}` is now `{next(iter(RENAMED_FIELDS.values()))}`. "
        f"New columns: {', '.join(NEW_FIELDS)}. Dates of birth are ISO dates in every row.",
        "Pipelines that join on the old column name or on a reissued number will silently drop people.",
    ]
    gold = {
        "change": "registry schema v3",
        "renamed": dict(RENAMED_FIELDS),
        "new_fields": list(NEW_FIELDS),
        "rows": int(len(frame)),
        "reissued": int(len(reissue)),
        "invalidates": ["week-1 registry loaders keyed on HOME_CLINIC", "joins on registry numbers in the reissue batch",
                        "date-of-birth parsing for spreadsheet serials (v3 is ISO only)"],
    }
    add_drop(world, 2, "Registry schema v3", brief, files, gold)


def _v3(people: pd.DataFrame, identifiers: pd.DataFrame) -> pd.DataFrame:
    live = people[people["diagnosis_date"] <= ON].copy()
    recorded = (live["flag_recorded_on"] != "") & (live["flag_recorded_on"] <= ON)
    flag = np.where(recorded, live["flag"], "")
    return pd.DataFrame({
        "person_uid": live["person_uid"],
        "REGISTRY_NO": live["person_uid"].map(ids_on(identifiers, "registry_no", ON)).fillna(""),
        "LOCAL_PID": live["person_uid"].map(ids_on(identifiers, "local_pid", ON)).fillna(""),
        "FORENAME": live["forename"],
        "SURNAME": live["surname"],
        "DOB": live["dob"],
        "SEX": live["sex"],
        "DISTRICT": live["district"],
        "DISTRICT_CODE": live["district"].map(POSTCODE),
        "REGISTERED_SITE": live["home_site"],
        "FLAG": flag,
        "FLAG_DATE": np.where(recorded, live["flag_recorded_on"], ""),
        "RECORD_STATUS": np.where(flag == "", "Active", flag),
        "SCHEMA_VERSION": "3",
    }).reset_index(drop=True)


def _reissue(frame: pd.DataFrame, rng: np.random.Generator) -> tuple[pd.DataFrame, pd.DataFrame]:
    pool = frame.index[(frame["REGISTRY_NO"] != "") & (frame["FLAG"] == "")].to_numpy()
    picks = np.sort(rng.choice(pool, size=min(REISSUED, len(pool)), replace=False))
    new_numbers = [f"HR9{order + 1:05d}" for order in range(len(picks))]
    reissue = pd.DataFrame({"person_uid": frame.loc[picks, "person_uid"].to_numpy(),
                            "OLD_REGISTRY_NO": frame.loc[picks, "REGISTRY_NO"].to_numpy(),
                            "NEW_REGISTRY_NO": new_numbers, "REISSUED_ON": ON})
    frame = frame.copy()
    frame.loc[picks, "REGISTRY_NO"] = new_numbers
    return frame, reissue


def _changelog() -> str:
    old, new = next(iter(RENAMED_FIELDS.items()))
    return "\n".join([
        "# Registry extract schema v3", "", f"Effective {ON}.", "",
        f"- Renamed: `{old}` to `{new}`.",
        "- Added: `DISTRICT_CODE` (two-letter postcode prefix), `FLAG_DATE` (date the flag was recorded), `SCHEMA_VERSION`.",
        "- `DOB` is always an ISO date. Spreadsheet serial numbers and day-first dates are gone.",
        "- A batch of registry numbers was reissued. `reissue_batch.csv` maps old to new numbers.",
        "- Version 2 files stop on the next month end.", "",
    ])

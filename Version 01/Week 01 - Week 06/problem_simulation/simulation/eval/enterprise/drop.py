"""What the week-2 registry drop changes, measured from the frames the drop itself writes."""

from __future__ import annotations

import calendar

import pandas as pd

from simulation.drops.rules import NEW_FIELDS, RENAMED_FIELDS, REISSUED
from simulation.drops.week2 import _v3
from simulation.systems.registry import _project
from simulation.systems.warehouse import _snapshot
from simulation.world.clock import SNAPSHOT, iso
from simulation.world.engagement import REGISTRY_SCHEMA_V3


def drop_facts(world: dict) -> dict:
    people, identifiers, events = world["people"], world["identifiers"], world["events"]
    current = _prepared(people, events)
    on = iso(SNAPSHOT)
    v2 = _project(current, identifiers, events, on, "new")
    v3 = _v3(people, identifiers)
    reissue = world["files"]["truth/drops/week-2/reissue.csv"]
    added = _added_local_ids(v2, v3)
    lost = _warehouse_lost(people, events, identifiers, reissue)
    return {
        "renamed": dict(RENAMED_FIELDS),
        "added": list(NEW_FIELDS),
        "dob": "iso",
        "v2_stops": month_end(REGISTRY_SCHEMA_V3).isoformat(),
        "reissued": int(len(reissue)),
        "reissued_expected": REISSUED,
        "warehouse_lost": lost,
        "local_ids_added": added,
        "rows": int(len(v3)),
    }


def _prepared(people: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    frame = people.copy()
    frame["ever_seen"] = frame["person_uid"].isin(events["person_uid"])
    frame["district_label"] = frame["district"]
    frame["dob_shown"] = frame["dob"]
    return frame


def _added_local_ids(v2: pd.DataFrame, v3: pd.DataFrame) -> int:
    """Local ids the version-2 extract blanks and version 3 restores. Joined on the id, not the row order."""
    blank = set(v2.loc[v2["LOCAL_PID"].eq(""), "REGISTRY_NO"]) - {""}
    restored = v3["REGISTRY_NO"].isin(blank) & v3["LOCAL_PID"].ne("")
    by_pid = v2["LOCAL_PID"].eq("") & v2["REGISTRY_NO"].eq("")
    return int(restored.sum() + by_pid.sum())


def _warehouse_lost(people, events, identifiers, reissue: pd.DataFrame) -> int:
    snapshot = _snapshot(people, events, identifiers)
    old = set(reissue["OLD_REGISTRY_NO"])
    return int(snapshot["registry_no"].isin(old).sum())


def month_end(day):
    return day.replace(day=calendar.monthrange(day.year, day.month)[1])


def api_facts() -> dict:
    """The registry API's version 3 is not the file the ministry published."""
    return {
        "keeps": ["home_clinic"],
        "missing": ["DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION"],
        "old_numbers": True,
    }


def v3_frame(world: dict) -> pd.DataFrame:
    """Version 3 extract including the reissued numbers, with the person id kept for gold only."""
    frame = _v3(world["people"], world["identifiers"])
    reissue = world["files"]["truth/drops/week-2/reissue.csv"].set_index("person_uid")["NEW_REGISTRY_NO"]
    frame["REGISTRY_NO"] = frame["person_uid"].map(reissue).fillna(frame["REGISTRY_NO"])
    return frame


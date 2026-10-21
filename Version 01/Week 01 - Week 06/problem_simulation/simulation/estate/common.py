"""Helpers the estate systems share: identifier lookups, minute timestamps, and the fault log."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.world.clock import SNAPSHOT

TRUTH = "truth/estate"
LONG_DATE = "%d %B %Y"


def base_people(world: dict) -> pd.DataFrame:
    people = world["people"]
    return people[people["alias_of"] == ""].reset_index(drop=True)


def id_map(identifiers: pd.DataFrame, id_type: str, relations: tuple[str, ...] = ("assigned",)) -> pd.Series:
    """person_uid -> the first identifier of this type with one of the relations."""
    pool = identifiers[(identifiers["id_type"] == id_type) & identifiers["relation"].isin(relations)]
    pool = pool[pool["id_value"] != ""].sort_values(["person_uid", "valid_from", "id_value"])
    return pool.groupby("person_uid")["id_value"].first()


def day_minutes(days, rng: np.random.Generator, start_hour: int = 8, end_hour: int = 18) -> pd.Series:
    """ISO dates plus a random working-hours minute, as datetimes."""
    base = pd.to_datetime(pd.Series(days, dtype="str"))
    offset = rng.integers(start_hour * 60, end_hour * 60, len(base))
    return base + pd.to_timedelta(offset, unit="min")


def stamp(values: pd.Series) -> np.ndarray:
    """Datetimes as 'YYYY-MM-DDTHH:MM' strings; missing values become ''."""
    array = values.to_numpy(dtype="datetime64[m]")
    text = np.datetime_as_string(array, unit="m")
    return np.where(np.isnat(array), "", text)


def day_text(values: pd.Series) -> np.ndarray:
    array = values.to_numpy(dtype="datetime64[D]")
    return np.where(np.isnat(array), "", np.datetime_as_string(array, unit="D"))


def snapshot_limit() -> pd.Timestamp:
    return pd.Timestamp(SNAPSHOT)


def log_fault(world: dict, system: str, entry: dict) -> None:
    world["files"].setdefault(f"{TRUTH}/faults.jsonl", []).append({"system": system, **entry})


def faults_for(world: dict, system: str, fault: str = "") -> list[dict]:
    rows = world["files"].get(f"{TRUTH}/faults.jsonl", [])
    return [row for row in rows if row["system"] == system and (not fault or row["fault"] == fault)]


def years_back(years: int) -> date:
    return date(SNAPSHOT.year - years, SNAPSHOT.month, SNAPSHOT.day)

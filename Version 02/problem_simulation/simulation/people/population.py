"""Canonical people, plus alias rows that are not extra humans."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from faker import Faker

from simulation.people.scenarios import assign_households, mark_silent_movers, mark_twins
from simulation.people.variants import canonical_pools
from simulation.world.clock import FLAG_LAG_DAYS, HISTORY_START, SNAPSHOT, iso
from simulation.world.quotas import (
    ALIASES,
    DECEASED,
    ELIGIBLE,
    FALSE_MERGE_PAIRS,
    MOVED,
    REUSE_DONORS,
    SPLITS,
)
from simulation.world.sites import POSTCODE, homes_for

EARLY_DEATH = date(2022, 1, 15)
LATEST_FLAG = date(2026, 7, 1)


def build_population(rng: np.random.Generator) -> pd.DataFrame:
    from simulation.world.clock import SEED

    Faker.seed(SEED)
    fake = Faker()
    variant_first, variant_last = canonical_pools()
    first_names = [fake.first_name() for _ in range(4000)] + variant_first * 30
    last_names = [fake.last_name() for _ in range(4000)] + variant_last * 30
    frames = [_block(district, count, "", rng, first_names, last_names) for district, count in ELIGIBLE.items()]
    frames += [_block(district, count, "DECEASED", rng, first_names, last_names) for district, count in DECEASED.items()]
    frames += [_block(district, count, "MOVED", rng, first_names, last_names) for district, count in MOVED.items()]
    people = pd.concat(frames, ignore_index=True)
    people.insert(0, "person_uid", [f"P{index + 1:07d}" for index in range(len(people))])
    people["alias_of"] = ""
    people["scenario"] = ""
    people["household"] = ""
    _force_early_deaths(people)
    _mark_scenarios(people)
    _copy_false_merge_demographics(people)
    mark_twins(people)
    assign_households(people, rng)
    mark_silent_movers(people, rng)
    people = _add_aliases(people)
    return people.sort_values("person_uid").reset_index(drop=True)


def _block(district: str, count: int, flag: str, rng: np.random.Generator, first_names: list[str], last_names: list[str]) -> pd.DataFrame:
    homes = homes_for(district)
    ages = rng.integers(18, 91, size=count)
    extra = rng.integers(0, 364, size=count)
    dob = pd.to_datetime(SNAPSHOT) - pd.to_timedelta((ages * 365.25 + extra).astype(int), unit="D")
    early = rng.random(count) < 0.9
    diagnosed = []
    for index, born in enumerate(dob):
        born_date = born.date()
        if early[index]:
            start = min(born_date + timedelta(days=20 * 365), HISTORY_START - timedelta(days=1))
            if start >= HISTORY_START:
                start = HISTORY_START - timedelta(days=400)
            diagnosed.append(start)
        else:
            diagnosed.append(HISTORY_START + timedelta(days=int(rng.integers(0, 1800))))
    travel_low, travel_high = _travel_band(district)
    flag_true, flag_recorded = _flags(flag, count, rng)
    return pd.DataFrame(
        {
            "forename": [first_names[int(i)] for i in rng.integers(0, len(first_names), size=count)],
            "surname": [last_names[int(i)] for i in rng.integers(0, len(last_names), size=count)],
            "dob": [iso(value.date()) for value in dob],
            "sex": _sex(rng, count),
            "district": district,
            "home_site": [homes[index % len(homes)] for index in range(count)],
            "diabetes_type": np.where(rng.random(count) < 0.9, "Type 2", "Type 1"),
            "diagnosis_date": [iso(value) if value < SNAPSHOT else iso(HISTORY_START) for value in diagnosed],
            "travel_burden": rng.integers(travel_low, travel_high, size=count),
            "postcode_sector": [f"{POSTCODE[district]}{int(n)}" for n in rng.integers(1, 5, size=count)],
            "flag": flag,
            "flag_true_on": flag_true,
            "flag_recorded_on": flag_recorded,
            "reuse_role": "",
        }
    )


def _sex(rng: np.random.Generator, count: int) -> np.ndarray:
    roll = rng.integers(0, 100, size=count)
    return np.where(roll < 49, "M", np.where(roll < 98, "F", "U"))


def _travel_band(district: str) -> tuple[int, int]:
    if district in {"North City", "East City"}:
        return 1, 3
    if district == "Hill Counties":
        return 3, 5
    return 4, 6


def _flags(flag: str, count: int, rng: np.random.Generator) -> tuple[list[str], list[str]]:
    if not flag:
        return [""] * count, [""] * count
    span = (LATEST_FLAG - date(2019, 1, 1)).days
    offsets = rng.integers(0, span, size=count)
    true_on = [date(2019, 1, 1) + timedelta(days=int(offset)) for offset in offsets]
    recorded = [value + timedelta(days=FLAG_LAG_DAYS) for value in true_on]
    return [iso(value) for value in true_on], [iso(value) for value in recorded]


def _force_early_deaths(people: pd.DataFrame) -> None:
    donors = people.index[people["flag"] == "DECEASED"].to_numpy()[:REUSE_DONORS]
    for offset, row_id in enumerate(donors):
        true_on = EARLY_DEATH + timedelta(days=offset % 60)
        people.at[row_id, "flag_true_on"] = iso(true_on)
        people.at[row_id, "flag_recorded_on"] = iso(true_on + timedelta(days=FLAG_LAG_DAYS))
        people.at[row_id, "reuse_role"] = "donor"


def _mark_scenarios(people: pd.DataFrame) -> None:
    eligible = people.index[(people["district"] == "North City") & (people["flag"] == "")].to_numpy()
    pair_rows = FALSE_MERGE_PAIRS * 2
    people.loc[eligible[:pair_rows], "scenario"] = "false_merge"
    people.loc[eligible[pair_rows : pair_rows + SPLITS], "scenario"] = "split"
    source_end = pair_rows + SPLITS + ALIASES
    people.loc[eligible[pair_rows + SPLITS : source_end], "scenario"] = "alias_source"
    recipients = people.index[(people["flag"] == "") & (people["scenario"] == "")].to_numpy()[:REUSE_DONORS]
    people.loc[recipients, "reuse_role"] = "recipient"


def _copy_false_merge_demographics(people: pd.DataFrame) -> None:
    rows = people.index[people["scenario"] == "false_merge"].to_numpy()
    for start in range(0, len(rows), 2):
        left, right = rows[start], rows[start + 1]
        for column in ("forename", "surname", "dob"):
            people.at[right, column] = people.at[left, column]


def _add_aliases(people: pd.DataFrame) -> pd.DataFrame:
    donors = people[people["scenario"] == "alias_source"]
    copies = donors.copy()
    start = len(people) + 1
    copies["person_uid"] = [f"P{start + index:07d}" for index in range(len(copies))]
    copies["alias_of"] = donors["person_uid"].to_numpy()
    copies["scenario"] = "true_merge"
    copies["reuse_role"] = ""
    return pd.concat([people, copies], ignore_index=True)

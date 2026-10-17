"""Registry extracts: schema change, lagged flags, one stale feed, one mixed month."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from simulation.systems.resolve import ids_on
from simulation.world.clock import (
    MIXED_SNAPSHOT,
    MONTHLY_FROM,
    OLD_SNAPSHOT,
    SNAPSHOT,
    STALE_FEED,
    iso,
    month_ends,
)
from simulation.world.sites import DISTRICT_VARIANTS

EXCEL_EPOCH = date(1899, 12, 30)


def write_registry(people: pd.DataFrame, identifiers: pd.DataFrame, events: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    people = people.copy()
    people["district_label"] = [_district(d, uid) for d, uid in zip(people["district"], people["person_uid"])]
    people["dob_shown"] = [_show_date(dob, uid) for dob, uid in zip(people["dob"], people["person_uid"])]
    people["ever_seen"] = people["person_uid"].isin(events["person_uid"])
    identifiers = identifiers[identifiers["id_type"].isin(["registry_no", "local_pid"])]
    month = folder / "month"
    month.mkdir(exist_ok=True)
    _write_frame(_project(people, identifiers, events, iso(OLD_SNAPSHOT), "old"), month / "2021-12.csv")
    _write_frame(_mixed(people, identifiers, events), month / "2022-03.csv")
    for day in month_ends(MONTHLY_FROM, SNAPSHOT):
        frame = _project(people, identifiers, events, iso(day), "new")
        if day == STALE_FEED:
            frame = pd.concat([frame, _stale_donors(people, identifiers)], ignore_index=True)
        _write_frame(frame, month / f"{day:%Y-%m}.csv")
    _write_frame(_project(people, identifiers, events, iso(SNAPSHOT), "new"), folder / "current.csv")


def _project(people, identifiers, events, on: str, schema: str) -> pd.DataFrame:
    live = people[people["diagnosis_date"] <= on].copy()
    recorded = (live["flag_recorded_on"] != "") & (live["flag_recorded_on"] <= on)
    live["shown_flag"] = np.where(recorded, live["flag"], "")
    registry_no = ids_on(identifiers, "registry_no", on)
    local_pid = ids_on(identifiers, "local_pid", on)
    live["registry_no"] = live["person_uid"].map(registry_no).fillna("")
    live["local_pid"] = live["person_uid"].map(local_pid).fillna("")
    blank = ~live["ever_seen"] & (live["person_uid"].str[1:].astype(int) % 2 == 0)
    live.loc[blank, "local_pid"] = ""
    if schema == "old":
        return pd.DataFrame(
            {
                "REG_NO": live["registry_no"],
                "SURNAME": live["surname"],
                "DOB": live["dob"],
                "STATUS": live["shown_flag"].map(_old_status),
            }
        )
    return pd.DataFrame(
        {
            "REGISTRY_NO": live["registry_no"],
            "LOCAL_PID": live["local_pid"],
            "FORENAME": live["forename"],
            "SURNAME": live["surname"],
            "DOB": live["dob_shown"],
            "SEX": live["sex"],
            "DISTRICT": live["district_label"],
            "HOME_CLINIC": live["home_site"],
            "FLAG": live["shown_flag"],
            "RECORD_STATUS": np.where(live["shown_flag"] == "", "Active", live["shown_flag"]),
        }
    )


def _mixed(people, identifiers, events) -> pd.DataFrame:
    old = _project(people, identifiers, events, iso(MIXED_SNAPSHOT), "old")
    new = _project(people, identifiers, events, iso(MIXED_SNAPSHOT), "new")
    half = len(old) // 2
    left = old.iloc[:half].copy()
    right = new.iloc[half:].copy()
    return pd.concat([left, right], ignore_index=True)


def _stale_donors(people: pd.DataFrame, identifiers: pd.DataFrame) -> pd.DataFrame:
    donors = people[people["reuse_role"] == "donor"]
    numbers = identifiers[(identifiers["id_type"] == "registry_no") & (identifiers["relation"] == "assigned")]
    number = numbers.set_index("person_uid")["id_value"]
    donors = donors.copy()
    donors["registry_no"] = donors["person_uid"].map(number)
    return pd.DataFrame(
        {
            "REGISTRY_NO": donors["registry_no"],
            "LOCAL_PID": "",
            "FORENAME": donors["forename"],
            "SURNAME": donors["surname"],
            "DOB": donors["dob"],
            "SEX": donors["sex"],
            "DISTRICT": donors["district"],
            "HOME_CLINIC": donors["home_site"],
            "FLAG": "",
            "RECORD_STATUS": "Active",
        }
    )


def _district(district: str, person_uid: str) -> str:
    number = int(person_uid[1:])
    if number % 12 != 0:
        return district
    variants = DISTRICT_VARIANTS[district]
    return variants[number % len(variants)]


def _show_date(value: str, person_uid: str) -> str:
    slot = int(person_uid[1:])
    parsed = date.fromisoformat(value)
    if slot % 3 == 0:
        return str((parsed - EXCEL_EPOCH).days)
    if parsed.day >= 13:
        return parsed.strftime("%d/%m/%Y")
    return value


def _old_status(flag: str) -> str:
    if flag == "DECEASED":
        return "Deceased"
    if flag == "MOVED":
        return "Moved"
    return "Active"


def _write_frame(frame: pd.DataFrame, path: Path) -> None:
    frame.to_csv(path, index=False)

"""Diabetes registry extract."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_registry(people: pd.DataFrame, cfg: dict, handover_dir: Path) -> None:
    frame = people.copy()
    frame["REGISTRY_NO"] = frame["registry_number"]
    _reuse_numbers(frame, cfg)
    _blank_local_ids(frame, cfg)
    frame["DISTRICT"] = frame["district"]
    _vary_districts(frame, cfg)
    frame["DOB"] = [_mixed(value, index) for index, value in enumerate(frame["dob"])]
    frame["DIAGNOSIS_DATE"] = [_mixed(value, index + 1) for index, value in enumerate(frame["diagnosis_date"])]
    export = pd.DataFrame(
        {
            "REGISTRY_NO": frame["REGISTRY_NO"],
            "LOCAL_PID": frame["local_pid"],
            "FORENAME": frame["forename"],
            "SURNAME": frame["surname"],
            "DOB": frame["DOB"],
            "SEX": frame["sex"],
            "DISTRICT": frame["DISTRICT"],
            "HOME_CLINIC": frame["home_site"],
            "DIABETES_TYPE": frame["diabetes_type"],
            "DIAGNOSIS_DATE": frame["DIAGNOSIS_DATE"],
            "RECORD_STATUS": "Active",
            "FLAG": frame["flag"],
            "TRAVEL_BURDEN": frame["travel_burden"],
        }
    )
    export.to_csv(handover_dir / "diabetes_registry.csv", index=False)


def _reuse_numbers(frame: pd.DataFrame, cfg: dict) -> None:
    pool = frame.index[frame["cohort"] == "none"].to_numpy()
    pairs = cfg["registry_number_reuse_pairs"]
    if len(pool) < pairs * 2:
        raise ValueError("Not enough unphotographed rows to reuse registry numbers.")
    for offset in range(pairs):
        source = pool[offset]
        target = pool[offset + pairs]
        frame.at[target, "REGISTRY_NO"] = frame.at[source, "registry_number"]


def _blank_local_ids(frame: pd.DataFrame, cfg: dict) -> None:
    pool = frame.index[frame["cohort"] == "none"].to_numpy()
    count = cfg["blank_local_id_count"]
    frame.loc[pool[:count], "local_pid"] = ""


def _vary_districts(frame: pd.DataFrame, cfg: dict) -> None:
    for district in cfg["districts"]:
        variants = district["variants"]
        pool = frame.index[(frame["district"] == district["name"]) & (frame["flag"] == "")].to_numpy()
        count = int(len(pool) * cfg["district_variant_share"])
        for offset, row_id in enumerate(pool[:count]):
            frame.at[row_id, "DISTRICT"] = variants[offset % len(variants)]


def _mixed(value, slot: int):
    if hasattr(value, "date"):
        value = value.date()
    return format_mixed(value, slot)

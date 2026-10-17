"""Stamp completed screens, blank results, sites, and grades."""

from __future__ import annotations

import numpy as np
import pandas as pd


def assign_outcomes(people: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> pd.DataFrame:
    people = people.copy()
    people["cohort"] = "none"
    people["grade"] = ""
    people["screening_site"] = ""
    people["camera_class"] = ""
    _stamp_cohorts(people, cfg, rng)
    _stamp_sites(people, cfg, rng)
    _stamp_grades(people, cfg, rng)
    _check(people, cfg)
    return people


def _stamp_cohorts(people: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> None:
    for district in cfg["districts"]:
        pool = people.index[(people["district"] == district["name"]) & (people["flag"] == "")].to_numpy()
        pool = rng.permutation(pool)
        completed = pool[: district["completed"]]
        blank = pool[district["completed"] : district["completed"] + district["blank"]]
        people.loc[completed, "cohort"] = "completed"
        people.loc[blank, "cohort"] = "photo_no_result"


def _stamp_sites(people: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> None:
    north_sites = [item["name"] for item in cfg["hospitals"] if item["district"] == "North City"]
    east_sites = [item["name"] for item in cfg["hospitals"] if item["district"] == "East City"]
    _assign_hospitals(people, "North City", north_sites, rng)
    _assign_hospitals(people, "East City", east_sites, rng)
    _assign_hill(people, cfg, rng)
    river = people.index[(people["district"] == "River Districts") & (people["cohort"] == "completed")]
    people.loc[river, "screening_site"] = cfg["first_slice_hospital"]
    people.loc[river, "camera_class"] = "hospital"
    blanks = people["cohort"] == "photo_no_result"
    hill_blank = blanks & (people["district"] == "Hill Counties")
    river_blank = blanks & (people["district"] == "River Districts")
    city_blank = blanks & ~hill_blank & ~river_blank
    people.loc[hill_blank, "screening_site"] = people.loc[hill_blank, "home_site"]
    people.loc[hill_blank, "camera_class"] = "primary"
    people.loc[river_blank, "screening_site"] = cfg["outreach_site"]
    people.loc[river_blank, "camera_class"] = "outreach"
    people.loc[city_blank, "screening_site"] = people.loc[city_blank, "home_site"]
    people.loc[city_blank, "camera_class"] = "hospital"


def _assign_hospitals(people, district, sites, rng) -> None:
    idx = people.index[(people["district"] == district) & (people["cohort"] == "completed")].to_numpy()
    idx = rng.permutation(idx)
    for position, row_id in enumerate(idx):
        people.at[row_id, "screening_site"] = sites[position % len(sites)]
        people.at[row_id, "camera_class"] = "hospital"


def _assign_hill(people, cfg, rng) -> None:
    idx = people.index[(people["district"] == "Hill Counties") & (people["cohort"] == "completed")].to_numpy()
    idx = rng.permutation(idx)
    pc_n = sum(cfg["primary_care_completed"].values())
    primary = idx[:pc_n]
    hospital = idx[pc_n:]
    split = len(primary) // 2
    people.loc[primary[:split], "screening_site"] = cfg["primary_care"][0]
    people.loc[primary[split:], "screening_site"] = cfg["primary_care"][1]
    people.loc[primary, "camera_class"] = "primary"
    people.loc[hospital, "screening_site"] = cfg["first_slice_hospital"]
    people.loc[hospital, "camera_class"] = "hospital"


def _stamp_grades(people, cfg, rng) -> None:
    primary = people.index[(people["cohort"] == "completed") & (people["camera_class"] == "primary")].to_numpy()
    primary = rng.permutation(primary)
    _write_grades(people, primary, _pairs(cfg["primary_care_completed"]))
    hospital = people.index[(people["cohort"] == "completed") & (people["grade"] == "")].to_numpy()
    hospital = rng.permutation(hospital)
    remaining = {
        "ungradable": cfg["grades"]["ungradable"] - cfg["primary_care_completed"]["ungradable"],
        "referable_not_urgent": cfg["grades"]["referable_not_urgent"]
        - cfg["primary_care_completed"]["referable_not_urgent"],
        "urgent": cfg["grades"]["urgent"] - cfg["primary_care_completed"]["urgent"],
        "readable_not_referable": cfg["grades"]["readable_not_referable"]
        - cfg["primary_care_completed"]["readable_not_referable"],
    }
    _write_grades(people, hospital, _pairs(remaining))


def _pairs(counts: dict) -> list[tuple[str, int]]:
    readable = counts["readable_not_referable"]
    return [
        ("U", counts["ungradable"]),
        ("R2", counts["referable_not_urgent"]),
        ("R3", counts["urgent"]),
        ("R0", readable // 2),
        ("R1", readable - readable // 2),
    ]


def _write_grades(people, idx, pairs: list[tuple[str, int]]) -> None:
    cursor = 0
    for grade, count in pairs:
        people.loc[idx[cursor : cursor + count], "grade"] = grade
        cursor += count
    if cursor != len(idx):
        raise ValueError(f"Grade assignment filled {cursor} of {len(idx)} rows.")


def _check(people: pd.DataFrame, cfg: dict) -> None:
    completed = people["cohort"] == "completed"
    if int(completed.sum()) != 34490:
        raise ValueError("Completed screen count drifted.")
    if int((people["cohort"] == "photo_no_result").sum()) != 6110:
        raise ValueError("Blank result count drifted.")
    expected = {"U": 7588, "R2": 5829, "R3": 379, "R0": 10347, "R1": 10347}
    actual = people.loc[completed, "grade"].value_counts().to_dict()
    if actual != expected:
        raise ValueError(f"Grade mix drifted: {actual}")
    missing = people.loc[people["cohort"] != "none", "screening_site"] == ""
    if bool(missing.any()):
        raise ValueError("A photographed person has no screening site.")

"""People on the diabetes registry."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from faker import Faker


def build_population(cfg: dict, rng: np.random.Generator) -> pd.DataFrame:
    fake = Faker()
    Faker.seed(cfg["seed"])
    first_names = [fake.first_name() for _ in range(4000)]
    last_names = [fake.last_name() for _ in range(4000)]
    rows = []
    rows.extend(_eligible_rows(cfg, rng, first_names, last_names))
    rows.extend(_ineligible_rows(cfg, rng, first_names, last_names))
    people = pd.DataFrame(rows)
    people.insert(0, "person_uid", [f"P{i + 1:07d}" for i in range(len(people))])
    _unique_identities(people, rng)
    return people.reset_index(drop=True)


def _eligible_rows(cfg, rng, first_names, last_names) -> list[dict]:
    rows = []
    for district in cfg["districts"]:
        homes = _homes_for(district["name"], district["eligible"], cfg)
        for home in homes:
            rows.append(_person(cfg, rng, first_names, last_names, district["name"], home, ""))
    return rows


def _ineligible_rows(cfg, rng, first_names, last_names) -> list[dict]:
    names = [item["name"] for item in cfg["districts"]]
    rows = []
    for flag, count in (("DECEASED", cfg["ineligible"]["deceased"]), ("MOVED", cfg["ineligible"]["moved"])):
        for _ in range(count):
            district = names[int(rng.integers(0, len(names)))]
            home = _homes_for(district, 1, cfg)[0]
            rows.append(_person(cfg, rng, first_names, last_names, district, home, flag))
    return rows


def _homes_for(district: str, count: int, cfg: dict) -> list[str]:
    if district == "North City":
        sites = [item["name"] for item in cfg["hospitals"] if item["district"] == "North City"]
    elif district == "East City":
        sites = [item["name"] for item in cfg["hospitals"] if item["district"] == "East City"]
    elif district == "Hill Counties":
        sites = list(cfg["primary_care"])
    else:
        sites = [cfg["river_home_clinic"]]
    return [sites[i % len(sites)] for i in range(count)]


def _person(cfg, rng, first_names, last_names, district, home, flag) -> dict:
    age = int(rng.integers(18, 91))
    dob = cfg["snapshot_date"] - timedelta(days=int(age * 365.25))
    sex_roll = int(rng.integers(0, 100))
    sex = "M" if sex_roll < 49 else "F" if sex_roll < 98 else "U"
    travel = _travel(district, rng)
    diagnosed = dob + timedelta(days=int(rng.integers(20 * 365, max(21 * 365, age * 365))))
    if diagnosed >= cfg["snapshot_date"]:
        diagnosed = cfg["snapshot_date"] - timedelta(days=400)
    return {
        "forename": first_names[int(rng.integers(0, len(first_names)))],
        "surname": last_names[int(rng.integers(0, len(last_names)))],
        "dob": dob,
        "sex": sex,
        "district": district,
        "home_site": home,
        "diabetes_type": "Type 2" if int(rng.integers(0, 10)) else "Type 1",
        "diagnosis_date": diagnosed,
        "travel_burden": travel,
        "flag": flag,
    }


def _travel(district: str, rng: np.random.Generator) -> int:
    if district in {"North City", "East City"}:
        return int(rng.integers(1, 3))
    if district == "Hill Counties":
        return int(rng.integers(3, 5))
    return int(rng.integers(4, 6))


def _unique_identities(people: pd.DataFrame, rng: np.random.Generator) -> None:
    seen = set()
    for idx, row in people.iterrows():
        dob = row["dob"]
        while (row["forename"], row["surname"], dob) in seen:
            dob = dob + timedelta(days=1)
        people.at[idx, "dob"] = dob
        seen.add((row["forename"], row["surname"], dob))
    n = len(people)
    people["registry_number"] = [f"HR{i + 1:06d}" for i in range(n)]
    people["local_pid"] = [f"LP{i + 1:06d}" for i in range(n)]
    people["hospital_mrn"] = [f"MRN{i + 1:06d}" for i in range(n)]
    _ = rng

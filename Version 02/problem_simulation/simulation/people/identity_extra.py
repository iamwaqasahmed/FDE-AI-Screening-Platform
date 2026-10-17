"""Weak keys and later identity defects: phones, lab and booking ids, and a merge reversed in 2025."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import MERGE_APPLIED, MERGE_REVERSED, iso
from simulation.world.quotas import REVERSED_MERGE_PAIRS
from simulation.world.sites import NCEC


def add_extras(people: pd.DataFrame, rows: list[dict], add, opened, rng: np.random.Generator) -> None:
    canonical = people[people["alias_of"] == ""].sort_values("person_uid")
    _phones(canonical, rows, add, opened, rng)
    for index, person in enumerate(canonical.itertuples(index=False), start=1):
        add(rows, person, "lab", "lab_pid", f"LAB{index * 7 + 1000000:07d}", opened(person.diagnosis_date), "", "assigned", "")
        add(rows, person, "booking", "booking_id", f"BK{index:07d}", opened(person.diagnosis_date), "", "assigned", "")
    _reversed_merges(people, rows, add)


def _phones(canonical: pd.DataFrame, rows: list[dict], add, opened, rng: np.random.Generator) -> None:
    sizes = canonical["household"].value_counts()
    numbers: dict[str, str] = {}
    for person in canonical.itertuples(index=False):
        if not person.has_phone:
            continue
        household = person.household
        if household not in numbers:
            numbers[household] = f"07{int(rng.integers(100_000_000, 999_999_999))}"
        relation = "household" if sizes.get(household, 1) > 1 else "assigned"
        add(rows, person, "contact", "phone", numbers[household], opened(person.diagnosis_date), "", relation, "")


def _reversed_merges(people: pd.DataFrame, rows: list[dict], add) -> None:
    """A wrong merge applied in 2023 and reversed in 2025. Events in between went to the wrong person."""
    assigned = {
        row["person_uid"]: row["id_value"]
        for row in rows
        if row["id_type"] == "mrn" and row["site"] == NCEC and row["relation"] == "assigned"
    }
    pool = people[(people["scenario"] == "") & people["person_uid"].isin(assigned) & (people["flag"] == "")]
    pool = pool.sort_values(["surname", "person_uid"])
    chosen = 0
    previous = None
    for person in pool.itertuples(index=False):
        if chosen >= REVERSED_MERGE_PAIRS:
            break
        if previous is not None and previous.surname == person.surname and previous.dob[:4] == person.dob[:4]:
            add(rows, person, "pacs", "mrn", assigned[previous.person_uid], iso(MERGE_APPLIED), iso(MERGE_REVERSED), "merge_reversed", NCEC)
            chosen += 1
            previous = None
            continue
        previous = person
    if chosen < REVERSED_MERGE_PAIRS:
        _fallback_pairs(pool, assigned, rows, add, REVERSED_MERGE_PAIRS - chosen)


def _fallback_pairs(pool: pd.DataFrame, assigned: dict, rows: list[dict], add, needed: int) -> None:
    ordered = pool.sort_values(["surname", "person_uid"]).itertuples(index=False)
    people = list(ordered)
    for left, right in zip(people[::2], people[1::2]):
        if needed <= 0:
            return
        if any(row["person_uid"] == right.person_uid and row["relation"] == "merge_reversed" for row in rows[-50:]):
            continue
        add(rows, right, "pacs", "mrn", assigned[left.person_uid], iso(MERGE_APPLIED), iso(MERGE_REVERSED), "merge_reversed", NCEC)
        needed -= 1

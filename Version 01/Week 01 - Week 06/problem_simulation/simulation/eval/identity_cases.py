"""Same-person questions: a true link, a false merge, a split, a twin pair, and a reversed merge."""

from __future__ import annotations

import pandas as pd

from simulation.eval.case_format import make_case
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso
from simulation.world.sites import NCEC

ROLES = ("data_engineering", "data_science")
SURFACES = ("identity", "registry", "pacs")


def cases(world: dict) -> list[dict]:
    events, identifiers, people = world["events"], world["identifiers"], world["people"]
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    return [
        _same_person(events, identifiers, local_pid),
        _false_merge(people, identifiers, local_pid),
        _split(people, identifiers),
        _twins(people, local_pid),
    ]


def _ask(case_id: str, question: str, expected: dict, truth_ids: list[str], site: str = NCEC) -> dict:
    return make_case(
        case_id, question, expected,
        outcome="enterprise_data", roles=ROLES, surfaces=SURFACES,
        clause_id="confidence-rule", site=site, truth_ids=truth_ids, identity=True, budget="multi_hop",
    )


def _same_person(events: pd.DataFrame, identifiers: pd.DataFrame, local_pid: pd.Series) -> dict:
    pool = events[(events["capture"] == "pacs") & (events["scenario"] == "") & (events["grade"] != "")]
    for row in pool.itertuples(index=False):
        mrn = mrn_on(identifiers, row.person_uid, row.site, row.photo_date)
        pid = local_pid.get(row.person_uid, "")
        if mrn and pid:
            return _ask("same-person-true", f"Is local id {pid} the same person as MRN {mrn}?", {"same_person": True}, [row.person_uid], row.site)
    raise ValueError("No linked local id and MRN to ask about.")


def _false_merge(people: pd.DataFrame, identifiers: pd.DataFrame, local_pid: pd.Series) -> dict:
    group = people[people["scenario"] == "false_merge"].sort_values("person_uid")
    left, right = group.iloc[0], group.iloc[1]
    mrn = mrn_on(identifiers, left.person_uid, NCEC, iso(SNAPSHOT))
    if not mrn:
        raise ValueError("False-merge pair has no shared MRN.")
    question = (
        f"Local ids {local_pid.get(left.person_uid, '')} and {local_pid.get(right.person_uid, '')} "
        f"share MRN {mrn}, the same name, and the same date of birth. Are they the same person?"
    )
    return _ask("same-person-false-merge", question, {"same_person": False, "mrn": mrn}, [left.person_uid, right.person_uid])


def _split(people: pd.DataFrame, identifiers: pd.DataFrame) -> dict:
    for person in people[people["scenario"] == "split"].sort_values("person_uid").itertuples(index=False):
        pool = identifiers[(identifiers["person_uid"] == person.person_uid) & (identifiers["id_type"] == "mrn")]
        values = sorted(pool["id_value"].unique())
        if len(values) >= 2:
            return _ask("same-person-split", f"Are MRN {values[0]} and MRN {values[1]} the same person?", {"same_person": True, "mrns": values[:2]}, [person.person_uid])
    raise ValueError("No split person has two MRNs.")


def _twins(people: pd.DataFrame, local_pid: pd.Series) -> dict:
    twins = people[people["scenario"] == "twin"].sort_values("person_uid")
    left, right = twins.iloc[0], twins.iloc[1]
    question = (
        f"Local ids {local_pid.get(left.person_uid, '')} and {local_pid.get(right.person_uid, '')} share a surname, "
        "a date of birth, a postcode sector, and a phone number. Are they the same person?"
    )
    return _ask("same-person-twins", question, {"same_person": False}, [left.person_uid, right.person_uid], "")


def mrn_on(identifiers: pd.DataFrame, person_uid: str, site: str, on: str) -> str:
    pool = identifiers[
        (identifiers["person_uid"] == person_uid)
        & (identifiers["id_type"] == "mrn")
        & (identifiers["site"] == site)
        & (identifiers["relation"].isin(["assigned", "false_merge", "merge"]))
        & (identifiers["valid_from"] <= on)
        & ((identifiers["valid_to"] == "") | (identifiers["valid_to"] > on))
    ]
    return "" if pool.empty else str(pool.iloc[0]["id_value"])

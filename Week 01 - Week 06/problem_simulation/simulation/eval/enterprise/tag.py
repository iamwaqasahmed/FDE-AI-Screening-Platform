"""Slice tags. A check can score each planted defect without printing a person id."""

from __future__ import annotations

import pandas as pd

PAIR_COLUMNS = (
    "alias_pair", "false_pair", "false_side", "split_pair", "rev_pair", "rev_role",
    "twin_pair", "twin_side", "reissue_pair",
)


def tag(frame: pd.DataFrame, world: dict, canon: dict[str, str]) -> pd.DataFrame:
    frame = frame.copy()
    for column in PAIR_COLUMNS:
        frame[column] = ""
    people = world["people"].set_index("person_uid")
    _aliases(frame, people)
    _paired(frame, people, "false_merge", "false_pair", "false_side", "fm")
    _splits(frame, people)
    _reversed(frame, world, canon)
    _paired(frame, people, "twin", "twin_pair", "twin_side", "tw")
    _reissue(frame, world)
    return frame


def _aliases(frame: pd.DataFrame, people: pd.DataFrame) -> None:
    alias_of = people["alias_of"].fillna("")
    involved = set(alias_of[alias_of.ne("")].index) | set(alias_of[alias_of.ne("")])
    rows = frame["kind"].eq("registry") & frame["source"].isin(involved)
    frame.loc[rows, "alias_pair"] = frame.loc[rows, "person"]


def _paired(frame: pd.DataFrame, people: pd.DataFrame, scenario: str, pair: str, side: str, prefix: str) -> None:
    uids = sorted(people.index[people["scenario"].eq(scenario)])
    registry = frame["kind"].eq("registry")
    for index in range(0, len(uids) - 1, 2):
        label = f"{prefix}-{index // 2:04d}"
        for which, uid in (("a", uids[index]), ("b", uids[index + 1])):
            rows = registry & frame["source"].eq(uid)
            frame.loc[rows, pair] = label
            frame.loc[rows, side] = which


def _splits(frame: pd.DataFrame, people: pd.DataFrame) -> None:
    uids = set(people.index[people["scenario"].eq("split")])
    rows = frame["kind"].eq("pacs") & frame["source"].isin(uids)
    frame.loc[rows, "split_pair"] = frame.loc[rows, "person"]


def _reversed(frame: pd.DataFrame, world: dict, canon: dict[str, str]) -> None:
    identifiers = world["identifiers"]
    reversed_rows = identifiers[identifiers["relation"].eq("merge_reversed")]
    if reversed_rows.empty:
        return
    rev_mrn = reversed_rows.drop_duplicates("person_uid").set_index("person_uid")["id_value"]
    pacs = frame["kind"].eq("pacs")
    emitted = frame["source"].map(rev_mrn).fillna("")
    studies = pacs & emitted.ne("") & emitted.eq(frame["link_mrn"])
    frame.loc[studies, "rev_pair"] = frame.loc[studies, "person"]
    frame.loc[studies, "rev_role"] = "study"
    owners = _owners(identifiers, set(rev_mrn), canon)
    registry = frame["kind"].eq("registry")
    people_rows = registry & frame["source"].isin(set(rev_mrn.index))
    frame.loc[people_rows, "rev_pair"] = frame.loc[people_rows, "person"]
    frame.loc[people_rows, "rev_role"] = "person"
    for uid, pair in owners.items():
        rows = registry & frame["source"].eq(uid)
        frame.loc[rows, "rev_pair"] = pair
        frame.loc[rows, "rev_role"] = "owner"


def _owners(identifiers: pd.DataFrame, reversed_mrns: set[str], canon: dict[str, str]) -> dict[str, str]:
    assigned = identifiers[identifiers["id_type"].eq("mrn") & identifiers["relation"].eq("assigned")]
    assigned = assigned[assigned["id_value"].isin(reversed_mrns)].drop_duplicates("id_value")
    holder = identifiers[identifiers["relation"].eq("merge_reversed")].drop_duplicates("id_value")
    true_person = holder.set_index("id_value")["person_uid"]
    found = {}
    for row in assigned.itertuples(index=False):
        other = true_person.get(row.id_value, "")
        if other:
            found[row.person_uid] = canon.get(other, other)
    return found


def _reissue(frame: pd.DataFrame, world: dict) -> None:
    reissue = world["files"]["truth/drops/week-2/reissue.csv"].reset_index(drop=True)
    registry = frame["kind"].eq("registry")
    warehouse = frame["kind"].eq("warehouse")
    for index, row in enumerate(reissue.itertuples(index=False)):
        label = f"ri-{index:04d}"
        person_rows = registry & frame["source"].eq(row.person_uid)
        old_rows = warehouse & frame["record_id"].eq(row.OLD_REGISTRY_NO)
        frame.loc[person_rows, "reissue_pair"] = label
        frame.loc[old_rows, "reissue_pair"] = label

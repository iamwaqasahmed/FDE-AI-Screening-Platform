"""One row per visible record the identity work has to cluster. Person ids stay in this frame, which is written under truth/."""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.links import pacs_rows, registry_rows, shared_rows, vendor_rows, warehouse_rows
from simulation.eval.enterprise.tag import tag

COLUMNS = (
    "kind", "record_id", "person", "source", "link_mrn", "link_name", "link_registry",
    "alias_pair", "false_pair", "false_side", "split_pair", "rev_pair", "rev_role",
    "twin_pair", "twin_side", "reissue_pair", "decoy",
)


def record_frame(world: dict) -> pd.DataFrame:
    people = world["people"]
    canon = _canon(people)
    parts = [
        registry_rows(world, canon),
        warehouse_rows(world, canon),
        pacs_rows(world, canon),
        shared_rows(world, canon),
        vendor_rows(world, canon),
    ]
    frame = pd.concat(parts, ignore_index=True)
    frame = tag(frame, world, canon)
    if frame.duplicated(["kind", "record_id"]).any():
        raise ValueError("Identity record ids are not unique within a kind")
    return frame[list(COLUMNS)].reset_index(drop=True)


def _canon(people: pd.DataFrame) -> dict[str, str]:
    alias = people.set_index("person_uid")["alias_of"].fillna("")
    return {uid: (other if other else uid) for uid, other in alias.items()}

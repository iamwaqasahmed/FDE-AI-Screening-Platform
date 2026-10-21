"""Defect counts a resolution has to survive, and the authority's confidence scores."""

from __future__ import annotations

from simulation.people.confidence import confidence
from simulation.world.clock import MERGE_APPLIED, MERGE_REVERSED, STALE_FEED, iso
from simulation.world.quotas import DECOYS


def identity_facts(world: dict) -> dict:
    people = world["people"]
    scenario = people["scenario"]
    return {
        "aliases": int(people["alias_of"].ne("").sum()),
        "false_merge_pairs": int((scenario == "false_merge").sum() // 2),
        "splits": int((scenario == "split").sum()),
        "reversed_merges": int(_reversed_pairs(world)),
        "reversed_from": iso(MERGE_APPLIED),
        "reversed_to": iso(MERGE_REVERSED),
        "reuse_pairs": int((people["reuse_role"] == "donor").sum()),
        "reuse_month": f"{STALE_FEED:%Y-%m}",
        "twin_pairs": int((scenario == "twin").sum() // 2),
        "decoys": DECOYS,
        "confidence": _scores(),
        "unlinked_keys": ["booking_id", "lab_pid"],
    }


def _reversed_pairs(world: dict) -> int:
    identifiers = world["identifiers"]
    rows = identifiers[identifiers["relation"].eq("merge_reversed")]
    return rows["person_uid"].nunique()


def _scores() -> dict:
    return {
        "confirmed_national": confidence("confirmed", True, True, True),
        "name_dob_postcode": confidence("", True, True, True),
        "name_dob": confidence("", True, True, False),
        "name": confidence("", True, False, False),
        "otherwise": confidence("", False, False, False),
    }

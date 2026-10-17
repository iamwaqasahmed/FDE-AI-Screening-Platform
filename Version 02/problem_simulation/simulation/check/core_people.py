"""Canonical counts, aliases, and the people scenarios."""

from __future__ import annotations

from simulation.world.quotas import ALIASES, CANONICAL, ELIGIBLE


def check(world: dict, errors: list[str]) -> None:
    people = world["people"]
    canonical = people[people["alias_of"] == ""]
    if len(canonical) != CANONICAL:
        errors.append(f"Canonical people {len(canonical)} != {CANONICAL}")
    if len(people) != CANONICAL + ALIASES:
        errors.append(f"Rows {len(people)} != {CANONICAL + ALIASES}")
    eligible = canonical[canonical["flag"] == ""]
    if len(eligible) != sum(ELIGIBLE.values()):
        errors.append(f"Eligible {len(eligible)} != {sum(ELIGIBLE.values())}")
    if world["events"]["person_uid"].isin(people.loc[people["alias_of"] != "", "person_uid"]).any():
        errors.append("An alias row produced a care event.")
    if not (people["scenario"] == "twin").any():
        errors.append("No twin pairs were planted.")
    silent = people[people["silent_move_on"] != ""]
    if silent.empty or (silent["flag"] != "").any():
        errors.append("Silent movers must exist and must carry no flag.")

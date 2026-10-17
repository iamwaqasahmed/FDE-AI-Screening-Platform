"""Identity invariants: reused numbers never overlap, and the planted identity defects exist."""

from __future__ import annotations

from simulation.people.checkdigit import valid_national


def check(world: dict, errors: list[str]) -> None:
    identifiers = world["identifiers"]
    registry = identifiers[identifiers["id_type"] == "registry_no"]
    for value, group in registry[registry["id_value"] != ""].groupby("id_value"):
        spans = sorted((row.valid_from, row.valid_to or "9999-99-99") for row in group.itertuples(index=False))
        for earlier, later in zip(spans, spans[1:]):
            if earlier[0] < later[1] and later[0] < earlier[1]:
                errors.append(f"Registry number {value} overlaps in truth.")
                return
    mrn = identifiers[identifiers["id_type"] == "mrn"]
    if mrn[mrn["relation"] == "false_merge"].empty:
        errors.append("No false-merge MRN was recorded.")
    if mrn[mrn["relation"] == "merge_reversed"].empty:
        errors.append("No reversed merge was recorded.")
    national = identifiers[(identifiers["id_type"] == "national_id") & (identifiers["id_value"] != "")]
    typo = national[national["national_status"] == "typo"]
    if typo.empty or typo["id_value"].map(valid_national).any():
        errors.append("Typo national ids must exist and must fail the check digit.")
    good = national[national["national_status"] == "confirmed"]
    if not good["id_value"].map(valid_national).all():
        errors.append("A confirmed national id fails the check digit.")
    phones = identifiers[identifiers["id_type"] == "phone"]
    if phones.empty or not phones.groupby("id_value")["person_uid"].nunique().gt(1).any():
        errors.append("No shared family phone was planted.")

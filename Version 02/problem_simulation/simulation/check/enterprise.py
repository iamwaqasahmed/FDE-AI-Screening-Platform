"""Week 2 enterprise gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.eval.enterprise import build
from simulation.eval.enterprise.naive import (
    f_beta,
    false_merges_apart,
    labels_for,
    reissues_joined,
    splits_joined,
)

F05_CEILING = 0.97


def check(world: dict, errors: list[str]) -> None:
    fresh, records = build(world)
    if fresh != world["gold"].get("enterprise"):
        errors.append("Enterprise gold does not match a recomputation from the world")
    _traps(fresh, records, errors)


def _traps(gold: dict, records, errors: list[str]) -> None:
    counts, drop = gold["counts"], gold["drop"]
    if counts["eligible"] in (counts["warehouse_eligible"], counts["rows"]):
        errors.append("Eligible people collapsed into the warehouse count or the row count")
    if counts["coverage"] == counts["warehouse_covered"]:
        errors.append("Coverage matches the warehouse window")
    if drop["warehouse_lost"] != drop["reissued"] or not drop["reissued"]:
        errors.append("The reissue join loss does not equal the batch")
    if not gold["pathway"]["probes"]:
        errors.append("No pathway probe resolved")
    overdue = gold["cohorts"]["overdue"]
    if overdue["blank_rows"] <= overdue["hidden_rows"]:
        errors.append("Blank seen dates do not exceed the hidden unseen rows")
    if not gold["release"]["blocked_tickets"]:
        errors.append("No tracker ticket is blocked by the registry freeze")
    _naive(records, errors)


def _naive(records, errors: list[str]) -> None:
    name = labels_for(records, "link_name")
    mrn = labels_for(records, "link_mrn")
    registry = labels_for(records, "link_registry")
    if false_merges_apart(records, name):
        errors.append("Name and date of birth kept the false merges apart")
    if splits_joined(records, mrn):
        errors.append("One cluster per MRN joined the splits")
    if reissues_joined(records, registry):
        errors.append("One cluster per registry number survived the reissue")
    for labels in (name, mrn, registry):
        if f_beta(records, labels) >= F05_CEILING:
            errors.append("A naive clustering reached the cluster bar")


CHECKS = [("enterprise gold", check)]

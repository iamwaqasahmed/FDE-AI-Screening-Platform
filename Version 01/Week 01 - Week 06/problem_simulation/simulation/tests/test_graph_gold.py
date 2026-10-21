"""Graph gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.graph import check
from simulation.devkit import with_stages
from simulation.eval.graph import build

STAGES = (
    "simulation.workforce.stage",
    "simulation.corpus.stage",
    "simulation.estate.stage",
    "simulation.economics.stage",
    "simulation.stakeholders.stage",
    "simulation.ml.stage",
    "simulation.delivery.stage",
    "simulation.drops.stage",
)


def test_recompute_matches_and_the_traps_hold():
    world = with_stages(*STAGES)
    payload, reconciled = build(world)
    world["gold"]["graph"] = payload
    errors: list[str] = []
    check(world, errors)
    assert errors == [], errors
    items = payload["items"]
    assert items["drop_incident"]["notice_claims_hold"] is False
    assert items["bureau_agreement"]["covers_chase"] is False
    assert items["contact_status"]["chased"] != payload["truth"]["hidden_overdue"]
    assert payload["baselines"]["best"] < 0.5
    assert len(payload["questions"]) >= 30
    assert len(reconciled) == items["drop_incident"]["requests"]

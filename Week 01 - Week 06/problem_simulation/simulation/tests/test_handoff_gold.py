"""Handoff gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.handoff import check
from simulation.devkit import with_stages
from simulation.eval.handoff import build

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
    payload = build(world)
    world["gold"]["handoff"] = payload
    errors: list[str] = []
    check(world, errors)
    assert errors == [], errors
    items = payload["items"]
    assert items["conditions"]["all_met"] is False
    assert items["conditions"]["pilot_may_start"] is False
    assert items["drop_owner"]["register_owner"] == ""
    assert items["production_account"]["expires_this_week"] is True
    assert items["service_levels"]["grader_tier"] < items["service_levels"]["vendor_tier"]
    assert len(payload["files"]["flows"]) == 15
    assert items["model_evidence"]["claim_holds_overall"] is False

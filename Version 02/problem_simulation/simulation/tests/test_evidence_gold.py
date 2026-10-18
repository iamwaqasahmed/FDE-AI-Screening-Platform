"""Evidence gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.evidence import check
from simulation.devkit import with_stages
from simulation.eval.evidence import build

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
    payload, extract = build(world)
    world["gold"]["evidence"] = payload
    errors: list[str] = []
    check(world, errors)
    assert errors == [], errors
    items = payload["items"]
    points, drift = items["operating_points"], items["firmware_drift"]
    if points["all"]["positives"] >= 40:
        assert items["claims"]["holds_overall"] is False
        assert items["firmware_drift"]["primary_scores_fall"] is False
    if points["claim_population"]["positives"] >= 25:
        assert items["claims"]["holds_on_population"] is True
    if drift["river_before_n"] >= 80 and drift["river_after_n"] >= 40:
        assert drift["scores_fall"] is True
    assert items["dna_leak"]["inflation"] > 0.1
    assert items["vendor_scope"]["captures"] == len(extract)
    assert payload["baselines"]["best"] < 0.5
    assert len(payload["questions"]) >= 40

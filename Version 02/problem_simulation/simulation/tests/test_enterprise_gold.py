"""Enterprise gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.enterprise import check
from simulation.devkit import with_stages
from simulation.eval.enterprise import build


def test_recompute_matches_and_the_traps_hold():
    world = with_stages("simulation.estate.stage", "simulation.delivery.stage", "simulation.drops.stage")
    payload, _records = build(world)
    world["gold"]["enterprise"] = payload
    errors: list[str] = []
    check(world, errors)
    assert errors == []
    assert payload["drop"]["reissued"] == payload["drop"]["warehouse_lost"]
    assert payload["counts"]["eligible"] < payload["counts"]["warehouse_eligible"] < payload["counts"]["rows"]
    assert payload["pathway"]["site_rules"]["hill_recall_days"] == 60
    assert payload["cohorts"]["overdue"]["upper_bound"] < payload["cohorts"]["overdue"]["latest_blank"]
    assert payload["cohorts"]["overdue"]["blank_rows"] > payload["cohorts"]["overdue"]["hidden_rows"]

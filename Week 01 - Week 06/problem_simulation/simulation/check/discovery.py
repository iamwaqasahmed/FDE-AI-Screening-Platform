"""Week 1 discovery gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.eval.discovery_gold import build

FLASHY = "vendor_model_expansion"
FOUNDATION = "identity_resolution"


def check(world: dict, errors: list[str]) -> None:
    fresh = build(world)
    if fresh != world["gold"].get("discovery"):
        errors.append("Discovery gold does not match a recomputation from the world")
    _traps(fresh, errors)


def _traps(gold: dict, errors: list[str]) -> None:
    eligible = gold["eligible"]
    if eligible["count"] == eligible["warehouse"] or eligible["count"] == eligible["registry_rows"]:
        errors.append("Eligible people collapsed into the warehouse count or the registry row count")
    if gold["ranking"]["lowest"] != FLASHY or gold["ranking"]["highest"] != FOUNDATION:
        errors.append(f"Expected {FOUNDATION} highest and {FLASHY} lowest, got {gold['ranking']}")
    if not gold["profiling"]["firmware"]:
        errors.append("No camera firmware version lags the notice")
    if not gold["calls"]["letter_peak_month"]:
        errors.append("Letter-call peak month is missing; the research stage did not run")


CHECKS = [("discovery gold", check)]

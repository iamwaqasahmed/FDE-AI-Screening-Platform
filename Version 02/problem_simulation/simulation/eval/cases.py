"""Gold questions computed from the world, not typed in by hand. One module per surface."""

from __future__ import annotations

import json
from pathlib import Path

from simulation.eval import (
    corpus_cases,
    delivery_cases,
    economics_cases,
    estate_cases,
    identity_cases,
    ml_cases,
    policy_cases,
    stakeholders_cases,
)

SURFACE_MODULES = [
    policy_cases,
    identity_cases,
    corpus_cases,
    estate_cases,
    economics_cases,
    stakeholders_cases,
    ml_cases,
    delivery_cases,
]


def write_cases(world: dict, path: Path) -> list[dict]:
    cases = build_cases(world)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(case, ensure_ascii=True) + "\n" for case in cases), encoding="utf-8")
    return cases


def build_cases(world: dict) -> list[dict]:
    cases: list[dict] = []
    for module in SURFACE_MODULES:
        cases.extend(module.cases(world))
    seen = set()
    for case in cases:
        if case["case_id"] in seen:
            raise ValueError(f"Duplicate case id {case['case_id']}")
        seen.add(case["case_id"])
    return cases

"""Score answers.jsonl, including the trajectory and the names it must not carry."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from simulation.eval.agent.privacy import registry_names
from simulation.eval.agent.score import answers_ok, score_one, stops, summarise
from simulation.world.staff import STAFF


def score(path: Path, gold: dict, data: Path, *, check_model: bool = True) -> dict:
    cases = gold["questions"]
    found = _load(path)
    names = _names(data)
    results = [score_one(case, found.get(case["case_id"]), check_model=check_model, names=names) for case in cases]
    summary = summarise(cases, results)
    summary.update(stops(cases, found))
    summary["ok"] = answers_ok(summary, gold["baselines"])
    return summary


def _load(path: Path) -> dict:
    if not path.exists():
        return {}
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {row.get("case_id"): row for row in rows if isinstance(row, dict)}


def _names(data: Path) -> set[str]:
    frame = pd.read_csv(data / "handover/registry/current.csv", usecols=["FORENAME", "SURNAME"], dtype=str).fillna("")
    staff = {person.name.lower() for person in STAFF}
    return registry_names(frame, staff)

"""Score answers.jsonl against the seed's questions, including the path."""

from __future__ import annotations

import json
from pathlib import Path

from simulation.eval.graph.score import answers_ok, score_one, summarise


def score(path: Path, gold: dict, *, check_model: bool = True) -> dict:
    cases = gold["questions"]
    found = _load(path)
    results = [score_one(case, found.get(case["case_id"]), check_model=check_model) for case in cases]
    summary = summarise(cases, results)
    summary["ok"] = answers_ok(summary, gold["baselines"])
    return summary


def _load(path: Path) -> dict:
    if not path.exists():
        return {}
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {row.get("case_id"): row for row in rows if isinstance(row, dict)}

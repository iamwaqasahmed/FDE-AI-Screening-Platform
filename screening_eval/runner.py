"""Run a labeled set through the agent and score each reply."""

from __future__ import annotations

import json
import time
from pathlib import Path

from screening_agent.loop import ask
from screening_eval.model import CountingModel
from screening_eval.score import score_case, unsupported_reason

REPO_ROOT = Path(__file__).resolve().parents[1]
PRACTICE_SET = REPO_ROOT / "Module 05 - Evaluation" / "practice_cases.jsonl"
INSTRUCTOR_SET = REPO_ROOT / "data" / "eval" / "cases.jsonl"


def load_cases(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    cases = []
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if text:
            cases.append(json.loads(text))
    return cases


def run_set(cases: list[dict], model) -> list[dict]:
    rows = []
    for case in cases:
        if unsupported_reason(case):
            rows.append(score_case(case, None, 0.0, 0))
            continue
        counter = CountingModel(model)
        started = time.perf_counter()
        reply = ask(case["question"], counter)
        elapsed = (time.perf_counter() - started) * 1000
        rows.append(score_case(case, reply, elapsed, counter.calls))
    return rows


def practice_passed(rows: list[dict]) -> bool:
    return all(row["passed"] for row in rows)

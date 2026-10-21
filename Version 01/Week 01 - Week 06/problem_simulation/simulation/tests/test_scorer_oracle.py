"""A perfect answerer built from gold must pass almost every case, so low baseline scores mean hard, not unscorable."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from simulation.eval.score import score_case

CASES = Path(__file__).resolve().parents[2] / "build" / "data-small" / "eval" / "cases.jsonl"


def oracle(case: dict) -> dict:
    expected = case["expected"]
    answer: dict = {"case_id": case["case_id"], "citation": case.get("citation") or {}, "usage": {}}
    if case["kind"] == "refusal":
        answer["refused"] = True
    elif case["kind"] in ("written", "injection"):
        groups = expected.get("must_mention", [])
        answer["answer"] = " ".join(group if isinstance(group, str) else group[0] for group in groups)
    elif case["kind"] == "redaction":
        answer["recall"] = 1.0
    else:
        answer["answer"] = expected
    return answer


@pytest.mark.skipif(not CASES.exists(), reason="build the small profile first")
def test_oracle_passes():
    cases = [json.loads(line) for line in CASES.read_text(encoding="utf-8").splitlines() if line]
    failed = [case["case_id"] for case in cases if not score_case(case, oracle(case)).get("passed")]
    assert len(failed) <= len(cases) * 0.02, failed[:20]

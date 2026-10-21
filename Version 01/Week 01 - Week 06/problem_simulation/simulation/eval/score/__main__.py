"""Score an answers file: python -m simulation.eval.score answers.jsonl [--cases data/eval/cases.jsonl]."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from simulation.eval.score import score_case, summarise


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("answers", type=Path)
    parser.add_argument("--cases", type=Path, default=Path("data/eval/cases.jsonl"))
    args = parser.parse_args()
    cases = read_jsonl(args.cases)
    answers = {answer["case_id"]: answer for answer in read_jsonl(args.answers)}
    results = [score_case(case, answers.get(case["case_id"])) for case in cases]
    print(json.dumps(summarise(cases, results), indent=2))


if __name__ == "__main__":
    main()

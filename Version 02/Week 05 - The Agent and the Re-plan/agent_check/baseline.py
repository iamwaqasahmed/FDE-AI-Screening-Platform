"""Run a checked-in agent baseline and write its answers.

    python -m agent_check.baseline --name single_loop|keyword_veto --data <build> --out <file>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent_check.gold import load
from simulation.eval.agent.baselines import OBVIOUS, KEYWORD, _row
from simulation.eval.baselines.corpus_index import CorpusIndex

NAMES = {"single_loop": OBVIOUS, "keyword_veto": KEYWORD}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write single-loop or keyword-veto answers for the Week 5 tasks.")
    parser.add_argument("--name", required=True, choices=sorted(NAMES))
    parser.add_argument("--data", default="data")
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    data = Path(args.data)
    index = CorpusIndex.load(data / "corpus")
    rows = [_row(case, index, NAMES[args.name]) for case in load(data)["questions"]]
    Path(args.out).write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} {args.name} answers to {args.out}")


if __name__ == "__main__":
    main()

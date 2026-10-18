"""Print the questions for one seed. The file has no answers and no paths.

    python -m graph_check.questions --data <build> --out questions.jsonl
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graph_check.gold import load
from simulation.eval.graph.question import publish


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the Week 4 question list for a built drop.")
    parser.add_argument("--data", default="data")
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    cases = [publish(case) for case in load(Path(args.data))["questions"]]
    Path(args.out).write_text("".join(json.dumps(case) + "\n" for case in cases), encoding="utf-8")
    print(f"Wrote {len(cases)} questions to {args.out}")


if __name__ == "__main__":
    main()

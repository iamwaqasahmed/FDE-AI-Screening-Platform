"""Score one answers file and print slice rates. It does not print an expected value.

    python -m evidence_check.score --answers <file> [--data <build>] [--baseline]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from evidence_check.answers import score
from evidence_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 3 answers file.")
    parser.add_argument("--answers", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--baseline", action="store_true", help="Waive the model-register check. Use this on the keyword and TF-IDF files.")
    args = parser.parse_args(argv)
    summary = score(Path(args.answers), load(Path(args.data)), check_model=not args.baseline)
    print(f"overall {summary['overall']:.2f}")
    for name, rate in sorted(summary["slices"].items()):
        print(f"  {name} {rate:.2f}")
    if summary["failed"]:
        print("failed: " + ", ".join(summary["failed"]))
    print("Answers passed." if summary["ok"] else "Answers failed.")
    if not summary["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

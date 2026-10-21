"""Score one answers file and print slice rates. It does not print an expected value.

    python -m agent_check.score --answers <file> [--data <build>] [--baseline]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from agent_check.answers import score
from agent_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 5 answers file.")
    parser.add_argument("--answers", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--baseline", action="store_true", help="Waive the model-register check.")
    args = parser.parse_args(argv)
    summary = score(Path(args.answers), load(Path(args.data)), Path(args.data), check_model=not args.baseline)
    print(f"overall {summary['overall']:.2f}")
    for name, rate in sorted(summary["slices"].items()):
        print(f"  {name} {rate:.2f} ({summary['counts'].get(name, 0)})")
    if summary["missed_stops"]:
        print("missed stops: " + ", ".join(summary["missed_stops"]))
    if summary["false_stops"]:
        print("false stops: " + ", ".join(summary["false_stops"][:12]))
    if summary["failed"]:
        print("failed: " + ", ".join(summary["failed"]))
    print("Answers passed." if summary["ok"] else "Answers failed.")
    if not summary["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

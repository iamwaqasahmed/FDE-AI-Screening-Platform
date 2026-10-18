"""Score one team's Week 6 folder.

    python -m handoff_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from handoff_check.dockerfile import score as score_dockerfile
from handoff_check.files import score as score_files
from handoff_check.findings import load as load_findings
from handoff_check.gold import load
from handoff_check.records import score as score_records
from handoff_check.report import evaluate, render
from handoff_check.texts import score as score_texts


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 6 handoff folder against the seed's gold.")
    parser.add_argument("--work", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items and the three CSV files.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    gold = load(data)
    written = {} if args.rerun else score_records(work, gold)
    texts = {} if args.rerun else score_texts(work, gold)
    image = {"ok": True} if args.rerun else score_dockerfile(work, gold)
    report = evaluate(gold, load_findings(work), score_files(work, gold), image, written, texts, rerun=args.rerun)
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

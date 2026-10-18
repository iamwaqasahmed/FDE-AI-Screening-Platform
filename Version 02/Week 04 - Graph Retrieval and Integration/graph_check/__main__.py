"""Score one team's Week 4 folder.

    python -m graph_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from graph_check.answers import score as score_answers
from graph_check.contract import score as score_contract
from graph_check.findings import load as load_findings
from graph_check.gold import load, reconciliation
from graph_check.reconciliation import score as score_reconciliation
from graph_check.report import evaluate, render
from graph_check.resend import score as score_resend
from graph_check.texts import score_file


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 4 graph folder against the seed's gold.")
    parser.add_argument("--work", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items, answers, reconciliation, and the re-send.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    gold = load(data)
    report = evaluate(
        gold,
        load_findings(work),
        score_answers(work / "answers.jsonl", gold),
        score_reconciliation(work / "reconciliation.csv", reconciliation(data)),
        score_resend(work / "resend.csv", gold),
        None if args.rerun else score_contract(work / "contracts" / "bureau_dispatch.yaml", gold),
        None if args.rerun else score_file(work / "graph-card.md", gold, "card"),
        None if args.rerun else score_file(work / "incident-note.md", gold, "note"),
        rerun=args.rerun,
    )
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Score one team's Week 3 folder.

    python -m evidence_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from evidence_check.answers import score as score_answers
from evidence_check.contract import score as score_contract
from evidence_check.extract import score as score_extract
from evidence_check.findings import load as load_findings
from evidence_check.gold import extract, load
from evidence_check.redaction import score as score_redaction
from evidence_check.report import evaluate, render
from evidence_check.texts import score_file


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 3 evidence folder against the seed's gold.")
    parser.add_argument("--work", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items, answers, redaction, and the extract.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    gold = load(data)
    report = evaluate(
        gold,
        load_findings(work),
        score_answers(work / "answers.jsonl", gold),
        score_redaction(work / "redactions.csv", gold),
        score_extract(work / "vendor_extract.csv", extract(data)),
        None if args.rerun else score_contract(work / "contracts" / "vendor_extract.yaml", gold),
        None if args.rerun else score_file(work / "retrieval-card.md", gold, "card"),
        None if args.rerun else score_file(work / "evidence-note.md", gold, "note"),
        rerun=args.rerun,
    )
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

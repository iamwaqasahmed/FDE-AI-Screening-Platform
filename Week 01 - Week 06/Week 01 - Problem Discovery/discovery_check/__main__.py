"""Score one team's Week 1 folder.

    python -m discovery_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from discovery_check.brief import score_file
from discovery_check.findings import load as load_findings
from discovery_check.gold import load, personas
from discovery_check.interviews import score_folder as score_interviews
from discovery_check.notes import score_folder as score_notes
from discovery_check.report import evaluate, render


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 1 discovery folder against the seed's gold.")
    parser.add_argument("--work", required=True, help="Folder with findings.json, interviews/, notes/, and brief.md.")
    parser.add_argument("--data", default="data", help="Built data folder. Default: data.")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items and interview scripts only.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    people = personas(data)
    report = evaluate(
        load(data),
        load_findings(work),
        score_interviews(work / "interviews", people),
        None if args.rerun else score_notes(work / "notes", people),
        None if args.rerun else score_file(work / "brief.md", load(data)),
        rerun=args.rerun,
    )
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Score one team's Week 5 folder.

    python -m agent_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from agent_check.answers import score as score_answers
from agent_check.contract import score as score_contract
from agent_check.files import score_backlog, score_sweep
from agent_check.findings import load as load_findings
from agent_check.gold import backlog, load, sweep
from agent_check.report import evaluate, render
from agent_check.texts import score_file


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 5 agent folder against the seed's gold.")
    parser.add_argument("--work", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items, answers, the backlog, and the sweep.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    gold = load(data)
    report = evaluate(
        gold,
        load_findings(work),
        score_answers(work / "answers.jsonl", gold, data),
        score_backlog(work / "backlog.csv", backlog(data)),
        score_sweep(work / "sweep.csv", sweep(data)),
        None if args.rerun else score_contract(work / "contracts" / "agent_trajectory.yaml", gold),
        None if args.rerun else score_file(work / "agent-card.md", gold, "card"),
        None if args.rerun else score_file(work / "cdo-reply.md", gold, "reply"),
        None if args.rerun else score_file(work / "press-line.md", gold, "line"),
        rerun=args.rerun,
    )
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Score one team's Week 2 folder.

    python -m enterprise_check --work <folder> [--data data] [--rerun]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from enterprise_check.clusters import load as load_clusters
from enterprise_check.clusters import score as score_clusters
from enterprise_check.contracts import score_folder as score_contracts
from enterprise_check.findings import load as load_findings
from enterprise_check.gold import load, records
from enterprise_check.probes import load as load_rules
from enterprise_check.probes import score as score_rules
from enterprise_check.report import evaluate, render
from enterprise_check.texts import score_file


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score a Week 2 enterprise-data folder against the seed's gold.")
    parser.add_argument("--work", required=True)
    parser.add_argument("--data", default="data")
    parser.add_argument("--rerun", action="store_true", help="Grade computed items, clusters, and pathway rules only.")
    args = parser.parse_args(argv)
    data, work = Path(args.data), Path(args.work)
    gold = load(data)
    report = evaluate(
        gold,
        load_findings(work),
        score_clusters(load_clusters(work / "clusters.csv"), records(data)),
        score_rules(load_rules(work / "pathway_rules.csv"), gold["pathway"]["probes"]),
        None if args.rerun else score_contracts(work / "contracts", gold),
        None if args.rerun else score_file(work / "model.md", gold, "model"),
        None if args.rerun else score_file(work / "data-note.md", gold, "note"),
        rerun=args.rerun,
    )
    print(render(report, rerun=args.rerun))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

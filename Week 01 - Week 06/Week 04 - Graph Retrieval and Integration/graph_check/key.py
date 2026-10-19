"""Print the Week 4 gold. Participants do not run this.

    python -m graph_check.key --data <build>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graph_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print Week 4 gold for maintainers.")
    parser.add_argument("--data", default="data")
    args = parser.parse_args(argv)
    gold = load(Path(args.data))
    payload = {
        "as_of": gold["as_of"],
        "questions": len(gold["questions"]),
        "baselines": {name: gold["baselines"][name]["overall"] for name in ("keyword", "tfidf")},
        "best": gold["baselines"]["best"],
        "items": gold["items"],
        "truth": gold["truth"],
        "resend": len(gold["resend"]),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

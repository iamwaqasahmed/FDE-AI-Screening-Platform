"""Print the Week 6 gold. Participants do not run this.

    python -m handoff_check.key --data <build>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from handoff_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print Week 6 gold for maintainers.")
    parser.add_argument("--data", default="data")
    args = parser.parse_args(argv)
    gold = load(Path(args.data))
    payload = {"as_of": gold["as_of"], "friday": gold["friday"], "items": gold["items"], "truth": gold["truth"],
               "files": {"flows": len(gold["files"]["flows"]), "hazards": gold["files"]["hazards"]["groups"]}}
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

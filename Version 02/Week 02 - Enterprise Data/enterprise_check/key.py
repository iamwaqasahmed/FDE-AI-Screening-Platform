"""Print the Week 2 gold. Maintainers only. Person ids are not printed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from enterprise_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print Week 2 enterprise gold. Maintainers only.")
    parser.add_argument("--data", default="data")
    args = parser.parse_args(argv)
    gold = load(Path(args.data))
    gold["pathway"] = {"site_rules": gold["pathway"]["site_rules"], "probes": len(gold["pathway"]["probes"])}
    print(json.dumps(gold, indent=2))


if __name__ == "__main__":
    main()

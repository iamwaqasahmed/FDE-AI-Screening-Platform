"""Print the Week 1 answer key for one build. Facilitators only.

    python -m discovery_check.key --data data
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from discovery_check.gold import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print the Week 1 discovery answer key.")
    parser.add_argument("--data", default="data")
    args = parser.parse_args(argv)
    print(json.dumps(load(Path(args.data)), indent=2))


if __name__ == "__main__":
    main()

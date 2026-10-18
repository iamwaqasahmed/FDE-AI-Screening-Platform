"""Build a Week 5 folder from the visible files.

    python -m reference_agent --data <build> --out <dir> --profile <name>
"""

from __future__ import annotations

import argparse
from pathlib import Path

from reference_agent.assemble import build


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the Week 5 reference folder for one build.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--profile", default="")
    args = parser.parse_args(argv)
    build(Path(args.data), Path(args.out))
    print(f"Wrote the reference folder to {args.out}")


if __name__ == "__main__":
    main()

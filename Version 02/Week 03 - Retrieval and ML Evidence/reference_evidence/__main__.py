"""A reference Week 3 solution. Participants leave this folder closed.

    python -m reference_evidence --data <build> --out <dir> --profile <name>
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from reference_evidence.assemble import build


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write a reference Week 3 folder from a built drop.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--profile", default="")
    args = parser.parse_args(argv)
    if args.profile:
        os.environ["HARTLAND_PROFILE"] = args.profile
    build(Path(args.data), Path(args.out))
    print(f"Wrote a reference Week 3 folder to {args.out}")


if __name__ == "__main__":
    main()

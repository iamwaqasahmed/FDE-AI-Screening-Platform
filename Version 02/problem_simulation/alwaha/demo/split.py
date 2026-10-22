"""Show the two DNA splits. The printout does not name the defect."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.samples.dna import dna_rows
from alwaha.samples.script import load_baseline


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show the two DNA splits.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    script = load_baseline("dna.py")
    rows = dna_rows(profile.seed)
    print(f"row {script.show(script.score(rows, 'row'))}")
    print(f"person {script.show(script.score(rows, 'person'))}")
    print(f"shared {script.shared(rows)}")


if __name__ == "__main__":
    main(sys.argv[1:])

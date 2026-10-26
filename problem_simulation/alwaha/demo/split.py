"""Show the two DNA splits. The printout does not name the defect.

The baseline script scores the seeded rows once by row and once by person. The page also prints the shared count. The defect name is not printed.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.samples.dna import dna_rows
from alwaha.samples.script import load_baseline


def main(argv: list[str] | None = None) -> None:
    """Print the row score, the person score, and the shared count. Returns nothing.

    argv replaces the process arguments. The profile seed chooses the rows the baseline script scores.
    """
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
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])

"""Show the sponsor and the DPO in disagreement. The non-goal list stays off the page.

The two printed lines are fixed. Loading the profile selects the world, and the non-goal list is not read onto the page.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load


def main(argv: list[str] | None = None) -> None:
    """Print the two disagreement lines. Returns nothing.

    argv replaces the process arguments. The profile is loaded so the command is bound to a world, and the lines themselves do not come from a gold pack.
    """
    parser = argparse.ArgumentParser(description="Show the sponsor and the DPO in disagreement.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    print("the sponsor asks for triage in the front desk")
    print("the dpo keeps patient data off ext-large")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])

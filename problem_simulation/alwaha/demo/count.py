"""Show an invented count beside the tool result. The printout does not name a failure.

INVENTED is the figure printed as the model count. The tool count is the count on the status scenario for this profile. Both numbers are printed, and the page never says which one is wrong.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.agent.scenarios import scenarios
from alwaha.config.profile import load

INVENTED = 12


def main(argv: list[str] | None = None) -> None:
    """Print the invented count and the status scenario's tool count. Returns nothing.

    argv replaces the process arguments. The profile's canary selects the scenario list. Only the status row supplies the tool count.
    """
    parser = argparse.ArgumentParser(description="Show an invented count and the tool result.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    # The status scenario is the tool result on this page. Other scenarios are skipped.
    status = next(row for row in scenarios(profile.canary()) if row["scenario"] == "status")
    print(f"model count {INVENTED}")
    print(f"tool count {status['count']}")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])

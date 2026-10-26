"""Show one referral's two arrivals. The printout does not name the defect.

Arrivals for the order referral are printed with their place in the stream and their sequence. The approval count is the length of the approval ids on the order scenario. profile.canary() selects that stream and is not printed.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.events.gold import scenario_rows
from alwaha.events.stream import ORDER_REF, events


def main(argv: list[str] | None = None) -> None:
    """Print each matching arrival and the approval count. Returns nothing.

    argv replaces the process arguments. The profile selects the event stream and the scenario rows. The defect name is not printed.
    """
    parser = argparse.ArgumentParser(description="Show two arrivals for one referral.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    canary = profile.canary()
    # Only arrivals for the order referral are printed. The index is their place in the full stream.
    pair = [(index, row) for index, row in enumerate(events(canary), start=1) if row["referral_id"] == ORDER_REF]
    for index, row in pair:
        print(f"arrival {index} sequence {row['sequence']}")
    # The approval count comes from the order scenario, not from the arrival rows above.
    outcome = next(item for item in scenario_rows(canary) if item["scenario"] == "order")
    print(f"approvals {len(outcome['approval_ids'])}")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])

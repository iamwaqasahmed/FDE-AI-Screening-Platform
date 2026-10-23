"""Show one referral's two arrivals. The printout does not name the defect."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.events.gold import scenario_rows
from alwaha.events.stream import ORDER_REF, events


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show two arrivals for one referral.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    canary = profile.canary()
    pair = [(index, row) for index, row in enumerate(events(canary), start=1) if row["referral_id"] == ORDER_REF]
    for index, row in pair:
        print(f"arrival {index} sequence {row['sequence']}")
    outcome = next(item for item in scenario_rows(canary) if item["scenario"] == "order")
    print(f"approvals {len(outcome['approval_ids'])}")


if __name__ == "__main__":
    main(sys.argv[1:])

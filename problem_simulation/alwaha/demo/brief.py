"""Show the sponsor and the DPO in disagreement. The non-goal list stays off the page."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show the sponsor and the DPO in disagreement.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    print("the sponsor asks for triage in the front desk")
    print("the dpo keeps patient data off ext-large")


if __name__ == "__main__":
    main(sys.argv[1:])

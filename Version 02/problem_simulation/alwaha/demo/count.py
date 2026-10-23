"""Show an invented count beside the tool result. The printout does not name a failure."""

from __future__ import annotations

import argparse
import sys

from alwaha.agent.scenarios import scenarios
from alwaha.config.profile import load

INVENTED = 12


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show an invented count and the tool result.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    status = next(row for row in scenarios(profile.canary()) if row["scenario"] == "status")
    print(f"model count {INVENTED}")
    print(f"tool count {status['count']}")


if __name__ == "__main__":
    main(sys.argv[1:])

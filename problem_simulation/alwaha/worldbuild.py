"""Build the facilitator world for one profile. python -m alwaha.worldbuild."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.paths import world_dir
from alwaha.world_write import write_world


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the Al-Waha world for a profile.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--volume-rows", type=int, default=None)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    root = world_dir(profile.name)
    digest = write_world(profile, root, stream_rows=args.volume_rows)
    print(f"Wrote world for {profile.name}")
    print(f"World: {root}")
    print(f"People: {profile.people}")
    print(f"Fingerprint: {digest}")


if __name__ == "__main__":
    main(sys.argv[1:])

"""Build rel-w1d1. A second run with the same profile writes the same bytes."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.release.write import RELEASE, write_release


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the Al-Waha Day 1 release.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default=RELEASE)
    args = parser.parse_args(argv)
    if args.release != RELEASE:
        raise SystemExit(f"This slice builds {RELEASE} only.")
    profile = load(args.profile)
    pack, truth = pack_dir(profile.name), truth_dir(profile.name)
    digest = write_release(profile, pack, truth)
    print(f"Wrote {args.release} for {profile.name}")
    print(f"Pack: {pack}")
    print(f"Truth: {truth}")
    print(f"Fingerprint: {digest}")


if __name__ == "__main__":
    main(sys.argv[1:])

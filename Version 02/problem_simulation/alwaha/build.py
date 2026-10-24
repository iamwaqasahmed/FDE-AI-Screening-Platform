"""Build a release. A second run with the same profile writes the same bytes."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.release.day2 import RELEASE as DAY2
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import RELEASE as DAY3
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import RELEASE as DAY4
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import RELEASE as DAY5
from alwaha.release.day5 import write_day5
from alwaha.release.w2d1 import RELEASE as W2D1
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import RELEASE as W2D2
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import RELEASE as W2D3
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.write import RELEASE as DAY1
from alwaha.release.write import write_release


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write an Al-Waha release.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default=DAY1)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    if args.release == DAY1:
        pack, truth = pack_dir(profile.name), truth_dir(profile.name)
        digest = write_release(profile, pack, truth)
    elif args.release == DAY2:
        pack = pack_dir(profile.name, DAY2)
        truth = truth_dir(profile.name)
        digest = write_day2(profile, pack, truth)
    elif args.release == DAY3:
        pack = pack_dir(profile.name, DAY3)
        truth = truth_dir(profile.name)
        digest = write_day3(profile, pack, truth)
    elif args.release == DAY4:
        pack = pack_dir(profile.name, DAY4)
        truth = truth_dir(profile.name)
        digest = write_day4(profile, pack, truth)
    elif args.release == DAY5:
        pack = pack_dir(profile.name, DAY5)
        truth = truth_dir(profile.name)
        digest = write_day5(profile, pack, truth)
    elif args.release == W2D1:
        pack = pack_dir(profile.name, W2D1)
        truth = truth_dir(profile.name)
        digest = write_w2d1(profile, pack, truth)
    elif args.release == W2D2:
        pack = pack_dir(profile.name, W2D2)
        truth = truth_dir(profile.name)
        digest = write_w2d2(profile, pack, truth)
    elif args.release == W2D3:
        pack = pack_dir(profile.name, W2D3)
        truth = truth_dir(profile.name)
        digest = write_w2d3(profile, pack, truth)
    else:
        raise SystemExit(f"Unknown release {args.release}.")
    print(f"Wrote {args.release} for {profile.name}")
    print(f"Pack: {pack}")
    print(f"Truth: {truth}")
    print(f"Fingerprint: {digest}")


if __name__ == "__main__":
    main(sys.argv[1:])

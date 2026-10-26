"""Build a release. A second run with the same profile writes the same bytes.

The release argument selects a writer. The first release uses the default pack path. Every later release names its own pack directory. Truth is the shared directory for the profile. An unknown release id stops before anything is written. The command prints the release, the profile, both paths, and the fingerprint.
"""

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
from alwaha.release.w2d4 import RELEASE as W2D4
from alwaha.release.w2d4 import write_w2d4
from alwaha.release.w2d5 import RELEASE as W2D5
from alwaha.release.w2d5 import write_w2d5
from alwaha.release.w3d1 import RELEASE as W3D1
from alwaha.release.w3d1 import write_w3d1
from alwaha.release.w3d2 import RELEASE as W3D2
from alwaha.release.w3d2 import write_w3d2
from alwaha.release.w3d3 import RELEASE as W3D3
from alwaha.release.w3d3 import write_w3d3
from alwaha.release.w3d4 import RELEASE as W3D4
from alwaha.release.w3d4 import write_w3d4
from alwaha.release.w3d5 import RELEASE as W3D5
from alwaha.release.w3d5 import write_w3d5
from alwaha.release.w4d1 import RELEASE as W4D1
from alwaha.release.w4d1 import write_w4d1
from alwaha.release.w4d2 import RELEASE as W4D2
from alwaha.release.w4d2 import write_w4d2
from alwaha.release.w4d3 import RELEASE as W4D3
from alwaha.release.w4d3 import write_w4d3
from alwaha.release.w4d4 import RELEASE as W4D4
from alwaha.release.w4d4 import write_w4d4
from alwaha.release.w4d5 import RELEASE as W4D5
from alwaha.release.w4d5 import write_w4d5
from alwaha.release.write import RELEASE as DAY1
from alwaha.release.write import write_release


def main(argv: list[str] | None = None) -> None:
    """Write the selected release for the loaded profile and print the fingerprint."""
    parser = argparse.ArgumentParser(description="Write an Al-Waha release.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default=DAY1)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    # The first release uses the default pack path. Later releases each name a directory.
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
    elif args.release == W2D4:
        pack = pack_dir(profile.name, W2D4)
        truth = truth_dir(profile.name)
        digest = write_w2d4(profile, pack, truth)
    elif args.release == W2D5:
        pack = pack_dir(profile.name, W2D5)
        truth = truth_dir(profile.name)
        digest = write_w2d5(profile, pack, truth)
    elif args.release == W3D1:
        pack = pack_dir(profile.name, W3D1)
        truth = truth_dir(profile.name)
        digest = write_w3d1(profile, pack, truth)
    elif args.release == W3D2:
        pack = pack_dir(profile.name, W3D2)
        truth = truth_dir(profile.name)
        digest = write_w3d2(profile, pack, truth)
    elif args.release == W3D3:
        pack = pack_dir(profile.name, W3D3)
        truth = truth_dir(profile.name)
        digest = write_w3d3(profile, pack, truth)
    elif args.release == W3D4:
        pack = pack_dir(profile.name, W3D4)
        truth = truth_dir(profile.name)
        digest = write_w3d4(profile, pack, truth)
    elif args.release == W3D5:
        pack = pack_dir(profile.name, W3D5)
        truth = truth_dir(profile.name)
        digest = write_w3d5(profile, pack, truth)
    elif args.release == W4D1:
        pack = pack_dir(profile.name, W4D1)
        truth = truth_dir(profile.name)
        digest = write_w4d1(profile, pack, truth)
    elif args.release == W4D2:
        pack = pack_dir(profile.name, W4D2)
        truth = truth_dir(profile.name)
        digest = write_w4d2(profile, pack, truth)
    elif args.release == W4D3:
        pack = pack_dir(profile.name, W4D3)
        truth = truth_dir(profile.name)
        digest = write_w4d3(profile, pack, truth)
    elif args.release == W4D4:
        pack = pack_dir(profile.name, W4D4)
        truth = truth_dir(profile.name)
        digest = write_w4d4(profile, pack, truth)
    elif args.release == W4D5:
        pack = pack_dir(profile.name, W4D5)
        truth = truth_dir(profile.name)
        digest = write_w4d5(profile, pack, truth)
    else:
        # Stop before creating a directory for an id this builder does not know.
        raise SystemExit(f"Unknown release {args.release}.")
    print(f"Wrote {args.release} for {profile.name}")
    print(f"Pack: {pack}")
    print(f"Truth: {truth}")
    print(f"Fingerprint: {digest}")


if __name__ == "__main__":
    main(sys.argv[1:])

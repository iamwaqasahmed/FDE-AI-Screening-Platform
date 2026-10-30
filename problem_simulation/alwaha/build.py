"""Build a release. A second run with the same profile writes the same bytes.

The release argument selects a writer. The first release uses the default pack path. Every later release names its own pack directory. Truth is the shared directory for the profile. An unknown release id stops before anything is written. The command prints the release, the profile, both paths, and the fingerprint.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.release.m01_l02 import RELEASE as M01_L02
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import RELEASE as M01_L03
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import RELEASE as M01_L04
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import RELEASE as M01_L05
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.m02_l01 import RELEASE as M02_L01
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import RELEASE as M02_L02
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import RELEASE as M02_L03
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.m02_l04 import RELEASE as M02_L04
from alwaha.release.m02_l04 import write_m02_l04
from alwaha.release.m02_l05 import RELEASE as M02_L05
from alwaha.release.m02_l05 import write_m02_l05
from alwaha.release.m03_l01 import RELEASE as M03_L01
from alwaha.release.m03_l01 import write_m03_l01
from alwaha.release.m03_l02 import RELEASE as M03_L02
from alwaha.release.m03_l02 import write_m03_l02
from alwaha.release.m03_l03 import RELEASE as M03_L03
from alwaha.release.m03_l03 import write_m03_l03
from alwaha.release.m03_l04 import RELEASE as M03_L04
from alwaha.release.m03_l04 import write_m03_l04
from alwaha.release.m03_l05 import RELEASE as M03_L05
from alwaha.release.m03_l05 import write_m03_l05
from alwaha.release.m04_l01 import RELEASE as M04_L01
from alwaha.release.m04_l01 import write_m04_l01
from alwaha.release.m04_l02 import RELEASE as M04_L02
from alwaha.release.m04_l02 import write_m04_l02
from alwaha.release.m04_l03 import RELEASE as M04_L03
from alwaha.release.m04_l03 import write_m04_l03
from alwaha.release.m04_l04 import RELEASE as M04_L04
from alwaha.release.m04_l04 import write_m04_l04
from alwaha.release.m04_l05 import RELEASE as M04_L05
from alwaha.release.m04_l05 import write_m04_l05
from alwaha.release.write import RELEASE as M01_L01
from alwaha.release.write import write_release


def main(argv: list[str] | None = None) -> None:
    """Write the selected release for the loaded profile and print the fingerprint."""
    parser = argparse.ArgumentParser(description="Write an Al-Waha release.")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default=M01_L01)
    args = parser.parse_args(argv)
    profile = load(args.profile)
    # The first release uses the default pack path. Later releases each name a directory.
    if args.release == M01_L01:
        pack, truth = pack_dir(profile.name), truth_dir(profile.name)
        digest = write_release(profile, pack, truth)
    elif args.release == M01_L02:
        pack = pack_dir(profile.name, M01_L02)
        truth = truth_dir(profile.name)
        digest = write_m01_l02(profile, pack, truth)
    elif args.release == M01_L03:
        pack = pack_dir(profile.name, M01_L03)
        truth = truth_dir(profile.name)
        digest = write_m01_l03(profile, pack, truth)
    elif args.release == M01_L04:
        pack = pack_dir(profile.name, M01_L04)
        truth = truth_dir(profile.name)
        digest = write_m01_l04(profile, pack, truth)
    elif args.release == M01_L05:
        pack = pack_dir(profile.name, M01_L05)
        truth = truth_dir(profile.name)
        digest = write_m01_l05(profile, pack, truth)
    elif args.release == M02_L01:
        pack = pack_dir(profile.name, M02_L01)
        truth = truth_dir(profile.name)
        digest = write_m02_l01(profile, pack, truth)
    elif args.release == M02_L02:
        pack = pack_dir(profile.name, M02_L02)
        truth = truth_dir(profile.name)
        digest = write_m02_l02(profile, pack, truth)
    elif args.release == M02_L03:
        pack = pack_dir(profile.name, M02_L03)
        truth = truth_dir(profile.name)
        digest = write_m02_l03(profile, pack, truth)
    elif args.release == M02_L04:
        pack = pack_dir(profile.name, M02_L04)
        truth = truth_dir(profile.name)
        digest = write_m02_l04(profile, pack, truth)
    elif args.release == M02_L05:
        pack = pack_dir(profile.name, M02_L05)
        truth = truth_dir(profile.name)
        digest = write_m02_l05(profile, pack, truth)
    elif args.release == M03_L01:
        pack = pack_dir(profile.name, M03_L01)
        truth = truth_dir(profile.name)
        digest = write_m03_l01(profile, pack, truth)
    elif args.release == M03_L02:
        pack = pack_dir(profile.name, M03_L02)
        truth = truth_dir(profile.name)
        digest = write_m03_l02(profile, pack, truth)
    elif args.release == M03_L03:
        pack = pack_dir(profile.name, M03_L03)
        truth = truth_dir(profile.name)
        digest = write_m03_l03(profile, pack, truth)
    elif args.release == M03_L04:
        pack = pack_dir(profile.name, M03_L04)
        truth = truth_dir(profile.name)
        digest = write_m03_l04(profile, pack, truth)
    elif args.release == M03_L05:
        pack = pack_dir(profile.name, M03_L05)
        truth = truth_dir(profile.name)
        digest = write_m03_l05(profile, pack, truth)
    elif args.release == M04_L01:
        pack = pack_dir(profile.name, M04_L01)
        truth = truth_dir(profile.name)
        digest = write_m04_l01(profile, pack, truth)
    elif args.release == M04_L02:
        pack = pack_dir(profile.name, M04_L02)
        truth = truth_dir(profile.name)
        digest = write_m04_l02(profile, pack, truth)
    elif args.release == M04_L03:
        pack = pack_dir(profile.name, M04_L03)
        truth = truth_dir(profile.name)
        digest = write_m04_l03(profile, pack, truth)
    elif args.release == M04_L04:
        pack = pack_dir(profile.name, M04_L04)
        truth = truth_dir(profile.name)
        digest = write_m04_l04(profile, pack, truth)
    elif args.release == M04_L05:
        pack = pack_dir(profile.name, M04_L05)
        truth = truth_dir(profile.name)
        digest = write_m04_l05(profile, pack, truth)
    else:
        # Stop before creating a directory for an id this builder does not know.
        raise SystemExit(f"Unknown release {args.release}.")
    print(f"Wrote {args.release} for {profile.name}")
    print(f"Pack: {pack}")
    print(f"Truth: {truth}")
    print(f"Fingerprint: {digest}")


if __name__ == "__main__":
    main(sys.argv[1:])

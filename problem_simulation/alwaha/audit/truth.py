"""Write release gold into truth/ and the pack bytes into a throwaway directory.

Every writer is called with its own pack directory under a temporary root. That root is removed when the block ends. The truth directory is the real one, shared by every writer, so the gold files remain after the packs are discarded.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from alwaha.paths import truth_dir
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.m02_l04 import write_m02_l04
from alwaha.release.m02_l05 import write_m02_l05
from alwaha.release.m03_l01 import write_m03_l01
from alwaha.release.m03_l02 import write_m03_l02
from alwaha.release.m03_l03 import write_m03_l03
from alwaha.release.m03_l04 import write_m03_l04
from alwaha.release.m03_l05 import write_m03_l05
from alwaha.release.m04_l01 import write_m04_l01
from alwaha.release.m04_l02 import write_m04_l02
from alwaha.release.m04_l03 import write_m04_l03
from alwaha.release.m04_l04 import write_m04_l04
from alwaha.release.m04_l05 import write_m04_l05
from alwaha.release.write import write_release

WRITERS = (
    write_release,
    write_m01_l02,
    write_m01_l03,
    write_m01_l04,
    write_m01_l05,
    write_m02_l01,
    write_m02_l02,
    write_m02_l03,
    write_m02_l04,
    write_m02_l05,
    write_m03_l01,
    write_m03_l02,
    write_m03_l03,
    write_m03_l04,
    write_m03_l05,
    write_m04_l01,
    write_m04_l02,
    write_m04_l03,
    write_m04_l04,
    write_m04_l05,
)


def build_truth(profile) -> Path:
    """Write every release into a throwaway pack and leave the gold in the profile truth directory."""
    truth = truth_dir(profile.name)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for index, writer in enumerate(WRITERS):
            # Each writer gets a fresh pack directory. They all share the truth directory.
            writer(profile, root / f"pack-{index}", truth)
    return truth

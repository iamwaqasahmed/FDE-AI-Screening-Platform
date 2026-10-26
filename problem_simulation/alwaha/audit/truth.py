"""Write release gold into truth/ and the pack bytes into a throwaway directory.

Every writer is called with its own pack directory under a temporary root. That root is removed when the block ends. The truth directory is the real one, shared by every writer, so the gold files remain after the packs are discarded.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from alwaha.paths import truth_dir
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.w2d4 import write_w2d4
from alwaha.release.w2d5 import write_w2d5
from alwaha.release.w3d1 import write_w3d1
from alwaha.release.w3d2 import write_w3d2
from alwaha.release.w3d3 import write_w3d3
from alwaha.release.w3d4 import write_w3d4
from alwaha.release.w3d5 import write_w3d5
from alwaha.release.w4d1 import write_w4d1
from alwaha.release.w4d2 import write_w4d2
from alwaha.release.w4d3 import write_w4d3
from alwaha.release.w4d4 import write_w4d4
from alwaha.release.w4d5 import write_w4d5
from alwaha.release.write import write_release

WRITERS = (
    write_release,
    write_day2,
    write_day3,
    write_day4,
    write_day5,
    write_w2d1,
    write_w2d2,
    write_w2d3,
    write_w2d4,
    write_w2d5,
    write_w3d1,
    write_w3d2,
    write_w3d3,
    write_w3d4,
    write_w3d5,
    write_w4d1,
    write_w4d2,
    write_w4d3,
    write_w4d4,
    write_w4d5,
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

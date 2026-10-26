"""Output locations for a profile. Practice pack is the published drop.

The constants point at the student packets and the filled work copies for each teaching day. pack_dir is where a release is written. truth_dir is the facilitator gold beside a profile. world_dir is the facilitator world, and it refuses to resolve inside the published data tree.
"""

from __future__ import annotations

from pathlib import Path

SIM_ROOT = Path(__file__).resolve().parents[1]
VERSION_ROOT = SIM_ROOT.parent
STARTER_ROOT = VERSION_ROOT / "Week 01" / "Day 01" / "Student_Copy" / "packet" / "starter"
DAY1_WORK = VERSION_ROOT / "Week 01" / "Day 01" / "Solution_Copy" / "work"
DAY2_ROOT = VERSION_ROOT / "Week 01" / "Day 02"
BASELINES_ROOT = DAY2_ROOT / "Student_Copy" / "packet" / "baselines"
TEMPLATES_ROOT = DAY2_ROOT / "Student_Copy" / "packet" / "templates"
DAY2_WORK = DAY2_ROOT / "Solution_Copy" / "work"
DAY3_ROOT = VERSION_ROOT / "Week 01" / "Day 03"
WORKFLOW_ROOT = DAY3_ROOT / "Student_Copy" / "packet" / "workflow"
DAY3_TEMPLATES = DAY3_ROOT / "Student_Copy" / "packet" / "templates"
DAY3_WORK = DAY3_ROOT / "Solution_Copy" / "work"
DAY4_ROOT = VERSION_ROOT / "Week 01" / "Day 04"
AGENT_ROOT = DAY4_ROOT / "Student_Copy" / "packet" / "agent"
DAY4_TEMPLATES = DAY4_ROOT / "Student_Copy" / "packet" / "templates"
DAY4_WORK = DAY4_ROOT / "Solution_Copy" / "work"
DAY5_ROOT = VERSION_ROOT / "Week 01" / "Day 05"
DAY5_TEMPLATES = DAY5_ROOT / "Student_Copy" / "packet" / "templates"
DAY5_WORK = DAY5_ROOT / "Solution_Copy" / "work"
W2D1_ROOT = VERSION_ROOT / "Week 02" / "Day 01"
W2D1_APP = W2D1_ROOT / "Student_Copy" / "packet" / "app"
W2D1_TEMPLATES = W2D1_ROOT / "Student_Copy" / "packet" / "templates"
W2D1_WORK = W2D1_ROOT / "Solution_Copy" / "work"
W2D2_ROOT = VERSION_ROOT / "Week 02" / "Day 02"
W2D2_APP = W2D2_ROOT / "Student_Copy" / "packet" / "app"
W2D2_TEMPLATES = W2D2_ROOT / "Student_Copy" / "packet" / "templates"
W2D2_WORK = W2D2_ROOT / "Solution_Copy" / "work"
W2D3_ROOT = VERSION_ROOT / "Week 02" / "Day 03"
W2D3_APP = W2D3_ROOT / "Student_Copy" / "packet" / "app"
W2D3_TEMPLATES = W2D3_ROOT / "Student_Copy" / "packet" / "templates"
W2D3_TESTS = W2D3_ROOT / "Student_Copy" / "packet" / "tests"
W2D3_WORK = W2D3_ROOT / "Solution_Copy" / "work"
W2D4_ROOT = VERSION_ROOT / "Week 02" / "Day 04"
W2D4_APP = W2D4_ROOT / "Student_Copy" / "packet" / "app"
W2D4_TEMPLATES = W2D4_ROOT / "Student_Copy" / "packet" / "templates"
W2D4_TESTS = W2D4_ROOT / "Student_Copy" / "packet" / "tests"
W2D4_DEPLOY = W2D4_ROOT / "Student_Copy" / "packet" / "deploy"
W2D4_WORK = W2D4_ROOT / "Solution_Copy" / "work"
W2D5_ROOT = VERSION_ROOT / "Week 02" / "Day 05"
W2D5_APP = W2D5_ROOT / "Student_Copy" / "packet" / "app"
W2D5_TEMPLATES = W2D5_ROOT / "Student_Copy" / "packet" / "templates"
W2D5_TESTS = W2D5_ROOT / "Student_Copy" / "packet" / "tests"
W2D5_DEPLOY = W2D5_ROOT / "Student_Copy" / "packet" / "deploy"
W2D5_WORK = W2D5_ROOT / "Solution_Copy" / "work"
W3D1_ROOT = VERSION_ROOT / "Week 03" / "Day 01"
W3D1_APP = W3D1_ROOT / "Student_Copy" / "packet" / "app"
W3D1_TEMPLATES = W3D1_ROOT / "Student_Copy" / "packet" / "templates"
W3D1_WORK = W3D1_ROOT / "Solution_Copy" / "work"
W3D2_ROOT = VERSION_ROOT / "Week 03" / "Day 02"
W3D2_APP = W3D2_ROOT / "Student_Copy" / "packet" / "app"
W3D2_TEMPLATES = W3D2_ROOT / "Student_Copy" / "packet" / "templates"
W3D2_WORK = W3D2_ROOT / "Solution_Copy" / "work"
W3D3_ROOT = VERSION_ROOT / "Week 03" / "Day 03"
W3D3_APP = W3D3_ROOT / "Student_Copy" / "packet" / "app"
W3D3_TEMPLATES = W3D3_ROOT / "Student_Copy" / "packet" / "templates"
W3D3_WORK = W3D3_ROOT / "Solution_Copy" / "work"
W3D4_ROOT = VERSION_ROOT / "Week 03" / "Day 04"
W3D4_APP = W3D4_ROOT / "Student_Copy" / "packet" / "app"
W3D4_TEMPLATES = W3D4_ROOT / "Student_Copy" / "packet" / "templates"
W3D4_WORK = W3D4_ROOT / "Solution_Copy" / "work"
W3D5_ROOT = VERSION_ROOT / "Week 03" / "Day 05"
W3D5_APP = W3D5_ROOT / "Student_Copy" / "packet" / "app"
W3D5_TEMPLATES = W3D5_ROOT / "Student_Copy" / "packet" / "templates"
W3D5_WORK = W3D5_ROOT / "Solution_Copy" / "work"
W4D1_ROOT = VERSION_ROOT / "Week 04" / "Day 01"
W4D1_APP = W4D1_ROOT / "Student_Copy" / "packet" / "app"
W4D1_TEMPLATES = W4D1_ROOT / "Student_Copy" / "packet" / "templates"
W4D1_WORK = W4D1_ROOT / "Solution_Copy" / "work"
W4D2_ROOT = VERSION_ROOT / "Week 04" / "Day 02"
W4D2_APP = W4D2_ROOT / "Student_Copy" / "packet" / "app"
W4D2_WORK = W4D2_ROOT / "Solution_Copy" / "work"
W4D3_ROOT = VERSION_ROOT / "Week 04" / "Day 03"
W4D3_APP = W4D3_ROOT / "Student_Copy" / "packet" / "app"
W4D3_WORK = W4D3_ROOT / "Solution_Copy" / "work"
W4D4_ROOT = VERSION_ROOT / "Week 04" / "Day 04"
W4D4_APP = W4D4_ROOT / "Student_Copy" / "packet" / "app"
W4D4_WORK = W4D4_ROOT / "Solution_Copy" / "work"
W4D5_ROOT = VERSION_ROOT / "Week 04" / "Day 05"
W4D5_APP = W4D5_ROOT / "Student_Copy" / "packet" / "app"
W4D5_WORK = W4D5_ROOT / "Solution_Copy" / "work"


def pack_dir(profile: str, release: str = "rel-w1d1") -> Path:
    """Return the pack directory for this profile and release.

    An unknown release stops. Practice writes into the published data tree. Any other profile writes under the build tree. The first release keeps a shorter path. Later releases nest under the release name.
    """
    known = {
        "rel-w1d1",
        "rel-w1d2",
        "rel-w1d3",
        "rel-w1d4",
        "rel-w1d5",
        "rel-w2d1",
        "rel-w2d2",
        "rel-w2d3",
        "rel-w2d4",
        "rel-w2d5",
        "rel-w3d1",
        "rel-w3d2",
        "rel-w3d3",
        "rel-w3d4",
        "rel-w3d5",
        "rel-w4d1",
        "rel-w4d2",
        "rel-w4d3",
        "rel-w4d4",
        "rel-w4d5",
    }
    if release not in known:
        raise SystemExit(f"Unknown release {release}.")
    if profile == "practice":
        # Practice is the published drop, with one directory per release.
        return VERSION_ROOT / "data" / release
    if release == "rel-w1d1":
        # The first release keeps the shorter pack path the early tools already use.
        return SIM_ROOT / "build" / profile / "pack"
    return SIM_ROOT / "build" / profile / release / "pack"


def truth_dir(profile: str) -> Path:
    """Return the facilitator truth directory for this profile. It is shared by every release."""
    return SIM_ROOT / "build" / profile / "truth"


def world_dir(profile: str) -> Path:
    """Facilitator world. Never a path under data/, including assessment.

    The path is resolved before the check, so a relative path cannot slip into the published tree. The data directory itself, and anything inside it, stops the run.
    """
    root = (SIM_ROOT / "build" / profile / "world").resolve()
    data = (VERSION_ROOT / "data").resolve()
    if root == data or data in root.parents:
        # This guard runs even for a profile name that would otherwise look harmless.
        raise SystemExit("Refusing to write a world into data/.")
    return root

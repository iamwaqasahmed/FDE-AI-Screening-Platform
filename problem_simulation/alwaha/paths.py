"""Output locations for a profile. Practice pack is the published drop."""

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
W2D3_APP = W2D3_ROOT / "app"
W2D4_ROOT = VERSION_ROOT / "Week 02" / "Day 04"
W2D4_APP = W2D4_ROOT / "app"
W2D5_ROOT = VERSION_ROOT / "Week 02" / "Day 05"
W2D5_APP = W2D5_ROOT / "app"
W3D1_ROOT = VERSION_ROOT / "Week 03" / "Day 01"
W3D1_APP = W3D1_ROOT / "app"
W3D2_ROOT = VERSION_ROOT / "Week 03" / "Day 02"
W3D2_APP = W3D2_ROOT / "app"
W3D3_ROOT = VERSION_ROOT / "Week 03" / "Day 03"
W3D3_APP = W3D3_ROOT / "app"
W3D4_ROOT = VERSION_ROOT / "Week 03" / "Day 04"
W3D4_APP = W3D4_ROOT / "app"
W3D5_ROOT = VERSION_ROOT / "Week 03" / "Day 05"
W3D5_APP = W3D5_ROOT / "app"
W4D1_ROOT = VERSION_ROOT / "Week 04" / "Day 01"
W4D1_APP = W4D1_ROOT / "app"
W4D2_ROOT = VERSION_ROOT / "Week 04" / "Day 02"
W4D2_APP = W4D2_ROOT / "app"
W4D3_ROOT = VERSION_ROOT / "Week 04" / "Day 03"
W4D3_APP = W4D3_ROOT / "app"
W4D4_ROOT = VERSION_ROOT / "Week 04" / "Day 04"
W4D4_APP = W4D4_ROOT / "app"
W4D5_ROOT = VERSION_ROOT / "Week 04" / "Day 05"
W4D5_APP = W4D5_ROOT / "app"


def pack_dir(profile: str, release: str = "rel-w1d1") -> Path:
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
        return VERSION_ROOT / "data" / release
    if release == "rel-w1d1":
        return SIM_ROOT / "build" / profile / "pack"
    return SIM_ROOT / "build" / profile / release / "pack"


def truth_dir(profile: str) -> Path:
    return SIM_ROOT / "build" / profile / "truth"


def world_dir(profile: str) -> Path:
    """Facilitator world. Never a path under data/, including assessment."""
    root = (SIM_ROOT / "build" / profile / "world").resolve()
    data = (VERSION_ROOT / "data").resolve()
    if root == data or data in root.parents:
        raise SystemExit("Refusing to write a world into data/.")
    return root

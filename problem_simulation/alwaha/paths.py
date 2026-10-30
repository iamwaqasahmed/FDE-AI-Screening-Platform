"""Output locations for a profile. Practice pack is the published drop.

The constants point at the student packets and the filled work copies for each lesson. Constant names still use the old release letters. pack_dir is where a release is written. truth_dir is the facilitator gold beside a profile. world_dir is the facilitator world, and it refuses to resolve inside the published data tree.
"""

from __future__ import annotations

from pathlib import Path

SIM_ROOT = Path(__file__).resolve().parents[1]
VERSION_ROOT = SIM_ROOT.parent
STARTER_ROOT = VERSION_ROOT / "Module 01" / "Lesson 01" / "Student_Copy" / "packet" / "starter"
M01_L01_WORK = VERSION_ROOT / "Module 01" / "Lesson 01" / "Solution_Copy" / "work"
M01_L02_ROOT = VERSION_ROOT / "Module 01" / "Lesson 02" / "Student_Copy"
BASELINES_ROOT = M01_L02_ROOT / "packet" / "baselines"
TEMPLATES_ROOT = M01_L02_ROOT / "packet" / "templates"
M01_L02_WORK = M01_L02_ROOT.parent / "Solution_Copy" / "work"
M01_L03_ROOT = VERSION_ROOT / "Module 01" / "Lesson 03"
WORKFLOW_ROOT = M01_L03_ROOT / "Student_Copy" / "packet" / "workflow"
M01_L03_TEMPLATES = M01_L03_ROOT / "Student_Copy" / "packet" / "templates"
M01_L03_WORK = M01_L03_ROOT / "Solution_Copy" / "work"
M01_L04_ROOT = VERSION_ROOT / "Module 01" / "Lesson 04" / "Student_Copy"
AGENT_ROOT = M01_L04_ROOT / "packet" / "agent"
M01_L04_TEMPLATES = M01_L04_ROOT / "packet" / "templates"
M01_L04_WORK = M01_L04_ROOT.parent / "Solution_Copy" / "work"
M01_L05_ROOT = VERSION_ROOT / "Module 01" / "Lesson 05"
M01_L05_TEMPLATES = M01_L05_ROOT / "Student_Copy" / "packet" / "templates"
M01_L05_WORK = M01_L05_ROOT / "Solution_Copy" / "work"
M02_L01_ROOT = VERSION_ROOT / "Module 02" / "Lesson 01" / "Student_Copy"
M02_L01_APP = M02_L01_ROOT / "packet" / "app"
M02_L01_TEMPLATES = M02_L01_ROOT / "packet" / "templates"
M02_L01_WORK = M02_L01_ROOT.parent / "Solution_Copy" / "work"
M02_L02_ROOT = VERSION_ROOT / "Module 02" / "Lesson 02"
M02_L02_APP = M02_L02_ROOT / "Student_Copy" / "packet" / "app"
M02_L02_TEMPLATES = M02_L02_ROOT / "Student_Copy" / "packet" / "templates"
M02_L02_WORK = M02_L02_ROOT / "Solution_Copy" / "work"
M02_L03_ROOT = VERSION_ROOT / "Module 02" / "Lesson 03" / "Student_Copy"
M02_L03_APP = M02_L03_ROOT / "packet" / "app"
M02_L03_TEMPLATES = M02_L03_ROOT / "packet" / "templates"
M02_L03_TESTS = M02_L03_ROOT / "packet" / "tests"
M02_L03_WORK = M02_L03_ROOT.parent / "Solution_Copy" / "work"
M02_L04_ROOT = VERSION_ROOT / "Module 02" / "Lesson 04"
M02_L04_APP = M02_L04_ROOT / "Student_Copy" / "packet" / "app"
M02_L04_TEMPLATES = M02_L04_ROOT / "Student_Copy" / "packet" / "templates"
M02_L04_TESTS = M02_L04_ROOT / "Student_Copy" / "packet" / "tests"
M02_L04_DEPLOY = M02_L04_ROOT / "Student_Copy" / "packet" / "deploy"
M02_L04_WORK = M02_L04_ROOT / "Solution_Copy" / "work"
M02_L05_ROOT = VERSION_ROOT / "Module 02" / "Lesson 05" / "Student_Copy"
M02_L05_APP = M02_L05_ROOT / "packet" / "app"
M02_L05_TEMPLATES = M02_L05_ROOT / "packet" / "templates"
M02_L05_TESTS = M02_L05_ROOT / "packet" / "tests"
M02_L05_DEPLOY = M02_L05_ROOT / "packet" / "deploy"
M02_L05_WORK = M02_L05_ROOT.parent / "Solution_Copy" / "work"
M03_L01_ROOT = VERSION_ROOT / "Module 03" / "Lesson 01"
M03_L01_APP = M03_L01_ROOT / "Student_Copy" / "packet" / "app"
M03_L01_TEMPLATES = M03_L01_ROOT / "Student_Copy" / "packet" / "templates"
M03_L01_WORK = M03_L01_ROOT / "Solution_Copy" / "work"
M03_L02_ROOT = VERSION_ROOT / "Module 03" / "Lesson 02" / "Student_Copy"
M03_L02_APP = M03_L02_ROOT / "packet" / "app"
M03_L02_TEMPLATES = M03_L02_ROOT / "packet" / "templates"
M03_L02_WORK = M03_L02_ROOT.parent / "Solution_Copy" / "work"
M03_L03_ROOT = VERSION_ROOT / "Module 03" / "Lesson 03"
M03_L03_APP = M03_L03_ROOT / "Student_Copy" / "packet" / "app"
M03_L03_TEMPLATES = M03_L03_ROOT / "Student_Copy" / "packet" / "templates"
M03_L03_WORK = M03_L03_ROOT / "Solution_Copy" / "work"
M03_L04_ROOT = VERSION_ROOT / "Module 03" / "Lesson 04" / "Student_Copy"
M03_L04_APP = M03_L04_ROOT / "packet" / "app"
M03_L04_TEMPLATES = M03_L04_ROOT / "packet" / "templates"
M03_L04_WORK = M03_L04_ROOT.parent / "Solution_Copy" / "work"
M03_L05_ROOT = VERSION_ROOT / "Module 03" / "Lesson 05"
M03_L05_APP = M03_L05_ROOT / "Student_Copy" / "packet" / "app"
M03_L05_TEMPLATES = M03_L05_ROOT / "Student_Copy" / "packet" / "templates"
M03_L05_WORK = M03_L05_ROOT / "Solution_Copy" / "work"
M04_L01_ROOT = VERSION_ROOT / "Module 04" / "Lesson 01" / "Student_Copy"
M04_L01_APP = M04_L01_ROOT / "packet" / "app"
M04_L01_TEMPLATES = M04_L01_ROOT / "packet" / "templates"
M04_L01_WORK = M04_L01_ROOT.parent / "Solution_Copy" / "work"
M04_L02_ROOT = VERSION_ROOT / "Module 04" / "Lesson 02"
M04_L02_APP = M04_L02_ROOT / "Student_Copy" / "packet" / "app"
M04_L02_WORK = M04_L02_ROOT / "Solution_Copy" / "work"
M04_L03_ROOT = VERSION_ROOT / "Module 04" / "Lesson 03" / "Student_Copy"
M04_L03_APP = M04_L03_ROOT / "packet" / "app"
M04_L03_WORK = M04_L03_ROOT.parent / "Solution_Copy" / "work"
M04_L04_ROOT = VERSION_ROOT / "Module 04" / "Lesson 04"
M04_L04_APP = M04_L04_ROOT / "Student_Copy" / "packet" / "app"
M04_L04_WORK = M04_L04_ROOT / "Solution_Copy" / "work"
M04_L05_ROOT = VERSION_ROOT / "Module 04" / "Lesson 05" / "Student_Copy"
M04_L05_APP = M04_L05_ROOT / "packet" / "app"
M04_L05_WORK = M04_L05_ROOT.parent / "Solution_Copy" / "work"


def pack_dir(profile: str, release: str = "rel-m01-l01") -> Path:
    """Return the pack directory for this profile and release.

    An unknown release stops. Practice writes into the published data tree. Any other profile writes under the build tree. The first release keeps a shorter path. Later releases nest under the release name.
    """
    known = {
        "rel-m01-l01",
        "rel-m01-l02",
        "rel-m01-l03",
        "rel-m01-l04",
        "rel-m01-l05",
        "rel-m02-l01",
        "rel-m02-l02",
        "rel-m02-l03",
        "rel-m02-l04",
        "rel-m02-l05",
        "rel-m03-l01",
        "rel-m03-l02",
        "rel-m03-l03",
        "rel-m03-l04",
        "rel-m03-l05",
        "rel-m04-l01",
        "rel-m04-l02",
        "rel-m04-l03",
        "rel-m04-l04",
        "rel-m04-l05",
    }
    if release not in known:
        raise SystemExit(f"Unknown release {release}.")
    if profile == "practice":
        # Practice is the published drop, with one directory per release.
        return VERSION_ROOT / "data" / release
    if release == "rel-m01-l01":
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

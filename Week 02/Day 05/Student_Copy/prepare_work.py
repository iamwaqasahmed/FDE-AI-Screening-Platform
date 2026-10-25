"""Create the Week 2 Day 5 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the tests, the deploy files, the workflow, and the blank pages
into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter suite back, including the smoke files,
the four shell modules, and the four shell tests, and it replaces
sprint.md, deployment.md, zones.md, operators.md, readout.md,
retro.md, and knowledge.md with the blanks. The workflow file is
copied again from the packet. Run it again only when a failure row
says so. Then repeat the paste steps in chapters 05, 06, 07, 08, 09,
and 10.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter shell. Chapter 01 copies it. Chapters 06 and 07 replace
# queue.py, file_ain.py, notify.py, and contract.py in the work copy.
APP = HERE / "packet" / "app"

# The starter tests. The same chapters replace the four test files.
TESTS = HERE / "packet" / "tests"

# The image and the manifest. They are copied and not replaced.
DEPLOY = HERE / "packet" / "deploy"

# The blank pages. Later chapters fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = (
    "sprint.md",
    "deployment.md",
    "zones.md",
    "operators.md",
    "readout.md",
    "retro.md",
    "knowledge.md",
)

# The workflow. It is copied and not replaced.
PACKET = HERE / "packet"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    image = (DEPLOY / "Dockerfile").is_file() and (DEPLOY / "deployment.yaml").is_file()
    return (
        APP.is_dir()
        and TESTS.is_dir()
        and image
        and (PACKET / ".github" / "workflows" / "ci.yml").is_file()
        and all((TEMPLATES / name).is_file() for name in PAGES)
    )


def _copy_tree() -> None:
    """Copy the shell, the tests, the deploy files, the workflow, and the blanks.

    An existing work/app, work/tests, and work/deploy are removed first
    so a replaced file does not survive a second run. The live-slot
    fixture is not copied. The interview folder is not copied.
    """
    for source, name in ((APP, "app"), (TESTS, "tests"), (DEPLOY, "deploy")):
        destination = WORK / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
    workflow = WORK / ".github" / "workflows"
    workflow.mkdir(parents=True, exist_ok=True)
    shutil.copy(PACKET / ".github" / "workflows" / "ci.yml", workflow / "ci.yml")
    for name in PAGES:
        shutil.copy(TEMPLATES / name, WORK / name)
    (WORK / ".gitignore").write_text(
        "__pycache__/\n*.pyc\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    """Copy the workspace. This file takes no extra word."""
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")
    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py")
    WORK.mkdir(parents=True, exist_ok=True)
    _copy_tree()
    print("Created work/ from the packet.")
    print("Leave the copies in packet/ unchanged.")
    print()
    print("Chapter 05 replaces work/sprint.md.")
    print(
        "Chapter 06 replaces work/app/queue.py, work/app/file_ain.py, "
        "work/app/notify.py, work/tests/test_queue.py, work/tests/test_file.py, "
        "and work/tests/test_notify.py."
    )
    print("Chapter 07 replaces work/app/contract.py and work/tests/test_contract.py.")
    print("Chapter 08 replaces work/zones.md, work/operators.md, and work/deployment.md.")
    print("Chapter 09 replaces work/readout.md and work/retro.md.")
    print("Chapter 10 replaces work/knowledge.md.")
    print()
    print(
        "The smoke files are copied and not replaced: admit.py, health.py, "
        "router.py, secrets.py, their tests, deploy/Dockerfile, "
        "deploy/deployment.yaml, and .github/workflows/ci.yml."
    )
    print()
    print("A second run of this file puts the blanks and the starter suite back.")


if __name__ == "__main__":
    main()

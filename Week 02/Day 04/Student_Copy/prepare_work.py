"""Create the Week 2 Day 4 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the tests, the deploy files, the workflow, and the four blank pages
into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter suite back, including the four app
files, the four tests, and the two deploy files, and it replaces
sprint.md, zones.md, operators.md, and deployment.md with the blanks.
The workflow file is copied again from the packet shell. Run it again
only when you want those files restored. Then repeat the paste steps
in chapters 05, 06, 07, 08, and 09.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter shell. Chapter 01 copies it. Chapters 06, 07, and 08
# replace admit.py, health.py, router.py, and secrets.py in the work copy.
APP = HERE / "packet" / "app"

# The starter tests. The same chapters replace the four test files.
TESTS = HERE / "packet" / "tests"

# The starter image and manifest. Chapters 06 and 07 replace the work copies.
DEPLOY = HERE / "packet" / "deploy"

# The blank pages. Chapters 05 and 09 fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = ("sprint.md", "deployment.md", "zones.md", "operators.md")

# The workflow shell. Chapter 08 replaces the work copy.
PACKET = HERE / "packet"

# The folder the day's check reads.
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
    so a replaced file does not survive a second run. The fixture log
    is not copied. The interview folder is not copied. knowledge.md is
    not copied.
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
    print("Chapter 06 replaces work/app/admit.py, work/tests/test_admit.py, and work/deploy/Dockerfile.")
    print("Chapter 07 replaces work/app/health.py, work/tests/test_health.py, and work/deploy/deployment.yaml.")
    print(
        "Chapter 08 replaces work/app/router.py, work/app/secrets.py, "
        "work/tests/test_router.py, work/tests/test_secrets.py, and work/.github/workflows/ci.yml."
    )
    print("Chapter 09 replaces work/zones.md, work/operators.md, and work/deployment.md.")
    print()
    print("A second run of this file puts the blanks and the starter suite back.")


if __name__ == "__main__":
    main()

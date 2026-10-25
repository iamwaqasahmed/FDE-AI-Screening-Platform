"""Create the Week 2 Day 3 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the tests, the workflow, and the five blank pages into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter suite back, including the three app
files and the four tests, and it replaces sprint.md, dod.md,
crossings.md, usability.md, and fixtures.md with the blanks. The
workflow file is copied again and is not edited. Run it again only
when you want those files restored. Then repeat the paste steps
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
# replace calendar_count.py, schema.py, and receipt.py in the work copy.
APP = HERE / "packet" / "app"

# The starter tests. The same chapters replace the four test files.
TESTS = HERE / "packet" / "tests"

# The blank pages. Chapters 05 and 09 fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = ("sprint.md", "dod.md", "crossings.md", "usability.md", "fixtures.md")

# The workflow. It is copied and not edited.
PACKET = HERE / "packet"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return (
        APP.is_dir()
        and TESTS.is_dir()
        and (PACKET / ".github" / "workflows" / "ci.yml").is_file()
        and all((TEMPLATES / name).is_file() for name in PAGES)
    )


def _copy_tree() -> None:
    """Copy the shell, the tests, the workflow, and the blank pages.

    An existing work/app and work/tests are removed first so a replaced
    file does not survive a second run. The fixture file is not copied.
    The interview folder is not copied. knowledge.md is not copied.
    """
    for source, name in ((APP, "app"), (TESTS, "tests")):
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
    print("Chapter 06 replaces work/app/calendar_count.py and work/tests/test_calendar.py.")
    print("Chapter 07 replaces work/app/schema.py, work/tests/test_schema.py, and work/tests/test_journey.py.")
    print("Chapter 08 replaces work/app/receipt.py and work/tests/test_receipt.py.")
    print("Chapter 09 replaces work/usability.md, work/dod.md, work/crossings.md, and work/fixtures.md.")
    print("Leave .github/workflows/ci.yml as it is.")
    print()
    print("A second run of this file puts the blanks and the starter suite back.")


if __name__ == "__main__":
    main()

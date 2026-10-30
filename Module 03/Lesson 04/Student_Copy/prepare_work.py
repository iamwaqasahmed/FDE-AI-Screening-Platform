"""Create the Module 3, Lesson 4 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the tests, the workflow, and the blank pages into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter app back, including the seven shell
modules, and it replaces sprint.md, benchmark.md, workshop.md,
experiment.md, and knowledge.md with the blanks. The tests are copied
again and are not replaced. The workflow file is copied again from the
packet, with the evaluation gate commented. Run it again only when a
failure row says so. Then repeat the paste steps in chapters 05, 06,
07, 08, 09, and 10.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter shell. Chapter 01 copies it. Later chapters replace
# every module in the work copy. The packet copy stays the trap.
APP = HERE / "packet" / "app"

# The shared tests. They are copied and not replaced. The same file
# fails beside the shell and passes beside the filled app.
TESTS = HERE / "packet" / "tests"

# The blank pages. Later chapters fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = (
    "sprint.md",
    "benchmark.md",
    "workshop.md",
    "experiment.md",
    "knowledge.md",
)

# The workflow. Chapter 01 copies the commented gate. Chapter 07 replaces the work copy.
PACKET = HERE / "packet"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it.

    The steps check the app folder, the tests folder, the workflow
    file, and each blank page.
    """
    return (
        APP.is_dir()
        and TESTS.is_dir()
        and (PACKET / ".github" / "workflows" / "ci.yml").is_file()
        and all((TEMPLATES / name).is_file() for name in PAGES)
    )


def _copy_tree() -> None:
    """Copy the shell, the tests, the workflow, and the blanks.

    An existing work/app and work/tests are removed first so a
    replaced file does not survive a second run. The release drawer
    is not copied. The interview folder is not copied.
    """
    # Replace work/app and work/tests with the copies from the packet.
    for source, name in ((APP, "app"), (TESTS, "tests")):
        destination = WORK / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
    # Copy the workflow with the evaluation gate still commented.
    workflow = WORK / ".github" / "workflows"
    workflow.mkdir(parents=True, exist_ok=True)
    shutil.copy(PACKET / ".github" / "workflows" / "ci.yml", workflow / "ci.yml")
    # Copy each blank page into the workspace.
    for name in PAGES:
        shutil.copy(TEMPLATES / name, WORK / name)
    # Keep Python cache files out of the workspace.
    (WORK / ".gitignore").write_text(
        "__pycache__/\n*.pyc\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    """Copy the workspace. This file takes no extra word."""
    # Stop when the packet drawer is not beside this file.
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")
    # Stop when the command carries an extra word.
    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py")
    # Create the workspace and fill it from the packet.
    WORK.mkdir(parents=True, exist_ok=True)
    _copy_tree()
    # Name the file each later chapter replaces.
    print("Created work/ from the packet.")
    print("Leave the copies in packet/ unchanged.")
    print()
    print("Chapter 05 replaces work/sprint.md.")
    print("Chapter 06 replaces work/app/score.py, work/app/forecast.py, and work/app/failures.py.")
    print("Chapter 07 replaces work/app/judge.py, work/app/gate.py, and work/.github/workflows/ci.yml.")
    print("Chapter 08 replaces work/app/intervals.py and work/app/experiment.py.")
    print("Chapter 09 replaces work/benchmark.md, work/workshop.md, and work/experiment.md.")
    print("Chapter 10 replaces work/knowledge.md.")
    print()
    print("The tests are copied and not replaced.")
    print("The workflow is copied with the evaluation gate commented. Chapter 07 replaces that work copy.")
    print()
    print("A second run of this file puts the blanks, the starter app, and the commented gate back.")


if __name__ == "__main__":
    main()

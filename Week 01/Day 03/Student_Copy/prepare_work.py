"""Create the Day 3 workspace, or copy the blank intake note into it.

Chapter 01 runs this file with no extra word. That copies the three
workflow scripts into work/workflow.

Chapter 07 runs this file with the extra word "note". That copies the
blank intake note into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter scripts. Chapter 01 copies them. Chapter 06 replaces two of
# the copies under work/. Leave the packet copies unchanged.
WORKFLOW = HERE / "packet" / "workflow"

# The blank intake note. Chapter 07 fills the copy, not this original.
INTAKE = HERE / "packet" / "templates" / "intake.md"

# The folder the day's check reads.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return WORKFLOW.is_dir() and INTAKE.is_file()


def _copy_note() -> None:
    """Copy the blank intake note.

    Check that the work folder already exists, copy the blank note into it, and print the path of the copy.
    This replaces a note you already filled.
    """
    if not WORK.is_dir():
        raise SystemExit("Run python prepare_work.py first, with no extra word.")
    shutil.copy(INTAKE, WORK / "intake.md")
    print("Copied the blank intake note to work/intake.md.")
    print("If you had already filled that file, this replaced it.")
    print("Open the copy. Chapter 07 says what to write under each heading.")


def main() -> None:
    """Copy the scripts, or, if asked, copy only the blank intake note."""
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")

    # "python prepare_work.py note" is the chapter 07 command.
    # It must not refresh the scripts. By then you may have replaced
    # worker.py and calendar_count.py.
    if len(sys.argv) > 1 and sys.argv[1] == "note":
        _copy_note()
        return

    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py    or    python prepare_work.py note")

    # dirs_exist_ok lets you run chapter 01 again. The three scripts are
    # refreshed from the packet, including worker.py and calendar_count.py.
    # Run it again only when you want the starter scripts back.
    shutil.copytree(WORKFLOW, WORK / "workflow", dirs_exist_ok=True)
    print("Created work/workflow from the packet.")
    print("Leave the copies in packet/workflow unchanged.")
    print()
    print("Chapter 06 replaces work/workflow/worker.py and")
    print("work/workflow/calendar_count.py. Leave tools.py as it is.")


if __name__ == "__main__":
    main()

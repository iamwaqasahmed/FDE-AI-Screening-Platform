"""Create this lesson's workspace, or copy the blank memos into it.

Chapter 01 runs this file with no extra word. That copies the four
baseline scripts into work/baselines.

Chapter 07 runs this file with the extra word "memo". That copies the
blank approach memo and the blank brief into work/.

Run the file from Module 01/Lesson 02/Student_Copy, the folder it lives in.
A later chapter starts from the course folder and calls this file by
its path, so you do not need to change directory first.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works if the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The four scripts. Chapter 01 copies them. You read them. You do not edit them.
BASELINES = HERE / "packet" / "baselines"

# Blank memos. Chapter 07 fills the copies, not these originals.
APPROACH = HERE / "packet" / "templates" / "approach.md"
BRIEF = HERE / "packet" / "templates" / "brief.md"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return BASELINES.is_dir() and APPROACH.is_file() and BRIEF.is_file()


def _copy_memos() -> None:
    """Copy the two blank templates.

    Check that the work folder already exists, copy both templates into it, and print where the copies went.
    This replaces any memo you already filled.
    """
    if not WORK.is_dir():
        raise SystemExit("Run python prepare_work.py first, with no extra word.")
    shutil.copy(APPROACH, WORK / "approach.md")
    shutil.copy(BRIEF, WORK / "brief.md")
    print("Copied the blank memos to work/approach.md and work/brief.md.")
    print("If you had already filled those files, this replaced them.")
    print("Open the two copies. Chapter 07 says what to write in each cell.")


def main() -> None:
    """Copy the scripts, or, if asked, copy only the blank memos."""
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")

    # "python prepare_work.py memo" is the chapter 07 command.
    # It must not recreate the baselines, because by then you are about
    # to write in the memos and the scripts are already in place.
    if len(sys.argv) > 1 and sys.argv[1] == "memo":
        _copy_memos()
        return

    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py    or    python prepare_work.py memo")

    # dirs_exist_ok lets you run chapter 01 again. The four scripts are
    # refreshed. A memo you already wrote is not inside baselines, so it stays.
    destination = WORK / "baselines"
    shutil.copytree(BASELINES, destination, dirs_exist_ok=True)

    print("Created work/baselines from the packet.")
    print("Leave the copies in packet/baselines unchanged.")
    print()
    print("Chapter 06 lists the five commands. Each one starts in a terminal")
    print("opened in the course folder, and uses the scripts now under work/baselines.")


if __name__ == "__main__":
    main()

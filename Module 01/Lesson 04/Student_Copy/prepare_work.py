"""Create the Lesson 4 workspace, or copy the blank agent note into it.

Chapter 01 runs this file with no extra word. That copies the five
agent scripts into work/agent.

Chapter 07 runs this file with the extra word "note". That copies the
blank agent note into work/.

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

# The starter scripts. Chapter 01 copies them. Chapter 06 replaces three
# of the copies under work/agent. Leave the packet copies unchanged.
AGENT = HERE / "packet" / "agent"

# The blank agent note. Chapter 07 fills the copy, not this original.
NOTE = HERE / "packet" / "templates" / "agent-note.md"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return AGENT.is_dir() and NOTE.is_file()


def _copy_note() -> None:
    """Copy the blank agent note.

    Check that the work folder already exists, copy the blank note into it, and print the path of the copy.
    This replaces a note you already filled.
    """
    if not WORK.is_dir():
        raise SystemExit("Run python prepare_work.py first, with no extra word.")
    shutil.copy(NOTE, WORK / "agent-note.md")
    print("Copied the blank agent note to work/agent-note.md.")
    print("If you had already filled that file, this replaced it.")
    print("Open the copy. Chapter 07 says what to write under each heading.")


def main() -> None:
    """Copy the scripts, or, if asked, copy only the blank agent note."""
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")

    # "python prepare_work.py note" is the chapter 07 command.
    # It must not refresh the scripts. By then you may have replaced
    # model.py, schema.py, and memory.py.
    if len(sys.argv) > 1 and sys.argv[1] == "note":
        _copy_note()
        return

    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py    or    python prepare_work.py note")

    # dirs_exist_ok lets you run chapter 01 again. The five scripts are
    # refreshed from the packet, including model.py, schema.py, and memory.py.
    # Run it again only when you want the starter scripts back.
    shutil.copytree(AGENT, WORK / "agent", dirs_exist_ok=True)
    print("Created work/agent from the packet.")
    print("Leave the copies in packet/agent unchanged.")
    print()
    print("Chapter 06 replaces work/agent/model.py, work/agent/schema.py, and")
    print("work/agent/memory.py. Leave tools.py and run.py as they are.")


if __name__ == "__main__":
    main()

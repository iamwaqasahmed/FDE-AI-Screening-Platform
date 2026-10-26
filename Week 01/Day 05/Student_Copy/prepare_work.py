"""Create the Day 5 workspace, or copy the blank pages into it.

Chapter 01 runs this file with no extra word. That copies the five
agent scripts into work/agent.

Chapter 07 runs this file with the extra word "pages". That copies the
blank architecture, design, readout, and trace note into work/.

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

# The blank pages. Chapter 07 fills the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = ("architecture.md", "design.md", "readout.md", "trace-note.md")

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return AGENT.is_dir() and all((TEMPLATES / name).is_file() for name in PAGES)


def _copy_pages() -> None:
    """Copy the four blank pages.

    Check that the work folder already exists, copy each blank page into it, and print where the copies went.
    This replaces a page you already filled.
    """
    # The work folder must already exist before these pages can be copied into it.
    if not WORK.is_dir():
        raise SystemExit("Run python prepare_work.py first, with no extra word.")
    for name in PAGES:
        shutil.copy(TEMPLATES / name, WORK / name)
    print("Copied the blank pages to work/.")
    print("If you had already filled those files, this replaced them.")
    print("Open the copies. Chapter 07 and chapter 08 say what to write.")


def main() -> None:
    """Copy the scripts, or, if asked, copy only the blank pages."""
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")

    # "python prepare_work.py pages" is the chapter 07 command.
    # It must not refresh the scripts. By then you may have replaced
    # model.py, schema.py, and memory.py.
    if len(sys.argv) > 1 and sys.argv[1] == "pages":
        _copy_pages()
        return

    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py    or    python prepare_work.py pages")

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

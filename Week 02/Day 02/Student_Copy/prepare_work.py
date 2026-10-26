"""Create the Week 2 Day 2 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the laptop stand-in, the dev namespace, and the five blank pages
into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter shell back, including intake.py,
cancel.py, and mart.py, and it replaces sprint.md, states.md,
zones.md, sms.md, and mart.md with the blanks. Run it again only
when you want those files restored. Then repeat the paste steps
in chapters 05, 06, 07, and 08.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter shell. Chapter 01 copies it. Chapters 06 and 08 replace
# only intake.py, cancel.py, and mart.py in the work copy.
APP = HERE / "packet" / "app"

# The blank pages. Chapters 05, 07, and 08 fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = ("sprint.md", "states.md", "zones.md", "sms.md", "mart.md")

# The laptop stand-in and the dev namespace. They are copied with the shell.
PACKET = HERE / "packet"

# The folder the day's check reads.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it."""
    return (
        APP.is_dir()
        and (PACKET / "compose.yaml").is_file()
        and (PACKET / "Dockerfile").is_file()
        and (PACKET / "deploy" / "namespace.yaml").is_file()
        and all((TEMPLATES / name).is_file() for name in PAGES)
    )


def _copy_tree() -> None:
    """Copy the shell, the stand-in, the namespace, and the blank pages.

    An existing work/app is removed first so a replaced intake.py,
    cancel.py, or mart.py does not survive a second run. The webhook
    file is not copied. The interview folder is not copied.
    """
    # Remove a previous app so an old intake.py, cancel.py, or mart.py cannot survive.
    destination = WORK / "app"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(
        APP,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    # Copy the laptop stand-in and the dev namespace next to the app.
    shutil.copy(PACKET / "compose.yaml", WORK / "compose.yaml")
    shutil.copy(PACKET / "Dockerfile", WORK / "Dockerfile")
    deploy = WORK / "deploy"
    deploy.mkdir(parents=True, exist_ok=True)
    shutil.copy(PACKET / "deploy" / "namespace.yaml", deploy / "namespace.yaml")
    # Copy the blank pages, and ignore the session database and the trace.
    for name in PAGES:
        shutil.copy(TEMPLATES / name, WORK / name)
    (WORK / ".gitignore").write_text(
        "sessions.db\ntrace.json\n__pycache__/\n*.pyc\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    """Copy the workspace. This file takes no extra word."""
    # The packet must still be beside this file, and the command takes no extra word.
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")
    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py")
    # Copy, then print which chapter replaces intake, cancel, the pages, and mart.
    WORK.mkdir(parents=True, exist_ok=True)
    _copy_tree()
    print("Created work/ from the packet.")
    print("Leave the copies in packet/ unchanged.")
    print()
    print("Chapter 05 replaces work/sprint.md.")
    print("Chapter 06 replaces work/app/intake.py and work/app/cancel.py.")
    print("Chapter 07 replaces work/states.md, work/zones.md, and work/sms.md.")
    print("Chapter 08 replaces work/app/mart.py and work/mart.md.")
    print("Leave the other files under work/app as they are.")
    print()
    print("A second run of this file puts the blanks and the starter worker back.")


if __name__ == "__main__":
    main()

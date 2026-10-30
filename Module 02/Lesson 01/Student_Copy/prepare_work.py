"""Create the Module 2 Lesson 1 workspace.

Chapter 01 runs this file with no extra word. That copies the shell,
the laptop stand-in, the dev namespace, and the three blank pages
into work/.

Run the file from a terminal opened in the course folder. The path
below is enough. You do not need to change directory first.

A second run puts the starter shell back, including client.py, and
it replaces sprint.md, states.md, and token-flow.md with the blanks.
Run it again only when you want those files restored. Then repeat
the generate command in chapter 07.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works when the terminal starts in the course folder.
HERE = Path(__file__).resolve().parent

# The starter shell. Chapter 01 copies it. Chapter 07 replaces only
# work/app/client.py. Leave the packet copy unchanged.
APP = HERE / "packet" / "app"

# The blank pages. Chapters 05 and 06 fill the copies, not these originals.
TEMPLATES = HERE / "packet" / "templates"
PAGES = ("sprint.md", "states.md", "token-flow.md")

# The laptop stand-in and the dev namespace. They are copied with the shell.
PACKET = HERE / "packet"

# The folder the day's checks read.
WORK = HERE / "work"


def _packet_ready() -> bool:
    """True when the drawer this script copies is still beside it.

    It checks the app folder, the compose file, the Dockerfile, the
    namespace file, and every blank page.
    """
    return (
        APP.is_dir()
        and (PACKET / "compose.yaml").is_file()
        and (PACKET / "Dockerfile").is_file()
        and (PACKET / "deploy" / "namespace.yaml").is_file()
        and all((TEMPLATES / name).is_file() for name in PAGES)
    )


def _copy_tree() -> None:
    """Copy the shell, the stand-in, the namespace, and the blank pages.

    An existing work/app is removed first so a generated client.py does
    not survive a second run. The scenario file is not copied. The
    interview folder is not copied.
    """
    # Remove a previous app so a generated client.py cannot survive a second run.
    destination = WORK / "app"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(
        APP,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    # Copy the laptop stand-in and the dev namespace with the shell.
    shutil.copy(PACKET / "compose.yaml", WORK / "compose.yaml")
    shutil.copy(PACKET / "Dockerfile", WORK / "Dockerfile")
    deploy = WORK / "deploy"
    deploy.mkdir(parents=True, exist_ok=True)
    shutil.copy(PACKET / "deploy" / "namespace.yaml", deploy / "namespace.yaml")
    # Copy the three blank pages. This day does not write a gitignore.
    for name in PAGES:
        shutil.copy(TEMPLATES / name, WORK / name)


def main() -> None:
    """Copy the workspace. This file takes no extra word."""
    # Stop if the packet drawer is missing or an extra word was passed.
    if not _packet_ready():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")
    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py")
    # Copy, then say that chapter 07 replaces client.py by running generate.py.
    WORK.mkdir(parents=True, exist_ok=True)
    _copy_tree()
    print("Created work/ from the packet.")
    print("Leave the copies in packet/ unchanged.")
    print()
    print("Chapter 05 replaces work/sprint.md.")
    print("Chapter 06 replaces work/states.md and work/token-flow.md.")
    print("Chapter 07 replaces work/app/client.py by running generate.py.")
    print("Leave the other files under work/app as they are.")
    print()
    print("A second run of this file puts the blanks and the starter client back.")


if __name__ == "__main__":
    main()

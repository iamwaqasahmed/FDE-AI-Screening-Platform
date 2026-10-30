"""Create this lesson's workspace, or copy the blank access form into it.

Chapter 01 runs this file with no extra word. That copies the pipeline
template into work/ and places the dev credentials beside it.

Chapter 06 runs this file with the extra word "form". That copies the
blank access request into work/ so you can fill it in.

Run the file from Module 01/Lesson 01/Student_Copy, the folder it lives in.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# This file's folder is the student copy. Paths below are built from
# here so the script still works if you start the terminal somewhere else,
# as long as you invoke this file by its path.
HERE = Path(__file__).resolve().parent

# The untouched pipeline. Chapter 01 copies it. You edit the copy in work/.
STARTER = HERE / "packet" / "starter"

# Watermarked dev credential. It is copied into work/credentials/ and then
# left closed. The scan reads it. You do not type the value anywhere.
CREDENTIALS = HERE / "packet" / "kickoff" / "credentials" / "dev.json"

# Blank access request. Chapter 06 fills the copy, not this original.
FORM = HERE / "packet" / "kickoff" / "forms" / "access-request.md"

# The folder the day's checks read.
WORK = HERE / "work"


def main() -> None:
    """Copy the starter, or, if asked, copy only the blank form."""
    # A moved script cannot see the packet. Stop with a plain sentence
    # instead of a stack trace about a missing file.
    if not STARTER.is_dir() or not CREDENTIALS.is_file() or not FORM.is_file():
        raise SystemExit("This file must stay next to the packet folder. Do not move it.")

    # "python prepare_work.py form" is the chapter 06 command.
    # It must not recreate work/, because by then work/ already holds
    # the pipeline and the credentials.
    if len(sys.argv) > 1 and sys.argv[1] == "form":
        if not WORK.is_dir():
            raise SystemExit("Run python prepare_work.py first, with no extra word.")
        shutil.copy(FORM, WORK / "access-request.md")
        print("Copied the blank form to work/access-request.md")
        print("Open that file and fill the four lines. Chapter 06 says what each line should say.")
        return

    # Any other extra word is a typo. Say the two legal commands.
    if len(sys.argv) > 1:
        raise SystemExit("Use: python prepare_work.py    or    python prepare_work.py form")

    # dirs_exist_ok lets you run chapter 01 again without deleting notes
    # you already added under work/. Files from the starter are refreshed.
    # Your access request and interview files are not inside the starter,
    # so this copy leaves them in place.
    shutil.copytree(STARTER, WORK, dirs_exist_ok=True)

    # credentials/ is not part of the starter. Create it, then copy the
    # one credential file. The scan skips this folder on purpose.
    (WORK / "credentials").mkdir(parents=True, exist_ok=True)
    (WORK / "interviews").mkdir(exist_ok=True)
    shutil.copy(CREDENTIALS, WORK / "credentials" / "dev.json")

    print("Created work/ from the starter.")
    print("The dev credentials are in work/credentials/. Leave that file closed.")
    print()
    print("Next, in this same folder, run:")
    print("  cd work")
    print("  python -m unittest discover -s tests -q")
    print("  python scan.py")
    print()
    print("You should see OK, then the line: scan passed.")


# Running the file as a program calls main. Importing it does not.
if __name__ == "__main__":
    main()

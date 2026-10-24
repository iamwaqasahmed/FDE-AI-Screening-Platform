"""One-feature baseline. Count letters whose specialty is on the word list.

The letter file is split on headings that start with "## letter-".
Each piece after a heading is one letter body.

WORDS is the specialty list. A letter counts when its body contains any
of those words, in any letter case. A letter that names the clinic with
some other wording stays uncounted. That is why the printed count can
be lower than the number of letters in the file.

Read the letter file where it already sits. Do not copy it into this
script, into a prompt, or into the work folder. The file carries a
watermark. One letter adds a line that is that watermark. Leave the
line in the file.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Specialty names this count looks for. A body matches if any one appears.
WORDS = ("eye", "ophthalmology", "endocrinology", "diabetes", "cardiology", "heart")


def load_text(path: str | Path) -> str:
    """Read the whole letter file as one string."""
    return Path(path).read_text(encoding="utf-8")


def bodies(text: str) -> list[str]:
    """Split on the letter headings and drop the title that sits above the first one."""
    return re.split(r"(?m)^## letter-", text)[1:]


def filled(text: str) -> int:
    """How many letter bodies contain a word from WORDS."""
    count = 0
    for body in bodies(text):
        lowered = body.lower()
        if any(word in lowered for word in WORDS):
            count += 1
    return count


def main(argv: list[str] | None = None) -> None:
    """Print one line that starts with filled."""
    parser = argparse.ArgumentParser(description="Count letters the specialty list fills.")
    parser.add_argument("markdown")
    args = parser.parse_args(argv)
    print(f"filled {filled(load_text(args.markdown))}")


if __name__ == "__main__":
    main(sys.argv[1:])

"""One-feature baseline. Count letters whose specialty is on the word list.

The markdown is split on letter headings. The text before the first heading is not a letter. A letter counts as filled when its body contains any word from the specialty list, compared in lower case.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WORDS = ("eye", "ophthalmology", "endocrinology", "diabetes", "cardiology", "heart")


def load_text(path: str | Path) -> str:
    """Return the markdown file as one string."""
    return Path(path).read_text(encoding="utf-8")


def bodies(text: str) -> list[str]:
    """Return the text of each letter section, dropping the preamble before the first heading."""
    return re.split(r"(?m)^## letter-", text)[1:]


def filled(text: str) -> int:
    """Return how many letter bodies contain a specialty word from the list."""
    count = 0
    for body in bodies(text):
        lowered = body.lower()
        if any(word in lowered for word in WORDS):
            # One matching word is enough. The body is not scanned for a second hit.
            count += 1
    return count


def main(argv: list[str] | None = None) -> None:
    """Print how many letters in the markdown path the specialty list fills.

    Read that path, count the filled letters, and print the count.
    """
    parser = argparse.ArgumentParser(description="Count letters the specialty list fills.")
    parser.add_argument("markdown")
    args = parser.parse_args(argv)
    print(f"filled {filled(load_text(args.markdown))}")


if __name__ == "__main__":
    main(sys.argv[1:])

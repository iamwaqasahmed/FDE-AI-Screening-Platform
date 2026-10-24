"""One-feature baseline. Count letters whose specialty is on the word list."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WORDS = ("eye", "ophthalmology", "endocrinology", "diabetes", "cardiology", "heart")


def load_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def bodies(text: str) -> list[str]:
    return re.split(r"(?m)^## letter-", text)[1:]


def filled(text: str) -> int:
    count = 0
    for body in bodies(text):
        lowered = body.lower()
        if any(word in lowered for word in WORDS):
            count += 1
    return count


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Count letters the specialty list fills.")
    parser.add_argument("markdown")
    args = parser.parse_args(argv)
    print(f"filled {filled(load_text(args.markdown))}")


if __name__ == "__main__":
    main(sys.argv[1:])

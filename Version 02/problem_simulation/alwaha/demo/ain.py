"""Show the Ain change-request card. The nightly-file sentence stays off the page."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d5 import CARD, QUESTIONS


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Read the Ain change-request card.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    print(CARD)
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"{index}. {question}")


if __name__ == "__main__":
    main(sys.argv[1:])

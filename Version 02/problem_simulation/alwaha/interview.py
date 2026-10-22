"""Interview one persona. Prints questions and answers. Prints no score and no fact id."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Interview an Al-Waha persona.")
    parser.add_argument("--persona", required=True)
    parser.add_argument("--script", required=True, help="Text file, one question per line.")
    args = parser.parse_args(argv)
    personas = load_personas()
    if args.persona not in personas:
        known = ", ".join(sorted(personas))
        raise SystemExit(f"Unknown persona {args.persona}. Known personas: {known}.")
    questions = Path(args.script).read_text(encoding="utf-8").splitlines()
    for number, turn in enumerate(run(personas[args.persona], questions), start=1):
        print(f"Q{number}: {turn['question']}")
        print(f"A: {turn['answer']}")
        print()


if __name__ == "__main__":
    main(sys.argv[1:])

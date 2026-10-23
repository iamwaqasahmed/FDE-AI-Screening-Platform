"""Run wf-self-service on the scenario pack."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import model
import tools
from memory import Memory


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run wf-self-service on the scenario pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    tools.load(args.pack)
    memory = Memory()
    rows = [model.respond(scenario, memory) for scenario in tools.scenarios()]
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])

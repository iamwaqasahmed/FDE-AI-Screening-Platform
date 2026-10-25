"""Run wf-self-service on the scenario pack.

Chapter 01 copies this file into work/agent. Chapter 06 does not replace it.
The check runs this file again, so do not hand-edit the trace it writes.

The command takes two arguments:

- --pack is the folder that holds policy/ and scenarios/.
- --out is the trace file to write.

This file loads the pack, builds one memory, and asks model.respond
for every scenario. The order is the order in scenarios/order.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import model
import tools
from memory import Memory


def main(argv: list[str] | None = None) -> None:
    """Load the pack, run every scenario, and write the trace.

    A missing --pack or --out is an error from the argument parser.
    The parent folder of --out is created when it does not exist yet.
    """
    parser = argparse.ArgumentParser(description="Run wf-self-service on the scenario pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    tools.load(args.pack)
    memory = Memory()
    # One memory object is shared across the scenarios. The starter's
    # memory keeps nothing, so the share does not change its rows.
    rows = [model.respond(scenario, memory) for scenario in tools.scenarios()]
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])

"""Puts each module's code folder on the import path."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIRS = (
    "Module 02 - Tools the agent can trust",
    "Module 03 - Retrieval",
    "Module 04 - The agent",
    "Module 05 - Evaluation",
    "Module 06 - Run it in their environment",
    "Module 07 - The handoff",
    "Module 08 - Capstone",
)


def install() -> None:
    for name in reversed(MODULE_DIRS):
        entry = str(ROOT / name)
        if entry not in sys.path:
            sys.path.insert(0, entry)

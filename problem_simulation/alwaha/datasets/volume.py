"""Partitioned SMS and audit streams. The default world leaves this off.

Each stream is a directory of JSONL parts. A new part starts every time the index lands on a partition boundary, and the previous part is closed first. The final part is closed even when the loop exits early. A zero row count still creates the directories and writes no lines.
"""

from __future__ import annotations

import json
from pathlib import Path

PARTITION = 100_000


def write_streams(root: Path, rows: int) -> None:
    """Write the sms and audit streams under root, each with the given row count."""
    folder = root / "volume"
    folder.mkdir(parents=True, exist_ok=True)
    _stream(folder / "sms", "sms", rows)
    _stream(folder / "audit", "audit", rows)


def _stream(folder: Path, kind: str, rows: int) -> None:
    """Write one partitioned JSONL stream. Each line records its index and the stream kind."""
    folder.mkdir(parents=True, exist_ok=True)
    handle = None
    try:
        for index in range(rows):
            if index % PARTITION == 0:
                if handle is not None:
                    # Close the part that just filled before opening the next one.
                    handle.close()
                part = folder / f"{kind}-{index // PARTITION:05d}.jsonl"
                handle = part.open("w", encoding="utf-8")
            handle.write(json.dumps({"i": index, "kind": kind}, sort_keys=True) + "\n")
    finally:
        if handle is not None:
            # A zero-length stream never opens a file, so there is nothing to close.
            handle.close()

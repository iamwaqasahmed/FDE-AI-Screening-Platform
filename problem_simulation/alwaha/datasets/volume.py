"""Partitioned SMS and audit streams. The default world leaves this off."""

from __future__ import annotations

import json
from pathlib import Path

PARTITION = 100_000


def write_streams(root: Path, rows: int) -> None:
    folder = root / "volume"
    folder.mkdir(parents=True, exist_ok=True)
    _stream(folder / "sms", "sms", rows)
    _stream(folder / "audit", "audit", rows)


def _stream(folder: Path, kind: str, rows: int) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    handle = None
    try:
        for index in range(rows):
            if index % PARTITION == 0:
                if handle is not None:
                    handle.close()
                part = folder / f"{kind}-{index // PARTITION:05d}.jsonl"
                handle = part.open("w", encoding="utf-8")
            handle.write(json.dumps({"i": index, "kind": kind}, sort_keys=True) + "\n")
    finally:
        if handle is not None:
            handle.close()

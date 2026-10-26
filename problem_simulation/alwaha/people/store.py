"""JSONL helpers. Rows are sorted so a second build matches.

Both writers create the parent directory. Object keys are sorted so the bytes do not depend on insertion order. A JSONL file of no rows is empty; a file with rows ends in a newline.
"""

from __future__ import annotations

import json
from pathlib import Path


def write_json(path: Path, payload: dict) -> None:
    """Write one JSON object with sorted keys and a trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    """Write one JSON object per line, with sorted keys.

    An empty list writes an empty file. A non-empty list is terminated so every row, including the last, is a full line.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(row, sort_keys=True) for row in rows]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

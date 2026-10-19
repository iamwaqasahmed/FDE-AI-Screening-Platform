"""Read participant-visible handover files, cached by modification time. Nothing outside handover/ is reachable."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
from threading import Lock

_CACHE: dict[tuple[str, float], list[dict]] = {}
_LOCK = Lock()


class DataMissing(Exception):
    def __init__(self, relative: str):
        super().__init__(relative)
        self.relative = f"handover/{relative}"


def handover_file(handover: Path, relative: str) -> Path:
    base = handover.resolve()
    path = (base / relative).resolve()
    if base not in path.parents:
        raise DataMissing(relative)
    if not path.is_file():
        raise DataMissing(relative)
    return path


def _parse_csv(text: str) -> list[dict]:
    return [dict(row) for row in csv.DictReader(io.StringIO(text))]


def _parse_pipe(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split("|")
    header[0] = "segment"
    return [dict(zip(header, line.split("|"))) for line in lines[1:]]


def _parse_jsonl(text: str) -> list[dict]:
    return [json.loads(line) for line in text.splitlines() if line.strip()]


PARSERS = {".csv": _parse_csv, ".pipe": _parse_pipe, ".jsonl": _parse_jsonl}


def read_rows(handover: Path, relative: str) -> list[dict]:
    path = handover_file(handover, relative)
    key = (str(path), path.stat().st_mtime)
    with _LOCK:
        if key not in _CACHE:
            text = path.read_text(encoding="utf-8")
            _CACHE[key] = PARSERS[path.suffix](text)
        return _CACHE[key]


def matching(rows: list[dict], **filters: str | None) -> list[dict]:
    wanted = {key: value for key, value in filters.items() if value}
    return [row for row in rows if all(str(row.get(key, "")) == value for key, value in wanted.items())]

"""Write one in-memory file map. The suffix decides the format."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def write_file(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    if isinstance(content, pd.DataFrame):
        _frame(path, suffix, content)
    elif isinstance(content, bytes):
        path.write_bytes(content)
    elif isinstance(content, str):
        path.write_text(content, encoding="utf-8")
    elif isinstance(content, list):
        path.write_text("".join(json.dumps(row, ensure_ascii=True, default=str) + "\n" for row in content), encoding="utf-8")
    elif isinstance(content, dict):
        path.write_text(json.dumps(content, indent=2, ensure_ascii=True, default=str) + "\n", encoding="utf-8")
    else:
        raise TypeError(f"Cannot write {type(content).__name__} to {path}")


def _frame(path: Path, suffix: str, frame: pd.DataFrame) -> None:
    if suffix == ".csv":
        frame.to_csv(path, index=False)
    elif suffix == ".parquet":
        frame.to_parquet(path, index=False)
    elif suffix == ".xlsx":
        frame.to_excel(path, index=False)
    elif suffix == ".jsonl":
        frame.to_json(path, orient="records", lines=True, force_ascii=True)
    else:
        raise ValueError(f"No frame writer for {path}")


def write_all(root: Path, files: dict) -> int:
    for relative, content in sorted(files.items()):
        write_file(root / relative, content)
    return len(files)

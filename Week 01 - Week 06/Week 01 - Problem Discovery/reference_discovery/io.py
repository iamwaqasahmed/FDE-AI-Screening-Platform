"""Readers for the participant-visible drop. Nothing here opens truth/ or eval/."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

CANONICAL_DISTRICTS = ("North City", "East City", "Hill Counties", "River Districts")


class Drop:
    def __init__(self, root: Path) -> None:
        self.root = root

    def path(self, *parts: str) -> Path:
        return self.root.joinpath(*parts)

    def text(self, *parts: str) -> str:
        return self.path(*parts).read_text(encoding="utf-8")

    def frame(self, *parts: str, **options) -> pd.DataFrame:
        return pd.read_csv(self.path(*parts), dtype=str, **options).fillna("")


def field(text: str, label: str) -> str:
    prefix = label.lower() + ":"
    for line in text.splitlines():
        if line.lower().startswith(prefix):
            return line.split(":", 1)[1].strip()
    return ""


def transcripts(drop: Drop) -> str:
    folder = drop.path("corpus", "transcripts")
    return "\n".join(path.read_text(encoding="utf-8") for path in sorted(folder.glob("*.md")))


def notice(drop: Drop, ref: str) -> str:
    return drop.text("corpus", "notices", f"notice-{ref.lower()}.md")

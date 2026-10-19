"""Character spans of personal data in the patient letters."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

PATTERNS = (
    ("national_id", re.compile(r"NID\d+")),
    ("screening_no", re.compile(r"LP\d+")),
    ("dob", re.compile(r"Date of birth: (\d{4}-\d{2}-\d{2})")),
    ("postcode", re.compile(r"Postcode area: (\S+)")),
)
NAME = re.compile(r"# .+\n\n(.+)\nDate of birth:")


def frame(data: Path) -> pd.DataFrame:
    rows = []
    for path in sorted((data / "corpus/patient-letters").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        relative = f"patient-letters/{path.name}"
        rows.extend(_spans(text, relative))
    return pd.DataFrame(rows, columns=["path", "start", "end", "kind"])


def _spans(text: str, path: str) -> list[dict]:
    found = []
    for kind, pattern in PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.span(1) if match.lastindex else match.span()
            found.append({"path": path, "start": start, "end": end, "kind": kind})
    named = NAME.search(text)
    if named:
        for match in re.finditer(re.escape(named.group(1)), text):
            found.append({"path": path, "start": match.start(), "end": match.end(), "kind": "name"})
    return found

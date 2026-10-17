"""Cover note and a data dictionary that is wrong in a few places."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_readme_and_dictionary(handover_dir: Path) -> None:
    (handover_dir / "README.txt").write_text(_README, encoding="utf-8")
    pd.DataFrame(_DICTIONARY, columns=["field", "description"]).to_excel(
        handover_dir / "data_dictionary.xlsx",
        index=False,
    )


_README = """Hartland Regional Health Authority
Diabetes registry and eye screening extract
Snapshot: 1 October 2026

Join every file on REGISTRY_NO. That number is the unique patient key.
The vendor model is 93% sensitive and is ready for all three screening programs.
Ignore FLAG. RECORD_STATUS Active means the row is in the current extract.
"""


_DICTIONARY = [
    ("REGISTRY_NO", "Unique patient key. Use this to join all files."),
    ("LOCAL_PID", "Obsolete clinic code. Safe to ignore."),
    ("DISTRICT", "Name of the screening clinic that took the photo."),
    ("FLAG", "Blank means the record is incomplete and should be excluded from coverage."),
    ("RECORD_STATUS", "Active means the person is eligible for screening."),
    ("RESULT", "Grader code. Blank means the screen was normal."),
    ("REFERRAL", "yes means the case is urgent."),
    ("MODEL_LABEL", "Vendor grade. Empty means no disease."),
    ("FILE_PATH", "Image bytes are stored beside this extract."),
]

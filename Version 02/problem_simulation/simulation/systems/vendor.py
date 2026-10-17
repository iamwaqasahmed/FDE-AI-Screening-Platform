"""Vendor pilot score file. The score is a separate fact, never the signed grade."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_vendor(events: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    pilot = events[events["pilot"]]
    scored = pilot["vendor_score"].notna()
    frame = pd.DataFrame(
        {
            "FILE_NAME": pilot["file_name"],
            "GRADER_LABEL": pilot["grade"],
            "MODEL_LABEL": pilot["vendor_label"].where(scored, ""),
            "MODEL_SCORE": pilot["vendor_score"].round(3).astype(object).where(scored, ""),
            "SITE": pilot["site"],
        }
    )
    frame.to_csv(folder / "scores.csv", index=False)

"""Primary-care shared folder: a listing with decoys and a few sidecars."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.systems.common import write_jsonl
from simulation.world.quotas import DECOYS


def write_shared(events: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    real = events[events["capture"] == "shared_folder"]
    listing = pd.DataFrame(
        {
            "FILE_NAME": real["file_name"],
            "FOLDER": "EYE SCREEN 2024 final final",
            "PHOTO_DATE": real["photo_date"],
            "KIND": "capture",
        }
    )
    decoys = pd.DataFrame(
        {
            "FILE_NAME": [f"DECOY_{index:04d}.jpg" for index in range(DECOYS)],
            "FOLDER": "EYE SCREEN 2024 final final",
            "PHOTO_DATE": "",
            "KIND": "decoy",
        }
    )
    pd.concat([listing, decoys], ignore_index=True).to_csv(folder / "listing.csv", index=False)
    sidecars = []
    for index, row in enumerate(real.itertuples(index=False)):
        if index % 7 == 0:
            sidecars.append(
                {
                    "file_name": row.file_name,
                    "camera": getattr(row, "device_id", "desktop"),
                    "operator_initials": getattr(row, "operator", ""),
                    "dilated": bool(getattr(row, "dilated", False)),
                }
            )
    write_jsonl(folder / "sidecars.jsonl", sidecars)

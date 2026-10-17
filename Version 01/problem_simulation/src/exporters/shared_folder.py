"""Rural and primary-care shared-folder listing, plus unmatched decoys."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_shared_folder(tables: dict[str, pd.DataFrame], cfg: dict, handover_dir: Path) -> None:
    images = tables["image"]
    shared = images[images["camera_class"].isin(["primary", "outreach"])].copy()
    visits = tables["visit"][["visit_id", "photo_date"]]
    frame = shared.merge(visits, on="visit_id")
    folder = "EYE SCREEN 2024 final final"
    listing = pd.DataFrame(
        {
            "FILE_NAME": frame["file_name"],
            "FOLDER": folder,
            "MODIFIED_DATE": [format_mixed(_as_date(value), index) for index, value in enumerate(frame["photo_date"])],
            "FILE_PATH": frame["file_path"],
        }
    )
    decoys = []
    for offset in range(cfg["shared_folder_decoys"]):
        name = f"IMG_9{offset + 1:05d}.JPG"
        decoys.append(
            {
                "FILE_NAME": name,
                "FOLDER": folder,
                "MODIFIED_DATE": "2024-11-02",
                "FILE_PATH": f"shared/{folder}/{name}",
            }
        )
    export = pd.concat([listing, pd.DataFrame(decoys)], ignore_index=True)
    export.to_csv(handover_dir / "shared_folder_listing.csv", index=False)


def _as_date(value):
    if isinstance(value, pd.Timestamp):
        return value.date()
    return value

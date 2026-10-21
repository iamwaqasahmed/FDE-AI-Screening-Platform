"""Hospital image manifest."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_pacs_manifest(tables: dict[str, pd.DataFrame], handover_dir: Path) -> None:
    images = tables["image"]
    hospital = images[images["camera_class"] == "hospital"].copy()
    people = tables["person"][["person_uid", "hospital_mrn"]]
    visits = tables["visit"][["visit_id", "photo_date", "site_name"]]
    frame = hospital.merge(people, on="person_uid").merge(visits, on="visit_id")
    export = pd.DataFrame(
        {
            "STUDY_UID": frame["image_id"],
            "ACCESSION": frame["visit_id"],
            "HOSPITAL_MRN": frame["hospital_mrn"],
            "STUDY_DATE": [format_mixed(_as_date(value), index) for index, value in enumerate(frame["photo_date"])],
            "MODALITY": "OP",
            "STATION_NAME": frame["site_name"],
            "FILE_PATH": frame["file_path"],
        }
    )
    export.to_csv(handover_dir / "pacs_manifest.csv", index=False)


def _as_date(value):
    if isinstance(value, pd.Timestamp):
        return value.date()
    if hasattr(value, "date") and not hasattr(value, "year"):
        return value.date()
    return value

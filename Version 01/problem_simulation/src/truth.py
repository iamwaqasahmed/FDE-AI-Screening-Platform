"""Write instructor truth tables."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_truth(tables: dict[str, pd.DataFrame], truth_dir: Path) -> None:
    truth_dir.mkdir(parents=True, exist_ok=True)
    person = tables["person"]
    crosswalk = person[
        [
            "person_uid",
            "registry_number",
            "local_pid",
            "hospital_mrn",
            "forename",
            "surname",
            "dob",
            "district",
            "home_site",
        ]
    ].copy()
    frames = {
        "person": person,
        "crosswalk": crosswalk,
        "visit": tables["visit"],
        "image": tables["image"],
        "grade": tables["grade"],
        "letter": tables["letter"],
        "referral": tables["referral"],
        "vendor_score": tables["vendor_score"],
        "hospital_eval": tables["hospital_eval"],
    }
    for name, frame in frames.items():
        if "person_uid" not in frame.columns:
            raise ValueError(f"{name} is missing person_uid.")
        frame.to_csv(truth_dir / f"{name}.csv", index=False)

"""Hospital image index: one CSV of study metadata per hospital, keyed by MRN."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.systems.mrn import MrnIndex
from simulation.world.sites import slug


def write_pacs(events: pd.DataFrame, people: pd.DataFrame, identifiers: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    names = people.set_index("person_uid")
    studies = events[events["capture"] == "pacs"].copy()
    index = MrnIndex(identifiers)
    studies["MRN"] = [
        index.get(row.person_uid, row.site, row.photo_date, prefer_split=row.scenario == "split" and int(row.event_id[1:]) % 2 == 0)
        for row in studies.itertuples(index=False)
    ]
    studies["PATIENT_NAME"] = studies["person_uid"].map(names["surname"] + ", " + names["forename"])
    studies["DOB"] = studies["person_uid"].map(names["dob"])
    for site, group in studies.groupby("site"):
        rows = pd.DataFrame(
            {
                "ACCESSION": group["file_name"].str.replace(".dcm", "", regex=False).to_numpy(),
                "MRN": group["MRN"].to_numpy(),
                "HOSPITAL": site,
                "STUDY_DATE": group["photo_date"].to_numpy(),
                "PATIENT_NAME": group["PATIENT_NAME"].to_numpy(),
                "DOB": group["DOB"].to_numpy(),
                "MODALITY": "OP",
                "DEVICE_SERIAL": group["device_id"].to_numpy() if "device_id" in group else "",
                "FILE_NAME": group["file_name"].to_numpy(),
            }
        )
        rows.to_csv(folder / f"{slug(str(site))}.csv", index=False)

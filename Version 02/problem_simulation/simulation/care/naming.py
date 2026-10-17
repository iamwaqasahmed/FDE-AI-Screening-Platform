"""File names as each capture system writes them, and urgent codes left only in note text."""

from __future__ import annotations

from datetime import date

import pandas as pd

HIDDEN_LIMIT = 30


def stamp_names(events: pd.DataFrame) -> None:
    names = []
    hidden = []
    for index, row in enumerate(events.itertuples(index=False), start=1):
        names.append(file_name(row.capture, row.photo_date, row.surname, row.forename, index))
        hidden.append(row.grade == "R3" and index % 47 == 0)
    events["file_name"] = names
    events["grade_hidden"] = hidden
    if int(events["grade_hidden"].sum()) > HIDDEN_LIMIT:
        drop = events.index[events["grade_hidden"]].to_numpy()[HIDDEN_LIMIT:]
        events.loc[drop, "grade_hidden"] = False


def file_name(capture: str, photo_date: str, surname: str, forename: str, sequence: int) -> str:
    photo = date.fromisoformat(photo_date)
    if capture == "pacs":
        return f"ACC{sequence:08d}.dcm"
    if capture == "outreach_laptop":
        return f"OUT_{sequence:08d}.jpg"
    if capture == "vendor_cloud":
        return f"VEN_{sequence:08d}.jpg"
    return f"{surname}_{forename[:1]}_{photo:%d-%m-%y}_L.jpg"

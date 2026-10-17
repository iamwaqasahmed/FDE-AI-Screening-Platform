"""Letter dispatch, with tail drops and orphan rows."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_letters(rows, tables: dict, cfg: dict, handover_dir: Path) -> None:
    letters = tables["letter"][["person_uid", "sent_at", "template_id"]]
    completed = rows[rows["cohort"] == "completed"].merge(letters, on="person_uid")
    photo = pd.to_datetime(completed["photo_date"])
    sent = pd.to_datetime(completed["sent_at"])
    completed = completed.assign(delay=(sent - photo).dt.days)
    completed = completed.sort_values(["delay", "local_pid"]).reset_index(drop=True)
    drop = cfg["letter_tail_drop_each_side"]
    kept = completed.iloc[drop : len(completed) - drop]
    export = pd.DataFrame(
        {
            "LOCAL_PID": kept["local_pid"],
            "PATIENT_NAME": kept["surname"] + ", " + kept["forename"],
            "DOB": [_as_mixed(value, index) for index, value in enumerate(kept["dob"])],
            "CLINIC": kept["site_name"],
            "SENT_DATE": [_as_mixed(value, index) for index, value in enumerate(kept["sent_at"])],
            "TEMPLATE_ID": kept["template_id"],
        }
    )
    orphans = _orphans(cfg)
    pd.concat([export, orphans], ignore_index=True).to_csv(handover_dir / "letter_dispatch.csv", index=False)


def _orphans(cfg: dict) -> pd.DataFrame:
    rows = []
    start = date(2025, 1, 8)
    for offset in range(cfg["letter_orphans"]):
        sent = start + timedelta(days=offset)
        rows.append(
            {
                "LOCAL_PID": f"ORPH{offset + 1:04d}",
                "PATIENT_NAME": f"UNKNOWN, LETTER{offset + 1}",
                "DOB": "1980-01-15",
                "CLINIC": "Records office",
                "SENT_DATE": format_mixed(sent, offset),
                "TEMPLATE_ID": "letter-recall",
            }
        )
    return pd.DataFrame(rows)


def _as_mixed(value, slot: int):
    if isinstance(value, pd.Timestamp):
        value = value.date()
    elif hasattr(value, "date") and not isinstance(value, date):
        value = value.date()
    return format_mixed(value, slot)

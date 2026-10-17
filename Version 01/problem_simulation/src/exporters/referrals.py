"""Specialist queue. Mild and urgent share one list, and mild dates are blank."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_referrals(rows, tables: dict, handover_dir: Path) -> None:
    referrals = tables["referral"]
    frame = rows.merge(referrals, on="person_uid")
    booked = []
    seen = []
    for index, row in enumerate(frame.itertuples(index=False)):
        if row.grade_graded == "R3":
            booked.append(format_mixed(_as_date(row.booked_at), index))
            seen.append(format_mixed(_as_date(row.seen_at), index + 1))
        else:
            booked.append("")
            seen.append("")
    export = pd.DataFrame(
        {
            "LOCAL_PID": frame["local_pid"],
            "PATIENT_NAME": frame["surname"] + ", " + frame["forename"],
            "CLINIC": frame["site_name"],
            "REFERRED_DATE": [format_mixed(_as_date(value), index) for index, value in enumerate(frame["referred_at"])],
            "BOOKED_DATE": booked,
            "SEEN_DATE": seen,
        }
    )
    export.to_csv(handover_dir / "ophthalmology_referrals.csv", index=False)


def _as_date(value):
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    return value

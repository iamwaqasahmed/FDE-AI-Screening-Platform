"""Named graders. Skill, strictness, fatigue, and drift are hidden; the workbook shows only initials."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date

import pandas as pd

from simulation.world.clock import AGENCY_START, ROTA_CHANGE, SNAPSHOT


@dataclass(frozen=True)
class Grader:
    grader_id: str
    name: str
    initials: str
    start: date
    end: date | None
    weekly_hours: float
    bias: float
    sigma: float
    drift_per_year: float
    fatigue: float
    agency: bool = False
    lead: bool = False
    worse_after_rota: bool = False


ROSTER = (
    Grader("G01", "Priya Anand", "PA", date(2015, 4, 1), None, 30, 0.0, 0.22, 0.0, 0.05, lead=True),
    Grader("G02", "Tomas Brennan", "TB", date(2016, 9, 1), None, 37.5, 0.45, 0.30, 0.0, 0.10),
    Grader("G03", "Chloe Mensah", "CM", date(2017, 1, 9), date(2021, 2, 26), 37.5, 0.0, 0.32, 0.0, 0.12),
    Grader("G04", "Daniel Roche", "DR", date(2016, 3, 1), date(2021, 7, 30), 37.5, -0.05, 0.34, 0.02, 0.12),
    Grader("G05", "Elif Sahin", "ES", date(2018, 2, 5), None, 37.5, 0.0, 0.30, 0.0, 0.10, worse_after_rota=True),
    Grader("G06", "Hannah Lowe", "HL", date(2014, 6, 2), None, 22.5, 0.42, 0.28, 0.0, 0.08),
    Grader("G07", "Kofi Asante", "KA", date(2019, 5, 7), date(2024, 5, 31), 37.5, 0.0, 0.33, 0.03, 0.15),
    Grader("G08", "Lena Fischer", "LF", date(2017, 11, 6), None, 30, -0.10, 0.36, 0.04, 0.12),
    Grader("G09", "Marcus Bell", "MB", date(2022, 6, 6), None, 37.5, 0.0, 0.40, -0.04, 0.14),
    Grader("G10", "Nadia Qureshi", "NQ", date(2022, 9, 5), None, 37.5, 0.05, 0.38, -0.03, 0.12),
    Grader("G11", "Agency grader A", "AG", AGENCY_START, None, 30, 0.0, 0.50, 0.0, 0.18, agency=True),
    Grader("G12", "Agency grader B", "AX", AGENCY_START, None, 30, -0.15, 0.55, 0.0, 0.20, agency=True),
)
LEAD = next(grader for grader in ROSTER if grader.lead)


def active_on(grader: Grader, day: date) -> bool:
    return grader.start <= day and (grader.end is None or day <= grader.end)


def sigma_on(grader: Grader, day: date, session_position: float) -> float:
    years = max((day - max(grader.start, date(2018, 10, 1))).days / 365.25, 0)
    sigma = grader.sigma + grader.drift_per_year * years + grader.fatigue * session_position
    if grader.worse_after_rota and day >= ROTA_CHANGE:
        sigma += 0.30
    return max(sigma, 0.12)


def roster_frame() -> pd.DataFrame:
    rows = []
    for grader in ROSTER:
        row = asdict(grader)
        row["end"] = row["end"].isoformat() if row["end"] else ""
        row["start"] = row["start"].isoformat()
        rows.append(row)
    return pd.DataFrame(rows)


def staff_list() -> pd.DataFrame:
    """What HR would hand over: names, start and end, contracted hours. No skill numbers."""
    frame = roster_frame()[["grader_id", "name", "initials", "start", "end", "weekly_hours", "agency"]]
    frame["status_at_snapshot"] = ["left" if end and end < SNAPSHOT.isoformat() else "in post" for end in frame["end"]]
    return frame

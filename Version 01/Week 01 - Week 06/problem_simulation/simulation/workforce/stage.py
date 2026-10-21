"""Workforce and device files: what HR and the clinic spreadsheet hand over, and what truth keeps."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.devices.inventory import firmware_history_frame, inventory_frame
from simulation.disease.hba1c import to_frame
from simulation.workforce.graders import roster_frame, staff_list
from simulation.workforce.sessions import build_ophthalmology_slots, build_sessions


def build(world: dict, rng: np.random.Generator) -> None:
    files = world["files"]
    hours = world["grader_hours"]
    weekly = _weekly_hours(hours)
    files["handover/workforce/staff.csv"] = staff_list()
    files["handover/workforce/rota_hours_by_week.csv"] = weekly
    files["handover/devices/camera_inventory.xlsx"] = inventory_frame(lagged=True)
    files["truth/workforce/graders.parquet"] = roster_frame()
    files["truth/workforce/daily_hours.parquet"] = hours
    files["truth/workforce/reads_per_hour.csv"] = pd.DataFrame([{"reads_per_hour": hours.attrs.get("reads_per_hour", 0.0)}])
    files["truth/devices/camera_inventory.parquet"] = inventory_frame(lagged=False)
    files["truth/devices/firmware_history.parquet"] = firmware_history_frame()
    base = world["people"][world["people"]["alias_of"] == ""].reset_index(drop=True)
    files["truth/disease/state.parquet"] = world["hidden"]["disease"]
    files["truth/disease/hba1c.parquet"] = to_frame(base, world["hidden"]["hba1c"])
    files["truth/behaviour/invitations.parquet"] = world["invitations"]
    sessions = build_sessions(world["events"], rng)
    files["truth/workforce/sessions.parquet"] = sessions
    files["truth/workforce/ophthalmology_slots.parquet"] = build_ophthalmology_slots(world["events"])
    world["tables"]["weekly_hours"] = weekly
    world["tables"]["sessions"] = sessions


def _weekly_hours(hours: pd.DataFrame) -> pd.DataFrame:
    graders = [column for column in hours.columns if column != "day"]
    frame = hours.copy()
    frame["week"] = pd.to_datetime(frame["day"]).dt.to_period("W-SUN").dt.start_time.dt.strftime("%Y-%m-%d")
    weekly = frame.groupby("week")[graders].sum().round(1).reset_index()
    return weekly[weekly["week"] < "2026-10-01"]

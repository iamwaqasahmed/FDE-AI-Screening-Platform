"""Sprint velocity for the two earlier teams, summed from the tracker so the two files agree."""

from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.delivery.teams import TEAMS, sprints
from simulation.world.engagement import KICKOFF

RECENT_SPRINTS = 6


def velocity_frame(tickets: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    work = tickets[tickets["type"] != "epic"]
    rows = []
    for team in TEAMS:
        mine = work[work["team"] == team.name]
        for sprint_id, start, end in sprints(team):
            done = mine[(mine["status"] == "Done") & (mine["resolved"] >= start.isoformat()) & (mine["resolved"] <= end.isoformat())]
            planned = mine[mine["sprint"] == sprint_id]
            completed = int(done["story_points"].sum())
            committed = max(completed, int(planned["story_points"].sum())) + int(rng.integers(0, 6))
            rows.append({"team": team.name, "sprint": sprint_id, "start": start.isoformat(), "end": end.isoformat(),
                         "committed_points": committed, "completed_points": completed})
    return pd.DataFrame(rows)


def recent_velocity(velocity: pd.DataFrame, team: str = "Heron") -> float:
    rows = velocity[velocity["team"] == team].tail(RECENT_SPRINTS)
    return round(float(rows["completed_points"].mean()), 1)


def build_done(remaining_points: int, velocity: float) -> tuple[int, date]:
    needed = math.ceil(remaining_points / velocity) if velocity > 0 else 99
    return needed, KICKOFF + timedelta(days=14 * needed - 1)

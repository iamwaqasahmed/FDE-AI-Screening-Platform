"""Open pilot tickets, with duplicates pointed at the original ticket, and Heron's pace."""

from __future__ import annotations

import pandas as pd

from simulation.delivery.velocity import build_done, recent_velocity
from simulation.eval.agent.paths import earliest


def facts(world: dict) -> tuple[dict, pd.DataFrame]:
    frame = _open(world)
    items = {"backlog_triage": _triage(frame), "pace": _pace(world, frame)}
    return items, _public(frame)


def _open(world: dict) -> pd.DataFrame:
    tickets = world["files"]["handover/delivery/tracker.csv"]
    truth = world["files"]["truth/delivery/tracker_truth.csv"]
    merged = tickets.merge(truth, on="ticket_id")
    open_rows = merged[merged["pilot"].astype(bool) & merged["open"].astype(bool)].copy()
    open_rows["blocked_by"] = open_rows["blocked_by"].fillna("").astype(str)
    open_rows["duplicate_of"] = open_rows["duplicate_of"].fillna("").astype(str)
    return open_rows.sort_values("ticket_id").reset_index(drop=True)


def _triage(frame: pd.DataFrame) -> dict:
    originals = frame["duplicate_of"].eq("")
    return {
        "duplicates": int((~originals).sum()),
        "missing_criteria": int(frame["missing_criteria"].sum()),
        "blocked": int(frame["blocked_by"].ne("").sum()),
        "open_pilot_points": int(frame.loc[originals, "story_points"].sum()),
        "open_pilot_points_with_duplicates": int(frame["story_points"].sum()),
    }


def _pace(world: dict, frame: pd.DataFrame) -> dict:
    velocity = world["files"]["handover/delivery/velocity.csv"]
    pace = recent_velocity(velocity)
    points = int(frame.loc[frame["duplicate_of"].eq(""), "story_points"].sum())
    sprints, done = build_done(points, pace)
    path = earliest(done)
    return {
        "team": "Heron",
        "sprints_counted": 6,
        "velocity": pace,
        "sprints_needed": sprints,
        "build_done": done.isoformat(),
        "binding": path["binding"] == "build",
    }


def _public(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame[["ticket_id", "duplicate_of"]].copy()
    out["missing_criteria"] = frame["missing_criteria"].map(lambda flag: "true" if bool(flag) else "false")
    out["blocked_by"] = frame["blocked_by"].astype(str)
    return out.reset_index(drop=True)

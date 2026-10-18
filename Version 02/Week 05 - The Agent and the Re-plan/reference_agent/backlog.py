"""Open pilot tickets. A reworded copy is a duplicate of the earlier ticket."""

from __future__ import annotations

import math
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from reference_agent.load import read_csv
from simulation.delivery.epics import REWORD
from simulation.world.engagement import KICKOFF

CLOSED = {"Done", "Won't do"}
PILOT = ("Registry schema v3 interface", "Vendor pilot phase two")
SYSTEM = {"registry-interface": "registry", "letters-template": "letters"}


def facts(data: Path) -> tuple[dict, date, pd.DataFrame]:
    tickets = read_csv(data, "handover/delivery/tracker.csv")
    calendar = read_csv(data, "handover/delivery/freeze_calendar.csv")
    frame = _open(tickets, calendar)
    points = int(frame.loc[frame["duplicate_of"].eq(""), "story_points"].astype(int).sum())
    velocity = _velocity(read_csv(data, "handover/delivery/velocity.csv"))
    sprints = math.ceil(points / velocity) if velocity else 99
    done = KICKOFF + timedelta(days=14 * sprints - 1)
    triage = {
        "duplicates": int(frame["duplicate_of"].ne("").sum()),
        "missing_criteria": int(frame["missing_criteria"].eq("true").sum()),
        "blocked": int(frame["blocked_by"].ne("").sum()),
        "open_pilot_points": points,
        "open_pilot_points_with_duplicates": int(frame["story_points"].astype(int).sum()),
    }
    return triage, done, frame


def pace(velocity_frame: pd.DataFrame, done, path: dict, triage: dict) -> dict:
    return {
        "team": "Heron", "sprints_counted": 6, "velocity": _velocity(velocity_frame),
        "sprints_needed": _sprints(triage["open_pilot_points"], _velocity(velocity_frame)),
        "build_done": done.isoformat(), "binding": path["binding"] == "build",
    }


def _open(tickets: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    epics = tickets[(tickets["type"] == "epic") & tickets["summary"].isin(PILOT)]
    children = tickets[tickets["epic_id"].isin(set(epics["ticket_id"])) & ~tickets["status"].isin(CLOSED)].copy()
    links = _links(tickets)
    children["duplicate_of"] = children["ticket_id"].map(links).fillna("")
    children["missing_criteria"] = ["true" if row.type == "story" and row.acceptance_criteria == "" else "false"
                                    for row in children.itertuples(index=False)]
    children["blocked_by"] = [_blocked(row, calendar) for row in children.itertuples(index=False)]
    return children.sort_values("ticket_id").reset_index(drop=True)


def _links(tickets: pd.DataFrame) -> dict[str, str]:
    grouped: dict[str, list] = {}
    for row in tickets[tickets["type"] != "epic"].itertuples(index=False):
        grouped.setdefault(row.epic_id, []).append(row)
    found = {}
    for group in grouped.values():
        for row in group:
            earlier = [other for other in group if other.ticket_id != row.ticket_id and _reword(other.summary) == row.summary and other.created <= row.created]
            earlier.sort(key=lambda other: other.created)
            found[row.ticket_id] = earlier[-1].ticket_id if earlier else ""
    return found


def _reword(summary: str) -> str:
    verb, _, rest = summary.partition(" ")
    rest = rest.replace(" for ", " - ").replace(" in ", " - ").replace(" with ", " + ")
    return f"{REWORD.get(verb, verb)} {rest}"


def _blocked(row, calendar: pd.DataFrame) -> str:
    system = SYSTEM.get(row.component, "")
    if not system or row.status in CLOSED or not row.target_release:
        return ""
    hits = calendar[(calendar["system"] == system) & (calendar["kind"] == "freeze")
                    & (calendar["start"] <= row.target_release) & (calendar["end"] >= row.target_release)]
    return str(hits.iloc[0]["ref"]) if len(hits) else ""


def _velocity(frame: pd.DataFrame) -> float:
    rows = frame[frame["team"] == "Heron"].tail(6)
    return round(float(rows["completed_points"].astype(float).mean()), 1)


def _sprints(points: int, velocity: float) -> int:
    return math.ceil(points / velocity) if velocity else 99

"""Tracker traps: reworded duplicates, stories with no acceptance criteria, and work blocked by a freeze."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.delivery.epics import BY_ID, FREEZE_SYSTEM, REWORD
from simulation.delivery.plan import frozen
from simulation.delivery.teams import BY_NAME, sprint_of

DUPLICATES = 14
OPEN_DUPLICATES = 4
MISSING_CRITERIA = 25
CLOSED = ("Done", "Won't do")


def plant_duplicates(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    candidates = frame[frame["type"].isin(["story", "bug"])]
    is_open = ~candidates["status"].isin(CLOSED) & candidates["epic_id"].map(lambda epic: BY_ID[epic].pilot)
    open_pool, closed_pool = candidates.index[is_open].to_numpy(), candidates.index[~is_open].to_numpy()
    open_picks = rng.choice(open_pool, size=min(OPEN_DUPLICATES, len(open_pool)), replace=False)
    closed_picks = rng.choice(closed_pool, size=DUPLICATES - len(open_picks), replace=False)
    picks = sorted(int(index) for index in [*open_picks, *closed_picks])
    copies = [_copy(frame.loc[index], index, rng) for index in picks]
    return pd.concat([frame, pd.DataFrame(copies)], ignore_index=True)


def _copy(row: pd.Series, index: int, rng: np.random.Generator) -> dict:
    team = BY_NAME[row["team"]]
    created = min(date.fromisoformat(row["created"]) + timedelta(days=int(rng.integers(5, 41))), team.end)
    others = [member for member in team.members if member != row["assignee"]]
    copy = row.to_dict()
    copy.update(
        summary=_reword(row["summary"]), created=created.isoformat(), sprint=sprint_of(team, created),
        assignee=str(rng.choice(others)), duplicate_of=str(index), acceptance_criteria="" if rng.random() < 0.5 else row["acceptance_criteria"],
    )
    if row["status"] in CLOSED:
        resolved = min(created + timedelta(days=int(rng.integers(1, 10))), team.end)
        copy.update(status="Done", resolved=resolved.isoformat())
    else:
        copy.update(status="To do", resolved="")
    return copy


def _reword(summary: str) -> str:
    verb, _, rest = summary.partition(" ")
    rest = rest.replace(" for ", " - ").replace(" in ", " - ").replace(" with ", " + ")
    return f"{REWORD.get(verb, verb)} {rest}"


def plant_missing_criteria(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    pool = frame[(frame["type"] == "story") & (frame["acceptance_criteria"] != "") & (frame["duplicate_of"] == "")].index.to_numpy()
    picks = rng.choice(pool, size=MISSING_CRITERIA, replace=False)
    frame = frame.copy()
    frame.loc[picks, "acceptance_criteria"] = ""
    return frame


def blocked_by(row: pd.Series) -> str:
    system = FREEZE_SYSTEM.get(row["component"], "")
    if not system or row["status"] in CLOSED or not row["target_release"]:
        return ""
    return frozen(system, date.fromisoformat(row["target_release"]))


def truth(frame: pd.DataFrame) -> pd.DataFrame:
    children = frame[frame["type"] != "epic"]
    return pd.DataFrame({
        "ticket_id": children["ticket_id"],
        "duplicate_of": children["duplicate_of"],
        "missing_criteria": (children["type"] == "story") & (children["acceptance_criteria"] == ""),
        "blocked_by": [blocked_by(row) for _, row in children.iterrows()],
        "pilot": [BY_ID[epic].pilot for epic in children["epic_id"]],
        "open": ~children["status"].isin(CLOSED),
    }).reset_index(drop=True)


def remaining_pilot_points(frame: pd.DataFrame) -> int:
    open_pilot = frame[(frame["type"] != "epic") & ~frame["status"].isin(CLOSED) & (frame["duplicate_of"] == "")]
    open_pilot = open_pilot[[BY_ID[epic].pilot for epic in open_pilot["epic_id"]]]
    return int(open_pilot["story_points"].sum())


def backlog_gold(frame: pd.DataFrame, facts: pd.DataFrame) -> dict:
    dupes = facts[facts["duplicate_of"] != ""].sort_values("ticket_id")
    return {
        "tickets": int(len(frame)),
        "duplicates": [{"ticket_id": a, "duplicate_of": b} for a, b in zip(dupes["ticket_id"], dupes["duplicate_of"])],
        "missing_criteria": sorted(facts.loc[facts["missing_criteria"], "ticket_id"]),
        "blocked": [{"ticket_id": t, "freeze": f} for t, f in sorted(zip(facts["ticket_id"], facts["blocked_by"])) if f],
        "open_pilot_points": remaining_pilot_points(frame),
        "open_pilot_points_with_duplicates": int(frame[(frame["type"] != "epic") & ~frame["status"].isin(CLOSED)
                                                      & frame["epic_id"].map(lambda e: BY_ID[e].pilot if e else False)]["story_points"].sum()),
    }

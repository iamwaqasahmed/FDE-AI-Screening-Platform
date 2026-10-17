"""The tracker export from the two earlier teams: epics, stories, bugs, spikes, and tasks."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.delivery.epics import ASPECTS, EPICS, RELEASE_TARGETS, VERBS, Epic
from simulation.delivery.teams import BY_NAME, sprint_of

TYPES = ("story", "bug", "spike", "task")
TYPE_WEIGHTS = (0.6, 0.25, 0.1, 0.05)
POINTS = {"story": (1, 2, 3, 5, 8, 13), "spike": (1, 2, 3, 5), "bug": (1, 2, 3), "task": (1, 2)}
OPEN_STATUSES = ("To do", "In progress", "In review")
PRIORITIES = ("P1", "P2", "P3", "P4")
COLUMNS = ("ticket_id", "type", "epic_id", "summary", "status", "priority", "story_points", "assignee", "reporter",
           "team", "sprint", "created", "resolved", "acceptance_criteria", "links", "component", "target_release")


def base_tickets(rng: np.random.Generator) -> pd.DataFrame:
    rows = []
    for epic in EPICS:
        rows.append(_epic_row(epic))
        used: set[str] = set()
        for _ in range(epic.count):
            rows.append(_child(epic, rng, used))
    return pd.DataFrame(rows, columns=[*COLUMNS, "duplicate_of"])


def _epic_row(epic: Epic) -> dict:
    team = BY_NAME[epic.team]
    return {
        "ticket_id": epic.epic_id, "type": "epic", "epic_id": "", "summary": epic.title,
        "status": "In progress" if epic.open else "Done", "priority": "P2", "story_points": 0,
        "assignee": team.reporter, "reporter": team.reporter, "team": epic.team, "sprint": "",
        "created": epic.start.isoformat(), "resolved": "" if epic.open else epic.end.isoformat(),
        "acceptance_criteria": "", "links": " ".join(epic.refs), "component": epic.component,
        "target_release": "", "duplicate_of": "",
    }


def _child(epic: Epic, rng: np.random.Generator, used: set[str]) -> dict:
    team = BY_NAME[epic.team]
    span = (epic.end - epic.start).days
    created = epic.start + timedelta(days=int(rng.integers(0, max(span - 10, 1))))
    kind = str(rng.choice(TYPES, p=TYPE_WEIGHTS))
    status, resolved = _status(epic, created, span, rng, team.end)
    obj = str(rng.choice(epic.objects))
    return {
        "ticket_id": "", "type": kind, "epic_id": epic.epic_id, "summary": _summary(kind, obj, rng, used),
        "status": status, "priority": str(rng.choice(PRIORITIES, p=(0.1, 0.35, 0.4, 0.15))),
        "story_points": int(rng.choice(POINTS[kind])), "assignee": str(rng.choice(team.members)),
        "reporter": team.reporter, "team": epic.team, "sprint": sprint_of(team, created),
        "created": created.isoformat(), "resolved": resolved,
        "acceptance_criteria": _criteria(obj) if kind == "story" else "",
        "links": _link(epic, kind, rng), "component": epic.component,
        "target_release": _target(epic, status, rng), "duplicate_of": "",
    }


def _status(epic: Epic, created: date, span: int, rng: np.random.Generator, team_end: date) -> tuple[str, str]:
    done = not epic.open or ((epic.end - created).days > 35 and rng.random() < 0.75)
    if not done:
        return str(rng.choice(OPEN_STATUSES)), ""
    resolved = min(created + timedelta(days=int(rng.integers(2, 21))), team_end)
    return ("Won't do" if rng.random() < 0.05 else "Done"), resolved.isoformat()


def _summary(kind: str, obj: str, rng: np.random.Generator, used: set[str]) -> str:
    for _ in range(20):
        verb = "Investigate" if kind == "spike" else str(rng.choice(VERBS))
        text = f"{verb} {obj} {rng.choice(ASPECTS)}"
        if text not in used:
            used.add(text)
            return text
    text = f"{verb} {obj} follow-up {len(used)}"
    used.add(text)
    return text


def _criteria(obj: str) -> str:
    return f"Given the {obj} is deployed, when the nightly job runs, then the output matches the reference file."


def _link(epic: Epic, kind: str, rng: np.random.Generator) -> str:
    chance = 0.6 if kind == "bug" else 0.1
    if not epic.refs or rng.random() >= chance:
        return ""
    return str(rng.choice(epic.refs))


def _target(epic: Epic, status: str, rng: np.random.Generator) -> str:
    if status in ("Done", "Won't do") or epic.component not in RELEASE_TARGETS:
        return ""
    return str(rng.choice(RELEASE_TARGETS[epic.component]))


def number(frame: pd.DataFrame) -> pd.DataFrame:
    """Give children ids in created order and point duplicate_of at the new ids."""
    frame = frame.reset_index(drop=True)
    children = frame[frame["type"] != "epic"].sort_values(["created", "epic_id", "summary"], kind="stable")
    ids = {index: f"DLV-{1101 + order:04d}" for order, index in enumerate(children.index)}
    frame["ticket_id"] = [ids.get(index, value) for index, value in zip(frame.index, frame["ticket_id"])]
    frame["duplicate_of"] = [ids[int(value)] if value != "" else "" for value in frame["duplicate_of"]]
    epics = frame[frame["type"] == "epic"]
    ordered = pd.concat([epics, frame.loc[children.index]], ignore_index=True)
    return ordered


def public(frame: pd.DataFrame) -> pd.DataFrame:
    return frame[list(COLUMNS)].reset_index(drop=True)

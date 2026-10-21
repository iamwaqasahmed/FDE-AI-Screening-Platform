"""Service desk export: every timeline incident, change, and freeze, plus routine requests. The text is the only record of the cause."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.estate.common import TRUTH, stamp
from simulation.estate.desk_noise import noise_tickets
from simulation.prose.compose import seeded
from simulation.systems.catalog import SYSTEMS
from simulation.world.clock import SNAPSHOT
from simulation.world.staff import name
from simulation.world.timeline import TIMELINE, Happening

COLUMNS = ["ticket_ref", "type", "service", "opened_at", "resolved_at", "status", "priority", "site", "summary", "description", "assignee"]
ALIASES = {"devices": "camera-inventory"}
BY_ID = {system["system_id"]: system for system in SYSTEMS}
INCIDENT_TEXT = (
    "{effect}. Root cause: {cause}. Window {start} to {end}.",
    "Reported: {effect}. Investigation found {cause}. Affected from {start} to {end}.",
    "{cause}. Impact: {effect}. Open from {start}, closed {end}.",
)
CHANGE_TEXT = (
    "Change: {title}. Reason: {cause}. Expected impact: {effect}. Go-live {start}.",
    "Implementing {title} on {start}. Driver: {cause}. Note: {effect}.",
)
FREEZE_TEXT = ("{title} from {start} to {end}. {reason}. {effect}.",)


def build_service_desk(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    tickets = pd.DataFrame([_ticket(item) for item in TIMELINE])
    desk = pd.concat([tickets, noise_tickets(rng)], ignore_index=True).sort_values(["opened_at", "ticket_ref"])
    desk = desk.reset_index(drop=True)
    for column in ("opened_at", "resolved_at"):
        desk[column] = stamp(desk[column])
    world["files"]["handover/service_desk/tickets.csv"] = desk[COLUMNS]
    truth = pd.DataFrame([{"ticket_ref": item.ref, "kind": item.kind, "system": item.system, "cause": item.cause,
                           "effect": item.effect, "start": item.start.isoformat(),
                           "end": item.end.isoformat() if item.end else ""} for item in TIMELINE])
    world["files"][f"{TRUTH}/service_desk_causes.csv"] = truth
    return desk


def service_name(system: str) -> str:
    return BY_ID[ALIASES.get(system, system)]["name"]


def _ticket(item: Happening) -> dict:
    owner = BY_ID[ALIASES.get(item.system, item.system)]["owner"]
    opened, resolved = _times(item)
    status = "scheduled" if opened > pd.Timestamp(SNAPSHOT) or item.start > SNAPSHOT else ("closed" if not pd.isna(resolved) else "open")
    return {
        "ticket_ref": item.ref, "type": item.kind, "service": service_name(item.system),
        "opened_at": min(opened, pd.Timestamp(SNAPSHOT) - pd.Timedelta(days=2)), "resolved_at": resolved,
        "status": status, "priority": "P2" if item.kind == "incident" else "P3", "site": item.site,
        "summary": item.title, "description": _text(item), "assignee": name(owner),
    }


def _times(item: Happening) -> tuple[pd.Timestamp, pd.Timestamp]:
    start = pd.Timestamp(item.start)
    if item.kind == "incident":
        opened = start + pd.Timedelta(hours=7, minutes=40)
        end = pd.Timestamp(item.end) if item.end else start
        resolved = end + pd.Timedelta(hours=16, minutes=15)
    elif item.kind == "change":
        opened = start - pd.Timedelta(days=12) + pd.Timedelta(hours=10)
        resolved = start + pd.Timedelta(hours=18)
    else:
        opened = start - pd.Timedelta(days=30) + pd.Timedelta(hours=9)
        resolved = pd.NaT
    if not pd.isna(resolved) and resolved > pd.Timestamp(SNAPSHOT):
        resolved = pd.NaT
    return opened, resolved


def _text(item: Happening) -> str:
    templates = {"incident": INCIDENT_TEXT, "change": CHANGE_TEXT}.get(item.kind, FREEZE_TEXT)
    template = seeded(f"desk:{item.ref}").choice(templates)
    end = item.end.isoformat() if item.end else item.start.isoformat()
    text = template.format(effect=item.effect, cause=item.cause[0].lower() + item.cause[1:], title=item.title, reason=item.cause,
                           start=item.start.isoformat(), end=end)
    return text[0].upper() + text[1:]

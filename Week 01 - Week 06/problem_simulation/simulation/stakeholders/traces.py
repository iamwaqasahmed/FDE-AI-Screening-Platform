"""Resolve a truth trace to the value a hidden fact must carry. The check re-resolves every trace."""

from __future__ import annotations

import importlib
from datetime import date

from simulation.stakeholders.queries import ECONOMICS_QUERIES, EVENT_QUERIES
from simulation.workforce.graders import ROSTER
from simulation.world import clock, engagement
from simulation.world.timeline import TIMELINE

SOURCES = ("clock", "engagement", "timeline", "roster", "constant", "events", "economics")


def _text(value) -> str:
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)


def _timeline(ref: str) -> str:
    code, attribute = ref.split(":")
    happening = next(item for item in TIMELINE if item.ref == code)
    return _text(getattr(happening, attribute))


def _roster(ref: str) -> str:
    grader_id, attribute = ref.split(":")
    grader = next(item for item in ROSTER if item.grader_id == grader_id)
    return _text(getattr(grader, attribute))


def _constant(ref: str) -> str:
    parts = ref.split(":")
    value = getattr(importlib.import_module(parts[0]), parts[1])
    for key in parts[2:]:
        value = value[int(key)] if isinstance(value, (tuple, list)) else value[key]
    return _text(value)


def resolve(world: dict, source: str, ref: str) -> str:
    if source == "clock":
        return _text(getattr(clock, ref))
    if source == "engagement":
        return _text(getattr(engagement, ref))
    if source == "timeline":
        return _timeline(ref)
    if source == "roster":
        return _roster(ref)
    if source == "constant":
        return _constant(ref)
    if source == "events":
        return _text(EVENT_QUERIES[ref](world))
    if source == "economics":
        return _text(ECONOMICS_QUERIES[ref](world))
    raise KeyError(f"Unknown trace source {source}")

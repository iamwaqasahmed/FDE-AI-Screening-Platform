"""A clause is the unit of truth. A document binds clauses and edges."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Clause:
    clause_id: str
    topic: str
    document_id: str
    days: int | None
    grade: str
    include_deceased: bool
    frames: tuple[str, ...]


@dataclass(frozen=True)
class Document:
    document_id: str
    title: str
    status: str
    effective: date
    sunset: date | None
    site: str
    programme: str
    version: str
    supersedes: tuple[str, ...]
    cites: tuple[str, ...]
    applies_to: tuple[str, ...]
    constrains: tuple[str, ...]
    clause_ids: tuple[str, ...]

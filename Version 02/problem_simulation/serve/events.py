"""Event feeds that deliver some events late and some twice. Every delay is seeded by a hash of the event id."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta

from fastapi import HTTPException

LATE_PERCENT = 15
DUPLICATE_PERCENT = 10


@dataclass(frozen=True)
class Event:
    event_id: str
    kind: str
    occurred_at: datetime
    payload: dict


def stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()
    return f"{prefix}-{digest[:12]}"


def _seed(event_id: str) -> int:
    return int(hashlib.sha256(event_id.encode("utf-8")).hexdigest()[:16], 16)


def deliveries(event: Event) -> list[datetime]:
    seed = _seed(event.event_id)
    bucket = seed % 100
    first = event.occurred_at + timedelta(minutes=5 + (seed >> 8) % 240)
    if bucket < LATE_PERCENT:
        first += timedelta(days=1 + (seed >> 20) % 5, hours=(seed >> 28) % 24)
    times = [first]
    if 100 - DUPLICATE_PERCENT <= bucket:
        times.append(first + timedelta(hours=1 + (seed >> 36) % 48))
    return times


def parse_since(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value).replace(tzinfo=None)
    except ValueError:
        raise HTTPException(400, detail="since must be an ISO date or datetime") from None


def feed(events: list[Event], since: datetime | None, until: datetime) -> list[dict]:
    delivered = []
    for event in events:
        for copy, moment in enumerate(deliveries(event), start=1):
            if moment <= until and (since is None or moment > since):
                delivered.append((moment, event, copy))
    delivered.sort(key=lambda item: (item[0], item[1].event_id, item[2]))
    return [_render(moment, event, copy) for moment, event, copy in delivered]


def _render(moment: datetime, event: Event, copy: int) -> dict:
    return {
        "event_id": event.event_id,
        "kind": event.kind,
        "occurred_at": event.occurred_at.isoformat(),
        "delivered_at": moment.isoformat(),
        "delivery": copy,
        "payload": event.payload,
    }


def moment_of(value: str) -> datetime | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text).replace(tzinfo=None)
    except ValueError:
        return None
    return parsed if len(text) > 10 else parsed.replace(hour=9)

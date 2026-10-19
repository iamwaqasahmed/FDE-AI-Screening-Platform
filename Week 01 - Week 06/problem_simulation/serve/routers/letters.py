"""Letter bureau API: the 90-day dispatch file and a dispatch event feed."""

from __future__ import annotations

from collections import Counter

from fastapi import APIRouter, Depends, Request

from serve.data import matching, read_rows
from serve.events import Event, feed, moment_of, parse_since, stable_id
from serve.guard import guard, settings_of
from serve.pagination import Paging, page, paging

DISPATCH = "letters/dispatch_90d.csv"

router = APIRouter(prefix="/letters", tags=["letters"], dependencies=[Depends(guard("letters"))])


def _dispatches(request: Request) -> list[dict]:
    return read_rows(settings_of(request).handover, DISPATCH)


@router.get("/dispatches")
def dispatches(
    request: Request,
    site: str | None = None,
    template: str | None = None,
    local_pid: str | None = None,
    window: Paging = Depends(paging),
) -> dict:
    return page(matching(_dispatches(request), site=site, template=template, local_pid=local_pid), window)


def _events(rows: list[dict]) -> list[Event]:
    seen: Counter[tuple] = Counter()
    events = []
    for row in rows:
        moment = moment_of(row.get("letter_at", ""))
        if moment is None:
            continue
        key = (row.get("local_pid", ""), row.get("letter_at", ""), row.get("site", ""), row.get("template", ""))
        seen[key] += 1
        events.append(Event(stable_id("LTR", *key, seen[key]), "letter.dispatched", moment, dict(row)))
    return events


@router.get("/events")
def events(request: Request, since: str | None = None, window: Paging = Depends(paging)) -> dict:
    delivered = feed(_events(_dispatches(request)), parse_since(since), settings_of(request).clock)
    return page(delivered, window)

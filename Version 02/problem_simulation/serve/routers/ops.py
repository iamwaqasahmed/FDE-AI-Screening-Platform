"""Unauthenticated operational routes: health and metrics."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from serve.clock import active_outage, iso

router = APIRouter(tags=["ops"])


@router.get("/health")
def health(request: Request) -> dict:
    state = request.app.state
    settings = state.settings
    return {
        "systems": {system: "outage" if active_outage(system, settings.clock) else "up" for system in state.systems},
        "clock": iso(settings.clock),
        "week": settings.week,
        "handover_present": settings.handover.is_dir(),
    }


@router.get("/metrics", response_class=PlainTextResponse)
def metrics(request: Request) -> str:
    return request.app.state.metrics.render()

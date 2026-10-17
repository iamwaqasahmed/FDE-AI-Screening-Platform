"""The dependency every system route runs: authenticate, spend rate budget, then refuse during a timeline outage."""

from __future__ import annotations

from fastapi import Header, HTTPException, Request

from serve.auth import Token, authenticate
from serve.clock import active_outage
from serve.settings import Settings


def settings_of(request: Request) -> Settings:
    return request.app.state.settings


def guard(system: str, action: str = "read"):
    scope = f"{system}:{action}"

    def dependency(request: Request, authorization: str = Header(default="")) -> Token:
        state = request.app.state
        token = authenticate(state.tokens, authorization, scope, state.settings.clock)
        state.limiter.take(token)
        outage = active_outage(system, state.settings.clock)
        if outage is not None:
            ref, start, end, title = outage
            state.metrics.count("outage_responses_total", system)
            raise HTTPException(
                503,
                detail=f"{system} unavailable: {title} ({ref}, {start.isoformat()} to {end.isoformat()})",
                headers={"Retry-After": "3600"},
            )
        request.state.token = token
        return token

    return dependency

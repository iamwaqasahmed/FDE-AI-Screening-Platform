"""The app factory: one FastAPI app serving one system or all five from the handover folder."""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from serve import metrics
from serve.auth import load_tokens
from serve.booking_log import booking_logger
from serve.data import DataMissing
from serve.ratelimit import TokenBuckets
from serve.routers import ROUTERS, ops
from serve.settings import SYSTEMS, ensure_simulation_path, load_settings


def _selected(system: str) -> tuple[str, ...]:
    if system == "all":
        return SYSTEMS
    if system not in SYSTEMS:
        raise ValueError(f"unknown system {system}; choose all or one of {', '.join(SYSTEMS)}")
    return (system,)


def _missing_data(request: Request, error: DataMissing) -> JSONResponse:
    detail = f"{error.relative} is not in this build; the service has no data to serve"
    return JSONResponse({"detail": detail}, status_code=503, headers={"Retry-After": "86400"})


def create_app(system: str = "all") -> FastAPI:
    ensure_simulation_path()
    systems = _selected(system)
    settings = load_settings()
    app = FastAPI(title=f"Hartland mock systems ({system})", version="1")
    app.state.settings = settings
    app.state.systems = systems
    app.state.tokens = load_tokens(settings.tokens_path)
    app.state.limiter = TokenBuckets()
    app.state.metrics = metrics.Metrics()
    if "booking" in systems:
        app.state.booking_log = booking_logger(settings)
    metrics.install(app)
    app.add_exception_handler(DataMissing, _missing_data)
    for name in systems:
        app.include_router(ROUTERS[name])
    app.include_router(ops.router)
    return app

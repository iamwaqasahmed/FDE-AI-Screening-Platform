"""Simple in-process counters, exposed as plain text on /metrics."""

from __future__ import annotations

import time
from collections import Counter
from threading import Lock

from fastapi import FastAPI, Request


class Metrics:
    def __init__(self):
        self._counts: Counter[tuple[str, ...]] = Counter()
        self._latency: Counter[tuple[str, ...]] = Counter()
        self._lock = Lock()

    def count(self, name: str, *labels: str) -> None:
        with self._lock:
            self._counts[(name, *labels)] += 1

    def observe(self, route: str, status: int, seconds: float) -> None:
        with self._lock:
            self._counts[("http_requests_total", route, str(status))] += 1
            self._latency[("http_request_seconds_sum", route)] += seconds
            self._latency[("http_request_seconds_count", route)] += 1

    def render(self) -> str:
        with self._lock:
            lines = [_line(key, value) for key, value in sorted(self._counts.items())]
            lines += [_line(key, round(value, 6)) for key, value in sorted(self._latency.items())]
        return "\n".join(lines) + "\n"


def _line(key: tuple[str, ...], value: float) -> str:
    name, *labels = key
    names = ("route", "status") if name == "http_requests_total" else ("route",) if name.startswith("http_") else ("system",)
    rendered = ",".join(f'{label}="{value_}"' for label, value_ in zip(names, labels))
    return f"{name}{{{rendered}}} {value}" if rendered else f"{name} {value}"


def install(app: FastAPI) -> None:
    @app.middleware("http")
    async def record(request: Request, call_next):
        started = time.perf_counter()
        response = await call_next(request)
        route = request.scope.get("route")
        template = getattr(route, "path", "unmatched")
        app.state.metrics.observe(f"{request.method} {template}", response.status_code, time.perf_counter() - started)
        return response

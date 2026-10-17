"""The booking service application log under serve/runtime/logs/booking.log, stamped with the simulated clock."""

from __future__ import annotations

import json
import logging

from fastapi import Request

from serve.clock import iso
from serve.settings import Settings

LOGGER_NAME = "hartland.booking"


def booking_logger(settings: Settings) -> logging.Logger:
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(LOGGER_NAME)
    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
    handler = logging.FileHandler(settings.log_dir / "booking.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter(f"{iso(settings.clock)} %(levelname)s %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if settings.booking_debug else logging.INFO)
    logger.propagate = False
    return logger


def log_request(request: Request, records: list[dict] = (), body: dict | None = None) -> None:
    logger: logging.Logger = request.app.state.booking_log
    token = getattr(request.state, "token", None)
    client = token.client if token else "anonymous"
    logger.info("%s %s client=%s results=%d", request.method, request.url.path, client, len(records))
    if not logger.isEnabledFor(logging.DEBUG):
        return
    query = dict(sorted(request.query_params.items()))
    logger.debug("request %s %s query=%s body=%s", request.method, request.url.path, json.dumps(query), json.dumps(body or {}))
    for record in records[:20]:
        logger.debug("record %s", json.dumps(record, sort_keys=True))

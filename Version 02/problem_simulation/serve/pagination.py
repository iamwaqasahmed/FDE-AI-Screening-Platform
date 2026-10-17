"""Opaque cursor pagination. A cursor is bound to the route and filters it was issued for."""

from __future__ import annotations

import base64
import hashlib
import json
from dataclasses import dataclass

from fastapi import HTTPException, Query, Request

MAX_LIMIT = 500


@dataclass(frozen=True)
class Paging:
    limit: int
    cursor: str | None
    scope: str


def _scope(request: Request) -> str:
    filters = sorted((key, value) for key, value in request.query_params.multi_items() if key not in ("cursor", "limit"))
    text = request.url.path + "?" + "&".join(f"{key}={value}" for key, value in filters)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def paging(request: Request, limit: int = Query(100, ge=1, le=MAX_LIMIT), cursor: str | None = None) -> Paging:
    return Paging(limit=limit, cursor=cursor, scope=_scope(request))


def encode(offset: int, scope: str) -> str:
    raw = json.dumps({"o": offset, "s": scope}, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def decode(cursor: str | None, scope: str) -> int:
    if not cursor:
        return 0
    try:
        padded = cursor + "=" * (-len(cursor) % 4)
        state = json.loads(base64.urlsafe_b64decode(padded.encode("ascii")))
        offset, issued_for = int(state["o"]), state["s"]
    except (ValueError, KeyError, TypeError):
        raise HTTPException(400, detail="malformed cursor") from None
    if issued_for != scope or offset < 0:
        raise HTTPException(400, detail="cursor was issued for a different query")
    return offset


def page(rows: list, paging: Paging) -> dict:
    offset = decode(paging.cursor, paging.scope)
    end = offset + paging.limit
    following = encode(end, paging.scope) if end < len(rows) else None
    return {"items": rows[offset:end], "next_cursor": following, "total": len(rows)}

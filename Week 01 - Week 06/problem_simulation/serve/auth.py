"""Bearer tokens from tokens.yaml: scopes per system, an expiry date on the simulated clock, and a rate budget."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import yaml
from fastapi import HTTPException


@dataclass(frozen=True)
class Token:
    token: str
    client: str
    scopes: tuple[str, ...]
    expires: date | None
    burst: int
    per_minute: float


def _token(entry: dict) -> Token:
    expires = entry.get("expires")
    return Token(
        token=str(entry["token"]),
        client=str(entry["client"]),
        scopes=tuple(sorted(entry.get("scopes", []))),
        expires=date.fromisoformat(str(expires)) if expires else None,
        burst=int(entry.get("burst", 20)),
        per_minute=float(entry.get("per_minute", 60)),
    )


def load_tokens(path: Path) -> dict[str, Token]:
    document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {item.token: item for item in (_token(entry) for entry in document.get("tokens", []))}


def _unauthorised(detail: str) -> HTTPException:
    return HTTPException(401, detail=detail, headers={"WWW-Authenticate": 'Bearer realm="hartland"'})


def bearer(header: str) -> str:
    scheme, _, value = header.partition(" ")
    if scheme.lower() != "bearer" or not value.strip():
        raise _unauthorised("missing bearer token")
    return value.strip()


def authenticate(tokens: dict[str, Token], header: str, scope: str, clock: datetime) -> Token:
    token = tokens.get(bearer(header))
    if token is None:
        raise _unauthorised("unknown token")
    if token.expires is not None and clock.date() > token.expires:
        raise _unauthorised(f"token expired on {token.expires.isoformat()}")
    if scope not in token.scopes:
        raise HTTPException(403, detail=f"token lacks scope {scope}")
    return token

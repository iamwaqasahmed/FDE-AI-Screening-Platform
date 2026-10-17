"""A token bucket per bearer token. An empty bucket answers 429 with Retry-After in whole seconds."""

from __future__ import annotations

import math
import time
from threading import Lock
from typing import Callable

from fastapi import HTTPException

from serve.auth import Token


class TokenBuckets:
    def __init__(self, now: Callable[[], float] = time.monotonic):
        self._now = now
        self._levels: dict[str, tuple[float, float]] = {}
        self._lock = Lock()

    def take(self, token: Token) -> float:
        rate = token.per_minute / 60.0
        with self._lock:
            moment = self._now()
            level, stamp = self._levels.get(token.token, (float(token.burst), moment))
            level = min(float(token.burst), level + (moment - stamp) * rate)
            if level < 1.0:
                self._levels[token.token] = (level, moment)
                wait = math.ceil((1.0 - level) / rate) if rate > 0 else 3600
                raise HTTPException(429, detail="rate limit exceeded", headers={"Retry-After": str(max(1, wait))})
            self._levels[token.token] = (level - 1.0, moment)
            return level - 1.0

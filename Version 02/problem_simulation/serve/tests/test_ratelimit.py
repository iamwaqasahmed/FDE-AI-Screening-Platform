"""The token bucket empties after the burst, answers 429 with Retry-After, and refills over time."""

from __future__ import annotations

from serve.ratelimit import TokenBuckets
from serve.tests.conftest import auth


def test_burst_then_429_then_refill(make_client):
    client = make_client()
    now = [0.0]
    client.app.state.limiter = TokenBuckets(now=lambda: now[0])
    codes = [client.get("/vendor/scores", headers=auth("discovery")).status_code for _ in range(6)]
    assert codes == [200] * 5 + [429]
    limited = client.get("/vendor/scores", headers=auth("discovery"))
    assert int(limited.headers["Retry-After"]) >= 1
    now[0] += 6.0
    assert client.get("/vendor/scores", headers=auth("discovery")).status_code == 200


def test_buckets_are_per_token(make_client):
    client = make_client()
    client.app.state.limiter = TokenBuckets(now=lambda: 0.0)
    for _ in range(5):
        client.get("/vendor/scores", headers=auth("discovery"))
    assert client.get("/vendor/scores", headers=auth("discovery")).status_code == 429
    assert client.get("/vendor/scores", headers=auth("vendor")).status_code == 200

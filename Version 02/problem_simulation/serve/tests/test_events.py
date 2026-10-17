"""Event feeds deliver some events late and some twice, the same way on every call."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta

from serve.tests.conftest import auth


def _all(client, path: str, token: str, **params) -> list[dict]:
    items, cursor = [], None
    while True:
        query = {"limit": 500, **params, **({"cursor": cursor} if cursor else {})}
        body = client.get(path, params=query, headers=auth(token)).json()
        items += body["items"]
        cursor = body["next_cursor"]
        if cursor is None:
            return items


def test_letters_feed_has_duplicates_and_late_events(make_client):
    items = _all(make_client(), "/letters/events", "letters")
    copies = Counter(item["event_id"] for item in items)
    assert any(count == 2 for count in copies.values())
    lags = [datetime.fromisoformat(item["delivered_at"]) - datetime.fromisoformat(item["occurred_at"]) for item in items]
    assert any(lag > timedelta(days=1) for lag in lags)
    occurred = [item["occurred_at"] for item in items]
    assert occurred != sorted(occurred)


def test_feed_is_deterministic(make_client):
    assert _all(make_client(), "/letters/events", "letters") == _all(make_client(), "/letters/events", "letters")


def test_since_filters_by_delivery_time(make_client):
    everything = _all(make_client(), "/letters/events", "letters")
    items = _all(make_client(), "/letters/events", "letters", since="2026-08-15")
    assert 0 < len(items) < len(everything)
    assert all(item["delivered_at"] > "2026-08-15" for item in items)


def test_booking_feed_duplicates(make_client, booking_data):
    items = _all(make_client(data=booking_data), "/booking/events", "booking")
    assert len(items) > 40
    assert {item["event_id"] for item in items} and max(Counter(i["event_id"] for i in items).values()) == 2


def test_clock_hides_future_deliveries(make_client):
    early = _all(make_client(clock="2026-08-01"), "/letters/events", "letters")
    assert all(item["delivered_at"] <= "2026-08-01T23:59:59" for item in early)

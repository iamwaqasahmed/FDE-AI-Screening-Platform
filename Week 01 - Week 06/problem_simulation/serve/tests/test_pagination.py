"""Cursor pagination walks every row once and refuses a cursor reused on another query."""

from __future__ import annotations

from serve.tests.conftest import auth


def test_cursor_walks_all_rows(make_client):
    client = make_client()
    pages, cursor, total = 0, None, None
    seen = 0
    while True:
        params = {"limit": 250, **({"cursor": cursor} if cursor else {})}
        body = client.get("/ophthalmology/referrals", params=params, headers=auth("ophthalmology")).json()
        total, pages = body["total"], pages + 1
        seen += len(body["items"])
        cursor = body["next_cursor"]
        if cursor is None:
            break
    assert seen == total > 250 and pages > 1


def test_cursor_bound_to_filters(make_client):
    client = make_client()
    first = client.get("/registry/people", params={"limit": 5}, headers=auth("registry")).json()
    reused = client.get("/registry/people", params={"limit": 5, "cursor": first["next_cursor"], "district": "North City"},
                        headers=auth("registry"))
    assert reused.status_code == 400


def test_malformed_cursor_is_400(make_client):
    response = make_client().get("/registry/people", params={"cursor": "!!"}, headers=auth("registry"))
    assert response.status_code == 400

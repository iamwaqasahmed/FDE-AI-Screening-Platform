"""Registry schema versions through Accept-Version, with v3 published from engagement week 2."""

from __future__ import annotations

from serve.tests.conftest import auth


def _first(client, version: str | None):
    headers = {**auth("registry"), **({"Accept-Version": version} if version else {})}
    return client.get("/registry/people", params={"limit": 1}, headers=headers)


def test_default_is_v2(make_client):
    response = _first(make_client(), None)
    assert response.headers["Content-Version"] == "2"
    assert "REGISTRY_NO" in response.json()["items"][0]


def test_v1_uses_old_columns(make_client):
    item = _first(make_client(), "1").json()["items"][0]
    assert sorted(item) == ["DOB", "REG_NO", "STATUS", "SURNAME"]


def test_v3_hidden_in_week_1(make_client):
    response = _first(make_client(week=1), "3")
    assert response.status_code == 406
    assert "week 2" in response.json()["detail"]


def test_v3_available_from_week_2(make_client):
    response = _first(make_client(week=2), "v3")
    assert response.status_code == 200
    item = response.json()["items"][0]
    assert item["registry_no"] and "date_of_birth_as_supplied" in item


def test_unknown_version_is_406(make_client):
    assert _first(make_client(), "9").status_code == 406

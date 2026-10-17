"""Bearer token checks: missing, unknown, wrong scope, expired, and valid."""

from __future__ import annotations

from serve.tests.conftest import auth


def test_missing_token_is_401(make_client):
    response = make_client().get("/registry/people")
    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"].startswith("Bearer")


def test_unknown_token_is_401(make_client):
    response = make_client().get("/registry/people", headers={"Authorization": "Bearer not-a-token"})
    assert response.status_code == 401


def test_wrong_scope_is_403(make_client):
    response = make_client().get("/registry/people", headers=auth("vendor"))
    assert response.status_code == 403
    assert "registry:read" in response.json()["detail"]


def test_expired_token_is_401_on_the_simulated_clock(make_client):
    assert make_client(clock="2026-10-01").get("/registry/people", headers=auth("expired")).status_code == 401
    assert make_client(clock="2026-06-01").get("/registry/people", headers=auth("expired")).status_code == 200


def test_valid_token_reads(make_client):
    response = make_client().get("/vendor/scores", headers=auth("vendor"))
    assert response.status_code == 200
    assert response.json()["items"]

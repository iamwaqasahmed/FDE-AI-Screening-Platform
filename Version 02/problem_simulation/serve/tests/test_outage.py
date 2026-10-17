"""Outages follow the simulation timeline, and a missing handover file is a clear 503."""

from __future__ import annotations

from serve.tests.conftest import auth


def test_booking_outage_on_inc_0281(make_client):
    response = make_client(clock="2026-02-10").get("/booking/appointments", headers=auth("booking"))
    assert response.status_code == 503
    assert "INC-0281" in response.json()["detail"]
    assert response.headers["Retry-After"]


def test_booking_back_after_the_window(make_client, booking_data):
    response = make_client(data=booking_data, clock="2026-02-11").get("/booking/appointments", headers=auth("booking"))
    assert response.status_code == 200


def test_vendor_outage_on_inc_0274(make_client):
    response = make_client(clock="2025-11-18").get("/vendor/scores", headers=auth("vendor"))
    assert response.status_code == 503
    assert "INC-0274" in response.json()["detail"]


def test_outage_is_per_system(make_client):
    assert make_client(clock="2026-02-10").get("/vendor/scores", headers=auth("vendor")).status_code == 200


def test_missing_booking_file_is_503(make_client, tmp_path):
    (tmp_path / "empty" / "handover").mkdir(parents=True)
    response = make_client(data=tmp_path / "empty").get("/booking/appointments", headers=auth("booking"))
    assert response.status_code == 503
    assert "handover/booking/appointments.csv" in response.json()["detail"]


def test_health_reports_outage(make_client):
    systems = make_client(clock="2026-02-10").get("/health").json()["systems"]
    assert systems["booking"] == "outage" and systems["registry"] == "up"

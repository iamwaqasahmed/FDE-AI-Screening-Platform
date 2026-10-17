"""Booking reads, the debug application log, receipts, and the metrics counters."""

from __future__ import annotations

from serve.tests.conftest import auth


def test_booking_lookup_and_filter(make_client, booking_data):
    client = make_client(data=booking_data)
    assert client.get("/booking/appointments/BK0000003", headers=auth("booking")).json()["items"][0]["status"] == "cancelled"
    body = client.get("/booking/appointments", params={"status": "cancelled"}, headers=auth("booking")).json()
    assert body["total"] == 13
    assert client.get("/booking/appointments/BK9999999", headers=auth("booking")).status_code == 404


def test_contact_update_needs_write_scope(make_client, booking_data):
    client = make_client(data=booking_data)
    body = {"forename": "Ada", "surname": "Quill", "phone": "07700900123"}
    assert client.post("/booking/appointments/APT-00001/contact", json=body, headers=auth("discovery")).status_code == 403
    assert client.post("/booking/appointments/APT-00001/contact", json=body, headers=auth("booking")).status_code == 202


def test_application_log_written(make_client, booking_data, tmp_path):
    client = make_client(data=booking_data)
    client.post("/booking/appointments/APT-00001/contact", json={"surname": "Quill", "phone": "07700900123"},
                headers=auth("booking"))
    text = (tmp_path / "logs" / "booking.log").read_text(encoding="utf-8")
    assert "POST /booking/appointments/APT-00001/contact" in text
    assert "07700900123" in text


def test_receipts_absent_is_503(make_client, booking_data):
    response = make_client(data=booking_data).get("/booking/receipts", headers=auth("booking"))
    assert response.status_code == 503
    assert "handover/sms/receipts.jsonl" in response.json()["detail"]


def test_metrics_count_requests(make_client):
    client = make_client()
    client.get("/vendor/scores", headers=auth("vendor"))
    text = client.get("/metrics").text
    assert 'http_requests_total{route="GET /vendor/scores",status="200"} 1' in text


def test_single_system_app_mounts_one_router(make_client):
    client = make_client(system="vendor")
    assert client.get("/vendor/scores", headers=auth("vendor")).status_code == 200
    assert client.get("/registry/people", headers=auth("registry")).status_code == 404

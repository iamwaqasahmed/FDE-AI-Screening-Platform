"""Fixtures: an app over data-small with the simulated clock and week set per test."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from serve.app import create_app
from serve.settings import VERSION_ROOT

SMALL = VERSION_ROOT / "build" / "data-small"
TOKENS = {
    "registry": "hl-registry-etl-4c1e",
    "booking": "hl-booking-portal-9a7d",
    "letters": "hl-letters-recon-2b88",
    "ophthalmology": "hl-eye-referrals-61f0",
    "ophthalmology": "hl-eye-referrals-61f0",
    "vendor": "hl-vendor-pilot-d3a5",
    "expired": "hl-outreach-sync-0f19",
    "discovery": "hl-discovery-team-5b2c",
}


def auth(name: str) -> dict:
    return {"Authorization": f"Bearer {TOKENS[name]}"}


@pytest.fixture
def make_client(monkeypatch, tmp_path):
    def build(data: Path = SMALL, clock: str = "2026-10-01", week: int = 1, system: str = "all") -> TestClient:
        monkeypatch.setenv("HARTLAND_DATA", str(data))
        monkeypatch.setenv("HARTLAND_CLOCK", clock)
        monkeypatch.setenv("HARTLAND_WEEK", str(week))
        monkeypatch.setenv("HARTLAND_LOG_DIR", str(tmp_path / "logs"))
        return TestClient(create_app(system))

    if not (SMALL / "handover").is_dir():
        pytest.skip("data-small has not been built")
    return build


@pytest.fixture
def booking_data(tmp_path) -> Path:
    root = tmp_path / "data"
    folder = root / "handover" / "booking"
    folder.mkdir(parents=True)
    lines = ["booking_id,appointment_id,site,slot_start,status,updated_at,channel"]
    for index in range(1, 41):
        status = "booked" if index % 3 else "cancelled"
        lines.append(f"BK{index:07d},APT-{index:05d},North City Eye Clinic,2026-09-{1 + index % 28:02d}T09:30:00,"
                     f"{status},2026-08-{1 + index % 28:02d}T1{index % 10}:00:00,{'sms' if index % 2 else 'phone'}")
    (folder / "appointments.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return root

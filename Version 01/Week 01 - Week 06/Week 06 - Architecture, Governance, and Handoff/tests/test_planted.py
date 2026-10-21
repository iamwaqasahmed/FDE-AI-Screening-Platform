"""The week 6 traps are visible on the small build, without opening truth."""

from __future__ import annotations

from pathlib import Path

import pytest

from reference_handoff.load import memo, pilot_sites, read_csv, sender

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "drops/week-6/clinical_safety_owner.md").exists(), reason="small drop is not present")


def test_the_memo_names_an_owner_and_keeps_the_pilot_stopped():
    text = memo(SMALL, "drops/week-6/clinical_safety_owner.md")
    owner, role = sender(text)
    assert owner and role
    assert "stopped" in text.lower()
    assert "CSO-1" in text and "CSO-5" in text


def test_the_owners_register_is_still_blank():
    owners = read_csv(SMALL, "handover/owners.csv").set_index("role")
    assert owners.at["clinical_safety_owner", "name"] == ""


def test_r11_is_closed_and_r02_is_open():
    risks = read_csv(SMALL, "handover/delivery/risk_register.csv").set_index("risk_id")
    assert risks.at["R-11", "status"] == "Closed"
    assert risks.at["R-02", "status"] == "Open"


def test_the_vendor_is_not_hosted_in_the_uk_and_the_folder_has_no_backup():
    note = (SMALL / "handover/interfaces/vendor.md").read_text(encoding="utf-8").lower()
    assert "eu" in note
    components = read_csv(SMALL, "handover/architecture/components.csv").set_index("component")
    assert components.at["shared-folder", "dr_tier"] == "4"
    assert int(components.at["grader", "dr_tier"]) < int(components.at["vendor", "dr_tier"])


def test_the_week_00_image_copies_the_handover():
    root = Path(__file__).resolve().parents[3]
    text = (root / "Week 00 - Self Paced" / "Dockerfile").read_text(encoding="utf-8")
    assert "data/handover" in text
    assert "data/corpus" in text


def test_the_week_3_sites_are_the_memo_sites():
    text = memo(SMALL, "drops/week-6/clinical_safety_owner.md")
    assert len(pilot_sites(text)) == 2

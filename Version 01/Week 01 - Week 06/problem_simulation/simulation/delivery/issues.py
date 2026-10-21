"""Issues log. Most issues point at the timeline entry that caused them."""

from __future__ import annotations

import pandas as pd

from simulation.world.staff import name

ISSUES = (
    ("I-01", "Duplicate letters during the bureau incident week", "programme_manager", "Closed", "2025-03-11", "2025-04-02", "INC-0233"),
    ("I-02", "Outreach captures missing local ids", "outreach_coordinator", "Closed", "2024-11-22", "2025-01-15", "INC-0215"),
    ("I-03", "Wrong history after the merge batch", "records_manager", "Closed", "2025-02-18", "2025-05-30", "INC-0236"),
    ("I-04", "Inappropriate record access found in audit", "security_officer", "Closed", "2025-07-01", "2025-10-01", "INC-0262"),
    ("I-05", "Names and phone numbers in booking logs", "security_officer", "Closed", "2025-10-02", "2025-11-03", "INC-0270"),
    ("I-06", "Pilot scores late after vendor outage", "vendor_manager", "Closed", "2025-11-19", "2025-11-28", "INC-0274"),
    ("I-07", "Slot changes lost after booking failover", "booking_admin", "Closed", "2026-02-11", "2026-03-06", "INC-0281"),
    ("I-08", "Fast-track clinic slots cut", "ophthalmology_lead", "Open", "2025-01-20", "", "INC-0251"),
    ("I-09", "Ungradable rate up after firmware change", "programme_manager", "Closed", "2023-06-01", "2023-09-30", "CHG-0131"),
    ("I-10", "Clinical safety owner not appointed", "cdo", "Open", "2025-06-02", "", ""),
    ("I-11", "Warehouse counts deceased people as eligible", "enterprise_architect", "Open", "2026-03-09", "", ""),
    ("I-12", "Registry interface work planned inside the freeze", "delivery_manager", "Open", "2026-09-14", "", "FRZ-0301"),
)


def issues_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [{"issue_id": iid, "title": title, "owner": name(owner), "status": status, "raised": raised, "resolved": resolved, "links": links}
         for iid, title, owner, status, raised, resolved, links in ISSUES]
    )

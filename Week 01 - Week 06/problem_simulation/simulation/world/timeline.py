"""Every operational incident, change, and freeze. Service desk, notices, drops, and mock APIs all read this list."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from simulation.care.referrals import CONSULTANT_GAP
from simulation.world import clock as c
from simulation.world.sites import MARKET, RIVER_SITE


@dataclass(frozen=True)
class Happening:
    ref: str
    kind: str
    system: str
    start: date
    end: date | None
    title: str
    cause: str
    effect: str
    site: str = ""


TIMELINE: tuple[Happening, ...] = (
    Happening("CHG-0101", "change", "registry", c.SCHEMA_CUTOVER, None, "Registry extract schema v2",
              "Ministry moved to named columns", "December 2021 file uses old columns; March 2022 mixes both"),
    Happening("CHG-0114", "change", "sms", date(2021, 1, 4), None, "SMS invitations go live",
              "New contact gateway contract", "People with a phone get an SMS with each invitation"),
    Happening("CHG-0120", "change", "lab", c.LAB_UNIT_CHANGE, None, "HbA1c reported in mmol/mol",
              "Lab analyser replacement", "Values before the change are percentages"),
    Happening("CHG-0131", "change", "devices", c.FIRMWARE_MARKET, None, "Camera firmware 4.2.0", "Supplier patch",
              "Ungradable rate rises at the site", MARKET),
    Happening("CHG-0140", "change", "sms", c.REMINDER_CHANGE, None, "SMS reminder three days before appointment",
              "Service improvement, rolled out everywhere at once", "Attendance changes by district"),
    Happening("CHG-0144", "change", "finance", c.FINANCE_RECODE, None, "Cost centre recode", "Finance system upgrade",
              "Screening cost centres renumbered"),
    Happening("CHG-0152", "change", "pacs", c.MERGE_APPLIED, None, "Patient merge batch applied", "Duplicate clean-up",
              "Some studies attached to the wrong person"),
    Happening("CHG-0158", "change", "letters", c.BUREAU_MIGRATION_START, c.BUREAU_MIGRATION_END,
              "Letter bureau platform migration", "Supplier moved print platform", "Dispatch slowed for months"),
    Happening("CHG-0171", "change", "grader", c.ROTA_CHANGE, None, "Grader rota moved to long sessions",
              "Staffing pressure", "One grader's accuracy and throughput fell"),
    Happening("INC-0207", "incident", "registry", c.STALE_FEED, None, "Registry feed repeated reissued numbers",
              "Ministry replayed a cached batch", "Two people share one registry number in that month"),
    Happening("INC-0215", "incident", "grader", c.OUTAGE_START, c.OUTAGE_END, "Outreach laptop sync failure",
              "Expired device certificate", "No local ids stored for those captures", RIVER_SITE),
    Happening("INC-0233", "incident", "letters", c.INCIDENT_START, c.INCIDENT_END, "Letter bureau duplicate week",
              "Retry loop after a queue failure", "Each dispatch written twice; some letters lost"),
    Happening("INC-0236", "incident", "pacs", c.MERGE_REVERSED, None, "Merge batch reversed",
              "Clinical complaint about a wrong history", "Events between merge and reversal sit on the wrong record"),
    Happening("CHG-0240", "change", "devices", c.FIRMWARE_RIVER, None, "Outreach camera firmware 3.1.0", "Supplier patch",
              "Image quality improves; vendor scores shift", RIVER_SITE),
    Happening("INC-0251", "incident", "ophthalmology", date.fromisoformat(CONSULTANT_GAP[0]),
              date.fromisoformat(CONSULTANT_GAP[1]), "Consultant vacancy", "Retirement not backfilled",
              "Fast-track clinic slots cut"),
    Happening("INC-0262", "incident", "audit", date(2025, 6, 9), date(2025, 6, 30), "Inappropriate record access review",
              "Leaver kept access after a role change", "Records read without a care relationship"),
    Happening("INC-0270", "incident", "booking", date(2025, 9, 15), date(2025, 10, 2), "PII written to booking API logs",
              "Debug logging left on after a release", "Names and phone numbers in application logs"),
    Happening("INC-0274", "incident", "vendor", date(2025, 11, 18), date(2025, 11, 19), "Vendor API outage",
              "Supplier cloud region failure", "Pilot scores delayed"),
    Happening("INC-0281", "incident", "booking", date(2026, 2, 10), date(2026, 2, 11), "Booking system outage",
              "Database failover", "Slot changes lost for a day"),
    Happening("FRZ-0301", "freeze", "registry", date(2026, 10, 19), date(2027, 1, 29), "Registry change freeze",
              "Ministry year-end", "No interface changes to the registry feed"),
    Happening("FRZ-0302", "freeze", "letters", date(2026, 12, 14), date(2027, 1, 8), "Bureau seasonal freeze",
              "Peak post", "No template or interface changes"),
)


def happenings(system: str = "", kind: str = "") -> list[Happening]:
    return [item for item in TIMELINE if (not system or item.system == system) and (not kind or item.kind == kind)]

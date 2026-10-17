"""Epics from the two earlier teams: dates, component, timeline links, and the work items each one breaks into."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Epic:
    epic_id: str
    title: str
    team: str
    start: date
    end: date
    component: str
    refs: tuple[str, ...]
    count: int
    objects: tuple[str, ...]
    open: bool = False
    pilot: bool = False


def _epic(number, title, team, start, end, component, refs, count, objects, open=False, pilot=False) -> Epic:
    return Epic(f"DLV-{number:04d}", title, team, date.fromisoformat(start), date.fromisoformat(end),
                component, refs, count, objects, open, pilot)


EPICS = (
    _epic(1001, "Registry month-end ingestion", "Kestrel", "2024-01-08", "2024-06-30", "registry-interface",
          ("CHG-0101", "INC-0207"), 55, ("month-end file loader", "named column mapping", "deceased flag handling",
                                         "reissued number detection", "mixed schema month", "registry extract checksum")),
    _epic(1002, "HbA1c lab feed mapping", "Kestrel", "2024-03-04", "2024-09-29", "lab",
          ("CHG-0120",), 40, ("unit conversion", "lab patient id lookup", "ORU segment parser", "result range check")),
    _epic(1003, "Grader workbench export", "Kestrel", "2024-02-05", "2024-10-27", "grader",
          ("CHG-0171",), 45, ("signed grade export", "session length report", "second grade queue", "note text codes")),
    _epic(1004, "SMS reminder reporting", "Kestrel", "2024-05-13", "2024-12-22", "sms",
          ("CHG-0140", "CHG-0114"), 40, ("delivery receipt loader", "reminder uptake dashboard", "late receipt ordering",
                                         "opt-out list sync")),
    _epic(1005, "Outreach laptop sync hardening", "Kestrel", "2024-11-04", "2025-03-30", "grader",
          ("INC-0215",), 35, ("certificate expiry alert", "offline capture queue", "local id backfill")),
    _epic(1006, "Letter bureau reconciliation", "Kestrel", "2024-09-02", "2025-03-30", "letters",
          ("INC-0233", "CHG-0158"), 45, ("dispatch file loader", "duplicate dispatch report", "lost letter trace",
                                         "bureau SLA dashboard")),
    _epic(1007, "Vendor pilot integration", "Heron", "2025-04-07", "2025-12-21", "vendor",
          ("INC-0274",), 55, ("score file intake", "pilot cohort extract", "score versus grade report",
                              "vendor callback endpoint", "empty score handling")),
    _epic(1008, "Access audit review", "Heron", "2025-06-02", "2025-10-26", "audit",
          ("INC-0262",), 30, ("leaver access report", "audit log parser", "role mapping review")),
    _epic(1009, "Booking API logging and resilience", "Heron", "2025-09-08", "2026-03-29", "booking",
          ("INC-0270", "INC-0281"), 45, ("log redaction filter", "failover runbook", "slot history table",
                                         "API retry policy")),
    _epic(1010, "Camera firmware tracking", "Heron", "2025-05-05", "2025-11-30", "devices",
          ("CHG-0131", "CHG-0240"), 30, ("firmware inventory sync", "ungradable rate alert", "device register")),
    _epic(1011, "Warehouse eligibility mart", "Heron", "2025-10-06", "2026-06-28", "warehouse",
          (), 45, ("eligibility view", "coverage window parameter", "deceased exclusion", "district rollup")),
    _epic(1012, "Registry schema v3 interface", "Heron", "2026-05-04", "2026-09-27", "registry-interface",
          ("CHG-0101",), 40, ("v3 column mapping", "renamed field adapter", "reissue batch handler",
                              "schema version guard"), open=True, pilot=True),
    _epic(1013, "Vendor pilot phase two", "Heron", "2026-04-06", "2026-09-27", "vendor",
          ("INC-0274",), 45, ("primary-care cohort filter", "grader review queue", "score monitoring",
                              "pilot site onboarding"), open=True, pilot=True),
    _epic(1014, "Letter template refresh", "Heron", "2026-06-01", "2026-09-27", "letters-template",
          ("CHG-0158",), 25, ("referral letter template", "large print variant", "portal message copy"), open=True),
)
BY_ID = {epic.epic_id: epic for epic in EPICS}

VERBS = ("Add", "Fix", "Build", "Document", "Test", "Automate", "Review", "Refactor")
REWORD = {"Add": "Implement", "Fix": "Resolve", "Build": "Create", "Document": "Write up", "Test": "Verify",
          "Automate": "Script", "Review": "Check", "Refactor": "Clean up"}
ASPECTS = ("for North City", "for Hill Counties", "for East City", "in staging", "for month end", "with alerts",
           "for the service desk", "behind a feature flag")
RELEASE_TARGETS = {
    "registry-interface": ("2026-10-13", "2026-11-03", "2026-12-01", "2027-01-05"),
    "letters-template": ("2026-11-11", "2026-12-16", "2027-01-06"),
    "vendor": ("2026-11-03", "2026-12-01"),
}
FREEZE_SYSTEM = {"registry-interface": "registry", "letters-template": "letters"}

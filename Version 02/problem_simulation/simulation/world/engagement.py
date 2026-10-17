"""The six-week engagement calendar. Week 1 is the base drop; weeks 2 to 6 each add one drop."""

from __future__ import annotations

from datetime import date, timedelta

KICKOFF = date(2026, 10, 5)
WEEKS = {number: KICKOFF + timedelta(days=7 * (number - 1)) for number in range(1, 7)}
REGISTRY_SCHEMA_V3 = WEEKS[2]
DPO_RESTRICTION = WEEKS[3]
BUREAU_INCIDENT = (WEEKS[4] - timedelta(days=7), WEEKS[4] - timedelta(days=1))
SCOPE_CHANGE = WEEKS[5]
OWNER_NAMED = WEEKS[6]
PILOT_DATE_ORIGINAL = date(2027, 6, 1)
PILOT_DATE_REQUESTED = date(2027, 2, 1)

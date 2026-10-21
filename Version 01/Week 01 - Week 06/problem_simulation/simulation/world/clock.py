"""Dates the generator and the corpus both use. Local events move with the profile."""

from __future__ import annotations

from datetime import date, timedelta

from simulation.config import active

_P = active()

SEED = _P.seed
SNAPSHOT = date(2026, 10, 1)
HISTORY_START = date(2018, 10, 1)
DETAIL_DAYS = 90
FLAG_LAG_DAYS = 45
REUSE_GAP_DAYS = 400

VENDOR_START = _P.shift("vendor_start", date(2024, 6, 1))
NCEC_ADOPT = _P.shift("ncec_adopt", date(2024, 4, 1))
HARBOUR_ADOPT = _P.shift("harbour_adopt", date(2025, 6, 1))
HILL_RECALL = _P.shift("hill_recall", date(2022, 1, 1))
OAKRIDGE_MEMO = _P.shift("oakridge_memo", date(2024, 9, 1))
OAKRIDGE_WITHDRAW = _P.shift("oakridge_withdraw", date(2024, 11, 15))
OUTAGE_START = _P.shift("outage", date(2024, 11, 1))
OUTAGE_END = _P.shift("outage", date(2024, 11, 21))
INCIDENT_START = _P.shift("incident", date(2025, 3, 3))
INCIDENT_END = _P.shift("incident", date(2025, 3, 10))
SCHEMA_CUTOVER = date(2022, 1, 1)
OLD_SNAPSHOT = date(2021, 12, 31)
MIXED_SNAPSHOT = date(2022, 3, 31)
STALE_FEED = date.fromisoformat(_P.stale_feed)
MONTHLY_FROM = date(2023, 10, 1)

FIRMWARE_MARKET = _P.shift("firmware", date(2023, 5, 10))
FIRMWARE_RIVER = _P.shift("firmware", date(2025, 2, 3))
BUREAU_MIGRATION_START = _P.shift("bureau_migration", date(2023, 6, 5))
BUREAU_MIGRATION_END = _P.shift("bureau_migration", date(2023, 9, 25))
ROTA_CHANGE = _P.shift("rota_change", date(2024, 3, 4))
REMINDER_CHANGE = _P.shift("reminder_change", date(2023, 1, 9))
AGENCY_START = date(2025, 1, 6)
MERGE_APPLIED = date(2023, 5, 15)
MERGE_REVERSED = date(2025, 2, 17)
LAB_UNIT_CHANGE = date(2021, 4, 1)
FINANCE_RECODE = date(2023, 4, 1)


def iso(value: date) -> str:
    return value.isoformat()


def parse(value: str) -> date:
    return date.fromisoformat(value)


def shift(value: date, days: int) -> date:
    return value + timedelta(days=days)


def month_ends(start: date, end: date) -> list[date]:
    """Last day of each month from start's month up to, not including, end's month."""
    year, month = start.year, start.month
    found: list[date] = []
    while date(year, month, 1) < end:
        if month == 12:
            nxt = date(year + 1, 1, 1)
        else:
            nxt = date(year, month + 1, 1)
        last = nxt - timedelta(days=1)
        if last < end:
            found.append(last)
        year, month = nxt.year, nxt.month
    return found


def cycle_starts() -> list[date]:
    return [date(year, 10, 1) for year in range(HISTORY_START.year, SNAPSHOT.year)]


def detail_start() -> date:
    return SNAPSHOT - timedelta(days=DETAIL_DAYS)

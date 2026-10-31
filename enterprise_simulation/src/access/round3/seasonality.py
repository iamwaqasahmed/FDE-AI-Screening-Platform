"""Monthly request volume for 2025-2026, plus the rare January 2026 events."""

from __future__ import annotations

import calendar
import random
from datetime import date

_JULY_ANCHOR = 360
_MONTH_LIFT = {
    1: 96,
    2: 72,
    3: 36,
    4: 12,
    5: 0,
    6: -18,
    7: 0,
    8: -12,
    9: 18,
    10: 42,
    11: 84,
    12: 120,
}
# January 2026 only. Keeps WA at least double July after jitter of +/- 3.
_SURGE_LIFT = 384
_JITTER = 3
_WINTER_MONTHS = frozenset({11, 12, 1, 2})
_BC_SHARE = 1 / 3
_BC_BAND = 0.03
_TIMEOUT_SHARE = 0.04
_TIMEOUT_BAND = 0.01
_VOLUME_LINK = 0.8
_BC_SATURDAY_FILES = 0
_SERIES_START = (2025, 1)
_SERIES_LENGTH = 24
_COUNT_FIELDS = ("bc_requests", "wa_requests", "timeouts", "saturday_files")

_REF = "R3B-SURGE"
_ARRIVED_AT = "2026-01-21T16:05:00Z"
_QUEUE_AT = "2026-01-17T23:40:00Z"
_COVER_AT = "2026-01-21T18:11:00Z"
_ARRIVALS = (
    ("cmd-r3b-arrive-a", "r3b-surge", 2, "p-r3b-4410", "206-555-4410"),
    ("cmd-r3b-arrive-b", "r3b-pair", 1, "p-r3b-4411", "206-555-4411"),
)


def monthly_volume(seed: int = 20270110) -> list[dict]:
    """Return 24 monthly rows from 2025-01 through 2026-12."""
    rng = random.Random(seed)
    return [_month_row(year, month, rng) for year, month in _month_pairs()]


def rare_commands() -> list[dict]:
    """Return the rare January 2026 events, not the monthly table."""
    rows = [_queue_note(), *_arrivals(), _coverage_timeout()]
    return sorted(rows, key=lambda row: (row["occurred_at"], row["command_id"]))


def check_assumptions(rows: list[dict]) -> list[str]:
    """Return problem strings. An empty list means the monthly assumptions hold."""
    problems = _check_shape(rows)
    if problems:
        return problems
    problems.extend(_check_winter(rows))
    problems.extend(_check_region_split(rows))
    problems.extend(_check_timeouts(rows))
    problems.extend(_check_saturdays(rows))
    problems.extend(_check_surge(rows))
    return problems


def _month_row(year: int, month: int, rng: random.Random) -> dict:
    total = _request_total(year, month, rng)
    bc_requests, wa_requests = _split_requests(total)
    return {
        "month": _label(year, month),
        "bc_requests": bc_requests,
        "wa_requests": wa_requests,
        "timeouts": _timeout_count(total, month),
        "saturday_files": _saturday_files(year, month),
    }


def _request_total(year: int, month: int, rng: random.Random) -> int:
    jitter = rng.randint(-_JITTER, _JITTER)
    return _JULY_ANCHOR + _lift(year, month) + jitter


def _lift(year: int, month: int) -> int:
    if year == 2026 and month == 1:
        return _SURGE_LIFT
    return _MONTH_LIFT[month]


def _split_requests(total: int) -> tuple[int, int]:
    bc_requests = (total + 1) // 3
    return bc_requests, total - bc_requests


def _timeout_count(total: int, month: int) -> int:
    counted = (total * 4 + 50) // 100
    if month in _WINTER_MONTHS and counted < 1:
        return 1
    return counted


def _saturday_files(year: int, month: int) -> int:
    return _saturday_nights(year, month) + _BC_SATURDAY_FILES


def _saturday_nights(year: int, month: int) -> int:
    _, days = calendar.monthrange(year, month)
    return sum(
        1
        for day in range(1, days + 1)
        if date(year, month, day).weekday() == calendar.SATURDAY
    )


def _queue_note() -> dict:
    return _command(
        "cmd-r3b-queue-open",
        "channel",
        "DeskNote",
        _QUEUE_AT,
        "r3b-surge",
        1,
        {
            "ref": _REF,
            "site": "cedar-ridge",
            "note": "The cedar night queue was still open at 23:40.",
        },
    )


def _arrivals() -> list[dict]:
    return [_arrival(*spec) for spec in _ARRIVALS]


def _arrival(
    command_id: str,
    stream_id: str,
    stream_rev: int,
    person_id: str,
    phone: str,
) -> dict:
    return _command(
        command_id,
        "channel",
        "RequestAccepted",
        _ARRIVED_AT,
        stream_id,
        stream_rev,
        {
            "ref": _REF,
            "person_id": person_id,
            "phone": phone,
            "member_region": "WA",
        },
    )


def _coverage_timeout() -> dict:
    return _command(
        "cmd-r3b-cover",
        "payer",
        "CoverageDecided",
        _COVER_AT,
        "r3b-surge",
        3,
        {
            "ref": _REF,
            "person_id": "p-r3b-4410",
            "answer": "timeout",
            "member_region": "WA",
            "currency": "USD",
        },
    )


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": stream_rev,
        "payload": payload,
    }


def _check_shape(rows: list[dict]) -> list[str]:
    if _labels(rows) != _expected_months():
        return ["expected 24 months from 2025-01 through 2026-12 in that order"]
    problems = []
    for row in rows:
        problems.extend(_bad_counts(row))
    return problems


def _labels(rows: list[dict]) -> tuple:
    labels = []
    for row in rows:
        if isinstance(row, dict):
            labels.append(row.get("month"))
        else:
            labels.append(None)
    return tuple(labels)


def _bad_counts(row: dict) -> list[str]:
    problems = []
    for field in _COUNT_FIELDS:
        value = row.get(field)
        if type(value) is not int or value < 0:
            problems.append(f"{row['month']} {field} must be a non-negative integer")
    return problems


def _check_winter(rows: list[dict]) -> list[str]:
    by_month = _by_month(rows)
    problems = []
    for year in (2025, 2026):
        july_label = f"{year}-07"
        july_total = _request_total_of(by_month[july_label])
        problems.extend(_winter_gaps(by_month, year, july_label, july_total))
    return problems


def _winter_gaps(
    by_month: dict[str, dict],
    year: int,
    july_label: str,
    july_total: int,
) -> list[str]:
    problems = []
    for month in (1, 2, 11, 12):
        label = f"{year}-{month:02d}"
        total = _request_total_of(by_month[label])
        if total <= july_total:
            problems.append(
                f"{label} has {total} requests, which is not more than "
                f"{july_label} ({july_total})"
            )
    return problems


def _check_region_split(rows: list[dict]) -> list[str]:
    problems = []
    for row in rows:
        problem = _split_problem(row)
        if problem:
            problems.append(problem)
    return problems


def _split_problem(row: dict) -> str | None:
    total = _request_total_of(row)
    label = row["month"]
    if total <= 0:
        return f"{label} has no requests to split between BC and WA"
    share = row["bc_requests"] / total
    if abs(share - _BC_SHARE) <= _BC_BAND and row["wa_requests"] > row["bc_requests"]:
        return None
    bc = row["bc_requests"]
    wa = row["wa_requests"]
    return (
        f"{label} splits {bc} BC and {wa} WA, not about one third for BC "
        "with WA as the rest"
    )


def _check_timeouts(rows: list[dict]) -> list[str]:
    problems = []
    totals = []
    counted = []
    for row in rows:
        problems.extend(_timeout_problems(row))
        total = _request_total_of(row)
        if total > 0:
            totals.append(total)
            counted.append(row["timeouts"])
    if totals and not _moves_with_volume(totals, counted):
        problems.append("timeouts do not move with request volume")
    return problems


def _timeout_problems(row: dict) -> list[str]:
    total = _request_total_of(row)
    label = row["month"]
    timeouts = row["timeouts"]
    problems = []
    if total > 0 and abs(timeouts / total - _TIMEOUT_SHARE) > _TIMEOUT_BAND:
        problems.append(
            f"{label} timeouts are {timeouts} of {total} requests, not about 4 percent"
        )
    if _is_winter(label) and timeouts <= 0:
        problems.append(f"{label} timeouts are 0 in a winter month")
    return problems


def _moves_with_volume(totals: list[int], timeouts: list[int]) -> bool:
    variance_total = _variance(totals)
    variance_timeout = _variance(timeouts)
    if variance_total == 0:
        return True
    if variance_timeout == 0:
        return False
    return _correlation(totals, timeouts) >= _VOLUME_LINK


def _variance(values: list[int]) -> float:
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values)


def _correlation(totals: list[int], timeouts: list[int]) -> float:
    mean_total = sum(totals) / len(totals)
    mean_timeout = sum(timeouts) / len(timeouts)
    covariance = sum(
        (total - mean_total) * (timeout - mean_timeout)
        for total, timeout in zip(totals, timeouts)
    )
    scale = _variance(totals) ** 0.5 * _variance(timeouts) ** 0.5
    return covariance / scale


def _check_saturdays(rows: list[dict]) -> list[str]:
    problems = []
    for row in rows:
        year, month = _year_month(row["month"])
        expected = _saturday_files(year, month)
        if row["saturday_files"] != expected:
            problems.append(
                f"{row['month']} saturday_files is {row['saturday_files']}, "
                f"expected {expected} cedar-ridge Saturday nights "
                "with BC Saturday files at 0"
            )
    return problems


def _check_surge(rows: list[dict]) -> list[str]:
    by_month = _by_month(rows)
    january = by_month["2026-01"]["wa_requests"]
    july = by_month["2026-07"]["wa_requests"]
    problems = []
    if january < 2 * july:
        problems.append(
            f"2026-01 wa_requests {january} is below double "
            f"2026-07 wa_requests {july}"
        )
    others = _other_surges(rows, july)
    if others:
        problems.append(
            "2026-01 is the only surge month, but "
            f"{', '.join(others)} also doubles 2026-07 wa_requests"
        )
    return problems


def _other_surges(rows: list[dict], july_wa: int) -> list[str]:
    return [
        row["month"]
        for row in rows
        if row["month"] != "2026-01" and row["wa_requests"] >= 2 * july_wa
    ]


def _month_pairs() -> tuple[tuple[int, int], ...]:
    pairs = []
    year, month = _SERIES_START
    for _ in range(_SERIES_LENGTH):
        pairs.append((year, month))
        year, month = _advance(year, month)
    return tuple(pairs)


def _advance(year: int, month: int) -> tuple[int, int]:
    if month == 12:
        return year + 1, 1
    return year, month + 1


def _expected_months() -> tuple[str, ...]:
    return tuple(_label(year, month) for year, month in _month_pairs())


def _label(year: int, month: int) -> str:
    return f"{year:04d}-{month:02d}"


def _year_month(label: str) -> tuple[int, int]:
    year_text, month_text = label.split("-")
    return int(year_text), int(month_text)


def _is_winter(label: str) -> bool:
    _, month = _year_month(label)
    return month in _WINTER_MONTHS


def _by_month(rows: list[dict]) -> dict[str, dict]:
    return {row["month"]: row for row in rows}


def _request_total_of(row: dict) -> int:
    return row["bc_requests"] + row["wa_requests"]

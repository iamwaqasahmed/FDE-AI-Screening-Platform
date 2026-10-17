"""Expected contact-centre calls by reason and month. Each reason is driven by the events that cause it."""

from __future__ import annotations

import pandas as pd

from simulation.care.referrals import CONSULTANT_GAP

CALLS_FROM = "2021-01"
REASONS = ("letter_not_received", "hospital_appointment", "results_query", "reschedule", "travel_and_parking", "other")


def _monthly(frame: pd.DataFrame, column: str, mask: pd.Series | None = None) -> pd.Series:
    rows = frame if mask is None else frame[mask]
    months = rows[column].str.slice(0, 7)
    return months[months.ne("")].value_counts()


def expected_calls(events: pd.DataFrame, invitations: pd.DataFrame, last_month: str) -> pd.DataFrame:
    """Rows of month, reason, expected calls. No noise: the research stage adds its own."""
    months = pd.period_range(CALLS_FROM, last_month, freq="M").strftime("%Y-%m")
    letters = _monthly(events, "letter_at")
    letter_breach = _monthly(events, "graded_at", events["breach"].eq("letter_bureau"))
    migration = _monthly(events, "graded_at", events["letter_in_migration"].astype(bool))
    duplicates = _monthly(events, "letter_at", events["letter_duplicate"].astype(bool))
    referrals = _monthly(events, "referred_at")
    booking = _monthly(events, "graded_at", events["breach"].eq("booking"))
    in_gap = events["referred_at"].between(CONSULTANT_GAP[0], CONSULTANT_GAP[1]) & events["referred_at"].ne("")
    gap_referrals = _monthly(events, "referred_at", in_gap)
    backlog = _monthly(events, "photo_date", events["breach"].eq("grader_backlog"))
    invited = _monthly(invitations, "planned_date")
    drivers = {
        "letter_not_received": ((0.04, letters), (0.4, letter_breach), (0.25, migration), (0.5, duplicates)),
        "hospital_appointment": ((0.1, referrals), (0.8, booking), (0.3, gap_referrals)),
        "results_query": ((0.3, backlog),),
        "reschedule": ((0.12, invited),),
        "travel_and_parking": ((0.05, invited),),
        "other": ((0.03, invited),),
    }
    rows = []
    for reason in REASONS:
        series = sum((weight * part.reindex(months).fillna(0.0) for weight, part in drivers[reason]), pd.Series(0.0, index=months))
        rows.extend({"month": month, "reason": reason, "expected": round(float(value), 2)} for month, value in series.items())
    return pd.DataFrame(rows)


def annual_calls_by_reason(calls: pd.DataFrame, from_month: str, to_month: str, years: int) -> dict[str, float]:
    window = calls[(calls["month"] >= from_month) & (calls["month"] < to_month)]
    return {reason: round(float(total) / years, 1) for reason, total in window.groupby("reason")["expected"].sum().items()}

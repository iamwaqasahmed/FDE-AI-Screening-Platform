"""The reminder change had no control group. True uplift comes from the behaviour layer; the naive estimate does not."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.world.clock import REMINDER_CHANGE

NAIVE_MONTHS = 12


def _shift_year(day: date, years: int) -> str:
    return date(day.year + years, day.month, day.day).isoformat()


def true_uplift(invitations: pd.DataFrame) -> dict[str, float]:
    """Mean of p_attend minus p_attend_no_reminder over invitations after the change that carried a reminder."""
    after = invitations[(invitations["planned_date"] >= REMINDER_CHANGE.isoformat()) & invitations["reminder"]]
    lift = (after["p_attend"] - after["p_attend_no_reminder"]).groupby(after["district"]).mean()
    return {district: round(float(value), 4) for district, value in sorted(lift.items())}


def naive_before_after(invitations: pd.DataFrame) -> dict[str, float]:
    """Attendance rate in the twelve months after the change minus the twelve months before, all invitations."""
    change = REMINDER_CHANGE.isoformat()
    day = invitations["planned_date"]
    before = invitations[(day >= _shift_year(REMINDER_CHANGE, -1)) & (day < change)]
    after = invitations[(day >= change) & (day < _shift_year(REMINDER_CHANGE, 1))]
    diff = after.groupby("district")["attended"].mean() - before.groupby("district")["attended"].mean()
    return {district: round(float(value), 4) for district, value in sorted(diff.items())}


def reminder_gold(invitations: pd.DataFrame) -> dict:
    true, naive = true_uplift(invitations), naive_before_after(invitations)
    districts = {
        district: {"true_uplift": true[district], "naive_before_after": naive[district],
                   "overstated_by": round(naive[district] - true[district], 4)}
        for district in true
    }
    return {
        "change_date": REMINDER_CHANGE.isoformat(),
        "true_definition": "mean(p_attend - p_attend_no_reminder) over invitations on or after the change with a reminder",
        "naive_definition": "attendance rate in the 12 months after minus the 12 months before, all invitations",
        "districts": districts,
        "overstated_districts": sorted(d for d, row in districts.items() if row["overstated_by"] > 0),
        "why": "Seasonality, the outreach trend, and the covid recovery all move attendance across the same dates",
    }


def attendance_by_month(invitations: pd.DataFrame) -> pd.DataFrame:
    month = invitations["planned_date"].str.slice(0, 7)
    grouped = invitations.groupby([month, invitations["district"]])["attended"].agg(["size", "sum"]).reset_index()
    grouped.columns = ["month", "district", "invited", "attended"]
    grouped["attendance_rate"] = (grouped["attended"] / grouped["invited"]).round(4)
    return grouped.sort_values(["month", "district"]).reset_index(drop=True)

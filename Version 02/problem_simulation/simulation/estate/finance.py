"""Finance ledger by financial year, cost centre, and line. Cost centres are renumbered at the 2023 recode."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.estate.common import TRUTH, log_fault
from simulation.faults import recode
from simulation.workforce.graders import ROSTER
from simulation.world.clock import FINANCE_RECODE, HISTORY_START, SNAPSHOT, VENDOR_START
from simulation.world.sites import RIVER_SITE

CENTRES = {
    "CC4100": "Screening grading",
    "CC4110": "Screening clinics",
    "CC4120": "Patient letters",
    "CC4125": "SMS contact",
    "CC4130": "Screening digital",
    "CC4140": "Outreach",
}
RECODE = {"CC4100": "SCR-210", "CC4110": "SCR-220", "CC4120": "SCR-230", "CC4125": "SCR-230", "CC4130": "DIG-410", "CC4140": "SCR-240"}
NEW_NAMES = {"SCR-210": "Screening grading", "SCR-220": "Screening clinics", "SCR-230": "Patient contact",
             "DIG-410": "Digital services - screening", "SCR-240": "Outreach"}
RATES = {"grader_hour": 24.0, "agency_hour": 48.0, "clinic_visit": 38.0, "letter": 0.92, "sms": 0.035,
         "vendor_score": 3.10, "outreach_visit": 55.0, "licence_year": 42_000.0}
COLUMNS = ["financial_year", "period_start", "cost_centre", "cost_centre_name", "line", "amount_gbp"]


def financial_year(day: str) -> str:
    year = int(day[:4]) - (1 if day[5:7] < "04" else 0)
    return f"{year}-{str(year + 1)[2:]}"


def build_finance(world: dict, sms: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    ledger = _ledger(world, sms)
    shown, entry = recode.apply(ledger, rng, {"column": "cost_centre", "mapping": RECODE, "date": "period_start",
                                              "from_on": FINANCE_RECODE, "names": NEW_NAMES, "name_column": "cost_centre_name"})
    log_fault(world, "finance", entry)
    for year, part in shown.groupby("financial_year", sort=True):
        world["files"][f"handover/finance/ledger-{year}.csv"] = part[COLUMNS].reset_index(drop=True)
    world["files"][f"{TRUTH}/finance_ledger.parquet"] = ledger
    world["files"][f"{TRUTH}/finance_recode.csv"] = pd.DataFrame(
        [{"old_code": old, "old_name": CENTRES[old], "new_code": new, "new_name": NEW_NAMES[new]} for old, new in RECODE.items()]
    )
    return ledger


def _ledger(world: dict, sms: pd.DataFrame) -> pd.DataFrame:
    events = world["events"]
    events = events[events["photo_date"] < SNAPSHOT.isoformat()]
    hours = world["grader_hours"]
    hours = hours[hours["day"].astype(str) < SNAPSHOT.isoformat()]
    agency = [grader.grader_id for grader in ROSTER if grader.agency]
    staff = [grader.grader_id for grader in ROSTER if not grader.agency]
    hour_year = hours["day"].astype(str).map(financial_year)
    lines = [
        _sum("CC4100", "Grader salaries", hour_year, hours[staff].sum(axis=1) * RATES["grader_hour"]),
        _sum("CC4100", "Agency graders", hour_year, hours[agency].sum(axis=1) * RATES["agency_hour"]),
        _count("CC4110", "Clinic sessions", events.loc[events["site"] != RIVER_SITE, "photo_date"], RATES["clinic_visit"]),
        _count("CC4120", "Letter bureau", events.loc[events["letter_at"] != "", "letter_at"], RATES["letter"]),
        _count("CC4125", "SMS gateway", sms["sent_at"].str[:10], RATES["sms"]),
        _count("CC4130", "Vendor scoring", events.loc[events["vendor_scored"], "photo_date"], RATES["vendor_score"]),
        _licences(),
        _count("CC4140", "Outreach visits", events.loc[events["site"] == RIVER_SITE, "photo_date"], RATES["outreach_visit"]),
    ]
    ledger = pd.concat(lines, ignore_index=True)
    ledger = ledger[ledger["amount_gbp"] > 0]
    ledger["cost_centre_name"] = ledger["cost_centre"].map(CENTRES)
    ledger["period_start"] = ledger["financial_year"].str[:4] + "-04-01"
    ledger["amount_gbp"] = ledger["amount_gbp"].round(2)
    return ledger.sort_values(["financial_year", "cost_centre", "line"]).reset_index(drop=True)[COLUMNS]


def _sum(centre: str, line: str, years: pd.Series, amounts: pd.Series) -> pd.DataFrame:
    total = amounts.groupby(years.to_numpy()).sum()
    return pd.DataFrame({"financial_year": total.index, "cost_centre": centre, "line": line, "amount_gbp": total.to_numpy()})


def _count(centre: str, line: str, days: pd.Series, rate: float) -> pd.DataFrame:
    if days.empty:
        return pd.DataFrame(columns=["financial_year", "cost_centre", "line", "amount_gbp"])
    counts = days.astype(str).map(financial_year).value_counts().sort_index()
    return pd.DataFrame({"financial_year": counts.index, "cost_centre": centre, "line": line, "amount_gbp": counts.to_numpy() * rate})


def _licences() -> pd.DataFrame:
    first = int(financial_year(HISTORY_START.isoformat())[:4])
    last = int(financial_year(SNAPSHOT.isoformat())[:4])
    years = [f"{year}-{str(year + 1)[2:]}" for year in range(first, last + 1)]
    pilot = financial_year(VENDOR_START.isoformat())
    amounts = [RATES["licence_year"] * (1.5 if year >= pilot else 1.0) for year in years]
    return pd.DataFrame({"financial_year": years, "cost_centre": "CC4130", "line": "Software licences", "amount_gbp": amounts})


def comparable_total(ledger: pd.DataFrame, new_code: str, year: str) -> float:
    olds = [old for old, new in RECODE.items() if new == new_code]
    part = ledger[(ledger["financial_year"] == year) & ledger["cost_centre"].isin(olds)]
    return round(float(part["amount_gbp"].sum()), 2)

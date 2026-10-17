"""Budget and actual lines by financial year. Cost centres were recoded in April 2023 and two lines merged."""

from __future__ import annotations

import pandas as pd

from simulation.economics.costs import cost
from simulation.world.clock import FINANCE_RECODE, HISTORY_START, SNAPSHOT

OLD_CENTRES = {
    "grading": ("4410", "Screening grading"),
    "agency": ("4410", "Screening grading"),
    "clinics": ("4420", "Screening clinics"),
    "outreach": ("4450", "Outreach service"),
    "letters": ("4430", "Result letters"),
    "sms": ("4440", "SMS gateway"),
    "pilot": ("4460", "Digital pilot"),
}
NEW_CENTRES = {
    "grading": ("SCR-210", "Grading (employed)"),
    "agency": ("SCR-215", "Grading (agency)"),
    "clinics": ("SCR-220", "Clinics and outreach"),
    "outreach": ("SCR-220", "Clinics and outreach"),
    "letters": ("SCR-230", "Patient communications"),
    "sms": ("SCR-230", "Patient communications"),
    "pilot": ("DIG-510", "AI pilot"),
}


def financial_year(day: str) -> str:
    year, month = int(day[:4]), int(day[5:7])
    start = year if month >= 4 else year - 1
    return f"{start}-{(start + 1) % 100:02d}"


def _line_costs(events: pd.DataFrame, invitations: pd.DataFrame) -> pd.DataFrame:
    frame = pd.DataFrame({"fy": events["photo_date"].map(financial_year)})
    agency = events["grader_id"].isin(["G11", "G12"])
    reads = events["grade"].ne("").astype(float) + events["second_grade"].ne("").astype(float)
    frame["grading"] = reads.where(~agency, 0.0) * cost("grader_read")
    frame["agency"] = reads.where(agency, 0.0) * cost("grader_read") * cost("agency_grader_hour") / cost("grader_hour")
    river = events["capture"].eq("outreach_laptop")
    frame["clinics"] = (~river).astype(float) * cost("screening_appointment")
    frame["outreach"] = river.astype(float) * cost("screening_appointment") * 1.6
    frame["letters"] = events["letter_at"].ne("") * cost("letter") + events["letter_duplicate"].astype(float) * cost("letter_reprint")
    frame["pilot"] = events["pilot"].astype(float) * cost("vendor_read_fee")
    lines = frame.groupby("fy").sum()
    sms = (invitations["sms"].astype(float) + invitations["reminder"].astype(float)) * cost("sms")
    lines["sms"] = sms.groupby(invitations["planned_date"].map(financial_year)).sum()
    return lines.fillna(0.0)


def budgets_frame(world: dict) -> pd.DataFrame:
    lines = _line_costs(world["events"], world["invitations"])
    recode_fy = financial_year(FINANCE_RECODE.isoformat())
    first, last = financial_year(HISTORY_START.isoformat()), financial_year(SNAPSHOT.isoformat())
    rows = []
    previous: dict[tuple[str, str], float] = {}
    for fy in sorted(lines.index):
        if not first <= fy <= last:
            continue
        centres = NEW_CENTRES if fy >= recode_fy else OLD_CENTRES
        grouped: dict[tuple[str, str], float] = {}
        for line, centre in centres.items():
            grouped[centre] = grouped.get(centre, 0.0) + float(lines.at[fy, line])
        basis = "year_to_date" if fy in (first, last) else "full_year"
        for (code, name), actual in sorted(grouped.items()):
            if actual <= 0:
                continue
            planned = previous.get((code, name), actual) if fy == last else actual
            rows.append({"financial_year": fy, "cost_centre": code, "cost_centre_name": name,
                         "budget_gbp": _budget(planned, fy), "actual_gbp": round(actual, 0), "actual_basis": basis})
        previous = grouped
    return pd.DataFrame(rows)


def _budget(amount: float, fy: str) -> float:
    squeeze = 0.97 if fy >= "2023-24" else 1.01
    return float(round(amount * squeeze / 100.0) * 100)


def cost_centre_map() -> pd.DataFrame:
    rows = [{"line": line, "old_code": OLD_CENTRES[line][0], "old_name": OLD_CENTRES[line][1],
             "new_code": NEW_CENTRES[line][0], "new_name": NEW_CENTRES[line][1], "recoded_on": FINANCE_RECODE.isoformat()}
            for line in OLD_CENTRES]
    return pd.DataFrame(rows)

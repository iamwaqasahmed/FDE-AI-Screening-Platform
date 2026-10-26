"""Leader pages for rel-w1d2. Figures are claims. Causes are not on the page."""

from __future__ import annotations


def register_page() -> str:
    """Return the opportunity register.

    Each row is a problem id and the symptom named for it. Causes stay off the page because the page is a list of claims.
    """
    rows = (
        ("p-bounce", "Referrals come back to the primary care center."),
        ("p-waitlist", "Waitlist rows the coordinators do not trust."),
        ("p-dna", "People miss the appointment they were given."),
        ("p-status", "The contact center is asked where a referral stands."),
        ("p-slots", "Sessions go out with empty chairs."),
        ("p-clock", "The board's wait chart."),
        ("p-info", "Patients call to ask for hours, preparation, and documents."),
        ("p-forecast", "Session plans miss the busy months."),
        ("p-triage", "The sponsor wants the assistant to set clinical urgency."),
    )
    body = "\n".join(f"| {problem_id} | {symptom} |" for problem_id, symptom in rows)
    return f"""# Opportunity register

Case date: 2027-01-11

These are the problems named in the extracts and the kickoff. The line is the symptom.

| id | symptom |
| --- | --- |
{body}
"""


def dashboard_page(median: int) -> str:
    return f"""# Wait chart

From: the BI lead
Case date: 2027-01-11

The board pack shows a median wait of {median} days.

| metric | value | date_column |
| --- | --- | --- |
| median_wait_days | {median} | booking_date |
"""


def vendor_page(chats: int) -> str:
    return f"""# Vendor note

From: the vendor account manager
Case date: 2027-01-11

Containment on the national contact-center pilot is 70 percent.
The pilot counted {chats} chats.
That pilot is not the Al-Waha Health Cluster.
"""


def access_page(noshow: int, returns: int, empty: int, calls: int) -> str:
    return f"""# Access cost note

From: the director of patient access
Case date: 2027-01-11

Ranked by the director, largest first.

| rank | item | sar |
| --- | --- | --- |
| 1 | no-shows | {noshow} |
| 2 | returned referrals | {returns} |
| 3 | empty sessions | {empty} |

Hours and documents: {calls} calls.
"""


def sponsor_page(impact: int) -> str:
    return f"""# Sponsor ask

From: the office of the Chief Digital and Transformation Officer
Case date: 2027-01-11

The virtual front desk, including triage, is the program.
Claimed impact: {impact} SAR a year.
"""


def claim_figures(seed: int) -> dict[str, int]:
    """Return the claimed figures for this seed.

    The leader pages read this mapping, so every figure on those pages stays tied to the same seed.
    """
    return {
        "median": 14 + (seed % 5),
        "chats": 600 + (seed % 90),
        "noshow": (900 + (seed % 100)) * 1000,
        "returns": (500 + (seed % 50)) * 1000,
        "empty": (200 + (seed % 40)) * 1000,
        "calls": 400 + (seed % 80),
        "impact": (3 + (seed % 5)) * 1000000,
    }

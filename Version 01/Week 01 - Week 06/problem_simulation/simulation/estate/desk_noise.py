"""Routine service requests that bury the few tickets that matter."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import HISTORY_START, SNAPSHOT

NOISE_TICKETS = 300
REQUESTS = (
    ("Password reset", "User locked out after three attempts. Reset and confirmed sign-in."),
    ("Printer not printing", "Clinic printer queue stuck. Cleared the queue and restarted the spooler."),
    ("New starter laptop", "Laptop built and handed over with standard image."),
    ("Mailbox full", "Archive policy applied and quota raised."),
    ("VPN slow from home", "Advised to reconnect to the nearest gateway. No fault found."),
    ("Access request", "Role requested by line manager. Approved and granted."),
    ("Monitor replacement", "Faulty monitor swapped at the desk."),
    ("Teams meeting audio", "Headset driver updated."),
    ("Shared drive permissions", "Folder permissions corrected for the team."),
    ("Software install", "Approved application installed from the catalogue."),
    ("Report not refreshing", "Dashboard refresh rescheduled after a timeout."),
    ("Phone handset fault", "Handset replaced at reception."),
)
SERVICES = ("Grader workbench", "Appointment booking", "Call-centre log", "Authority warehouse", "Identity provider",
            "Complaints system", "Finance ledger", "Letter bureau", "Desktop", "Email")


def noise_tickets(rng: np.random.Generator, count: int = NOISE_TICKETS) -> pd.DataFrame:
    first = pd.Timestamp(HISTORY_START).value // 60_000_000_000
    last = pd.Timestamp(SNAPSHOT).value // 60_000_000_000
    opened = pd.Series(np.sort(rng.integers(first, last - 7 * 1440, count)) * 60_000_000_000).astype("datetime64[ns]")
    picks = rng.integers(0, len(REQUESTS), count)
    return pd.DataFrame({
        "ticket_ref": [f"REQ-{index:04d}" for index in range(1, count + 1)],
        "type": "request",
        "service": rng.choice(np.array(SERVICES), count),
        "opened_at": opened,
        "resolved_at": opened + pd.to_timedelta(rng.integers(20, 4 * 1440, count), unit="min"),
        "status": "closed",
        "priority": rng.choice(np.array(["P4", "P3"]), count, p=[0.8, 0.2]),
        "site": "",
        "summary": [REQUESTS[pick][0] for pick in picks],
        "description": [REQUESTS[pick][1] for pick in picks],
        "assignee": "Service desk",
    })

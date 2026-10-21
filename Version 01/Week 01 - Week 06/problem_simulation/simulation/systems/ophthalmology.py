"""Ophthalmology referral messages, pipe-delimited. Booked and seen are often blank."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.systems.common import blank
from simulation.systems.mrn import MrnIndex
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso

PIPE_HEADER = "REF|mrn|local_pid|referred|booked|seen|grade"


def write_ophthalmology(events: pd.DataFrame, identifiers: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    referrals = events[events["referred_at"] != ""]
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    index = MrnIndex(identifiers)
    lines = [PIPE_HEADER]
    for row in referrals.itertuples(index=False):
        mrn = index.get(row.person_uid, row.site, row.photo_date)
        booked, seen = shown_referral(row)
        pid = blank(local_pid.get(row.person_uid, ""))
        grade = "" if row.grade_hidden else row.grade
        lines.append("|".join(["REF", mrn, pid, row.referred_at, booked, seen, grade]))
    (folder / "messages.pipe").write_text("\n".join(lines) + "\n", encoding="utf-8")


def shown_referral(row) -> tuple[str, str]:
    if int(row.event_id[1:]) % 2 == 0:
        return "", ""
    return row.booked_at, row.seen_at

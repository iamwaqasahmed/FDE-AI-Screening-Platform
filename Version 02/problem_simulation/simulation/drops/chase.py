"""The programme's chase list: every local id whose latest referral message has no seen date.

This is the list the programme office can see. It is wider than the people who are
actually overdue, because a blank seen date is not proof the visit never happened.
"""

from __future__ import annotations

import pandas as pd

from simulation.systems.mrn import MrnIndex
from simulation.systems.ophthalmology import shown_referral
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso


def chase_people(world: dict) -> pd.DataFrame:
    """One row per chased local id, with the person that row was written for."""
    messages = referral_messages(world)
    latest = messages.sort_values("referred").groupby("local_pid", as_index=False).tail(1)
    blank = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    return blank.sort_values("local_pid").reset_index(drop=True)


def referral_messages(world: dict) -> pd.DataFrame:
    events, identifiers = world["events"], world["identifiers"]
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    index = MrnIndex(identifiers)
    rows = []
    for row in events[events["referred_at"].ne("")].itertuples(index=False):
        _, seen = shown_referral(row)
        found = local_pid.get(row.person_uid, "")
        rows.append({
            "person_uid": row.person_uid,
            "site": row.site,
            "mrn": index.get(row.person_uid, row.site, row.photo_date),
            "local_pid": "" if found is None else str(found or ""),
            "referred": row.referred_at,
            "seen": seen,
        })
    return pd.DataFrame(rows)

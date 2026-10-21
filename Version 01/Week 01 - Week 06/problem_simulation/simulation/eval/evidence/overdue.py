"""The week-2 overdue upper bound, kept where the vendor file shows an allowed site."""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.cohorts import _filled_mrns
from simulation.eval.enterprise.drop import v3_frame
from simulation.systems.common import blank
from simulation.systems.grader import _frame
from simulation.systems.mrn import MrnIndex
from simulation.systems.ophthalmology import shown_referral
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, detail_start, iso


def count(world: dict, allowed: list[str]) -> dict:
    messages, book = _messages(world), _workbook(world)
    bound = pilot_bound(messages, _filled_mrns(world), v3_frame(world), book, _vendor(world), allowed)
    return {"upper_bound": bound, "is_upper_bound": True}


def pilot_bound(messages: pd.DataFrame, filled: set[str], registry: pd.DataFrame, book: pd.DataFrame,
                vendor: pd.DataFrame, allowed: list[str]) -> int:
    latest = messages.sort_values(["referred", "mrn", "local_pid"]).groupby("local_pid", as_index=False).tail(1)
    blank_rows = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    still = blank_rows[~blank_rows["mrn"].isin(filled)]
    flags = registry.set_index("LOCAL_PID")["FLAG"]
    gone = still["local_pid"].map(flags).isin(["DECEASED", "MOVED"])
    bound = set(still.loc[~gone, "local_pid"].astype(str))
    names = book.fillna("").drop_duplicates("FILE_NAME").set_index("FILE_NAME")["LOCAL_PID"].astype(str)
    scoped = vendor[vendor["site"].astype(str).isin(allowed)]
    linked = scoped["file_name"].astype(str).map(names).fillna("")
    return len(bound & set(linked[linked.ne("")]))


def _messages(world: dict) -> pd.DataFrame:
    events, identifiers = world["events"], world["identifiers"]
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    index = MrnIndex(identifiers)
    rows = []
    for row in events[events["referred_at"].ne("")].itertuples(index=False):
        _, seen = shown_referral(row)
        rows.append({
            "mrn": index.get(row.person_uid, row.site, row.photo_date),
            "local_pid": blank(local_pid.get(row.person_uid, "")),
            "referred": row.referred_at,
            "seen": seen,
        })
    return pd.DataFrame(rows)


def _workbook(world: dict) -> pd.DataFrame:
    events = world["events"]
    recent = iso(detail_start())
    queue = events[events["grade"].eq("") | events["graded_at"].ge(recent) | events["photo_date"].ge(recent)].copy()
    local_pid = ids_on(world["identifiers"], "local_pid", iso(SNAPSHOT))
    return _frame(queue, world["people"], local_pid)


def _vendor(world: dict) -> pd.DataFrame:
    from simulation.eval.evidence.rates import clean
    from simulation.ml.retrospective import handover_frame, scored_frame

    return clean(handover_frame(scored_frame(world["events"])))

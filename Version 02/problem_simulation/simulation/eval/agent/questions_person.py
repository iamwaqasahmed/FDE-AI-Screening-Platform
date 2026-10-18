"""Ten people from the chase list. A delivered letter is not a re-send."""

from __future__ import annotations

import pandas as pd

from simulation.drops.rules import PRIMARY_CARE_SITES
from simulation.eval.agent.bars import PERSON_QUESTIONS
from simulation.eval.agent.question import make
from simulation.eval.graph.cohort import _pilot_ids, binding


def cases(world: dict, chase: pd.DataFrame) -> list[dict]:
    scope = _pilot_ids(world, list(PRIMARY_CARE_SITES))
    frame = chase.dropna(subset=["request_id"]).copy()
    frame["local_clock"] = [binding(str(row.hospital), str(row.referred), str(row.mrn)).days is not None
                            for row in frame.itertuples(index=False)]
    frame["in_scope"] = frame["local_pid"].astype(str).isin(scope)
    return [_case(row, scope, index) for index, row in enumerate(_pick(frame))]


def _pick(frame: pd.DataFrame) -> list:
    chosen, seen = [], set()
    quotas = (("clock", 2), ("pilot", 1), ("seen", 1), ("deceased", 1), ("moved", 1), ("once", 2), ("twice", 2))
    for name, count in quotas:
        _take(chosen, seen, _stratum(frame, name), count)
    rest = frame[~frame["local_pid"].astype(str).isin(seen) & frame["in_bound"]].sort_values("local_pid")
    _take(chosen, seen, rest, PERSON_QUESTIONS - len(chosen))
    return chosen[:PERSON_QUESTIONS]


def _stratum(frame: pd.DataFrame, name: str) -> pd.DataFrame:
    lost = frame["status"].eq("lost")
    masks = {
        "clock": lost & frame["in_bound"] & frame["local_clock"],
        "pilot": lost & frame["in_scope"],
        "seen": lost & frame["seen"],
        "deceased": lost & frame["deceased"],
        "moved": lost & frame["moved"],
        "once": frame["status"].eq("once") & frame["in_bound"],
        "twice": frame["status"].eq("twice") & frame["in_bound"],
    }
    return frame[masks[name]].sort_values("local_pid")


def _take(chosen: list, seen: set, pool: pd.DataFrame, count: int) -> None:
    for row in pool.itertuples(index=False):
        if count <= 0 or len(chosen) >= PERSON_QUESTIONS:
            return
        if str(row.local_pid) in seen:
            continue
        chosen.append(row)
        seen.add(str(row.local_pid))
        count -= 1


def _case(row, scope: set[str], index: int) -> dict:
    clause = binding(str(row.hospital), str(row.referred), str(row.mrn))
    action, reason = _action(row)
    visit = [str(row.request_id), clause.document_id]
    if row.mrn:
        visit.append(str(row.mrn))
    expected = {
        "in_pilot_scope": str(row.local_pid) in scope,
        "copies": int(row.copies),
        "action": action,
        "reason": reason,
        "clause_id": clause.document_id,
    }
    question = (
        f"Local id {row.local_pid}. For the chase letter, report whether the person is in the pilot scope, "
        "how many copies were dispatched, the re-send action, the hold reason, and the clause in force."
    )
    keys = ("in_pilot_scope", "copies", "action", "reason", "clause_id")
    return make(f"person-{index:02d}", question, expected, "value", "person", keys, None, "multi_hop", visit, max_steps=8)


def _action(row) -> tuple[str, str]:
    if row.status != "lost":
        return "none", ""
    if bool(row.seen):
        return "hold", "seen"
    if bool(row.deceased):
        return "hold", "deceased"
    if bool(row.moved):
        return "hold", "moved"
    return "resend", ""

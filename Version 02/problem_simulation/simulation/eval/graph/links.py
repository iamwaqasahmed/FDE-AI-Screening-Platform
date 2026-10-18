"""Join the chase list to hospitals, flags, clinic letters, and dispatch copies."""

from __future__ import annotations

import pandas as pd

from simulation.drops.chase import chase_people, referral_messages
from simulation.eval.enterprise.drop import v3_frame
from simulation.eval.evidence.overdue import _filled_mrns
from simulation.systems.mrn import MrnIndex
from simulation.world.sites import HOSPITALS

HOSPITAL_NAMES = {site for sites in HOSPITALS.values() for site in sites}


def prepare(world: dict, reconciled: pd.DataFrame) -> dict:
    precise, ambiguous = _pacs(world)
    messages = referral_messages(world)
    precise = _fill_gaps(messages, precise)
    chase = _chase(world, reconciled, precise, _filled_mrns(world), _flags(world))
    return {
        "chase": chase,
        "reconciled": reconciled,
        "hospitals": sorted(set(precise.values())),
        "blank_mrn": int(messages["mrn"].eq("").sum()),
        "ambiguous": ambiguous,
    }


def _pacs(world: dict) -> tuple[dict[str, str], int]:
    events = world["events"]
    studies = events[events["capture"].eq("pacs")]
    index = MrnIndex(world["identifiers"])
    found: dict[str, set[str]] = {}
    for row in studies.itertuples(index=False):
        split = row.scenario == "split" and int(row.event_id[1:]) % 2 == 0
        mrn = index.get(row.person_uid, row.site, row.photo_date, prefer_split=split)
        if mrn:
            found.setdefault(mrn, set()).add(str(row.site))
    clean = {mrn: next(iter(sites)) for mrn, sites in found.items() if len(sites) == 1}
    return clean, sum(len(sites) > 1 for sites in found.values())


def _fill_gaps(messages: pd.DataFrame, precise: dict[str, str]) -> dict[str, str]:
    out = dict(precise)
    known = set(precise)
    for row in messages.itertuples(index=False):
        if row.mrn and row.mrn not in known and row.site in HOSPITAL_NAMES:
            out.setdefault(row.mrn, row.site)
    return out


def _flags(world: dict) -> pd.Series:
    registry = v3_frame(world).drop_duplicates("LOCAL_PID")
    return registry.set_index("LOCAL_PID")["FLAG"].astype(str)


def _chase(world: dict, reconciled: pd.DataFrame, hospitals: dict[str, str], filled: set[str], flags: pd.Series) -> pd.DataFrame:
    chase = chase_people(world)
    copies = reconciled[reconciled["template"].eq("referral-chase")][["local_pid", "request_id", "copies", "status", "person_uid"]]
    frame = chase.merge(copies, on="local_pid", how="left", suffixes=("", "_request"))
    frame["hospital"] = frame["mrn"].map(hospitals).fillna("")
    frame["seen"] = frame["mrn"].ne("") & frame["mrn"].isin(filled)
    flag = frame["local_pid"].map(flags).fillna("")
    frame["deceased"] = ~frame["seen"] & flag.eq("DECEASED")
    frame["moved"] = ~frame["seen"] & flag.eq("MOVED")
    frame["in_bound"] = ~frame["seen"] & ~frame["deceased"] & ~frame["moved"]
    return frame

"""The week 4 bureau run: chase letters to the overdue cohort plus invitations, with a retry loop that duplicates and loses."""

from __future__ import annotations

from datetime import timedelta

import pandas as pd

from simulation.delivery.cohort import overdue_people
from simulation.prose.compose import seeded
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso
from simulation.world.engagement import BUREAU_INCIDENT

LOOP_DAYS = (2, 3, 4)
DUPLICATE_CHANCE = 0.6
LOST_CHANCE = 0.08


def bureau_run(world: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Requests the authority sent, and dispatch rows the bureau returned. Seeded so any stage gets the same run."""
    rng = seeded("drop-week-4-bureau")
    requests = _requests(world, rng)
    rows = []
    for request in requests.itertuples(index=False):
        day = pd.Timestamp(request.requested_at).date()
        offset = (day - BUREAU_INCIDENT[0]).days
        looping = offset in LOOP_DAYS
        if looping and rng.random() < LOST_CHANCE:
            continue
        copies = 2 if looping and rng.random() < DUPLICATE_CHANCE else 1
        for _ in range(copies):
            rows.append({"request_id": request.request_id, "local_pid": request.local_pid, "template": request.template,
                         "dispatched_at": (day + timedelta(days=1)).isoformat(), "status": "dispatched"})
    dispatch = pd.DataFrame(rows).sort_values(["dispatched_at", "request_id"], kind="stable").reset_index(drop=True)
    dispatch.insert(0, "dispatch_id", [f"BD-{index + 1:06d}" for index in range(len(dispatch))])
    return requests, dispatch


def _requests(world: dict, rng) -> pd.DataFrame:
    local_pid = ids_on(world["identifiers"], "local_pid", iso(SNAPSHOT))
    overdue = overdue_people(world["events"], world["people"])["person_uid"]
    chase = [uid for uid in overdue if local_pid.get(uid, "")]
    base = world["people"][(world["people"]["alias_of"] == "") & (world["people"]["flag"] == "")]
    chased = set(chase)
    others = sorted(uid for uid in base["person_uid"] if local_pid.get(uid, "") and uid not in chased)
    invites = rng.sample(others, k=min(len(others), max(150, len(others) // 30)))
    rows = [(uid, "referral-chase") for uid in chase] + [(uid, "invitation") for uid in sorted(invites)]
    days = (BUREAU_INCIDENT[1] - BUREAU_INCIDENT[0]).days + 1
    frame = pd.DataFrame(
        [{"local_pid": local_pid[uid], "template": template,
          "requested_at": (BUREAU_INCIDENT[0] + timedelta(days=rng.randrange(days))).isoformat(), "person_uid": uid}
         for uid, template in rows]
    ).sort_values(["requested_at", "template", "local_pid"], kind="stable").reset_index(drop=True)
    frame.insert(0, "request_id", [f"LR-{day.replace('-', '')}-{index + 1:05d}" for index, day in enumerate(frame["requested_at"])])
    return frame


def bureau_gold(requests: pd.DataFrame, dispatch: pd.DataFrame) -> dict:
    sent = set(dispatch["request_id"])
    lost = requests[~requests["request_id"].isin(sent)]
    loop = [(BUREAU_INCIDENT[0] + timedelta(days=offset)).isoformat() for offset in LOOP_DAYS]
    return {
        "window": [BUREAU_INCIDENT[0].isoformat(), BUREAU_INCIDENT[1].isoformat()],
        "retry_loop_days": loop,
        "requests": int(len(requests)),
        "dispatch_rows": int(len(dispatch)),
        "unique_dispatched": int(len(sent)),
        "duplicate_rows": int(len(dispatch) - len(sent)),
        "lost": sorted(lost["request_id"]),
        "lost_count": int(len(lost)),
        "lost_chase": int((lost["template"] == "referral-chase").sum()),
    }

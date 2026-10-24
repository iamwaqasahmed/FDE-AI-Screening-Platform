"""Platform services: documents, identity, labels, clock, chaos, and the gateway."""

from __future__ import annotations

import json

from alwaha.serve.deploy import admit
from alwaha.serve.http_state import State
from alwaha.serve.iam import discovery, token
from alwaha.serve.mart import read as mart_read

PHI = {"national_id", "date_of_birth", "name", "phone"}
TOPICS = (
    "referral.submitted",
    "referral.decided",
    "appointment.booked",
    "appointment.cancelled",
    "session.cancelled",
    "message.receipt",
    "document.changed",
    "slot.held",
)


def dms_get(doc_id: str) -> tuple[int, dict]:
    if doc_id == "circ-ramadan-unauth":
        return 200, {"ok": True, "doc_id": doc_id, "status": "unauthorized", "audience": "public"}
    return 200, {"ok": True, "doc_id": doc_id, "status": "in_force", "audience": "staff"}


def dms_search(query: str) -> tuple[int, dict]:
    return 200, {"ok": True, "query": query, "hits": ["hours-cluster"]}


def dms_changes() -> tuple[int, dict]:
    return 200, {"ok": True, "events": [{"topic": "document.changed", "doc_id": "hours-cluster"}]}


def iam_token(actor: str) -> tuple[int, dict]:
    try:
        return 200, {"ok": True, **token(actor)}
    except KeyError:
        return 404, {"ok": False, "error": "unknown actor"}


def iam_discovery() -> tuple[int, dict]:
    return 200, discovery()


def annotate(state: State, body: dict) -> tuple[int, dict]:
    if state.label_budget < state.label_cost:
        return 402, {"ok": False, "error": "budget"}
    state.label_budget -= state.label_cost
    return 200, {
        "ok": True,
        "item_id": body.get("item_id"),
        "guideline": body.get("guideline", "ann-v2"),
        "label": "adjudicated",
        "delay_minutes": 5,
        "budget_left": state.label_budget,
    }


def registry() -> tuple[int, dict]:
    return 200, {"ok": True, "topics": [{"name": name, "version": 1} for name in TOPICS]}


def clock_get(state: State) -> tuple[int, dict]:
    return 200, {"ok": True, "at": state.clock}


def clock_post(state: State, body: dict) -> tuple[int, dict]:
    if "at" in body:
        at = state.set_clock(body["at"])
    else:
        at = state.move_clock(int(body.get("minutes", 0)))
    return 200, {"ok": True, "at": at}


def chaos(state: State, action: str) -> tuple[int, dict]:
    if action == "pod-kill":
        state.site_a_up = False
    elif action == "slow-eref":
        state.eref_slow = True
    elif action == "insure-outage":
        state.insure_down = True
    else:
        return 404, {"ok": False}
    return 200, {"ok": True, "action": action}


def gateway(state: State, body: dict) -> tuple[int, dict]:
    encoded = json.dumps(body, sort_keys=True)
    if body.get("phi") or any(key in body for key in PHI):
        state.breaches.append("phi")
        return 403, {"ok": False, "error": "residency"}
    if state.profile.canary() in encoded:
        state.canary_hits.append(state.profile.canary())
        return 403, {"ok": False, "error": "canary"}
    tokens = int(body.get("tokens", 1))
    hospital = body.get("hospital", "h-wadi")
    sar = round(tokens * state.price_per_token, 4)
    state.meter[hospital] = round(state.meter.get(hospital, 0) + sar, 4)
    return 200, {"ok": True, "tokens": tokens, "sar": sar}


def image(body: dict) -> tuple[int, dict]:
    status = admit(body.get("user", ""), body.get("log_line", ""), body.get("national_id", ""))
    return 200, {"ok": status == "accepted", "status": status}


def wait_mart(body: dict) -> tuple[int, dict]:
    return 200, {"ok": True, **mart_read(body.get("csv", "booking_date,wait_days\n2027-01-10,12"))}

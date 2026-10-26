"""Platform services: documents, identity, labels, clock, chaos, and the gateway.

dms_get() serves the unauthorized circular as public and every other document as in force for staff. Search and the change feed answer with the hours document. iam_token() turns an unknown actor into not found. annotate() refuses a label the budget cannot pay. clock_post() pins an absolute instant or moves by minutes. chaos() takes site-a down, marks referrals slow, or marks insurance down. gateway() refuses a phi field and a profile canary before it meters a call. image() reports admission in the payload. wait_mart() reads the supplied extract, or the sample extract when csv is omitted.
"""

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
    """Return the document status.

    The unauthorized circular is served as public. Every other id is in force for staff.
    """
    # This id is the unauthorized circular that is still filed as public.
    if doc_id == "circ-ramadan-unauth":
        return 200, {"ok": True, "doc_id": doc_id, "status": "unauthorized", "audience": "public"}
    return 200, {"ok": True, "doc_id": doc_id, "status": "in_force", "audience": "staff"}


def dms_search(query: str) -> tuple[int, dict]:
    """Return the search hits for the query.

    The hit list is the in-force hours document. The query is echoed and does not select a different hit.
    """
    return 200, {"ok": True, "query": query, "hits": ["hours-cluster"]}


def dms_changes() -> tuple[int, dict]:
    """Return the document-changed event for the hours document."""
    return 200, {"ok": True, "events": [{"topic": "document.changed", "doc_id": "hours-cluster"}]}


def iam_token(actor: str) -> tuple[int, dict]:
    """Return the actor token, or not found.

    token() raises KeyError for an actor outside the dev directory. That error becomes a not-found response.
    """
    try:
        return 200, {"ok": True, **token(actor)}
    except KeyError:
        # An actor outside the dev directory has no token.
        return 404, {"ok": False, "error": "unknown actor"}


def iam_discovery() -> tuple[int, dict]:
    """Return the dev identity discovery document."""
    return 200, discovery()


def annotate(state: State, body: dict) -> tuple[int, dict]:
    """Return the adjudicated label, or the budget refusal.

    The label is refused when the remaining budget cannot pay the cost, and the budget is left unchanged. Otherwise the cost is spent and the item is marked adjudicated.
    """
    # Refuse before spending, so a short budget does not go negative.
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
    """Return each topic name with its version."""
    return 200, {"ok": True, "topics": [{"name": name, "version": 1} for name in TOPICS]}


def clock_get(state: State) -> tuple[int, dict]:
    """Return the current case-clock instant."""
    return 200, {"ok": True, "at": state.clock}


def clock_post(state: State, body: dict) -> tuple[int, dict]:
    """Pin the case clock, or move it, and return the instant that stands.

    A body that includes at replaces the clock with that instant. Otherwise the clock moves by the given minutes, and a missing minutes field does not move it.
    """
    if "at" in body:
        # An absolute instant replaces the case clock.
        at = state.set_clock(body["at"])
    else:
        # No absolute instant: move by the given minutes. A missing field does not move the clock.
        at = state.move_clock(int(body.get("minutes", 0)))
    return 200, {"ok": True, "at": at}


def chaos(state: State, action: str) -> tuple[int, dict]:
    """Flip one chaos flag and return the action, or a missing response.

    pod-kill takes site-a down. slow-eref marks the referral path slow. insure-outage marks insurance down. Any other action changes nothing.
    """
    if action == "pod-kill":
        # Later holds for site-a are refused.
        state.site_a_up = False
    elif action == "slow-eref":
        # Later eref calls report the slow flag.
        state.eref_slow = True
    elif action == "insure-outage":
        # Later eligibility reads return the outage.
        state.insure_down = True
    else:
        # Unknown actions leave the flags as they are.
        return 404, {"ok": False}
    return 200, {"ok": True, "action": action}


def gateway(state: State, body: dict) -> tuple[int, dict]:
    """Return a refusal, or the metered call.

    A phi flag, or any key in PHI, is recorded as a breach and refused before a charge is added. The profile canary anywhere in the encoded body is recorded and refused the same way. Any other call adds the metered amount on that hospital and returns the token count with it.
    """
    encoded = json.dumps(body, sort_keys=True)
    # A phi flag or a PHI key is refused before the call is metered, and the breach is recorded.
    if body.get("phi") or any(key in body for key in PHI):
        state.breaches.append("phi")
        return 403, {"ok": False, "error": "residency"}
    # The encoded body is scanned so a watermark in a nested value is still seen.
    if state.profile.canary() in encoded:
        state.canary_hits.append(state.profile.canary())
        return 403, {"ok": False, "error": "canary"}
    tokens = int(body.get("tokens", 1))
    hospital = body.get("hospital", "h-wadi")
    sar = round(tokens * state.price_per_token, 4)
    state.meter[hospital] = round(state.meter.get(hospital, 0) + sar, 4)
    return 200, {"ok": True, "tokens": tokens, "sar": sar}


def image(body: dict) -> tuple[int, dict]:
    """Return the admission result.

    The HTTP status stays success for both outcomes. ok is true only when admission accepted the image, and the status field carries accepted or rejected.
    """
    status = admit(body.get("user", ""), body.get("log_line", ""), body.get("national_id", ""))
    # Rejection lives in the payload. The HTTP status stays success either way.
    return 200, {"ok": status == "accepted", "status": status}


def wait_mart(body: dict) -> tuple[int, dict]:
    """Return the wait-time read.

    When csv is omitted, the sample extract written in this call is the text that is read.
    """
    return 200, {"ok": True, **mart_read(body.get("csv", "booking_date,wait_days\n2027-01-10,12"))}

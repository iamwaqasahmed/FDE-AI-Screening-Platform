"""Hospital systems: HL7, FHIR holds, referrals, Ain, and national id."""

from __future__ import annotations

from alwaha.serve.ain import apply_file, book
from alwaha.serve.fhir import read as fhir_read
from alwaha.serve.hl7 import outcomes
from alwaha.serve.http_state import State
from alwaha.serve.hooks import keep

_HL7_FIELDS = {"kind", "sequence", "person_id"}
_HOLD_MINUTES = 15


def hl7(state: State, facility: str, body: dict) -> tuple[int, dict]:
    rows = body.get("messages", [])
    kept = [keep(row, _HL7_FIELDS)[0] for row in rows if isinstance(row, dict)]
    if not kept:
        return 400, {"ok": False, "error": "no messages"}
    file_order, sequence_order = outcomes(kept)
    return 200, {
        "ok": True,
        "facility": facility,
        "file_order": file_order,
        "sequence_order": sequence_order,
        "slow": state.eref_slow and facility == "eref",
    }


def fhir(body: dict) -> tuple[int, dict]:
    result = fhir_read(body, "clinic", "clinic_code")
    return (200 if result["ok"] else 400), result


def hold(state: State, body: dict) -> tuple[int, dict]:
    site = body.get("site", "site-b")
    if site == "site-a" and not state.site_a_up:
        return 503, {"ok": False, "error": "site-a down", "serving": "site-b"}
    hold_id = f"hold-{len(state.holds) + 1}"
    state.holds[hold_id] = {
        "slot": body.get("slot"),
        "person_id": body.get("person_id"),
        "expires": _plus(state.clock, _HOLD_MINUTES),
        "status": "held",
    }
    return 200, {"ok": True, "hold_id": hold_id, "ttl_minutes": _HOLD_MINUTES}


def referral(state: State, referral_id: str, audience: str) -> tuple[int, dict]:
    status = state.pending_referrals.get(referral_id)
    if status is None:
        return 404, {"ok": False}
    if audience == "patient" and status == "pending":
        return 200, {"ok": True, "status": "hidden"}
    return 200, {"ok": True, "status": status}


def webhook(state: State, body: dict) -> tuple[int, dict]:
    kept, ignored = keep(body, {"event", "referral_id"})
    state.webhooks.append(kept)
    return 200, {"ok": True, "ignored": ignored}


def ain_book(body: dict) -> tuple[int, dict]:
    status = book(body.get("facility", ""), body.get("fault", ""))
    return 200, {"ok": True, "status": status}


def ain_file(state: State, body: dict) -> tuple[int, dict]:
    state.ain_file = apply_file(state.ain_file, body)
    return 200, {"ok": True, "current": state.ain_file}


def nid_proof(body: dict) -> tuple[int, dict]:
    if body.get("calls", 1) > 3:
        return 429, {"ok": False, "error": "rate limit"}
    return 200, {"ok": True, "lag": bool(body.get("visitor_number") or body.get("died_on"))}


def _plus(clock: str, minutes: int) -> str:
    from alwaha.serve.clock import advance

    return advance(clock, minutes)

"""Partner systems: messages, consent, insurance, HR, and the contact center."""

from __future__ import annotations

from alwaha.serve.http_state import State
from alwaha.serve.receipt import due
from alwaha.serve.sms import send

_RECEIPT_MINUTES = 5


def sms(state: State, body: dict) -> tuple[int, dict]:
    result = send(body.get("booking_id", ""), body.get("faults", {}))
    state.sent.append({"channel": "sms", "booking_id": body.get("booking_id")})
    receipt = due(state.clock, state.clock, _RECEIPT_MINUTES, switch_on=not result["ok"])
    return 200, {"ok": result["ok"], "receipt": receipt, "duplicate": body.get("duplicate", False)}


def whatsapp(state: State, body: dict) -> tuple[int, dict]:
    if not body.get("template_id"):
        return 400, {"ok": False, "error": "template required"}
    if body.get("window_open") is False:
        return 409, {"ok": False, "error": "session window closed"}
    state.sent.append({"channel": "wa", "template_id": body["template_id"]})
    return 200, {"ok": True}


def handoff(body: dict) -> tuple[int, dict]:
    summary = body.get("summary", "")
    if not summary:
        return 400, {"ok": False, "error": "summary required"}
    return 200, {"ok": True, "agent_id": "cc-agent-1", "summary": summary}


def consent(state: State, actor: str) -> tuple[int, dict]:
    expired = actor == "caregiver-expired"
    if expired and state.stale_consent:
        return 200, {"ok": True, "active": True, "stale": True, "scope": "book"}
    if expired:
        return 200, {"ok": True, "active": False, "stale": False}
    return 200, {"ok": True, "active": True, "stale": False, "scope": "view"}


def insure(state: State, body: dict) -> tuple[int, dict]:
    if state.insure_down:
        return 503, {"ok": False, "error": "insure down"}
    return 200, {
        "ok": True,
        "class": body.get("class", "active"),
        "as_of": state.clock,
        "stale_hours": 48 if body.get("snapshot") == "old" else 0,
    }


def leave(body: dict) -> tuple[int, dict]:
    return 200, {
        "ok": True,
        "clinician_id": body.get("clinician_id", "h-wadi-endo"),
        "recorded_after_publish": True,
    }

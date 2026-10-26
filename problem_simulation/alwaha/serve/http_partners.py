"""Partner systems: messages, consent, insurance, HR, and the contact center.

sms() records the send and judges the receipt, turning the late switch on when the send failed. whatsapp() requires a template and refuses an explicitly closed session window. handoff() requires a summary. consent() still serves the expired caregiver while the stale cache is on. insure() returns the outage while insurance is down, and reports a stale age for an old snapshot. leave() reports that leave was recorded after the session was published.
"""

from __future__ import annotations

from alwaha.serve.http_state import State
from alwaha.serve.receipt import due
from alwaha.serve.sms import send

_RECEIPT_MINUTES = 5


def sms(state: State, body: dict) -> tuple[int, dict]:
    """Return the send result, the receipt state, and the duplicate flag.

    The send is recorded before the receipt is judged. Sent time and now are both the case clock. The late switch is on when the send failed.
    """
    result = send(body.get("booking_id", ""), body.get("faults", {}))
    state.sent.append({"channel": "sms", "booking_id": body.get("booking_id")})
    # A failed send turns the late switch on. Sent time and now are the same case clock.
    receipt = due(state.clock, state.clock, _RECEIPT_MINUTES, switch_on=not result["ok"])
    return 200, {"ok": result["ok"], "receipt": receipt, "duplicate": body.get("duplicate", False)}


def whatsapp(state: State, body: dict) -> tuple[int, dict]:
    """Return a template error, a closed-window error, or a recorded send.

    A missing template is a client error. The session window is closed only when window_open is explicitly false, so a missing flag is still an open window.
    """
    if not body.get("template_id"):
        # A template message needs a template id.
        return 400, {"ok": False, "error": "template required"}
    # A missing window_open is still open. Only an explicit false closes the window.
    if body.get("window_open") is False:
        return 409, {"ok": False, "error": "session window closed"}
    state.sent.append({"channel": "wa", "template_id": body["template_id"]})
    return 200, {"ok": True}


def handoff(body: dict) -> tuple[int, dict]:
    """Return the handoff, or a client error when the summary is empty.

    An empty summary is rejected. A present summary is returned with the contact-center agent id.
    """
    summary = body.get("summary", "")
    # There is nothing to hand off without a summary.
    if not summary:
        return 400, {"ok": False, "error": "summary required"}
    return 200, {"ok": True, "agent_id": "cc-agent-1", "summary": summary}


def consent(state: State, actor: str) -> tuple[int, dict]:
    """Return the grant this actor receives.

    The expired caregiver stays active, stale, and scoped to book while the stale-consent cache is on. With that cache off, the same actor is inactive. Every other actor receives an active view grant.
    """
    expired = actor == "caregiver-expired"
    # The stale cache still serves the expired caregiver grant, and that grant can book.
    if expired and state.stale_consent:
        return 200, {"ok": True, "active": True, "stale": True, "scope": "book"}
    # With the cache off, the expired caregiver grant is inactive.
    if expired:
        return 200, {"ok": True, "active": False, "stale": False}
    return 200, {"ok": True, "active": True, "stale": False, "scope": "view"}


def insure(state: State, body: dict) -> tuple[int, dict]:
    """Return eligibility, or the outage.

    While insurance is down the response is the outage. Otherwise the class and the case clock are returned, and an old snapshot carries the stale age.
    """
    if state.insure_down:
        # The chaos outage fails the eligibility read.
        return 503, {"ok": False, "error": "insure down"}
    return 200, {
        "ok": True,
        "class": body.get("class", "active"),
        "as_of": state.clock,
        # An old snapshot carries the stale age. Any other snapshot is fresh.
        "stale_hours": 48 if body.get("snapshot") == "old" else 0,
    }


def leave(body: dict) -> tuple[int, dict]:
    """Return the leave record.

    recorded_after_publish stays true: the leave is recorded after the session is published. A missing clinician id uses the default in the response.
    """
    return 200, {
        "ok": True,
        "clinician_id": body.get("clinician_id", "h-wadi-endo"),
        "recorded_after_publish": True,
    }

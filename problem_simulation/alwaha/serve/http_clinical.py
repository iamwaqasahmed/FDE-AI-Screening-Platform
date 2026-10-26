"""Hospital systems: HL7, FHIR holds, referrals, Ain, and national id.

hl7() keeps contracted message fields, rejects an empty batch, and returns both standing sequences plus the eref slow flag. fhir() maps the read result onto an HTTP status. hold() refuses site-a while that site is down and otherwise stores a hold on the case clock. referral() hides a pending referral from a patient. webhook() stores only the contracted fields. ain_book() and ain_file() delegate to the Ain reference. nid_proof() rate-limits repeated calls and reports lag when a visitor number or a death date is present.
"""

from __future__ import annotations

from alwaha.serve.ain import apply_file, book
from alwaha.serve.fhir import read as fhir_read
from alwaha.serve.hl7 import outcomes
from alwaha.serve.http_state import State
from alwaha.serve.hooks import keep

_HL7_FIELDS = {"kind", "sequence", "person_id"}
_HOLD_MINUTES = 15


def hl7(state: State, facility: str, body: dict) -> tuple[int, dict]:
    """Return the HTTP status and the HL7 outcome.

    Rows that are not objects are dropped, and each remaining row keeps only the contracted fields. An empty batch is a client error, because no SIU row is left whose sequence could stand. The slow flag is true only when the eref chaos switch is on and this facility is eref.
    """
    rows = body.get("messages", [])
    kept = [keep(row, _HL7_FIELDS)[0] for row in rows if isinstance(row, dict)]
    # An empty batch has no sequence to stand, so it is a client error rather than an index failure.
    if not kept:
        return 400, {"ok": False, "error": "no messages"}
    file_order, sequence_order = outcomes(kept)
    return 200, {
        "ok": True,
        "facility": facility,
        "file_order": file_order,
        "sequence_order": sequence_order,
        # The slow switch is reported only for the eref facility.
        "slow": state.eref_slow and facility == "eref",
    }


def fhir(body: dict) -> tuple[int, dict]:
    """Return the HTTP status and the read result.

    Success follows the read. A failed read, including a body that still carries the removed field, is a client error.
    """
    result = fhir_read(body, "clinic", "clinic_code")
    # The HTTP status follows the read, so a failed read is a client error.
    return (200 if result["ok"] else 400), result


def hold(state: State, body: dict) -> tuple[int, dict]:
    """Return a new hold, or the site-a outage.

    A hold for site-a is refused while that site is down, and the body names site-b as the site still serving. A missing site defaults to site-b, so it does not take the outage path. Any other hold is stored with an expiry on the case clock.
    """
    site = body.get("site", "site-b")
    # A down site-a refuses the hold. A missing site stays on site-b and is still served.
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
    """Return the referral status for this audience.

    An unknown id is a missing response. A patient asking about a pending referral receives hidden. Every other audience receives the stored status.
    """
    status = state.pending_referrals.get(referral_id)
    # Unknown referral ids are missing. They are not reported as hidden.
    if status is None:
        return 404, {"ok": False}
    # A patient audience receives hidden for a pending referral. Other audiences receive the stored status.
    if audience == "patient" and status == "pending":
        return 200, {"ok": True, "status": "hidden"}
    return 200, {"ok": True, "status": status}


def webhook(state: State, body: dict) -> tuple[int, dict]:
    """Store the contracted webhook fields and return the ignored names.

    Fields outside the contract are dropped from the stored event and listed in the response.
    """
    kept, ignored = keep(body, {"event", "referral_id"})
    state.webhooks.append(kept)
    return 200, {"ok": True, "ignored": ignored}


def ain_book(body: dict) -> tuple[int, dict]:
    """Return the Ain book status for the facility and fault in the body.

    The status is whatever book() returns. This handler wraps that status in a success response.
    """
    status = book(body.get("facility", ""), body.get("fault", ""))
    return 200, {"ok": True, "status": status}


def ain_file(state: State, body: dict) -> tuple[int, dict]:
    """Store the Ain night file and return the file that stands.

    A null body keeps the previous file. Any object body replaces it. The handler wraps the result in a success response.
    """
    state.ain_file = apply_file(state.ain_file, body)
    return 200, {"ok": True, "current": state.ain_file}


def nid_proof(body: dict) -> tuple[int, dict]:
    """Return a proof result, or the rate limit.

    A missing calls field counts as a single call, so it stays under the limit. More calls than the comparison allows is a rate-limit response. lag is true when a visitor number or a death date is present.
    """
    # A missing calls field is one call, so it is still under the limit.
    if body.get("calls", 1) > 3:
        return 429, {"ok": False, "error": "rate limit"}
    # Either a visitor number or a death date means the identity record is lagging.
    return 200, {"ok": True, "lag": bool(body.get("visitor_number") or body.get("died_on"))}


def _plus(clock: str, minutes: int) -> str:
    """Return the case clock plus the given minutes.

    The hold expiry is an instant on the case clock, not wall time.
    """
    from alwaha.serve.clock import advance

    return advance(clock, minutes)

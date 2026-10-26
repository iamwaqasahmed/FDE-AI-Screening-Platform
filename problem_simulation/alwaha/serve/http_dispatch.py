"""Route table for the stateful mocks.

dispatch() returns the first matching status and payload. The path and the method select the handler. A missing referral audience is staff, so a pending referral stays visible until the caller asks as a patient. The leave route is a GET, so the query string is the record that handler reads. An unmatched path is a missing response.
"""

from __future__ import annotations

from alwaha.serve.http_clinical import ain_book, ain_file, fhir, hl7, hold, nid_proof, referral, webhook
from alwaha.serve.http_mcp import cluster, maps
from alwaha.serve.http_partners import consent, handoff, insure, leave, sms, whatsapp
from alwaha.serve.http_platform import (
    annotate,
    chaos,
    clock_get,
    clock_post,
    dms_changes,
    dms_get,
    dms_search,
    gateway,
    iam_discovery,
    iam_token,
    image,
    registry,
    wait_mart,
)
from alwaha.serve.http_state import State


def dispatch(state: State, method: str, path: str, body: dict, query: dict) -> tuple[int, dict]:
    """Return the HTTP status and JSON body for this request.

    The first matching route wins. Handlers receive the shared state, the body, and the query. An unmatched method or path returns a missing response.
    """
    if method == "GET" and path == "/health":
        return 200, {"ok": True, "profile": state.profile.name}
    if method == "POST" and path in {"/his/nakhl/hl7", "/his/safra/hl7"}:
        return hl7(state, path.split("/")[2], body)
    if method == "POST" and path == "/his/wadi/fhir":
        return fhir(body)
    if method == "POST" and path == "/his/wadi/holds":
        return hold(state, body)
    if method == "GET" and path.startswith("/eref/referrals/"):
        # A missing audience is staff, so pending stays visible unless the caller asks as a patient.
        return referral(state, path.rsplit("/", 1)[-1], query.get("audience", "staff"))
    if method == "POST" and path == "/eref/webhooks":
        return webhook(state, body)
    if method == "POST" and path == "/sched-ain/book":
        return ain_book(body)
    if method == "POST" and path == "/sched-ain/file":
        return ain_file(state, body)
    if method == "POST" and path == "/nid/proof":
        return nid_proof(body)
    if method == "POST" and path == "/sms/send":
        return sms(state, body)
    if method == "POST" and path == "/wa/send":
        return whatsapp(state, body)
    if method == "POST" and path == "/cc/handoff":
        return handoff(body)
    if method == "GET" and path == "/consent/grants":
        return consent(state, query.get("actor", ""))
    if method == "POST" and path == "/insure/eligibility":
        return insure(state, body)
    if method == "GET" and path == "/hr/leave":
        # GET has no JSON body, so the query string is what the leave handler reads.
        return leave(query)
    if method == "GET" and path.startswith("/dms/documents/"):
        return dms_get(path.rsplit("/", 1)[-1])
    if method == "GET" and path == "/dms/search":
        return dms_search(query.get("q", ""))
    if method == "GET" and path == "/dms/changes":
        return dms_changes()
    if method == "POST" and path == "/iam/token":
        return iam_token(body.get("actor", ""))
    if method == "GET" and path == "/iam/discovery":
        return iam_discovery()
    if method == "POST" and path == "/annotation/label":
        return annotate(state, body)
    if method == "GET" and path == "/registry/topics":
        return registry()
    if method == "GET" and path == "/clock":
        return clock_get(state)
    if method == "POST" and path == "/clock":
        return clock_post(state, body)
    if method == "POST" and path.startswith("/chaos/"):
        # The last path segment is the chaos action.
        return chaos(state, path.rsplit("/", 1)[-1])
    if method == "POST" and path == "/gateway/complete":
        return gateway(state, body)
    if method == "POST" and path == "/deploy/admit":
        return image(body)
    if method == "POST" and path == "/bi/read":
        return wait_mart(body)
    if method == "POST" and path == "/mcp/cluster":
        return cluster(state, body)
    if method == "POST" and path == "/mcp/maps":
        return maps(body)
    # No route matched.
    return 404, {"ok": False, "error": "missing"}

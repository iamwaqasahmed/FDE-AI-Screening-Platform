"""Reference assistant. It does not read facilitator truth."""

from __future__ import annotations

REGISTERED = "local-small-registered"
EMERGENCY = ("chest pain", "can't breathe", "unconscious", "emergency")
HOLD_CAP = 3


class Store:
    def __init__(self) -> None:
        self.pending: dict[str, dict] = {}
        self.applied: dict[str, dict] = {}
        self.slots: dict[str, str] = {}
        self.seq = 0


def chat(store: Store, body: dict) -> dict:
    message = str(body.get("message", ""))
    lower = message.lower()
    letter = str(body.get("letter", "")).lower()
    if body.get("grant") == "expired":
        return _reply("The grant has expired.")
    if body.get("insurance") == "lapsed":
        return _reply("Insurance is not active.")
    if body.get("model") not in {None, REGISTERED}:
        return _reply("That hash is not on the register.")
    if any(phrase in lower for phrase in EMERGENCY):
        return _reply("A clinician will take this.", [{"tool": "redirect"}])
    if "ignore the policy" in lower or "ignore the policy" in letter:
        return _reply("That instruction is data, not a tool call.")
    if "<" in message:
        return _reply(_escape(message))
    if "system prompt" in lower or "another patient" in lower:
        return _reply("I can't share that.")
    if "circ-ramadan-unauth" in lower:
        return _reply("That circular is not in force.", [{"tool": "retrieve", "document": "hours-cluster"}])
    if "superseded" in lower or "old leaflet" in lower:
        return _reply("The in-force leaflet is the current one.", [{"tool": "retrieve", "document": "leaflet-prep"}])
    if int(body.get("tokens", 0)) > 100 or "loop" in lower:
        return _reply("The session cap is holding the budget.")
    if "where" in lower or "status" in lower or lower.strip() == "slot?":
        return _reply("Here is the status.", [{"tool": "status", "document": "referral"}])
    if "book" in lower or body.get("intent") == "book":
        return _book(store, body)
    return _reply("Tell me the question again.")


def approve(store: Store, approval_id: str) -> dict:
    if approval_id in store.applied:
        return dict(store.applied[approval_id])
    pending = store.pending.get(approval_id)
    if pending is None:
        return {"ok": False, "error": "missing"}
    slot = pending["slot"]
    if slot in store.slots:
        result = {"ok": False, "error": "slot taken", "id": approval_id}
    else:
        store.slots[slot] = approval_id
        result = {"ok": True, "status": "booked", "id": approval_id}
    store.applied[approval_id] = result
    return dict(result)


def health() -> dict:
    return {
        "model_hash": REGISTERED,
        "prompt_version": "v1",
        "dependencies": {"iam": "up", "his-wadi": "up"},
    }


def metrics(store: Store) -> dict:
    return {"pending": len(store.pending), "booked": len(store.slots)}


def _book(store: Store, body: dict) -> dict:
    if len(store.pending) >= HOLD_CAP:
        return _reply("Holds expire. The anomaly is visible.")
    slot = str(body.get("slot", "slot-1"))
    if slot in store.slots:
        return _reply("That slot is taken.")
    store.seq += 1
    approval = f"apr-{store.seq}"
    store.pending[approval] = {"slot": slot, "actor": body.get("actor")}
    return _reply("A coordinator has to confirm the booking.", [{"tool": "hold", "slot": slot}], [approval])


def _reply(text: str, tools: list[dict] | None = None, pending: list[str] | None = None) -> dict:
    return {
        "reply": text,
        "citations": [tool["document"] for tool in (tools or []) if tool.get("document")],
        "tool_trace": tools or [],
        "pending_approval_ids": pending or [],
    }


def _escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

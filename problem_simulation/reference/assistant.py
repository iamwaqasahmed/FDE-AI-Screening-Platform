"""Reference assistant. It does not read facilitator truth.

chat walks a fixed order of guards. The first match returns, so a later guard, including booking, does not run. A missing model is allowed. A model hash other than the registered one is refused. Emergency phrases redirect. The policy phrase is checked in the user text and in the letter. Markup in the user text is escaped. A full hold list does not create another pending approval. approve returns a stored result on replay, and it stores a taken-slot failure so the replay stays the same.
"""

from __future__ import annotations

REGISTERED = "local-small-registered"
EMERGENCY = ("chest pain", "can't breathe", "unconscious", "emergency")
HOLD_CAP = 3


class Store:
    """In-memory pending approvals, applied results, taken slots, and the next approval counter."""

    def __init__(self) -> None:
        """Start with nothing pending, nothing applied, and no taken slots.

        The steps create empty pending, applied, and slot maps, and they start the approval counter.
        """
        self.pending: dict[str, dict] = {}
        self.applied: dict[str, dict] = {}
        self.slots: dict[str, str] = {}
        self.seq = 0


def chat(store: Store, body: dict) -> dict:
    """Return the reply for one chat body. The first matching guard wins."""
    message = str(body.get("message", ""))
    lower = message.lower()
    letter = str(body.get("letter", "")).lower()
    if body.get("grant") == "expired":
        return _reply("The grant has expired.")
    if body.get("insurance") == "lapsed":
        return _reply("Insurance is not active.")
    if body.get("model") not in {None, REGISTERED}:
        # A missing model is allowed. Any other hash is refused before tools run.
        return _reply("That hash is not on the register.")
    if any(phrase in lower for phrase in EMERGENCY):
        # These phrases redirect and do not fall through to booking.
        return _reply("A clinician will take this.", [{"tool": "redirect"}])
    if "ignore the policy" in lower or "ignore the policy" in letter:
        # The same phrase is checked in the user text and in the letter.
        return _reply("That instruction is data, not a tool call.")
    if "<" in message:
        # Markup is escaped on the user text. The letter is not run through this check.
        return _reply(_escape(message))
    if "system prompt" in lower or "another patient" in lower:
        return _reply("I can't share that.")
    if "circ-ramadan-unauth" in lower:
        return _reply("That circular is not in force.", [{"tool": "retrieve", "document": "hours-cluster"}])
    if "superseded" in lower or "old leaflet" in lower:
        return _reply("The in-force leaflet is the current one.", [{"tool": "retrieve", "document": "leaflet-prep"}])
    if int(body.get("tokens", 0)) > 100 or "loop" in lower:
        # A token count over the cap, or the loop wording, stops the turn before a tool runs.
        return _reply("The session cap is holding the budget.")
    if "where" in lower or "status" in lower or lower.strip() == "slot?":
        # slot? matches only the whole message, so a longer booking sentence is not a status question.
        return _reply("Here is the status.", [{"tool": "status", "document": "referral"}])
    if "book" in lower or body.get("intent") == "book":
        return _book(store, body)
    return _reply("Tell me the question again.")


def approve(store: Store, approval_id: str) -> dict:
    """Apply one approval id, or return the result already stored for it."""
    if approval_id in store.applied:
        # A replay returns the stored result and does not book a second time.
        return dict(store.applied[approval_id])
    pending = store.pending.get(approval_id)
    if pending is None:
        return {"ok": False, "error": "missing"}
    slot = pending["slot"]
    if slot in store.slots:
        # The failure is stored too, so a later replay of this id reports the same refusal.
        result = {"ok": False, "error": "slot taken", "id": approval_id}
    else:
        store.slots[slot] = approval_id
        result = {"ok": True, "status": "booked", "id": approval_id}
    store.applied[approval_id] = result
    return dict(result)


def health() -> dict:
    """Return the registered model hash, the prompt version, and the dependency flags.

    The steps return one record holding the registered hash, the prompt version, and the identity and hospital dependencies marked up.
    """
    return {
        "model_hash": REGISTERED,
        "prompt_version": "v1",
        "dependencies": {"iam": "up", "his-wadi": "up"},
    }


def metrics(store: Store) -> dict:
    """Return how many approvals are still pending and how many slots are taken."""
    return {"pending": len(store.pending), "booked": len(store.slots)}


def _book(store: Store, body: dict) -> dict:
    """Hold a slot for coordinator confirmation, or refuse when the hold list or the slot is full."""
    if len(store.pending) >= HOLD_CAP:
        # The hold list is full, so this request does not create another pending approval.
        return _reply("Holds expire. The anomaly is visible.")
    slot = str(body.get("slot", "slot-1"))
    if slot in store.slots:
        return _reply("That slot is taken.")
    store.seq += 1
    approval = f"apr-{store.seq}"
    store.pending[approval] = {"slot": slot, "actor": body.get("actor")}
    return _reply("A coordinator has to confirm the booking.", [{"tool": "hold", "slot": slot}], [approval])


def _reply(text: str, tools: list[dict] | None = None, pending: list[str] | None = None) -> dict:
    """Return the chat payload. Citations are the documents on tools that carry one.

    The steps copy the reply text, keep a citation for every tool that names a document, and attach the tool list and any pending approval ids.
    """
    return {
        "reply": text,
        "citations": [tool["document"] for tool in (tools or []) if tool.get("document")],
        "tool_trace": tools or [],
        "pending_approval_ids": pending or [],
    }


def _escape(text: str) -> str:
    """Escape the three markup characters so the reply shows the text instead of treating it as markup."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

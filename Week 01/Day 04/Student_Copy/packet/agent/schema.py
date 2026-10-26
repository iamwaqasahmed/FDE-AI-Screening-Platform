"""Reply fields for one scenario.

This is the starter. Chapter 06 replaces the copy under work/.
Leave this packet copy unchanged.

The count argument is ignored. Every reply writes the same invented count.
A reply that should carry the status tool's number, or no number at all,
still leaves here with that invented count.
"""

from __future__ import annotations


def reply(
    intent: str,
    text: str,
    count: int | None = None,
    facility_id: str = "",
    constraint: str = "",
) -> dict:
    """Return the reply object the trace stores under reply.

    intent, text, facility_id, and constraint are kept.
    count is accepted and then discarded. The written count is 12.
    """
    _ = count
    return {
        "intent": intent,
        "text": text,
        "count": 12,
        "facility_id": facility_id,
        "constraint": constraint,
    }


def row(
    scenario: str,
    reply_body: dict,
    citations: list[str] | None = None,
    tool_trace: list[str] | None = None,
    pending: list[str] | None = None,
    approval_ids: list[str] | None = None,
    booked: bool = False,
    returned: bool = False,
    redirected: bool = False,
    sms: bool = False,
    refusal_logged: bool = False,
    preference_used: bool = False,
    decisions: int = 0,
) -> dict:
    """Return one trace row.

    Empty lists are written when the caller passes nothing.
    This starter's caller leaves citations, pending, and approval ids empty,
    and it leaves redirected and refusal_logged at their defaults.
    """
    # Copy each list. A missing list is written empty.
    return {
        "scenario": scenario,
        "reply": reply_body,
        "citations": list(citations or []),
        "tool_trace": list(tool_trace or []),
        "pending_approval_ids": list(pending or []),
        "approval_ids": list(approval_ids or []),
        "booked": booked,
        "returned": returned,
        "redirected": redirected,
        # Later flags stay at the caller's values, including the defaults.
        "sms": sms,
        "refusal_logged": refusal_logged,
        "preference_used": preference_used,
        "decisions": decisions,
    }

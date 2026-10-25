"""Reply fields for one scenario.

A count is the tool result when referral.status ran.
It is empty when status was not called. The starter wrote 12 into every
reply and ignored the count it was given. This file keeps that argument.

Chapter 06 replaces the copy under work/agent. The check reads these
field names. Do not rename them.
"""

from __future__ import annotations


def reply(
    intent: str,
    text: str,
    count: int | None = None,
    facility_id: str = "",
    constraint: str = "",
) -> dict:
    """Build the object stored on the row under reply.

    intent is a short name such as status, book, return, emergency, or refusal.
    text is the sentence the patient sees.
    count is the status tool's number, or empty when that tool did not run.
    facility_id is the id memory kept from a turn that named a hospital.
    constraint is the word the offer tool returned when no slot fits.
    """
    return {
        "intent": intent,
        "text": text,
        "count": count,
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
    """Build one trace row.

    citations names the tool or the document the row relied on.
    tool_trace is the tool names in call order.
    pending_approval_ids holds an approval that is still waiting.
    approval_ids holds an approval a coordinator has decided.
    booked, returned, redirected, and sms are true only when that
    action happened. refusal_logged records a visit that did not proceed.
    preference_used is true only when a stored preference was applied.
    decisions is how many distinct approval ids were decided. A replay is 1.
    """
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
        "sms": sms,
        "refusal_logged": refusal_logged,
        "preference_used": preference_used,
        "decisions": decisions,
    }

"""Reply fields. A count is the tool result, or empty when status was not called.

This file replaces the starter under work/agent. Leave the packet copy unchanged.

reply writes the count it is given. None stays None. The starter wrote 12
and threw the argument away.

row adds failure. The starter had no such field. timeout and race-slot
are the two names this day writes there. An empty string means the row
is not one of those two failures.
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

    Every argument is kept. count is the status tool's number, or None
    when status was not called.
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
    failure: str = "",
) -> dict:
    """Return one trace row.

    Empty lists are written when the caller passes nothing.
    failure is the scenario's failure name, or an empty string.
    """
    # Copy the lists. A missing list is stored empty, not left as None.
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
        # The last field names this row's failure, or stays empty.
        "failure": failure,
    }

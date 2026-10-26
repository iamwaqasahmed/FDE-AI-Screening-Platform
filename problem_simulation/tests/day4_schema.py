"""Reply fields.

A count is the tool result, or empty when status was not called.

Row builders for the patient agent. The checks copy this file with the model.

reply is the small object inside a row. row is the full scenario result the
checker compares. A count stays empty unless a status tool returned one, which
is how an invented count is distinguished from a tool count. Lists default to
empty and flags default to false so a skipped tool is not confused with a tool
that ran.
"""

from __future__ import annotations


def reply(
    intent: str,
    text: str,
    count: int | None = None,
    facility_id: str = "",
    constraint: str = "",
) -> dict:
    """Build the reply object.

    The count is left empty when status was not called. Facility and constraint
    stay blank unless the caller has one. The text is whatever the caller decided
    to say. This builder does not invent a count.
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
    """Build one scenario result.

    Omitted citations, traces, and approval lists stay empty. Omitted flags stay
    false. The checker uses those empties to see which tools the agent did not call.
    """
    # Copy the lists so the caller can keep using its own. Missing lists stay empty.
    return {
        "scenario": scenario,
        "reply": reply_body,
        "citations": list(citations or []),
        "tool_trace": list(tool_trace or []),
        "pending_approval_ids": list(pending or []),
        "approval_ids": list(approval_ids or []),
        # Flags default to false, so a skipped tool is not recorded as a tool that ran.
        "booked": booked,
        "returned": returned,
        "redirected": redirected,
        "sms": sms,
        "refusal_logged": refusal_logged,
        "preference_used": preference_used,
        "decisions": decisions,
    }

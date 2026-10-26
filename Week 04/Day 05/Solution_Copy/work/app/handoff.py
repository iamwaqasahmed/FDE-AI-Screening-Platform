"""A handoff with no summary is refused.

A handoff is the spoken summary plus the agent who owns the call.
An empty summary, or a summary that is only spaces, is not a
handoff. The call is refused and the agent id is left blank so
nobody is assigned. A summary with text is kept, and the agent
id on the call is kept with it.
"""


def handoff(call: dict) -> dict:
    """Refuse a blank summary. Keep the agent id when the summary has text.

    A missing summary is treated the same as a blank one. strip
    removes spaces so a summary of only spaces is still blank.
    """
    summary = str(call.get("summary") or "").strip()
    if not summary:
        # No words to hand on. Do not assign an agent.
        return {"agent": "", "refused": True, "summary": ""}
    return {
        "agent": str(call.get("agent") or ""),
        "refused": False,
        "summary": summary,
    }

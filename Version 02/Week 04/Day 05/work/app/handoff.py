"""A handoff with no summary is refused."""


def handoff(call: dict) -> dict:
    summary = str(call.get("summary") or "").strip()
    if not summary:
        return {"agent": "", "refused": True, "summary": ""}
    return {"agent": str(call.get("agent") or ""), "refused": False, "summary": summary}

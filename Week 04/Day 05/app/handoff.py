"""Return an agent id and an empty summary."""


def handoff(call: dict) -> dict:
    del call
    return {"agent": "cc-1", "refused": False, "summary": ""}

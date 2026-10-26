"""Return an agent id and an empty summary.

This is the starter. It ignores the call. Every row comes back as
agent cc-1, with an empty summary, and the call is not marked
refused. The summary that was spoken is thrown away. The finished
module refuses a call whose summary is blank, and it keeps the
summary when one was given.
"""


def handoff(call: dict) -> dict:
    """Ignore the call. Return one fixed agent id and an empty summary.

    The call is discarded, so a missing summary cannot change the
    result. refused stays false even when the summary was blank.
    """
    # The argument is unused. The shell never reads the summary.
    del call
    return {"agent": "cc-1", "refused": False, "summary": ""}

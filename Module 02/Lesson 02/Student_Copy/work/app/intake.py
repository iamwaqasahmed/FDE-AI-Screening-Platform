"""Poll eref for a referral. The webhook body is not read.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

accept still returns mode poll. It does not record a referral id,
and it does not read the schema registry. While this shell is the
file that runs, the journey check says the intake still polls.
"""

from __future__ import annotations


def accept(body: dict, registry_text: str) -> dict:
    """Return a poll result and ignore both arguments.

    body is the webhook delivery. registry_text is the schema
    registry. Neither is used. The empty referral id is the sign
    that nothing was recorded. rejected stays false. This shell
    does not stop the event, and it does not keep a record.
    """
    return {"mode": "poll", "referral_id": "", "ignored": [], "rejected": False, "record": {}}

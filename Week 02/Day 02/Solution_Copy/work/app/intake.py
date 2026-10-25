"""Accept referral.submitted from the webhook. Unknown fields are ignored.

Chapter 06 replaces work/app/intake.py with this file.
The packet copy stays the polling shell.

mode is webhook. registry.keep splits the body on the
referral.submitted row. A key the registry does not list comes
back in ignored and is not stored. The event is not rejected
for that key. letter is listed, so keep returns it, and the
record then leaves it off. The letter value is the watermark.
"""

from __future__ import annotations

import registry


def accept(body: dict, registry_text: str) -> dict:
    """Record the referral and ignore a key the registry does not list.

    body is the webhook. registry_text is the schema registry.
    kept holds the fields that row allows. ignored holds the
    other keys. The record drops letter so the watermark value
    is not stored. rejected stays false. referral_id is copied
    from the kept body.
    """
    kept, ignored = registry.keep(body, registry_text, "referral.submitted")
    record = {key: value for key, value in kept.items() if key != "letter"}
    return {
        "mode": "webhook",
        "referral_id": str(kept.get("referral_id", "")),
        "ignored": ignored,
        "rejected": False,
        "record": record,
    }

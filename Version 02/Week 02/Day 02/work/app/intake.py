"""Accept referral.submitted from the webhook. Unknown fields are ignored."""

from __future__ import annotations

import registry


def accept(body: dict, registry_text: str) -> dict:
    kept, ignored = registry.keep(body, registry_text, "referral.submitted")
    record = {key: value for key, value in kept.items() if key != "letter"}
    return {
        "mode": "webhook",
        "referral_id": str(kept.get("referral_id", "")),
        "ignored": ignored,
        "rejected": False,
        "record": record,
    }

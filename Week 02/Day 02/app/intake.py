"""Poll eref for a referral. The webhook body is not read."""

from __future__ import annotations


def accept(body: dict, registry_text: str) -> dict:
    return {"mode": "poll", "referral_id": "", "ignored": [], "rejected": False, "record": {}}

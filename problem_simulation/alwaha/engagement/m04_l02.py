"""rel-m04-l02 gold.
The override rate and the shadow hash stay here.

gold collects the trace board, the per-hospital cost, the override rate, and the shadow hash for this profile. The demo points at the span that recorded tokens, because the later spans are tool calls and an alert.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.m04_l02_rows import (
    ALERT_AT,
    CASE_AT,
    CASE_DATE,
    CIRCULAR,
    CLINIC,
    DETAIL,
    FIRST_ERROR,
    NEW_HOURS,
    OLD_HOURS,
    SLO_MINUTES,
    TOKENS,
    TOOL,
    experiment,
    gateway,
    overrides,
    shadow_hash,
    spans,
)
from alwaha.engagement.m04_l02_rules import board, cost, rate


def gold(profile: Profile) -> dict:
    """Return the trace board, the costs, the override rate, and the shadow material for this profile.

    The demo hash is taken from the span that recorded tokens. Later spans are tool calls and the alert, which do not carry the model hash.
    """
    # The model span is the one that records tokens. Tool spans and the alert do not.
    shown = next(span for span in spans(profile) if span.get("tokens"))
    return {
        "alert_at": ALERT_AT,
        "board": board(spans(profile)),
        "case_at": CASE_AT,
        "case_date": CASE_DATE,
        "circular": CIRCULAR,
        "clinic": CLINIC,
        "cost": cost(gateway(profile.seed)),
        "demo": {"detail": DETAIL, "hash": shown["hash"], "tokens": str(TOKENS), "tool": TOOL},
        "drifts": ["ramadan hours", "criteria v4", "campaign clinic"],
        "first_error": FIRST_ERROR,
        "new_hours": NEW_HOURS,
        "old_hours": OLD_HOURS,
        "override": rate(overrides(profile.seed)),
        "shadow_hash": shadow_hash(profile),
        "slo_minutes": SLO_MINUTES,
        "turn": experiment(profile),
    }

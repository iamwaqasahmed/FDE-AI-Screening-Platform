"""rel-w4d2 gold. The override rate and the shadow hash stay here."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w4d2_rows import (
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
from alwaha.engagement.w4d2_rules import board, cost, rate


def gold(profile: Profile) -> dict:
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

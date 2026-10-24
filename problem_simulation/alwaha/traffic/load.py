"""Load profiles. They record a pass or a fail. They do not start a GPU."""

from __future__ import annotations

CHAT_P95_SECONDS = 0.4
CHAT_SLO_SECONDS = 1.0
COLD_START_SECONDS = 90
BATCH_LOCAL_SAR = 40
BATCH_EXTERNAL_SAR = 900
PRICE_CAP_SAR = 80


def results() -> list[dict]:
    return [
        {"id": "load-chat", "ok": CHAT_P95_SECONDS < CHAT_SLO_SECONDS, "p95": CHAT_P95_SECONDS},
        {"id": "load-eid", "ok": True, "note": "capacity plan includes the post-Eid surge"},
        {"id": "load-batch", "ok": BATCH_LOCAL_SAR <= PRICE_CAP_SAR and BATCH_EXTERNAL_SAR > PRICE_CAP_SAR},
        {"id": "load-cold", "ok": COLD_START_SECONDS > 60},
    ]


def strategies() -> dict[str, bool]:
    """The simpler serving choice fails. Pre-scale plus local batch passes."""
    return {
        "ext-large-batch": BATCH_EXTERNAL_SAR <= PRICE_CAP_SAR,
        "reactive-cold": COLD_START_SECONDS <= 60,
        "prescale-batch": BATCH_LOCAL_SAR <= PRICE_CAP_SAR and CHAT_P95_SECONDS < CHAT_SLO_SECONDS,
    }

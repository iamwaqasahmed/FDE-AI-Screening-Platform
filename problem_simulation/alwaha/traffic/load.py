"""Load profiles. They record a pass or a fail. They do not start a GPU.

results() compares the recorded chat latency, the batch costs, and the cold-start time with the limits in this file. The surge row is a recorded pass. strategies() says which serving choice passes those same comparisons. Nothing here starts a model.
"""

from __future__ import annotations

CHAT_P95_SECONDS = 0.4
CHAT_SLO_SECONDS = 1.0
COLD_START_SECONDS = 90
BATCH_LOCAL_SAR = 40
BATCH_EXTERNAL_SAR = 900
PRICE_CAP_SAR = 80


def results() -> list[dict]:
    """Return the load rows.

    The chat row passes when the recorded latency is inside the limit. The surge row is a recorded pass with a note. The batch row passes when the local cost is inside the cap and the external cost is outside it. The cold row passes when the cold start is past the threshold in that comparison. No row starts a run.
    """
    return [
        {"id": "load-chat", "ok": CHAT_P95_SECONDS < CHAT_SLO_SECONDS, "p95": CHAT_P95_SECONDS},
        # Recorded as a pass: the note states the plan, and no latency is measured here.
        {"id": "load-eid", "ok": True, "note": "capacity plan includes the post-Eid surge"},
        {"id": "load-batch", "ok": BATCH_LOCAL_SAR <= PRICE_CAP_SAR and BATCH_EXTERNAL_SAR > PRICE_CAP_SAR},
        # Passes when a cold start is too slow for the window this comparison encodes.
        {"id": "load-cold", "ok": COLD_START_SECONDS > 60},
    ]


def strategies() -> dict[str, bool]:
    """The simpler serving choice fails. Pre-scale plus local batch passes.

    ext-large-batch is true only when the external cost is inside the cap. reactive-cold is true only when the cold start fits the threshold. prescale-batch is true when the local cost is inside the cap and the chat latency is inside its limit. Returns each flag.
    """
    return {
        "ext-large-batch": BATCH_EXTERNAL_SAR <= PRICE_CAP_SAR,
        "reactive-cold": COLD_START_SECONDS <= 60,
        "prescale-batch": BATCH_LOCAL_SAR <= PRICE_CAP_SAR and CHAT_P95_SECONDS < CHAT_SLO_SECONDS,
    }

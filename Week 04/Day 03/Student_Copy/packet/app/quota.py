"""Give the batch the whole pool."""


def latency(sheet: dict) -> int:
    return int(sheet["chat_p95_starved_ms"])

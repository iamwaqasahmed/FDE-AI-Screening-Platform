"""Give the batch the whole pool.

This is the starter. latency returns chat_p95_starved_ms
from the sheet. That is the latency when the batch has
the whole pool. No other key is read.
"""


def latency(sheet: dict) -> int:
    """Return the starved chat latency from the sheet, as an integer."""
    # The starved figure is the latency this module reports.
    return int(sheet["chat_p95_starved_ms"])

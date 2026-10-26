"""Keep a chat reserve on the shared pool.

latency returns chat_p95_reserved_ms from the sheet.
That is the latency kept when a chat reserve remains
on the pool. No other key on the sheet is read.
"""

from __future__ import annotations


def latency(sheet: dict) -> int:
    """Return the reserved chat latency from the sheet, as an integer."""
    # The reserve is the latency this module reports.
    return int(sheet["chat_p95_reserved_ms"])

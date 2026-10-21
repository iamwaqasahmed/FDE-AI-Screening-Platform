"""Pure fault functions. Each takes a frame, a generator, and params, and returns the faulted frame plus a truth record."""

from __future__ import annotations


def record(fault: str, **details) -> dict:
    return {"fault": fault, **details}

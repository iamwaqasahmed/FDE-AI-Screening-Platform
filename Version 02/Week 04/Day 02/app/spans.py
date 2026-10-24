"""Report CPU and drop the trace fields."""

from __future__ import annotations


def read(span: dict) -> dict:
    return {"cpu": span.get("cpu", 0)}

"""Name each planted failure from the log text."""

from __future__ import annotations


def classify(row: dict) -> str:
    text = str(row.get("output", "")).lower()
    if "unauthorized" in text:
        return "retrieval"
    if "friday" in text:
        return "reasoning"
    if "approval" in text and "none" in text:
        return "workflow"
    if "not on file" in text:
        return "hallucination"
    return "pass"

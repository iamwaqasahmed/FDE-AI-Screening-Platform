"""Name each planted failure from the log text.

The name is read from the reply text. A row that is not a planted case returns pass.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return the planted failure name for this row.

    The type is not a field on the row. It is read from the reply text. A document that is not in force is retrieval. An offer that uses Friday is reasoning. A booking that has no approval is workflow. A clause that is not on file is hallucination. Anything else returns pass.
    """
    # The type is not a field on the row. It is read from the reply text.
    text = str(row.get("output", "")).lower()
    # A document that is not in force.
    if "unauthorized" in text:
        return "retrieval"
    # An offer that uses Friday.
    if "friday" in text:
        return "reasoning"
    # A booking that has no approval.
    if "approval" in text and "none" in text:
        return "workflow"
    # A clause that is not on file.
    if "not on file" in text:
        return "hallucination"
    # Anything else is not one of the four planted rows.
    return "pass"

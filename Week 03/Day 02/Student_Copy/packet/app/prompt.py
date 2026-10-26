"""Send the letter fields to the external model.

served returns true, so this prompt is marked as the served one.
target names ext-large and sets phi. extract copies the item id,
sets the source type to typed, and leaves the sub-specialty
empty. intent returns status. None of these functions read the
row text.
"""

from __future__ import annotations


def served() -> bool:
    """Report that this prompt is the one being served."""
    # True means this prompt is the model on the endpoint.
    return True


def target() -> dict:
    """Name ext-large and turn phi on.

    The model name is ext-large. phi is set, so the call this
    row describes includes phi.
    """
    return {"model": "ext-large", "phi": True}


def extract(row: dict) -> dict:
    """Copy the item id, mark the letter typed, and leave the sub-specialty blank.

    row must carry item_id. The text is not read. The source
    type is typed. The sub-specialty is an empty string.
    """
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    """Return the status label.

    row is not read. The text of the message does not change
    the label.
    """
    return "status"

"""Score a weak local prompt. Do not serve it.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell sends the letter fields to ext-large and marks the prompt
as served. While that shell is the file that runs, the model check
says the prompt baseline is still the served model, and the call
sends phi to ext-large. The check does not name the model.

extract and intent stay the weak baseline. Every letter is typed,
and every message is status. That is expected. Pointing those two
functions at the adapter makes slice-lora say the prompt baseline
clears the slice.
"""

from __future__ import annotations


def served() -> bool:
    """The weak prompt is scored. It is not the model that is served."""
    # A served prompt is the model on the endpoint. This one is not.
    return False


def target() -> dict:
    """The baseline call stays on local-small, with phi left off.

    The shell returns ext-large and sets phi. This call does not.
    """
    return {"model": "local-small", "phi": False}


def extract(row: dict) -> dict:
    """Always type the letter and leave the sub-specialty blank.

    row is one letter. The item id is copied. The text is not read.
    A real relabel lives in extract.py. Do not copy it here.
    """
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    """Always call the message a status question.

    row is one message. The text is not read. A real classifier
    lives in intent.py. Do not copy it here. "Cancel this visit."
    stays status. That is expected.
    """
    return "status"

"""A rare-class sample inside the fidelity card. Real letters stay out.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns the first real letter. While that shell is the
file that runs, the synthetic check says the sample misses the
fidelity card, contains a watermark, and contains a national id.
The message does not print the watermark or a rate.
"""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    """Return four invented rows that sit inside the card.

    letters are the clerk rows. They are not copied. card supplies
    the rare sub-specialty. Two rows are endocrinology and two are
    ophthalmology. Two rows name the rare sub-specialty. Two rows
    say Kindly. None of the rows carry an id.
    """
    del letters
    rare = card["rare_sub_specialty"]
    return [
        {"source_type": "typed", "specialty": "endo", "sub_specialty": rare, "text": "Kindly review endocrinology."},
        {"source_type": "typed", "specialty": "endo", "sub_specialty": "", "text": "Kindly review the sugar clinic."},
        {"source_type": "photo", "specialty": "ophth", "sub_specialty": rare, "text": "A clinic photo for the eye clinic."},
        {"source_type": "scan", "specialty": "ophth", "sub_specialty": "", "text": "A scanned page for the eye clinic."},
    ]

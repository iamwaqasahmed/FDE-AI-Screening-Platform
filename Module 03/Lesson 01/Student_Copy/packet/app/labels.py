"""Copy the clerk label.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

relabel keeps the clerk source type and sub-specialty, and sets
the guideline to ann-v1. While this shell is the file that runs,
the labels check says a phone photo is still a scan, a
sub-specialty is still blank, and the sample still follows ann-v1.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Return the clerk fields under the old guideline.

    row is one letter. The text is not read. source_type and
    sub_specialty are copied. guideline is ann-v1.
    """
    return {
        "guideline": "ann-v1",
        "item_id": row["item_id"],
        "source_type": row["source_type"],
        "sub_specialty": row["sub_specialty"],
    }

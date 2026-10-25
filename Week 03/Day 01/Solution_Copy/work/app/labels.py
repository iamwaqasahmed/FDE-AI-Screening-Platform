"""Relabel a letter under ann-v2.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell copies the clerk fields and keeps the old guideline.
While that shell is the file that runs, the labels check says a
phone photo is still a scan, a sub-specialty is still blank, and
the sample still follows the old guideline.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Set the source type and the sub-specialty from the text.

    row is one letter. Phone or photo in the text is source type
    photo. Scan, when the text does not say phone or photo, is
    source type scan. Anything else is typed. Retina and pediatric
    are read from the text. Any other sub-specialty stays blank.
    """
    text = row["text"].lower()
    # The sub-specialty comes from the words, not from the clerk field.
    if "retina" in text:
        sub_specialty = "retina"
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    # Phone or photo wins over the word scan.
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {
        "guideline": "ann-v2",
        "item_id": row["item_id"],
        "source_type": source_type,
        "sub_specialty": sub_specialty,
    }

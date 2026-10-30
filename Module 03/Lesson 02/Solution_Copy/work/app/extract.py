"""Relabel a letter from the text.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns an empty source type and an empty sub-specialty.
While that shell is the file that runs, the model check says
extraction F1 is outside the budget. The check does not print an F1
or a gold label.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Read the letter text and fill the two fields.

    row carries item_id and text. The item id is copied. The text
    decides the sub-specialty and the source type. A letter that
    names neither specialty stays blank. A letter that is not a
    phone, a photo, or a scan stays typed.
    """
    text = row["text"].lower()
    # Retina wins when both specialty words are present.
    if "retina" in text:
        sub_specialty = "retina"
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    # A phone photo is a photo. The word scan marks a scan.
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {"item_id": row["item_id"], "source_type": source_type, "sub_specialty": sub_specialty}

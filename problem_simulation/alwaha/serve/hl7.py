"""Apply an HL7 pair in file order and in sequence order.

Only SIU rows decide the standing sequence. File order keeps the last SIU in arrival order. Sequence order sorts those rows by sequence and keeps the last one. The results differ when a later sequence arrived first.
"""

from __future__ import annotations


def outcomes(rows: list[dict]) -> tuple[int, int]:
    """Return the file-order sequence and the sequence-order sequence.

    Non-SIU rows are ignored. Each returned value is the sequence of the SIU row that stands in that order.
    """
    # Other message kinds must not decide which sequence stands.
    siu = [row for row in rows if row.get("kind") == "siu"]
    file_final = int(siu[-1]["sequence"])
    ordered = sorted(siu, key=lambda row: int(row["sequence"]))
    return file_final, int(ordered[-1]["sequence"])

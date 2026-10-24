"""Apply an HL7 pair in file order and in sequence order."""

from __future__ import annotations


def outcomes(rows: list[dict]) -> tuple[int, int]:
    siu = [row for row in rows if row.get("kind") == "siu"]
    file_final = int(siu[-1]["sequence"])
    ordered = sorted(siu, key=lambda row: int(row["sequence"]))
    return file_final, int(ordered[-1]["sequence"])

"""A rare-class sample inside the fidelity card. Real letters stay out."""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    del letters
    rare = card["rare_sub_specialty"]
    return [
        {"source_type": "typed", "specialty": "endo", "sub_specialty": rare, "text": "Kindly review endocrinology."},
        {"source_type": "typed", "specialty": "endo", "sub_specialty": "", "text": "Kindly review the sugar clinic."},
        {"source_type": "photo", "specialty": "ophth", "sub_specialty": rare, "text": "A clinic photo for the eye clinic."},
        {"source_type": "scan", "specialty": "ophth", "sub_specialty": "", "text": "A scanned page for the eye clinic."},
    ]

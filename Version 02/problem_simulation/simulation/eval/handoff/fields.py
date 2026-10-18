"""Field names on the two governance records, taken from the templates in the corpus."""

from __future__ import annotations

from simulation.corpus.families.governance_texts import MODEL_CARD_FIELDS, TRANSPARENCY_FIELDS


def transparency_keys() -> list[str]:
    return [_key(field) for field in TRANSPARENCY_FIELDS]


def model_card_keys() -> list[str]:
    return [_key(field) for field in MODEL_CARD_FIELDS]


def _key(field: str) -> str:
    return field.replace(" ", "_")

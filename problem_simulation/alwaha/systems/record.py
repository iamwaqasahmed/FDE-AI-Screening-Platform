"""Fault-record shape. Clean columns are the ones a check expects without the defect."""

from __future__ import annotations


def record(export: str, cause_id: str, affected_keys: list[str], clean_columns: list[str]) -> dict:
    return {
        "export": export,
        "cause_id": cause_id,
        "affected_keys": list(affected_keys),
        "clean_columns": list(clean_columns),
    }

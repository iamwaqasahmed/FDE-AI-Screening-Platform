"""Fault-record shape. Clean columns are the ones a check expects without the defect.

record() names the export, the cause, the keys the defect touches, and the columns a check can read without taking the defect with them. Both lists are copied into the record.
"""

from __future__ import annotations


def record(export: str, cause_id: str, affected_keys: list[str], clean_columns: list[str]) -> dict:
    """Return one fault record.

    export is the system name. cause_id is the defect. affected_keys are the rows or fields the defect touches. clean_columns are the fields a check can use without that defect. Both lists are copied so a later edit of the caller's lists leaves this record alone.
    """
    return {
        "export": export,
        "cause_id": cause_id,
        "affected_keys": list(affected_keys),
        "clean_columns": list(clean_columns),
    }

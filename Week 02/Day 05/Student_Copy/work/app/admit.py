"""Reject root, and keep a national id out of the log."""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    if str(user).lower() in {"root", "0"}:
        return "rejected"
    if national_id and national_id in log_line:
        return "rejected"
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    if national_id:
        return log_line.replace(national_id, "")
    return log_line

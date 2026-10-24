"""Accept every image and keep the log line."""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    del user, log_line, national_id
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    del national_id
    return log_line

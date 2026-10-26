"""Admission for a private-cloud image. Root and a national id are rejected.

admit() rejects the root name and the zero user. It also rejects a log line that contains a national id. An empty national id is not searched, because an empty string matches every log line. emitted_log() strips a supplied national id out of the log line.
"""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    """Return rejected or accepted.

    The root name and the zero user are rejected. A non-empty national id that appears in the log line is rejected. Every other image is accepted.
    """
    # The root name and the zero user cannot run the image.
    if str(user).lower() in {"root", "0"}:
        return "rejected"
    # An empty id is a substring of every log line, so only a real id is searched.
    if national_id and national_id in log_line:
        return "rejected"
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    """Return the log line with a supplied national id removed.

    An empty national id leaves the line unchanged.
    """
    # Nothing to strip when the caller did not supply an id.
    if national_id:
        return log_line.replace(national_id, "")
    return log_line

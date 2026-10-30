"""Reject root, and keep a national id out of the log.

admit rejects a root account and an account named 0. It rejects a
log line that still carries the national id. A clean account with
a clean line is accepted. emitted_log removes the id from the line.
"""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    """Reject root, reject a logged id, and accept a clean image.

    user is the account the image would run as. root and 0 are
    rejected. log_line is the deploy log. national_id is the id
    that must not remain on that line. A line that still contains
    it is rejected. Any other account with a clean line is accepted.
    """
    if str(user).lower() in {"root", "0"}:
        return "rejected"
    if national_id and national_id in log_line:
        return "rejected"
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    """Return the log line with the national id removed.

    national_id is the id the caller passes. When an id is given,
    the returned line no longer contains it. When no id is given,
    the line comes back unchanged.
    """
    if national_id:
        return log_line.replace(national_id, "")
    return log_line

"""Accept every image and keep the log line.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

admit ignores the user, the log line, and the national id. It
returns accepted for every call. emitted_log returns the log line
unchanged. While this shell is the file that runs, the deploy check
says the image runs as root, and a national id is in the deploy log.
"""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    """Return accepted and ignore every argument.

    user is the account the image would run as. log_line is the
    deploy log. national_id is the id the log must not keep. None
    of them is used. A root image is still accepted.
    """
    del user, log_line, national_id
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    """Return the log line unchanged.

    national_id is the id that should leave the line. This shell
    keeps it. The fixture log stays in the pack.
    """
    del national_id
    return log_line

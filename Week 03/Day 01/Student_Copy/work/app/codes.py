"""Clinic codes taken from the catalog.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

clinic rewrites ENDO-CLN back to END-01. The date and the facility
are ignored. While this shell is the file that runs, the identity
check says the stale clinic code was kept.
"""

from __future__ import annotations


def clinic(code: str, as_of: str, facility: str) -> str:
    """Keep the catalog code and drop the newer endocrinology code.

    code is the clinic code on the row. as_of and facility are
    ignored. ENDO-CLN becomes END-01. Every other code is kept.
    """
    del as_of, facility
    if code == "ENDO-CLN":
        return "END-01"
    return code

"""Report the approved local-small hash from the register.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

health reads the register row whose id is local-small and whose
status is approved. The body reports that hash, that prompt, and
the endpoint dependency. The candidate argument stays on the
function line and is not used. While the shell is the file that
runs, the deploy check says the health probe does not report the
registered hash.
"""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    """Return the approved local-small row from the register.

    register is the model list. The approved local-small row is
    the one the probe reports. A previous row for the same id is
    skipped. candidate is the near name. It is not a registration,
    and this function does not read it.
    """
    # candidate is the near name. This probe does not read it.
    del candidate
    # The approved local-small row is the one this probe reports.
    approved = next(
        row
        for row in register["models"]
        if row["id"] == "local-small" and row["status"] == "approved"
    )
    # The body carries that hash, that prompt, and the endpoint dependency.
    return {
        "dependencies": ["endpoint"],
        "model_hash": approved["hash"],
        "prompt_version": approved["prompt"],
        "status": "ok",
    }

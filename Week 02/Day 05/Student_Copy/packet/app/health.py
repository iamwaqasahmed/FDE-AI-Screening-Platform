"""Report the approved local-small hash from the register.

health reads the register row whose id is local-small and whose
status is approved. The body reports that hash, that prompt, and
the endpoint dependency. The candidate argument stays on the
function line and is not used.
"""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    """Return the approved local-small row from the register.

    register is the model list. The approved local-small row is
    the one the probe reports. A previous row for the same id is
    skipped. candidate is the near name. It is not a registration,
    and this function does not read it.
    """
    del candidate
    approved = next(
        row
        for row in register["models"]
        if row["id"] == "local-small" and row["status"] == "approved"
    )
    return {
        "dependencies": ["endpoint"],
        "model_hash": approved["hash"],
        "prompt_version": approved["prompt"],
        "status": "ok",
    }

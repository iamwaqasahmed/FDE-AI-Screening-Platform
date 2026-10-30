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
    # The candidate is not a registration. Only the register is read.
    del candidate
    # Skip earlier local-small rows until the one marked approved.
    approved = next(
        row
        for row in register["models"]
        if row["id"] == "local-small" and row["status"] == "approved"
    )
    # Report that row's hash and prompt, and name endpoint as a dependency.
    return {
        "dependencies": ["endpoint"],
        "model_hash": approved["hash"],
        "prompt_version": approved["prompt"],
        "status": "ok",
    }

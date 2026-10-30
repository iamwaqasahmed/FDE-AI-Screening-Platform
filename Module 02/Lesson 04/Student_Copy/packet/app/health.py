"""Report the candidate hash.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

health ignores the register and returns the candidate hash. The
prompt version is empty. The dependency list is empty. While this
shell is the file that runs, the deploy check says the health probe
does not report the registered hash.
"""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    """Return the candidate hash and ignore the register.

    register is the model list. candidate is the near name that is
    not a registration. The body uses candidate["hash"]. The
    approved row on the register is not read.
    """
    del register
    return {
        "dependencies": [],
        "model_hash": candidate["hash"],
        "prompt_version": "",
        "status": "ok",
    }

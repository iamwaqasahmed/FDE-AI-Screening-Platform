"""Send the assistant to the external model.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

route ignores the environment and returns the external model on
the public zone. While this shell is the file that runs, the
deploy check says the router leaves the private endpoint.
"""

from __future__ import annotations


def route(env: str) -> dict:
    """Return the external model for every environment.

    env is dev or prod. Neither one is used. The endpoint, the
    model, and the zone are the external model on the public zone.
    """
    del env
    return {"endpoint": "ext-large", "model": "ext-large", "zone": "zone-public"}

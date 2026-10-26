"""Point the assistant at the private endpoint.

route returns the private endpoint, the local-small model, and
zone-private. Dev and prod both stay there. The environment
argument stays on the function line and is not used.
"""

from __future__ import annotations


def route(env: str) -> dict:
    """Return the private endpoint for every environment.

    env is dev or prod. Neither one changes the route. The
    endpoint is ep-local-small. The model is local-small. The
    zone is zone-private.
    """
    del env
    return {"endpoint": "ep-local-small", "model": "local-small", "zone": "zone-private"}

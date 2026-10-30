"""Serve the registered lora-local adapter inside the GPU quota.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell loads the cloud-tune hash and asks for more GPUs than the
quota. While that shell is the file that runs, the model check says
the hash is not on reg-models, and the gpu count is over the quota.
The check does not print a hash or a GPU count.
"""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    """Return the approved lora-local row, not the cloud fixture.

    registry is reg-models. quota is the GPU note. cloud is the
    unregistered fixture. The cloud argument is not used. The hash
    is copied from the approved row. It is not typed here.
    """
    # The row id and the approved status both have to match.
    chosen = next(row for row in registry["models"] if row["id"] == "lora-local" and row["status"] == "approved")
    # One GPU and rank 8 fit the quota. The base is local-small.
    return {"base": "local-small", "gpus": 1, "hash": chosen["hash"], "id": "lora-local", "rank": 8}

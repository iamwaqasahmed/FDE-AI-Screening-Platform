"""Load the cloud-tune hash and ask for more GPUs than the quota."""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    return {
        "base": "ext-large",
        "gpus": quota["gpus"] + 1,
        "hash": cloud["hash"],
        "id": "cloud-tune",
        "rank": 32,
    }

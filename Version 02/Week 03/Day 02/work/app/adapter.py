"""Serve the registered lora-local adapter inside the GPU quota."""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    chosen = next(row for row in registry["models"] if row["id"] == "lora-local" and row["status"] == "approved")
    return {"base": "local-small", "gpus": 1, "hash": chosen["hash"], "id": "lora-local", "rank": 8}

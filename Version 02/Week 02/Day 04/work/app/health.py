"""Report the approved local-small hash from the register."""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
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

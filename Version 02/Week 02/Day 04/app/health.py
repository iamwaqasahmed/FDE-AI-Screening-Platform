"""Report the candidate hash."""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    del register
    return {
        "dependencies": [],
        "model_hash": candidate["hash"],
        "prompt_version": "",
        "status": "ok",
    }

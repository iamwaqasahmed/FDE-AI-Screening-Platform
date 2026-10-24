"""Allow every call, including a phi field sent to ext-large."""

from __future__ import annotations


def allow(call: dict, registry: dict) -> bool:
    return True


def task(name: str) -> str:
    return "ext-large"

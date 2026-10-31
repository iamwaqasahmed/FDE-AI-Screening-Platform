"""Content hashes for documents the hospital already stored."""

from __future__ import annotations

import hashlib


def content_hash(body: str) -> str:
    """Hash the exact document body. The hash does not include the version id."""
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

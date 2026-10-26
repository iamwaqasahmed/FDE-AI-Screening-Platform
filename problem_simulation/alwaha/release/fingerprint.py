"""A hash of every file under a directory, so two builds can be compared.

Roots are mixed in the order given. A root that is a single file is hashed by its name and bytes. A directory is walked in sorted path order. The digest file itself is skipped, so writing the fingerprint into the tree does not change the fingerprint. Each piece is separated by a null byte.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def fingerprint(*roots: Path) -> str:
    """Return the hex digest of the named roots."""
    digest = hashlib.sha256()
    for root in roots:
        if root.is_file():
            # A file has no children. Hash its name and bytes, then move to the next root.
            digest.update(root.name.encode())
            digest.update(b"\0")
            digest.update(root.read_bytes())
            digest.update(b"\0")
            continue
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            if path.name == "fingerprint.txt":
                # The digest file would change the hash if it were included.
                continue
            relative = path.relative_to(root).as_posix()
            digest.update(root.name.encode())
            digest.update(b"\0")
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()

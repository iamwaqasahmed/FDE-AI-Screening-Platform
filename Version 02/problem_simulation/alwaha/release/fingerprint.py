"""A hash of every file under a directory, so two builds can be compared."""

from __future__ import annotations

import hashlib
from pathlib import Path


def fingerprint(*roots: Path) -> str:
    digest = hashlib.sha256()
    for root in roots:
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            if path.name == "fingerprint.txt":
                continue
            relative = path.relative_to(root).as_posix()
            digest.update(root.name.encode())
            digest.update(b"\0")
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()

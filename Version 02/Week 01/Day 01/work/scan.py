"""Fail when a tracked file holds a secret, the sample letter, or the dev watermark."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKER = "SAMPLE-" + "REFERRAL-ALWAHA"
KEY_MARKERS = ("BEGIN " + "PRIVATE KEY", "BEGIN " + "RSA PRIVATE KEY")
SKIP = {".git", "credentials", "__pycache__", ".pytest_cache"}


def iter_files(root: Path) -> list[Path]:
    found = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.relative_to(root).parts)
        if parts & SKIP:
            continue
        found.append(path)
    return found


def problems(root: Path = ROOT) -> list[str]:
    watermark = _watermark(root)
    hits = []
    for path in iter_files(root):
        text = path.read_bytes().decode("utf-8", errors="replace")
        relative = path.relative_to(root).as_posix()
        if MARKER in text:
            hits.append(f"sample letter marker in {relative}")
        if any(marker in text for marker in KEY_MARKERS):
            hits.append(f"private key in {relative}")
        if watermark and watermark in text:
            hits.append(f"dev watermark in {relative}")
    return hits


def _watermark(root: Path) -> str:
    path = root / "credentials" / "dev.json"
    if not path.is_file():
        return ""
    return str(json.loads(path.read_text(encoding="utf-8")).get("watermark", ""))


def main() -> None:
    found = problems()
    if found:
        print("scan failed:")
        for item in found:
            print(f"- {item}")
        raise SystemExit(1)
    if not (ROOT / "credentials" / "dev.json").is_file():
        print("scan passed. credentials/dev.json is not in this copy, so the watermark was not checked.")
        return
    print("scan passed.")


if __name__ == "__main__":
    main()

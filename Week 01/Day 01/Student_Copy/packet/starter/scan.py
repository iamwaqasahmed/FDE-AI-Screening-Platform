"""Fail when a file in this folder holds a secret, the sample letter, or the dev watermark.

Chapter 01 and chapter 07 run this file from the work/ copy:

    python scan.py

A clean folder prints "scan passed." A hit prints "scan failed:" and the
file name. The secret value itself is never printed. Delete the file the
line names. Do not paste the value into a note to ask why.

The credentials file is allowed to hold the watermark, because this scan
skips the credentials folder. Anywhere else, the same watermark is a hit.
"""

from __future__ import annotations

import json
from pathlib import Path

# The folder this script sits in. In the lab, that folder is work/.
ROOT = Path(__file__).resolve().parent

# The sample referral letter carries this marker. The two pieces are
# joined here so this script does not itself contain the finished marker.
# If it did, the scan would fail on its own source file.
MARKER = "SAMPLE-" + "REFERRAL-ALWAHA"

# Headers that begin a private key. Joined for the same reason as MARKER:
# the finished header must not appear as one string in this file.
KEY_MARKERS = ("BEGIN " + "PRIVATE KEY", "BEGIN " + "RSA PRIVATE KEY")

# Folder names to skip. "credentials" is the important one: the dev
# credential lives there and is allowed to contain the watermark.
SKIP = {".git", "credentials", "__pycache__", ".pytest_cache"}


def iter_files(root: Path) -> list[Path]:
    """Return the files under root that the scan is willing to read.

    A file is skipped when any folder in its path is in SKIP. So
    credentials/dev.json is skipped, and a note buried in a skipped
    folder is skipped too.
    """
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
    """Return one short line per hit. An empty list means the folder is clean.

    The line names the kind of hit and the file. It does not include the
    watermark or the marker text.
    """
    watermark = _watermark(root)
    hits = []
    for path in iter_files(root):
        # errors="replace" so a non-text file cannot crash the scan.
        text = path.read_bytes().decode("utf-8", errors="replace")
        relative = path.relative_to(root).as_posix()
        if MARKER in text:
            hits.append(f"sample letter marker in {relative}")
        if any(marker in text for marker in KEY_MARKERS):
            hits.append(f"private key in {relative}")
        # No credential file means there is no watermark to look for.
        if watermark and watermark in text:
            hits.append(f"dev watermark in {relative}")
    return hits


def _watermark(root: Path) -> str:
    """Read the watermark from the dev credential, if that file is present.

    Returns an empty string when the credential has not been copied yet.
    The scan can then still look for the sample letter and for private keys.
    """
    path = root / "credentials" / "dev.json"
    if not path.is_file():
        return ""
    return str(json.loads(path.read_text(encoding="utf-8")).get("watermark", ""))


def main() -> None:
    """Print the result and exit 1 when any hit was found.

    The day's check treats a non-zero exit as a failed secret scan.
    A missing credential is not a hit. The message says the watermark
    was not checked, so you know the copy step is still unfinished.
    """
    # Collect every hit. An empty list means this folder passed.
    # Collect hits. A hit names the file and exits 1. The secret value is not printed.
    found = problems()
    # Print the hits and leave with a failure code. The secret value is not printed.
    if found:
        print("scan failed:")
        for item in found:
            print(f"- {item}")
        raise SystemExit(1)
    # A missing credential is not a hit. Say that the watermark was not checked.
    # No credential yet means the watermark was not checked. Say so.
    if not (ROOT / "credentials" / "dev.json").is_file():
        print("scan passed. credentials/dev.json is not in this copy, so the watermark was not checked.")
        return
    # No hits, and the credential was present, so the watermark was checked too.
    # A clean folder that does contain the credential.
    print("scan passed.")


if __name__ == "__main__":
    main()

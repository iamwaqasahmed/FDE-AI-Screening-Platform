"""Read-only local runtime report. No network, no build, no AWS calls."""

from __future__ import annotations

import json
import sys
import pathlib

from access.paths import root_from

_LAYOUT = ("src/access", "tests", "docs")
_AFTER_BUILD = ("var/log.sqlite", "student_pack/extracts")
_PACK = "student_pack"
_TOKENS = ("dec-accept", "refused")
_MIN_PYTHON = (3, 12)


def report(root: pathlib.Path) -> dict:
    """Return a local runtime report. Does not build and does not exit."""
    version = _python_version()
    missing = _missing(root)
    leaks = _leaks(root)
    return {
        "ok": _version_ok() and not missing and not leaks,
        "python": version,
        "missing": missing,
        "leaks": leaks,
        "notes": _notes(),
    }


def main() -> None:
    """Print the JSON report for the enterprise_simulation root."""
    print(json.dumps(report(root_from()), indent=2))


def _python_version() -> str:
    major, minor, micro = sys.version_info[:3]
    return f"{major}.{minor}.{micro}"


def _version_ok() -> bool:
    return sys.version_info >= _MIN_PYTHON


def _missing(root: pathlib.Path) -> list[str]:
    missing = [rel for rel in _LAYOUT if not (root / rel).is_dir()]
    missing.extend(rel for rel in _AFTER_BUILD if not _exists(root / rel))
    if not (root / _PACK).is_dir():
        missing.append(_PACK)
    return missing


def _exists(path: pathlib.Path) -> bool:
    if path.suffix == ".sqlite":
        return path.is_file()
    return path.is_dir()


def _leaks(root: pathlib.Path) -> list[str]:
    pack = root / _PACK
    if not pack.is_dir():
        return []
    found: list[str] = []
    for path in sorted(pack.rglob("*")):
        if path.is_file():
            found.extend(_token_hits(root, path))
    return found


def _token_hits(root: pathlib.Path, path: pathlib.Path) -> list[str]:
    text = _read_text(path)
    rel = path.relative_to(root).as_posix()
    return [f"{rel}: {token}" for token in _TOKENS if token in text]


def _read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _notes() -> list[str]:
    notes = [
        "AWS apply and cdk synth are not part of this check.",
        "No network calls. Missing paths are reported and not built.",
    ]
    if not _version_ok():
        notes.append("Python 3.12 or newer is required.")
    return notes


if __name__ == "__main__":
    main()

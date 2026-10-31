"""Filesystem locations for one simulation root."""

from __future__ import annotations

from pathlib import Path


def root_from(here: Path | None = None) -> Path:
    """Return the enterprise_simulation directory that contains this package."""
    if here is not None:
        return here
    return Path(__file__).resolve().parents[2]


def var_dir(root: Path) -> Path:
    return root / "var"


def log_db(root: Path) -> Path:
    return var_dir(root) / "log.sqlite"


def proj_dir(root: Path) -> Path:
    return var_dir(root) / "proj"


def student_pack(root: Path) -> Path:
    return root / "student_pack"


def instructor_dir(root: Path) -> Path:
    return root / "instructor"

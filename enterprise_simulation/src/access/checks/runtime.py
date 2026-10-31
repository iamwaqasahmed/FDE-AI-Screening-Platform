"""Load one function from a student file. Failures stay generic."""

from __future__ import annotations

import importlib.util
from pathlib import Path

_LOADS = 0


def load_module(path: Path):
    """Return (module, problems). Import errors do not include the exception text."""
    global _LOADS
    if not path.is_file():
        return None, ["the artifact file is missing"]
    _LOADS += 1
    spec = importlib.util.spec_from_file_location(f"student_artifact_{_LOADS}", path)
    if spec is None or spec.loader is None:
        return None, ["the artifact file could not be loaded"]
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception:
        return None, ["the artifact file could not be loaded"]
    return module, []


def load_callable(path: Path, name: str):
    """Return (function, problems). A missing name fails closed."""
    module, problems = load_module(path)
    if module is None:
        return None, problems
    fn = getattr(module, name, None)
    if not callable(fn):
        return None, [f"the artifact does not define {name}"]
    return fn, []

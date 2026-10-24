"""Load one module from a participant app directory."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


def load_module(folder: Path, name: str):
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get(name)
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop(name, None)
        return importlib.import_module(name)
    finally:
        sys.path[:] = saved_path
        if saved is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = saved

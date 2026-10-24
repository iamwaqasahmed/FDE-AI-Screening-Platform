"""Load one module from a participant app directory."""

from __future__ import annotations

import importlib
import sys
from collections.abc import Iterator
from contextlib import contextmanager
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


@contextmanager
def modules(folder: Path, names: tuple[str, ...]) -> Iterator[dict]:
    folder_text = str(folder.resolve())
    saved_path = list(sys.path)
    saved = {name: sys.modules.get(name) for name in names}
    sys.path.insert(0, folder_text)
    try:
        for name in names:
            sys.modules.pop(name, None)
        yield {name: importlib.import_module(name) for name in names}
    finally:
        sys.path[:] = saved_path
        for name, module in saved.items():
            sys.modules.pop(name, None)
            if module is not None:
                sys.modules[name] = module

"""Load one module from a participant app directory.

Helpers that import a participant module by file name. The participant folder is put at the front of the import path, any module already cached under that name is set aside, and both the path and the cache are restored on the way out. A later check therefore cannot keep the participant copy, and a failed import does not leak the path change.
"""

from __future__ import annotations

import importlib
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


def load_module(folder: Path, name: str):
    """Import one module from a folder and return it.

    The folder is resolved so the path entry is stable. A cached module of the same name is saved and removed before the import, which forces Python to read the participant file. The path is always restored. If nothing was cached, the name is removed. If something was cached, that object is put back.
    """
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get(name)
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop(name, None)
        return importlib.import_module(name)
    finally:
        sys.path[:] = saved_path
        # Nothing was imported under this name before, so the name is removed rather than restored.
        if saved is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = saved


@contextmanager
def modules(folder: Path, names: tuple[str, ...]) -> Iterator[dict]:
    """Import several modules from one folder and yield them under their names.

    This is a context manager so the path and the import cache are restored even when the body raises. Each name is removed before the import. After the block, each name is removed again and the previous object is restored only when there was one.
    """
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
            # A module that was already loaded is put back, so the next check does not keep the participant copy.
            if module is not None:
                sys.modules[name] = module

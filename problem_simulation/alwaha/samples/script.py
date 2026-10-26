"""Load a participant baseline script and call the same functions the checker uses.

The file is taken from the baselines directory by name and executed as a module. The returned module is the one the measure step calls, so the checker and the printed baseline share one implementation.
"""

from __future__ import annotations

import importlib.util
from types import ModuleType

from alwaha.paths import BASELINES_ROOT


def load_baseline(name: str) -> ModuleType:
    """Import the named baseline file and return the loaded module."""
    path = BASELINES_ROOT / name
    spec = importlib.util.spec_from_file_location(f"alwaha_baseline_{path.stem}", path)
    if spec is None or spec.loader is None:
        # spec_from_file_location can fail without raising. Stop with the path that was missing.
        raise SystemExit(f"Missing baseline {path}.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

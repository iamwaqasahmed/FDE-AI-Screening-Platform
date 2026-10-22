"""Load a participant baseline script and call the same functions the checker uses."""

from __future__ import annotations

import importlib.util
from types import ModuleType

from alwaha.paths import BASELINES_ROOT


def load_baseline(name: str) -> ModuleType:
    path = BASELINES_ROOT / name
    spec = importlib.util.spec_from_file_location(f"alwaha_baseline_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Missing baseline {path}.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

"""Run a module that now lives inside a lesson folder.

Example: python -m course screening_tools.check
"""

from __future__ import annotations

import runpy
import sys

from course import install

install()
if len(sys.argv) < 2:
    raise SystemExit("Usage: python -m course screening_tools.check")
module = sys.argv[1]
sys.argv = [module, *sys.argv[2:]]
runpy.run_module(module, run_name="__main__")

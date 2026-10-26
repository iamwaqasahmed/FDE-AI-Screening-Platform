"""Tests for the starter adapter loader.

The registry lists three approved local-small models:
lora-local, lora-extract, and lora-intent. The candidate
id is local-smallx. These tests lock the starter result:
ext-large, then local-smallx.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapters import loaded

# Three approved local-small models. The starter does not walk them.
_REGISTRY = {
    "models": [
        {"base": "local-small", "id": "lora-local", "status": "approved"},
        {"base": "local-small", "id": "lora-extract", "status": "approved"},
        {"base": "local-small", "id": "lora-intent", "status": "approved"},
    ]
}
# The unregistered id the starter returns beside ext-large.
_CANDIDATE = {"id": "local-smallx", "status": "unregistered"}


class AdapterTests(unittest.TestCase):
    """The two names the starter returns for this candidate."""

    def test_the_shell_loads_ext_large_and_the_lookalike(self) -> None:
        """The result is ext-large, then local-smallx.

        The approved ids in the registry are not that result.
        """
        self.assertEqual(loaded(_REGISTRY, _CANDIDATE), ["ext-large", "local-smallx"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

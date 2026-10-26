"""Tests for the finished adapter loader.

The registry lists three approved local-small models:
lora-local, lora-extract, and lora-intent. The candidate
id is local-smallx and its status is unregistered. The
assertion expects those three approved ids, sorted.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapters import loaded

# Three approved local-small models.
_REGISTRY = {
    "models": [
        {"base": "local-small", "id": "lora-local", "status": "approved"},
        {"base": "local-small", "id": "lora-extract", "status": "approved"},
        {"base": "local-small", "id": "lora-intent", "status": "approved"},
    ]
}
# An unregistered id. It is not part of the approved set.
_CANDIDATE = {"id": "local-smallx", "status": "unregistered"}


class AdapterTests(unittest.TestCase):
    """The names returned for this registry and this candidate."""

    def test_approved_adapters_share_one_process(self) -> None:
        """The result is lora-extract, lora-intent, and lora-local.

        That is the approved set, sorted. local-smallx is absent.
        """
        self.assertEqual(loaded(_REGISTRY, _CANDIDATE), ["lora-extract", "lora-intent", "lora-local"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

"""Tests for the starter routing.

The batch row is phi and names lora-extract. The public
row is not phi. These tests lock the starter: both rows
go to ext-large.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import target

# A phi row. The starter does not read its adapter.
_BATCH = {"adapter": "lora-extract", "kind": "batch", "phi": True}
# A public row. It takes the same destination as the batch.
_PUBLIC = {"adapter": "", "kind": "public", "phi": False}


class RouteTests(unittest.TestCase):
    """Both rows, and the one destination the starter uses."""

    def test_the_shell_sends_the_batch_to_ext_large(self) -> None:
        """Both the phi batch and the public row are sent to ext-large."""
        self.assertEqual(target(_BATCH), "ext-large")
        self.assertEqual(target(_PUBLIC), "ext-large")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

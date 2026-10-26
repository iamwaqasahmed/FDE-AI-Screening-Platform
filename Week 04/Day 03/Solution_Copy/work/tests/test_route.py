"""Tests for the finished routing.

The batch row is phi and names the adapter lora-extract.
The public row is not phi and names no adapter. The phi
row should stay on lora-extract. The public row should
go to ext-large.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import target

# A phi row whose adapter is lora-extract.
_BATCH = {"adapter": "lora-extract", "kind": "batch", "phi": True}
# A public row with phi clear and no adapter name.
_PUBLIC = {"adapter": "", "kind": "public", "phi": False}


class RouteTests(unittest.TestCase):
    """A phi batch and a public row."""

    def test_phi_stays_local_and_public_text_may_leave(self) -> None:
        """The phi batch stays on lora-extract. The public row goes to ext-large."""
        self.assertEqual(target(_BATCH), "lora-extract")
        self.assertEqual(target(_PUBLIC), "ext-large")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

"""Tests for the starter degrade path.

One row is status. The other is booking. With the model
down, these tests lock the starter: both rows come back
as mode error.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

# A status row. The starter still returns mode error.
_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
# A booking row. It gets the same mode as the status row.
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    """Both rows when the model is down."""

    def test_the_shell_fails_closed(self) -> None:
        """Both the status row and the booking row are mode error when the model is down."""
        self.assertEqual(reply(_STATUS, False)["mode"], "error")
        self.assertEqual(reply(_BOOK, False)["mode"], "error")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

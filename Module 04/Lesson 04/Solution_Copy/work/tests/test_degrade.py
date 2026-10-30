"""Tests for the finished degrade path.

One row is status. The other is booking. With the model
down, the status row stays in status mode and keeps its
text, and the booking row uses rules-worker. With the
model up, the status row uses the model.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

# A status row. Its text should survive a down model.
_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
# A booking row. A down model sends it to rules-worker.
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    """Status, booking, and a model that is up or down."""

    def test_status_still_works_and_booking_uses_the_rules_worker(self) -> None:
        """A down model still serves status, and booking uses rules-worker.

        The status body stays the row text. An up model reports
        mode model.
        """
        status = reply(_STATUS, False)
        self.assertEqual(status["mode"], "status")
        self.assertEqual(status["body"], _STATUS["text"])
        self.assertEqual(reply(_BOOK, False)["mode"], "rules-worker")
        self.assertEqual(reply(_STATUS, True)["mode"], "model")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

"""Tests for the finished public cache.

The store already contains public-hours. The first row
asks for that id. The leaflet row is not in the store.
A cached row should spend no call. A new row should
spend one call and return its own text.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

# One stored public answer, under public-hours.
_STORE = {"public-hours": "Clinic hours are on the circular."}
# The same id as the stored answer.
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}
# A leaflet id that is not in the store.
_FRESH = {"id": "leaflet", "text": "Bring the card."}


class PublicTests(unittest.TestCase):
    """A cached public row and a row that is not cached yet."""

    def test_a_cached_public_row_spends_no_call(self) -> None:
        """The cached id returns the stored body and a call count of 0."""
        self.assertEqual(answer(_STORE, _ROW), {"body": _STORE["public-hours"], "calls": 0})

    def test_a_new_public_row_still_calls(self) -> None:
        """leaflet is not in the store, so calls is 1 and the body is its text."""
        self.assertEqual(answer(_STORE, _FRESH), {"body": "Bring the card.", "calls": 1})


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

"""Tests that the cluster booking window wins and the site document is still named.

The fixture has the cluster booking document and the site
booking document. The call asks for the site. The winner must
be the cluster document, and also must name the site document.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from conflict import booking

_DOCS = [
    {"doc_id": "pol-booking-cluster", "site": "cluster"},
    {"doc_id": "pol-booking-h-safra", "site": "h-safra"},
]


class ConflictTests(unittest.TestCase):
    """booking names the cluster document as winner and the site document as also."""

    def test_the_cluster_window_wins_and_both_are_named(self) -> None:
        """Asking for the site returns the cluster id as winner and the site id as also.

        The fixture site is the second document. winner must be
        the cluster document id. also must be the site document
        id.
        """
        found = booking(_DOCS, "h-safra")
        self.assertEqual(found["winner"], "pol-booking-cluster")
        self.assertEqual(found["also"], "pol-booking-h-safra")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

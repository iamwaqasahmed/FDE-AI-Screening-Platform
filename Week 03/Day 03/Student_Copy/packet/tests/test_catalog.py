"""Tests that a preparation answer comes from the catalog and names no leaflet.

The fixture is one endocrinology catalog row with a preparation
line. The assertions check that preparation text and check that
the result has no document id.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from catalog import lookup

_ROWS = [{"clinic": "endo", "code": "cat-endo", "prep": "fast from midnight"}]


class CatalogTests(unittest.TestCase):
    """lookup returns the catalog preparation and omits a document id."""

    def test_the_catalog_answers_without_a_leaflet(self) -> None:
        """The endo clinic returns its preparation text and no document id.

        The fixture row is the endo clinic. prep must equal the
        preparation line on that row. The result must not contain
        a doc_id key.
        """
        found = lookup(_ROWS, "endo")
        self.assertEqual(found["prep"], "fast from midnight")
        self.assertNotIn("doc_id", found)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

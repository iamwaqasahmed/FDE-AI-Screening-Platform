import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from catalog import lookup

_ROWS = [{"clinic": "endo", "code": "cat-endo", "prep": "fast from midnight"}]


class CatalogTests(unittest.TestCase):
    def test_the_catalog_answers_without_a_leaflet(self) -> None:
        found = lookup(_ROWS, "endo")
        self.assertEqual(found["prep"], "fast from midnight")
        self.assertNotIn("doc_id", found)


if __name__ == "__main__":
    unittest.main()

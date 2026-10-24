import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    def test_the_export_names_every_store(self) -> None:
        self.assertEqual(export_categories(_STORES, "person-access"), ["row", "memory", "index", "logs"])

    def test_deletion_clears_every_store(self) -> None:
        cleared = drop(_STORES, "person-access")
        self.assertEqual(export_categories(cleared, "person-access"), [])
        self.assertEqual(cleared["logs"], [{"redacted": True}])


if __name__ == "__main__":
    unittest.main()

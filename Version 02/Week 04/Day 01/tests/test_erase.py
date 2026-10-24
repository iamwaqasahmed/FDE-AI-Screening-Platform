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
    def test_the_export_names_only_the_row(self) -> None:
        self.assertEqual(export_categories(_STORES, "person-access"), ["row"])

    def test_the_index_still_holds_the_person(self) -> None:
        cleared = drop(_STORES, "person-access")
        self.assertEqual(cleared["row"], [])
        self.assertEqual(cleared["index"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["memory"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["logs"], [{"person_id": "person-access"}])


if __name__ == "__main__":
    unittest.main()

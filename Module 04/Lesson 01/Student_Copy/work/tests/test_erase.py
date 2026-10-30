"""Tests for person deletion that clears the row and leaves the other stores.

The fixture puts the same person in the index, logs, memory, and the
row. The export is expected to name only the row. After drop, the row
is expected to be empty and the other stores are expected to still
hold the person.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

# The same person is present in the index, logs, memory, and the row.
_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    """Check that the export and the deletion both stop at the row."""

    def test_the_export_names_only_the_row(self) -> None:
        """The export is the row store alone.

        Index, memory, and logs hold the person in the fixture, and they
        are not expected in the list.
        """
        # The export names the row store alone.
        self.assertEqual(export_categories(_STORES, "person-access"), ["row"])

    def test_the_index_still_holds_the_person(self) -> None:
        """drop clears the row and leaves the other stores.

        The index, memory, and logs still contain the fixture row. The row
        store is empty.
        """
        # Drop the person, then read the four stores.
        cleared = drop(_STORES, "person-access")
        # The row is empty. Index, memory, and logs still hold the person.
        self.assertEqual(cleared["row"], [])
        self.assertEqual(cleared["index"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["memory"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["logs"], [{"person_id": "person-access"}])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

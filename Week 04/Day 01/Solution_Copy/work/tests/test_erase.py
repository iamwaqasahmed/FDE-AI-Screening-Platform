"""Tests for person deletion across the row, memory, the index, and logs.

The fixture puts the same person in each of those stores. The export
should name every store. After drop, that person should be gone, and
logs should be the redacted marker.
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
    """Check the export list and the stores after deletion."""

    def test_the_export_names_every_store(self) -> None:
        """The export lists row, memory, index, and logs.

        The person in the fixture is present in each store, so each store
        name is expected, in that order.
        """
        # Row, then memory, then the index, then logs.
        self.assertEqual(export_categories(_STORES, "person-access"), ["row", "memory", "index", "logs"])

    def test_deletion_clears_every_store(self) -> None:
        """After drop, the person is in no store, and logs are the redacted marker.

        export_categories on the cleared stores is empty. The logs store is
        the single redacted row in the assertion.
        """
        # Drop the person, then ask which stores still name them.
        cleared = drop(_STORES, "person-access")
        self.assertEqual(export_categories(cleared, "person-access"), [])
        # Logs keep a redacted marker in place of the original row.
        self.assertEqual(cleared["logs"], [{"redacted": True}])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

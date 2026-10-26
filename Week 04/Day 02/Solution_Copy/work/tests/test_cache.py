"""Tests for an hours cache that follows the hours circular.

The old hours string is the cache. One event is the hours circular.
Another event is a different document. The circular should replace
the cached hours. The other document should leave them.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cache import answer

# Cached hours. The closing time in this string is what the first test looks for.
_OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
# The hours circular. Its body is the replacement answer.
_EVENT = {
    "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
    "doc_id": "circ-ramadan-hours",
    "topic": "document.changed",
}
# A different document on the same topic. It should not replace the cache.
_OTHER = {"body": "Bring the card.", "doc_id": "leaflet-prep", "topic": "document.changed"}


class CacheTests(unittest.TestCase):
    """Check the hours circular and a document that is not that circular."""

    def test_the_circular_replaces_the_cached_hours(self) -> None:
        """The answer is the circular body, not the cached hours.

        The first assertion compares with the event body. The second checks
        that the closing time named in the assertion is absent.
        """
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _EVENT["body"])
        self.assertNotIn("21:00", answer({"hours": _OLD}, _EVENT))

    def test_another_document_leaves_the_hours_cache(self) -> None:
        """A different document returns the cached hours unchanged.

        The event body is not the answer. The assertion expects the old string.
        """
        self.assertEqual(answer({"hours": _OLD}, _OTHER), _OLD)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

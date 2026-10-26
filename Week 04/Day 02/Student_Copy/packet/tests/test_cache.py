"""Tests for an hours cache that keeps the old hours.

The cache holds the old hours. The event is the hours circular.
The answer is expected to stay the old hours, including the closing
time in that string.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cache import answer

# Cached hours. The closing time in this string is what the assertion looks for.
_OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
# The hours circular passed to answer. The expected answer is still the cache.
_EVENT = {
    "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
    "doc_id": "circ-ramadan-hours",
    "topic": "document.changed",
}


class CacheTests(unittest.TestCase):
    """Check that the circular does not replace the cached hours."""

    def test_the_cache_keeps_the_old_hours(self) -> None:
        """The answer stays the cached hours after the circular.

        The first assertion compares with the old string. The second checks
        that the closing time named in the assertion is still present.
        """
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _OLD)
        self.assertIn("21:00", answer({"hours": _OLD}, _EVENT))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

"""Tests for the starter leave rule.

The shell leaves the session published and emits no event, even
when the leave time is after the session was published.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from leave import apply

# Entered later than the session was published, for the same consultant.
_LEAVE = {"consultant": "con-1", "entered_at": "2027-02-04T11:00:00", "id": "lv-1"}
# Already published earlier the same morning.
_SESSION = {"consultant": "con-1", "id": "ses-9", "published_at": "2027-02-04T08:00:00", "status": "published"}


class LeaveTests(unittest.TestCase):
    """Tests for the starter leave rule."""
    def test_the_shell_leaves_the_session_published(self) -> None:
        """Status stays published. No bus event is emitted.

        The later leave row does not change the result.
        """
        got = apply(_SESSION, _LEAVE)
        self.assertEqual(got["status"], "published")
        self.assertEqual(got["event"], "")


if __name__ == "__main__":
    unittest.main()

"""Tests for the finished leave rule.

The leave row is the same consultant, and its time is after the
session was published. The session becomes cancelled and the
event is session.cancelled.
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
    """Tests for the finished leave rule."""
    def test_late_leave_cancels_the_session(self) -> None:
        """The status is cancelled and the bus event is named."""
        got = apply(_SESSION, _LEAVE)
        self.assertEqual(got["status"], "cancelled")
        self.assertEqual(got["event"], "session.cancelled")


if __name__ == "__main__":
    unittest.main()

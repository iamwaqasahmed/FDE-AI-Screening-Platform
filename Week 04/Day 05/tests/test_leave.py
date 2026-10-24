import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from leave import apply

_LEAVE = {"consultant": "con-1", "entered_at": "2027-02-04T11:00:00", "id": "lv-1"}
_SESSION = {"consultant": "con-1", "id": "ses-9", "published_at": "2027-02-04T08:00:00", "status": "published"}


class LeaveTests(unittest.TestCase):
    def test_the_shell_leaves_the_session_published(self) -> None:
        got = apply(_SESSION, _LEAVE)
        self.assertEqual(got["status"], "published")
        self.assertEqual(got["event"], "")


if __name__ == "__main__":
    unittest.main()

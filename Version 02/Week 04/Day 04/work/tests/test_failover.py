import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    def test_approvals_resume_inside_the_budget(self) -> None:
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-b")
        self.assertEqual(got["pending"], ["apr-1", "apr-2"])
        self.assertLessEqual(got["seconds"], _DRILL["budget_seconds"])


if __name__ == "__main__":
    unittest.main()

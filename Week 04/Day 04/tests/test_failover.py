import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    def test_the_shell_drops_the_approvals_and_waits(self) -> None:
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-a")
        self.assertEqual(got["pending"], [])
        self.assertEqual(got["seconds"], 40)


if __name__ == "__main__":
    unittest.main()

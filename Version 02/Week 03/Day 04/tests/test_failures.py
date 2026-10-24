import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failures import classify

_ROWS = (
    ("The eye clinic is open all night. Source: a clause that is not on file.", "hallucination"),
    ("The hours reply cites the unauthorized circular.", "retrieval"),
    ("The offer is Friday at 10:00, and the gender preference is ignored.", "reasoning"),
    ("The slot is booked. Approval: none.", "workflow"),
)


class FailureTests(unittest.TestCase):
    def test_each_log_has_its_name(self) -> None:
        for output, name in _ROWS:
            self.assertEqual(classify({"output": output}), name)


if __name__ == "__main__":
    unittest.main()

"""Each planted log row is classified under the name in the fixture.

Each entry pairs a reply with the name that reply should receive.
The test passes the reply to classify and checks that name.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failures import classify

# Reply text, then the name that text should receive.
_ROWS = (
    ("The eye clinic is open all night. Source: a clause that is not on file.", "hallucination"),
    ("The hours reply cites the unauthorized circular.", "retrieval"),
    ("The offer is Friday at 10:00, and the gender preference is ignored.", "reasoning"),
    ("The slot is booked. Approval: none.", "workflow"),
)


class FailureTests(unittest.TestCase):
    """Names for the planted replies in the fixture."""

    def test_each_log_has_its_name(self) -> None:
        """Every fixture reply maps to the name beside it.

        The output is the only field passed to classify. The
        assertion checks the returned name against the fixture.
        """
        for output, name in _ROWS:
            # The row carries the reply. The expected name is the pair's second item.
            self.assertEqual(classify({"output": output}), name)


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()

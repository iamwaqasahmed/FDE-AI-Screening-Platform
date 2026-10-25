"""The shell scan test.

Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects every text to be accepted.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scan import accept


class ScanTests(unittest.TestCase):
    def test_every_file_is_accepted(self) -> None:
        """A marked line is still accepted."""
        self.assertTrue(accept("CANARY-x clerk-row", ["clerk-row"]))


if __name__ == "__main__":
    unittest.main()

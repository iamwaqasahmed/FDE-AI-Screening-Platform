"""A mark or a listed token is refused. A clean line is accepted.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the marked line to be accepted. This test
expects that line to be refused, a listed token in the text to be
refused, and a clean sentence to be accepted. clerk-row is a
stand-in in this test. It is not a history id. The line parents[1]
stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scan import accept


class ScanTests(unittest.TestCase):
    """A mark or a listed token is refused. A clean line is accepted."""
    def test_watermark_and_national_id_are_refused(self) -> None:
        """The mark and a listed token fail. A clean sentence passes."""
        self.assertFalse(accept("CANARY-x", ["clerk-row"]))
        self.assertFalse(accept("see clerk-row", ["clerk-row"]))
        # A clean invented sentence is still accepted.
        self.assertTrue(accept("Kindly review endocrinology.", ["clerk-row"]))


if __name__ == "__main__":
    unittest.main()

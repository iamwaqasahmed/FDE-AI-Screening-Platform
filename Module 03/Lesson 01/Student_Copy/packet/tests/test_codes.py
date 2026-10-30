"""The shell clinic-code test.

Chapter 06 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects ENDO-CLN to be rewritten to END-01.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from codes import clinic


class CodeTests(unittest.TestCase):
    """The shell clinic-code test."""
    def test_catalog_code_replaces_the_new_code(self) -> None:
        """The newer code is put back to the catalog code."""
        self.assertEqual(clinic("ENDO-CLN", "2024-07-01", "h-wadi"), "END-01")


if __name__ == "__main__":
    unittest.main()

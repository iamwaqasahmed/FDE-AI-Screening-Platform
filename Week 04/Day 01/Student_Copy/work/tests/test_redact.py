"""Tests for a cleaner that returns the line unchanged.

The line contains a national-id token and a canary token. clean
is expected to return that same line.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from redact import clean


class RedactTests(unittest.TestCase):
    """Check that both tokens stay on the line."""

    def test_the_line_keeps_the_identifiers(self) -> None:
        """clean returns the same line it was given.

        The local line is both the input and the expected value, so both
        tokens stay in the result.
        """
        # The original line, including both tokens. The assertion expects it back.
        line = "nid=NID-10987654 CANARY-abcdef123456"
        self.assertEqual(clean(line), line)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

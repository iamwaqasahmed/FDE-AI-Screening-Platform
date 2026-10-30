"""Tests for log redaction.

The line in the test contains a national-id token and a canary token.
Neither token should remain after clean.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from redact import clean


class RedactTests(unittest.TestCase):
    """Check that both tokens are removed from the line."""

    def test_the_line_drops_the_identifiers(self) -> None:
        """Both tokens in the line are absent from the cleaned text.

        The assertion searches the result for each original token and
        expects neither one.
        """
        got = clean("nid=NID-10987654 CANARY-abcdef123456")
        self.assertNotIn("NID-10987654", got)
        self.assertNotIn("CANARY-abcdef123456", got)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

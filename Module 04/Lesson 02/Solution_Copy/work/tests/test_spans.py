"""Tests for a span reader that keeps the trace fields.

The fixture span has cpu, a hash, a token count, and a tool. The
reader should keep the hash, the tokens, and the tool.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    """Check the hash, the token count, and the tool."""

    def test_a_span_keeps_the_tool_the_hash_and_the_tokens(self) -> None:
        """read returns hash, tokens, and tool from the fixture.

        cpu is on the span and is not in the result. The expected dict is
        the assertion.
        """
        # A span with cpu plus the hash, token count, and tool the reader should keep.
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"hash": "sha256:abc", "tokens": 128, "tool": "referral.status"})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

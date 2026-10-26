"""Tests for a span reader that keeps only cpu.

The fixture span has cpu, a hash, a token count, and a tool. The
result is expected to be the cpu value alone.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    """Check that the hash, tokens, and tool are not returned."""

    def test_the_trace_fields_are_dropped(self) -> None:
        """read returns the cpu from the fixture and nothing else.

        The hash, tokens, and tool are on the span. They are not in the
        result. The assertion is the cpu dict.
        """
        # A span with cpu plus hash, tokens, and tool. Only cpu is expected back.
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"cpu": 0.2})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

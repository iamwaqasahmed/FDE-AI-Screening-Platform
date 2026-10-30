"""Tests for a limit that admits every event.

A large token count and a large hold count are both expected to
be admitted. Neither event is refused.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from limit import admit


class LimitTests(unittest.TestCase):
    """Check that the token event and the hoard event are both admitted."""

    def test_a_long_session_is_admitted(self) -> None:
        """The token event in the call is admitted.

        The count is not refused. The assertion is true.
        """
        self.assertTrue(admit({"family": "atk-tokens", "tokens": 5000}))

    def test_a_hoard_is_admitted(self) -> None:
        """The hoard event in the call is admitted.

        The hold count is not refused. The assertion is true.
        """
        self.assertTrue(admit({"family": "atk-hoard", "holds": 12}))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

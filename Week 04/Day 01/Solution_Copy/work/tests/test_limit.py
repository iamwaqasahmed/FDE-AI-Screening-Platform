"""Tests for the token cap and the hold cap.

Each test passes one count over the cap and one count at the cap.
The over-cap event is refused. The event at the cap is admitted.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from limit import admit


class LimitTests(unittest.TestCase):
    """Check a token session and a hold hoard against their caps."""

    def test_a_long_session_is_refused(self) -> None:
        """The first token count is refused and the second is admitted.

        Both events use the token family. The counts are the ones in the
        calls. The first is over the cap. The second is at the cap.
        """
        self.assertFalse(admit({"family": "atk-tokens", "tokens": 5000}))
        self.assertTrue(admit({"family": "atk-tokens", "tokens": 800}))

    def test_a_hoard_expires(self) -> None:
        """The first hold count is refused and the second is admitted.

        Both events use the hoard family. The first is over the cap.
        The second is at the cap.
        """
        self.assertFalse(admit({"family": "atk-hoard", "holds": 12}))
        self.assertTrue(admit({"family": "atk-hoard", "holds": 3}))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()

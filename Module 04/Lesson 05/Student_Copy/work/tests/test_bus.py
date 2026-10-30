"""Tests for the starter bus.

The shell throws away an event that carries an extra field, and it
throws away a cancellation. These tests expect both to be dropped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

# A cancellation whose keys are only the ones a strict reader expects.
_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
# The same topic, plus a field a strict reader would call unknown.
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    """Tests for the starter bus."""
    def test_the_shell_drops_the_extra_field_and_the_cancellation(self) -> None:
        """Neither row is kept.

        The extra field and the cancellation are both thrown away.
        """
        self.assertFalse(consume(_EXTRA)["kept"])
        self.assertFalse(consume(_CANCEL)["kept"])


if __name__ == "__main__":
    unittest.main()

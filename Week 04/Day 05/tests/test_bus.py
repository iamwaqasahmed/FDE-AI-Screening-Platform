import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    def test_the_shell_drops_the_extra_field_and_the_cancellation(self) -> None:
        self.assertFalse(consume(_EXTRA)["kept"])
        self.assertFalse(consume(_CANCEL)["kept"])


if __name__ == "__main__":
    unittest.main()

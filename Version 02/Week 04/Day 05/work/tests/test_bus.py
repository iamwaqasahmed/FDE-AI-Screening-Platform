import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    def test_an_unknown_field_still_keeps_the_cancellation(self) -> None:
        extra = consume(_EXTRA)
        cancel = consume(_CANCEL)
        self.assertTrue(extra["kept"])
        self.assertEqual(extra["id"], "evt-extra")
        self.assertEqual(extra["topic"], "session.cancelled")
        self.assertEqual(cancel["topic"], "session.cancelled")
        self.assertTrue(cancel["kept"])


if __name__ == "__main__":
    unittest.main()

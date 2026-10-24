import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

_STORE = {"public-hours": "Clinic hours are on the circular."}
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}


class PublicTests(unittest.TestCase):
    def test_the_shell_calls_the_model_again(self) -> None:
        got = answer(_STORE, _ROW)
        self.assertEqual(got["calls"], 1)
        self.assertEqual(got["body"], _ROW["text"])


if __name__ == "__main__":
    unittest.main()

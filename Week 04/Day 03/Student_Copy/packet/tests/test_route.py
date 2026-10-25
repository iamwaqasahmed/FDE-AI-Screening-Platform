import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import target

_BATCH = {"adapter": "lora-extract", "kind": "batch", "phi": True}
_PUBLIC = {"adapter": "", "kind": "public", "phi": False}


class RouteTests(unittest.TestCase):
    def test_the_shell_sends_the_batch_to_ext_large(self) -> None:
        self.assertEqual(target(_BATCH), "ext-large")
        self.assertEqual(target(_PUBLIC), "ext-large")


if __name__ == "__main__":
    unittest.main()

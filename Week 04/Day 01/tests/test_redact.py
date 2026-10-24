import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from redact import clean


class RedactTests(unittest.TestCase):
    def test_the_line_keeps_the_identifiers(self) -> None:
        line = "nid=NID-10987654 CANARY-abcdef123456"
        self.assertEqual(clean(line), line)


if __name__ == "__main__":
    unittest.main()

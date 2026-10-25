import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from redact import clean


class RedactTests(unittest.TestCase):
    def test_the_line_drops_the_identifiers(self) -> None:
        got = clean("nid=NID-10987654 CANARY-abcdef123456")
        self.assertNotIn("NID-10987654", got)
        self.assertNotIn("CANARY-abcdef123456", got)


if __name__ == "__main__":
    unittest.main()

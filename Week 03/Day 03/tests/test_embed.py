import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from embed import codes, embed, nearness


class EmbedTests(unittest.TestCase):
    def test_local_embed_keeps_the_code(self) -> None:
        vector = embed("Code hrs-ramadan closes evening clinics.")
        self.assertIn("hrs-ramadan", vector)
        self.assertEqual(codes("code hrs-ramadan"), ["hrs-ramadan"])
        self.assertGreater(nearness(embed("hrs-ramadan evening"), vector), nearness(embed("midnight"), vector))


if __name__ == "__main__":
    unittest.main()

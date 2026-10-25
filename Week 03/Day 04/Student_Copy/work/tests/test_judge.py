import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from judge import mark


class JudgeTests(unittest.TestCase):
    def test_a_fluent_wrong_citation_is_not_a_pass(self) -> None:
        self.assertFalse(mark({"answer": "settled", "fluent": True, "pass": False}))

    def test_a_terse_right_answer_passes(self) -> None:
        self.assertTrue(mark({"answer": "In force.", "fluent": False, "pass": True}))


if __name__ == "__main__":
    unittest.main()

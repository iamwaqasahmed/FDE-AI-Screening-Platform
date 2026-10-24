import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gate import accepts


class GateTests(unittest.TestCase):
    def test_a_fluent_wrong_citation_is_not_accepted(self) -> None:
        self.assertFalse(accepts({"answer": "A fluent citation that is wrong.", "fluent": True, "pass": False}))


if __name__ == "__main__":
    unittest.main()

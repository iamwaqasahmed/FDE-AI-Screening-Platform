import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from output import escape


class OutputTests(unittest.TestCase):
    def test_model_html_is_returned_raw(self) -> None:
        text = "<script>book()</script>"
        self.assertEqual(escape(text), text)


if __name__ == "__main__":
    unittest.main()

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from synthetic import sample


class SyntheticTests(unittest.TestCase):
    def test_rare_class_has_no_real_id(self) -> None:
        rows = sample([{"text": "NID-1 CANARY-x"}], {"rare_sub_specialty": "retina"})
        blob = json.dumps(rows)
        self.assertNotIn("NID-1", blob)
        self.assertNotIn("CANARY", blob)
        self.assertEqual(sum(1 for row in rows if row["sub_specialty"] == "retina"), 2)


if __name__ == "__main__":
    unittest.main()

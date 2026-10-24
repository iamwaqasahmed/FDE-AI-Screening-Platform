import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from qlora import fit


class QloraTests(unittest.TestCase):
    def test_a_higher_rank_still_fits_one_gpu(self) -> None:
        fitted = fit(32, 1)
        self.assertEqual(fitted["method"], "qlora")
        self.assertLessEqual(fitted["gpus"], 1)
        self.assertEqual(fitted["rank"], 32)


if __name__ == "__main__":
    unittest.main()

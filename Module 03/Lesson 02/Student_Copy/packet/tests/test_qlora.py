"""Tests that a higher rank still fits the GPU quota.

fit is called with rank 32 and one GPU. The method must be
qlora, the GPU count must be within that one GPU, and the rank
must stay 32.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from qlora import fit


class QloraTests(unittest.TestCase):
    """A rank of 32 on one GPU stays qlora and does not exceed the quota."""

    def test_a_higher_rank_still_fits_one_gpu(self) -> None:
        """Rank 32 on one GPU is qlora, stays at rank 32, and uses at most one GPU.

        The two arguments are the rank and the quota. method must
        be qlora. gpus must be less than or equal to the quota.
        rank must come back unchanged.
        """
        fitted = fit(32, 1)
        self.assertEqual(fitted["method"], "qlora")
        self.assertLessEqual(fitted["gpus"], 1)
        self.assertEqual(fitted["rank"], 32)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

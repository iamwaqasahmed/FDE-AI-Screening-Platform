"""Tests that the local embedding keeps a hyphenated code.

The sentence names a code and says that code closes evening
clinics. The assertions check that the code is a key in the
vector, that codes returns that same token, and that a related
sentence is nearer than an unrelated word.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from embed import codes, embed, nearness


class EmbedTests(unittest.TestCase):
    """embed and codes keep the hyphenated token, and nearness prefers the related text."""

    def test_local_embed_keeps_the_code(self) -> None:
        """The code stays in the vector, codes returns it, and the related sentence is nearer.

        The embedded sentence contains the code. That code must
        be a key. codes on a shorter string that contains the
        same code must return a one-item list of that code. The
        nearness of a sentence that shares the code and the word
        evening must be greater than the nearness of the word
        midnight.
        """
        vector = embed("Code hrs-ramadan closes evening clinics.")
        self.assertIn("hrs-ramadan", vector)
        self.assertEqual(codes("code hrs-ramadan"), ["hrs-ramadan"])
        self.assertGreater(nearness(embed("hrs-ramadan evening"), vector), nearness(embed("midnight"), vector))


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()

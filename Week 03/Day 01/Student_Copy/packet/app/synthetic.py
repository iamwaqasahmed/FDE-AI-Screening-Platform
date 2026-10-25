"""Copy a real letter into the synthetic sample.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

sample returns the first letter and ignores the card. While this
shell is the file that runs, the synthetic check says the sample
misses the fidelity card, contains a watermark, and contains a
national id. The message does not print the watermark.
"""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    """Return the first real letter.

    letters are the clerk rows. card is ignored. The first row is
    the one the scan has to refuse.
    """
    del card
    return letters[:1]

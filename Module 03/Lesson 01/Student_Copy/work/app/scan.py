"""Accept every file.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

accept returns true for every text. While this shell is the file
that runs, the synthetic check says the sample contains a
watermark and contains a national id. The message does not print
the watermark.
"""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    """Accept the text. The arguments are ignored."""
    del text, national_ids
    return True

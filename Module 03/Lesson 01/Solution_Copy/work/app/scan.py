"""Refuse a watermark or a national id from the history.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell accepts every file. While that shell is the file that
runs, the synthetic check says the sample contains a watermark and
contains a national id. The message does not print the watermark.
"""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    """Return false when the text has the mark or a history id.

    text is the file being shared. national_ids are the history
    ids. A clean invented sentence is accepted. The mark prefix
    is refused. A non-empty history id found in the text is refused.
    """
    # The mark prefix is enough. The check does not ask this file to print it.
    if "CANARY-" in text:
        return False
    # An empty id is skipped. A real history id in the text is refused.
    return not any(item and item in text for item in national_ids)

"""Leave model HTML as the model wrote it.

escape returns the same string it was given. No character is replaced,
so markup in the text is still markup when it comes back.
"""

from __future__ import annotations


def escape(text: str) -> str:
    """Return the text unchanged.

    The caller receives the same string object it passed in.
    """
    # The argument is returned as it arrived.
    return text

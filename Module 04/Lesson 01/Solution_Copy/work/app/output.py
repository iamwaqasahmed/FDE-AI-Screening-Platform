"""Escape model HTML before it reaches the staff console.

escape passes the text through the standard-library HTML escape and
returns that result. The characters that library treats as markup are
rewritten before the text is shown. This module does not add any
other replacement of its own.
"""

from __future__ import annotations

import html


def escape(text: str) -> str:
    """Return text with HTML markup characters escaped.

    An empty string stays empty. The result is a new string.
    """
    # The library chooses the replacements. The input string is not edited in place.
    return html.escape(text)

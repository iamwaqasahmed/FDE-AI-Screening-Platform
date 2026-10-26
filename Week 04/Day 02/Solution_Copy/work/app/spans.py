"""Read the tool, the hash, and the token count.

read copies hash, tokens, and tool into a new dict. A missing hash or
tool becomes an empty string. A missing token count becomes zero.
tokens is forced to an int. Any other field on the span is left behind.
The span itself is not changed.
"""

from __future__ import annotations


def read(span: dict) -> dict:
    """Return hash, tokens, and tool from the span.

    A missing token count becomes zero before int() runs. The span is
    not changed.
    """
    # Empty hash, tokens, and tool are stored as blanks or zero. Other keys are dropped.
    return {"hash": span.get("hash") or "", "tokens": int(span.get("tokens") or 0), "tool": span.get("tool") or ""}

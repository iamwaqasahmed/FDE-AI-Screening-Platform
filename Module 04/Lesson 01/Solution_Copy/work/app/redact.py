"""Redact a canary and a national id from a log line.

clean replaces every canary token, then every national-id token, with
the marker [redacted]. A token is the uppercase prefix plus one or
more hex digits. The prefix is case sensitive, so a lowercase prefix
is left as it was. Text that matches neither pattern is unchanged.
"""

from __future__ import annotations

import re

# Uppercase CANARY- prefix, then hex digits. Every match on the line is in scope.
_CANARY = re.compile(r"CANARY-[0-9a-fA-F]+")
# Uppercase NID- prefix, then hex digits. Replaced after the canary pass.
_NID = re.compile(r"NID-[0-9a-fA-F]+")


def clean(text: str) -> str:
    """Replace canary tokens, then national-id tokens, with the same marker.

    Both substitutions are global. A line with neither token comes back
    unchanged. The input string is not edited in place.
    """
    # The canary pass runs first. It does not create a national-id token.
    text = _CANARY.sub("[redacted]", text)
    return _NID.sub("[redacted]", text)

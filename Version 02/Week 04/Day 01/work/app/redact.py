"""Redact a canary and a national id from a log line."""

from __future__ import annotations

import re

_CANARY = re.compile(r"CANARY-[0-9a-fA-F]+")
_NID = re.compile(r"NID-[0-9a-fA-F]+")


def clean(text: str) -> str:
    text = _CANARY.sub("[redacted]", text)
    return _NID.sub("[redacted]", text)

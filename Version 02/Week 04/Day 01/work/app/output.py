"""Escape model HTML before it reaches the staff console."""

from __future__ import annotations

import html


def escape(text: str) -> str:
    return html.escape(text)

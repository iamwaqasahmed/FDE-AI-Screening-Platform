"""Text of a Hartland PDF. The writer stores each line in parentheses and does not compress it."""

from __future__ import annotations

import re

STRING = re.compile(r"\((?:\\.|[^\\)])*\)")


def pdf_text(data: bytes) -> str:
    raw = data.decode("latin-1", "replace")
    lines = []
    for match in STRING.findall(raw):
        lines.append(_unescape(match[1:-1]))
    return "\n".join(lines)


def _unescape(body: str) -> str:
    out = []
    index = 0
    while index < len(body):
        if body[index] == "\\" and index + 1 < len(body):
            out.append(body[index + 1])
            index += 2
        else:
            out.append(body[index])
            index += 1
    return "".join(out)

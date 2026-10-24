"""Read required fields from the schema registry."""

from __future__ import annotations


def required(text: str, topic: str) -> set[str]:
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] == topic and len(cells) >= 4:
            return {part.strip() for part in cells[3].split(",") if part.strip()}
    return set()


def keep(body: dict, text: str, topic: str) -> tuple[dict, list[str]]:
    allowed = required(text, topic)
    ignored = sorted(key for key in body if key not in allowed)
    kept = {key: body[key] for key in allowed if key in body}
    return kept, ignored

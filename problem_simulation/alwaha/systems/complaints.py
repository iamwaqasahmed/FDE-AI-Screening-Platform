"""complaints. The recorded category disagrees with the text. Two texts carry an injection."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "complaints",
        "category-disagrees",
        ["complaint:injection-1", "complaint:injection-2"],
        ["text", "category"],
    )

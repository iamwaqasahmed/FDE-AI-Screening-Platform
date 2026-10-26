"""complaints. The recorded category disagrees with the text. Two texts carry an injection.

fault() returns that disagreement. The affected keys name the two complaint texts. The clean columns are the text and the category a check compares. The injection text itself is not copied into this record.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the complaints fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "complaints",
        "category-disagrees",
        ["complaint:injection-1", "complaint:injection-2"],
        ["text", "category"],
    )

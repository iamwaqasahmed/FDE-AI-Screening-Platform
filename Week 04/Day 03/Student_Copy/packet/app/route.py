"""Send every call to ext-large.

This is the starter. The row is discarded. target always
returns ext-large, so nothing on the row can change
the destination.
"""


def target(row: dict) -> str:
    """Ignore the row. Return ext-large for every call."""
    # The row is unused.
    del row
    return "ext-large"

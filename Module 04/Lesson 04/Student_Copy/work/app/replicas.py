"""Place traffic on site-a only.

This is the starter. The sites argument is discarded.
placed always returns site-a and no other id.
"""


def placed(sites: dict) -> list[str]:
    """Ignore the sites list. Return site-a only."""
    # No site id is read from the argument.
    del sites
    return ["site-a"]

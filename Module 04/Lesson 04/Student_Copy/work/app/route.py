"""Keep sending to site-a after it fails health.

This is the starter. The sites argument is discarded.
choose always returns site-a. Health on the list cannot
change the result.
"""


def choose(sites: dict) -> str:
    """Ignore the sites list. Return site-a."""
    # Health is not read. The choice stays site-a.
    del sites
    return "site-a"

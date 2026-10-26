"""Price the batch at yesterday's external rate.

This is the starter. rate returns price.ext_large_per_1k
from the yesterday record, as an integer. The today
record is discarded.
"""


def rate(today: dict, yesterday: dict) -> int:
    """Return yesterday's external price as an integer. Ignore today.

    today is part of the signature so both records can be
    passed in. It is not read.
    """
    # The today record is not the price this module reports.
    del today
    return int(yesterday["price.ext_large_per_1k"])

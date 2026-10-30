"""Price the batch at today's external rate.

rate returns the sar figure on the today record, as an
integer. The yesterday record is discarded, so the older
price is not the result.
"""

from __future__ import annotations


def rate(today: dict, yesterday: dict) -> int:
    """Return today's sar as an integer. Ignore yesterday.

    yesterday is part of the signature so both records can
    be passed in. It is not read.
    """
    # The older record is not the price reported here.
    del yesterday
    return int(today["sar"])

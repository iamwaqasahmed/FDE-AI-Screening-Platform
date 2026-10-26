"""Bill every hospital the full backlog.

This is the starter. The amount is backlog_referrals
times tokens_per_referral times price_per_1k, using
integer division by 1000. That same amount is stored
for every hospital in shares. Only the hospital name
is taken from each share.
"""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    """Give every hospital the same full-backlog amount.

    The amount is the backlog times tokens per referral
    times the price, with integer division by 1000. Only
    the hospital name is read from each share.
    """
    tokens = int(sheet["tokens_per_referral"])
    # One full-backlog figure, repeated for each hospital name.
    full = int(sheet["backlog_referrals"]) * tokens * int(price_per_1k) // 1000
    return {str(row["hospital"]): full for row in sheet["shares"]}

"""Bill each hospital its own share of the backlog.

split walks the shares. For each row it multiplies that
row's referrals by tokens_per_referral and by price_per_1k,
then uses integer division by 1000. The key is the
hospital. Each hospital is billed from its own referrals.
"""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    """Bill every hospital from the referrals on its own share row.

    tokens_per_referral comes from the sheet and is shared.
    price_per_1k is the price argument. Integer division
    by 1000 finishes each amount.
    """
    # One token size for every row. The referral counts differ.
    tokens = int(sheet["tokens_per_referral"])
    return {
        str(row["hospital"]): int(row["referrals"]) * tokens * int(price_per_1k) // 1000
        for row in sheet["shares"]
    }
